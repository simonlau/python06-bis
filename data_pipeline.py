#!/usr/bin/env python3
# pyrefly: ignore-errors [explicit-any]
# ruff: file-ignore[any-type]

from abc import ABC, abstractmethod
from typing import (
    Any,
    Final,
    Literal,
    Protocol,
    TypeAlias,
    TypedDict,
    TypeGuard,
    runtime_checkable,
)

LogLevel = Literal["NOTICE", "ERROR", "WARNING", "INFO"]
ALLOWED_LOG_LEVELS: Final[set[str]] = {"NOTICE", "ERROR", "WARNING", "INFO"}


class Log(TypedDict):
    log_level: LogLevel
    log_message: str


OutputData: TypeAlias = tuple[int, str]
NumericData: TypeAlias = int | float | list[int | float]
TextData: TypeAlias = str | list[str]
LogData: TypeAlias = Log | list[Log]
StreamData: TypeAlias = NumericData | TextData | LogData


class DataProcessor(ABC):
    _list: list[str]
    _output: list[str]

    def __init__(self) -> None:
        self._list: list[str] = []
        self._output: list[str] = []

    def output(self) -> OutputData:
        s = self._list.pop(0)
        self._output.append(s)
        return len(self._output) - 1, s

    @property
    def total(self) -> int:
        return len(self._list) + len(self._output)

    @property
    def remainder(self) -> int:
        return len(self._list)

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


@runtime_checkable
class ExportPlugin(Protocol):
    def process_output(self, data: list[OutputData]) -> None:
        pass


class CsvExportPlugin:
    # ruff: ignore[no-self-use]
    def process_output(self, data: list[OutputData]) -> None:
        print("CSV Output")
        print(",".join(s for _, s in data))


class JsonExportPlugin:
    # ruff: ignore[no-self-use]
    def process_output(self, data: list[OutputData]) -> None:
        print("JSON Output")
        print({f"item_{num}": line for num, line in data})


class DataStream:
    _processors: list[DataProcessor]
    _stream: list[Any]

    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []
        self._stream: list[Any] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        self._stream.extend(stream)
        for proc in self._processors:
            for element in stream:
                if not proc.validate(element):
                    name = type(proc).__name__
                    msg = "Can't process element in stream"
                    print(f"{name} error - {msg}: {element}")
                else:
                    proc.ingest(element)

    def print_processors_stats(self) -> None:
        if len(self._processors) == 0:
            print("No processor found, no data")
            return

        for proc in self._processors:
            total = f"total {proc.total} items processed"
            rem = f"remaining {proc.remainder} on processor"
            name = type(proc).__name__
            print(f"{name}: {total}, {rem}")

    def output(self, name: str, num: int) -> None:
        proc = next(
            (p for p in self._processors if type(p).__name__ == name), None
        )
        if proc is None:
            return
        for _ in range(num):
            proc.output()

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self._processors:
            output = [proc.output() for _ in range(nb) if proc.remainder > 0]
            plugin.process_output(output)


def main() -> None:
    print("=== Code Nexus - Data Stream ===")
    print()
    print("Initialize Data Stream...")
    data_stream = DataStream()
    print("== DataStream statistics ==")
    data_stream.print_processors_stats()
    print()
    print("Registering Processors")
    data_stream.register_processor(NumericProcessor())
    data_stream.register_processor(TextProcessor())
    data_stream.register_processor(LogProcessor())
    print()
    log1: Log = {
        "log_level": "WARNING",
        "log_message": "Telnet access! Use ssh instead",
    }
    log2: Log = {"log_level": "INFO", "log_message": "User wil is connected"}

    data1: list[StreamData] = [
        "Hello world",
        [3.14, -1, 2.71],  # ruff: ignore[math-constant]
        [log1, log2],
        42,
        ["Hi", "five"],
    ]
    print(f"Send first batch of data on stream: {data1}")
    data_stream.process_stream(data1)
    print("== DataStream statistics ==")
    data_stream.print_processors_stats()
    print()
    print("Send 3 processed data from each processor to a CSV plugin")
    plugin1 = CsvExportPlugin()
    data_stream.output_pipeline(3, plugin1)
    print()
    print("== DataStream statistics ==")
    data_stream.print_processors_stats()
    print()
    log3: Log = {"log_level": "ERROR", "log_message": "500 server crash"}
    log4: Log = {
        "log_level": "NOTICE",
        "log_message": "Certificate expires in 10 days",
    }
    nums: list[int | float] = [32, 42, 64, 84, 128, 168]
    data2: list[StreamData] = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [log3, log4],
        nums,
        "World hello",
    ]
    print(f"Send another batch of data: {data2}")
    data_stream.process_stream(data2)
    print()
    print("== DataStream statistics ==")
    data_stream.print_processors_stats()
    print("Send 5 processed data from each processor to a JSON plugin")
    plugin2 = JsonExportPlugin()
    data_stream.output_pipeline(5, plugin2)
    print()
    print("== DataStream statistics ==")
    data_stream.print_processors_stats()


if __name__ == "__main__":
    main()
