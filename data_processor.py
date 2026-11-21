#!/usr/bin/env python3
# pyrefly: ignore-errors [explicit-any]
# ruff: file-ignore[any-type]

from abc import ABC, abstractmethod
from typing import Any, Final, Literal, TypedDict, TypeGuard

LogLevel = Literal["NOTICE", "ERROR"]
ALLOWED_LOG_LEVELS: Final[set[str]] = {"NOTICE", "ERROR"}


class Log(TypedDict):
    log_level: LogLevel
    log_message: str


class DataProcessor(ABC):
    _list: list[str]
    _outputted: int

    def __init__(self) -> None:
        self._list: list[str] = []
        self._outputted = 0

    def output(self) -> tuple[int, str]:
        i = self._outputted
        self._outputted += 1
        s = self._list.pop(0)
        return i, s

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass


def is_int_or_float_but_not_bool(x: Any) -> TypeGuard[int | float]:
    return isinstance(x, (int, float)) and not isinstance(x, bool)


def is_int_or_float_list(val: list[Any]) -> TypeGuard[list[int | float]]:
    return all(is_int_or_float_but_not_bool(x) for x in val)


def is_str_list(val: list[Any]) -> TypeGuard[list[str]]:
    return all(isinstance(x, str) for x in val)


def is_log(val: dict[Any, Any]) -> TypeGuard[Log]:
    return val["log_level"] in ALLOWED_LOG_LEVELS and isinstance(
        val["log_message"], str
    )


def is_log_list(val: list[Any]) -> TypeGuard[list[Log]]:
    return all(isinstance(x, dict) and is_log(x) for x in val)


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:  # ruff: ignore[no-self-use]
        match data:
            case int() | float():
                return True
            case list():
                return is_int_or_float_list(data)
            case _:
                return False

    def ingest(self, data: float | list[int] | list[float]) -> None:
        if not self.validate(data):
            msg = "Improper numeric data"
            raise ValueError(msg)
        match data:
            case int() | float():
                self._list.append(str(data))
            case list() if is_int_or_float_list(data):
                self._list.extend(str(item) for item in data)
            case list():
                return


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:  # ruff: ignore[no-self-use]
        match data:
            case str():
                return True
            case list():
                return is_str_list(data)
            case _:
                return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            msg = "Improper numeric data"
            raise ValueError(msg)
        match data:
            case str():
                self._list.append(data)
            case list() if is_str_list(data):
                self._list.extend(data)
            case list():
                return


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:  # ruff: ignore[no-self-use]
        match data:
            case dict():
                return is_log(data)
            case list():
                return is_log_list(data)
            case _:
                return False

    def ingest(self, data: Log | list[Log]) -> None:
        if not self.validate(data):
            msg = "Improper numeric data"
            raise ValueError(msg)
        match data:
            case {
                "log_level": str() as level,
                "log_message": str() as msg,
            } if level in ALLOWED_LOG_LEVELS:
                self._list.append(f"{level}: {msg}")
            case list() if is_log_list(data):
                self._list.extend(
                    f"{log['log_level']}: {log['log_message']}" for log in data
                )
            case list() | dict():
                return


def log_extract(num: int) -> None:
    if num > 1:
        print(f"Extracting {num} values...")
    else:
        print(f"Extracting {num} value...")


def run_numeric_processor() -> None:
    np = NumericProcessor()
    print("Testing Numeric Processor...")
    data: Any = 42
    print(f"Trying to validate input '{data}': {np.validate(data)}")
    data = "Hello"
    print(f"Trying to validate input '{data}': {np.validate(data)}")
    data = "foo"
    print(
        f"Test invalid ingestion of string '{data}' without prior validation:"
    )
    try:
        np.ingest(data)  # ty: ignore[invalid-argument-type]
    except ValueError as error:
        print(f"Got exception: {error}")
    data = [1, 2, 3, 4, 5]
    print(f"Processing data: {data}")
    np.ingest(data)
    limit = 3
    log_extract(3)
    for i in range(limit):
        print(f"Numeric value {i}: {np.output()[1]}")


def run_text_processor() -> None:
    print("Testing Text Processor...")
    tp = TextProcessor()
    data: Any = 42
    print(f"Trying to validate input '{data}': {tp.validate(data)}")
    data = ["Hello", "Nexus", "World"]
    print(f"Processing data: {data}")
    tp.ingest(data)
    limit = 1
    log_extract(1)
    for i in range(limit):
        print(f"Text value {i}: {tp.output()[1]}")


def run_log_processor() -> None:
    print("Testing Log Processor...")
    lp = LogProcessor()
    data: Any = "Hello"
    print(f"Trying to validate input {data}: {lp.validate(data)}")
    logs: list[Log] = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
    ]
    print(f"Processing data: {logs}")
    lp.ingest(logs)
    limit = 2
    log_extract(limit)
    for i in range(limit):
        print(f"Log Entry {i}: {lp.output()[1]}")


def main() -> None:
    print("=== Code Nexus - Data Processor ===")
    print(" ")
    run_numeric_processor()
    print(" ")
    run_text_processor()
    print(" ")
    run_log_processor()


if __name__ == "__main__":
    main()
