# Structural Pattern Matching in Python

> Source: https://realpython.com/structural-pattern-matching/
> Collected: 2026-11-09
> Published: Updated Oct 16, 2024

# Structural Pattern Matching in Python

by [Bartosz Zaczyński](#author) Updated Oct 16, 2024 Reading time estimate 2h 11m [](#reader-comments) [intermediate](/tutorials/intermediate/) [python](/tutorials/python/)

Mark as Completed Share

Table of Contents

- [Getting to Know Structural Pattern Matching](#getting-to-know-structural-pattern-matching)

  - [What Is Pattern Matching?](#what-is-pattern-matching)

  - [What Is a Structural Pattern?](#what-is-a-structural-pattern)

  - [When to Use Structural Pattern Matching?](#when-to-use-structural-pattern-matching)

- [Understanding the New Syntax and Semantics](#understanding-the-new-syntax-and-semantics)

  - [Soft Keywords in Python 3\.10 and Later](#soft-keywords-in-python-310-and-later)

  - [Match Statement and Case Clauses](#match-statement-and-case-clauses)

  - [Precedence of Structural Patterns](#precedence-of-structural-patterns)

  - [Default Case and the Wildcard Pattern](#default-case-and-the-wildcard-pattern)

- [Exploring Basic Pattern Types Supported by Python](#exploring-basic-pattern-types-supported-by-python)

  - [Literal Pattern](#literal-pattern)

  - [Value Pattern](#value-pattern)

  - [Capture Pattern](#capture-pattern)

- [Digging Into More Advanced Structural Patterns](#digging-into-more-advanced-structural-patterns)

  - [Sequence Pattern](#sequence-pattern)

  - [Mapping Pattern](#mapping-pattern)

  - [Class Pattern](#class-pattern)

- [Customizing Pattern Matching of Class Instances](#customizing-pattern-matching-of-class-instances)

- [Composing Complex Structural Patterns](#composing-complex-structural-patterns)

  - [OR Pattern: Union of Multiple Patterns](#or-pattern-union-of-multiple-patterns)

  - [AS Pattern: Alias of a Matched Subpattern](#as-pattern-alias-of-a-matched-subpattern)

  - [Group Pattern: Visual Grouping of Subpatterns](#group-pattern-visual-grouping-of-subpatterns)

  - [Guard: Logical Condition on Top of a Pattern](#guard-logical-condition-on-top-of-a-pattern)

- [Finding Practical Uses for Pattern Matching](#finding-practical-uses-for-pattern-matching)

  - [Read Deeply Nested Hierarchical Data](#read-deeply-nested-hierarchical-data)

  - [Parse and Process User Input](#parse-and-process-user-input)

  - [Traverse Recursive Data Structures](#traverse-recursive-data-structures)

  - [Enforce Types at Runtime to Validate Data](#enforce-types-at-runtime-to-validate-data)

  - [Overload a Callable Based on Its Arguments](#overload-a-callable-based-on-its-arguments)

  - [Emulate a C-Style Switch Statement in Python](#emulate-a-c-style-switch-statement-in-python)

- [Recognizing Python’s Pattern Matching Limitations](#recognizing-pythons-pattern-matching-limitations)

  - [Match Is a Statement, Not an Expression](#match-is-a-statement-not-an-expression)

  - [Case Clauses Aren’t Exhaustive](#case-clauses-arent-exhaustive)

  - [Case Clauses Don’t Fall Through](#case-clauses-dont-fall-through)

  - [Case Clauses Can Overlap](#case-clauses-can-overlap)

  - [Case Clauses Can’t Have Assignment Expressions](#case-clauses-cant-have-assignment-expressions)

  - [Not All Patterns Are Made Equal](#not-all-patterns-are-made-equal)

  - [Matching a Python Set Requires a Guard](#matching-a-python-set-requires-a-guard)

  - [Most Literal Patterns Match by Equality](#most-literal-patterns-match-by-equality)

  - [Floating-Point Patterns Are Imprecise](#floating-point-patterns-are-imprecise)

  - [String Patterns Are Not Sequences](#string-patterns-are-not-sequences)

  - [Captured Names May Wind Up Undefined](#captured-names-may-wind-up-undefined)

  - [Capture Patterns Can’t Reuse Variables](#capture-patterns-cant-reuse-variables)

  - [Union Patterns Bind the Same Names](#union-patterns-bind-the-same-names)

  - [Matching Constant Values Is Tricky](#matching-constant-values-is-tricky)

- [Conclusion](#conclusion)

[Remove ads](/account/join/)

Recommended Course

[Using Structural Pattern Matching in Python](/courses/structural-pattern-matching/) (53m)

Structural pattern matching is a powerful **control flow construct** invented decades ago that’s traditionally used by compiled languages, especially within the [functional programming paradigm](https://realpython.com/python-functional-programming/).

Most mainstream programming languages have since adopted some form of pattern matching, which offers concise and readable syntax while promoting a declarative code style. Although Python was late to join the party, it introduced structural pattern matching in the [3\.10](https://realpython.com/python310-new-features/) release.

**In this tutorial, you’ll:**

- Master the **syntax** of the `match` statement and `case` clauses

- Explore various **types of patterns** supported by Python

- Learn about **guards**, **unions**, **aliases**, and **name binding**

- Extract values from deeply nested **hierarchical data structures**

- Customize pattern matching for **user-defined classes**

- Identify and avoid **common pitfalls** in Python’s pattern matching

To get the most out of this tutorial, you should have a basic understanding of [conditional statements](https://realpython.com/python-conditional-statements/), [loops](https://realpython.com/python-for-loop/), [functions](https://realpython.com/defining-your-own-python-function/), and [classes](https://realpython.com/python-classes/) in Python. Additionally, familiarity with Python’s built-in [data structures](https://realpython.com/python-data-structures/), such as [tuples](https://realpython.com/python-tuple/), [lists](https://realpython.com/python-list/), and [dictionaries](https://realpython.com/python-dicts/), will be beneficial.

**Get Your Free Code:** [Click here to download the free sample code](https://realpython.com/bonus/structural-pattern-matching-code/) that shows you how to use structural pattern matching in Python.

 **Take the Quiz:** Test your knowledge with our interactive “Structural Pattern Matching” quiz. You’ll receive a score upon completion to help you track your learning progress:

---

[](/quizzes/structural-pattern-matching/)

![Structural Pattern Matching in Python](https://files.realpython.com/media/Structural-Pattern-Matching-in-Python-3.10_Watermarked-2.085d2bfb1940.jpg)

**Interactive Quiz**

[Structural Pattern Matching](/quizzes/structural-pattern-matching/)

In this quiz, you'll test your understanding of structural pattern matching in Python. This powerful control flow construct, introduced in Python 3\.10, offers concise and readable syntax while promoting a declarative code style.

## Getting to Know Structural Pattern Matching[](#getting-to-know-structural-pattern-matching "Permanent link")

Before taking advantage of structural pattern matching in your code, make sure that you’re running **Python 3\.10** or later, as you won’t be able to use it in earlier Python versions. Note that although the name **structural pattern matching** is often shortened to just **pattern matching**, the qualifier *structural* is crucial to understanding the use cases for this feature. In this section, you’ll get a high-level overview of structural pattern matching.

[ Remove ads](/account/join/)

### What Is Pattern Matching?[](#what-is-pattern-matching "Permanent link")

You can think of pattern matching as a form of [syntactic sugar](https://realpython.com/syntactic-sugar-python/) built on top of existing language constructs, including [conditional statements](https://realpython.com/python-conditional-statements/) and [tuple unpacking](https://realpython.com/python-tuple/#packing-and-unpacking-tuples). While you can absolutely live without pattern matching, it gives you new superpowers, making this feature more convenient than the conventional syntax in some situations.

Pattern matching often leads to more elegant, concise, and readable code written in a [declarative](https://en.wikipedia.org/wiki/Declarative_programming) style. To get a taste of it, take a quick look at the following example without trying to fully understand how it works just yet:

Language: Python

```
import json

def log(event):
    match json.loads(event):
        case {"keyboard": {"key": {"code": code}}}:
            print(f"Key pressed: {code}")
        case {"mouse": {"cursor": {"screen": [x, y]}}}:
            print(f"Mouse cursor: {x=}, {y=}")
        case _:
            print("Unknown event type")
```

The `match` statement takes a **subject**, which can be any valid Python expression, such as a string literal or a function call, and compares the resulting value to one or more **patterns** listed in the `case` clauses. The first pattern that matches the given subject will trigger the corresponding `case` block to run. You’ll learn more about the `match` statement and `case` clauses later in this tutorial.

At first glance, the syntax of structural pattern matching in Python looks a bit like the [`switch` statement](https://en.wikipedia.org/wiki/Switch_statement) found in the [C-family](https://en.wikipedia.org/wiki/List_of_C-family_programming_languages) programming languages if you squint your eyes:

Language: C

```
void log_event(enum Event event) {
    switch (event) {
        case KEYBOARD:
            printf("Keyboard event\n");
            break;
        case MOUSE:
            printf("Mouse event\n");
            break;
        default:
            printf("Unknown event\n");
    }
}
```

This resemblance is deceptive, though. The classic `switch` statement controls the execution flow based on the **exact value** stored in a variable. It effectively works as a chained sequence of mutually exclusive `if..elif...` equality comparisons, but with a more succinct and readable syntax.

Although you can use pattern matching this way, you’d be missing out on its true power and flexibility. Structural pattern matching was designed to go beyond value comparisons. In particular, it combines **conditional statements** or branching based on a logical predicate with **destructuring** or object deconstruction, which is the inverse of object construction. You’ll see examples of destructuring in the next section.

**Note:** Because pattern matching does two things at once, the Python interpreter can take advantage of this to optimize the underlying bytecode with specialized opcodes, making the code run slightly faster.

The brief code snippet above merely scratches the surface of what you can achieve with pattern matching, but it already shows you its expressiveness, especially when you compare it with the traditional `if...elif...` statements and [`isinstance()`](https://realpython.com/what-does-isinstance-do-in-python/) checks. Here’s one of the many ways you can implement the equivalent logic using standard Python:

Language: Python

```
import json

def log(event):
    parsed_event = json.loads(event)
    if (
        "keyboard" in parsed_event and
        "key" in parsed_event["keyboard"] and
        "code" in parsed_event["keyboard"]["key"]
    ):
        code = parsed_event["keyboard"]["key"]["code"]
        print(f"Key pressed: {code}")
    elif (
        "mouse" in parsed_event and
        "cursor" in parsed_event["mouse"] and
        "screen" in parsed_event["mouse"]["cursor"]
    ):
        screen = parsed_event["mouse"]["cursor"]["screen"]
        if isinstance(screen, list) and len(screen) == 2:
            x, y = screen
            print(f"Mouse cursor: x={x}, y={y}")
        else:
            print("Unknown event type")
    else:
        print("Unknown event type")
```

This code is functionally identical to the previous version but is longer and has more indentation levels than before. Additionally, it looks more verbose and [imperative](https://en.wikipedia.org/wiki/Imperative_programming) in style, describing not only *what* to do but also *how* to perform the individual steps. Granted, you could try making it slightly shorter by using the [Walrus operator](https://realpython.com/python-walrus-operator/) and following the [EAFP principle](https://realpython.com/python-lbyl-vs-eafp/) without explicit checks, but it’d remain somewhat convoluted.

It’s worth noting that structural pattern matching first emerged in compiled functional languages with static typing. The attempt to implement it in Python, which is a [dynamic language](https://en.wikipedia.org/wiki/Dynamic_programming_language), presented completely new and unique challenges. You can read more about them in the paper entitled [Dynamic Pattern Matching with Python](https://gvanrossum.github.io/docs/PyPatternMatching.pdf), which was co-authored by [Guido van Rossum](https://en.wikipedia.org/wiki/Guido_van_Rossum) and published in the proceedings of the Dynamic Languages Symposium in 2020\.

Now that you’ve seen the most basic form of pattern matching in Python, it’s time to unravel the meaning of a structural pattern.

### What Is a Structural Pattern?[](#what-is-a-structural-pattern "Permanent link")

Python supports several types of structural patterns, which you’ll explore in detail throughout this tutorial. Each pattern describes the structure of an object to match, including its **type**, **shape**, **value**, and **identity**. It can also specify the individual **pieces** of which an object is made. For example, you may want to define a pattern that will match [three-dimensional](https://en.wikipedia.org/wiki/Three-dimensional_space) points that lie on the z-axis:

Language: Python

```
match subject:
    case list([int() | float() as x, int() | float() as y, 0]):
        print(f"Point({x=}, {y=})")
```

The pattern defined in the `case` clause above will match a numeric list of size three whose last element is equal to zero. This concise pattern matching encapsulates the same logic as the following much longer code snippet:

Language: Python

```
if isinstance(subject, list) and len(subject) == 3:
    if (
        isinstance(subject[0], int | float) and
        isinstance(subject[1], int | float) and
        subject[2] == 0
    ):
        x, y, _ = subject
        print(f"Point({x=}, {y=})")
```

As you can see, structural patterns let you express intricate **conditional logic** clearly and precisely. Their second but equally important trait is selective **data extraction** from complex data structures. In this case, your pattern unpacks the first two values from the matched list and binds them to the `x` and `y` variables.

A common point of confusion about structural patterns is that they look familiar to most Python programmers but mean something completely different in the context of pattern matching. A pattern is *not* your typical [expression](https://docs.python.org/3/glossary.html#term-expression). Although it looks like an object literal or a [class constructor](https://realpython.com/python-class-constructor/), it doesn’t actually instantiate a new object. Here’s an example leveraging a [data class](https://realpython.com/python-data-classes/) to illustrate this:

Language: Python

```
>>> from dataclasses import dataclass

>>> @dataclass
... class User:
...     name: str
...
...     def __post_init__(self):
...         print(f"Created a new user named {self.name}")
...
>>> match User("Alice"):
...     case User("Bob"):
...         pass
...
Created a new user named Alice
```

The `User("Alice")` expression in the `match` statement does indeed create a new `User` instance, but a similarly looking `User("Bob")` pattern in the `case` clause doesn’t. Whether a piece of code becomes an expression or a structural pattern depends on *where* you put it. In particular, whatever follows a `case` clause is always interpreted as a pattern.

Patterns represent a relatively little-known concept in Python: **object deconstruction** or **destructuring**, which means pulling apart structured data. Before Python 3\.10, you had only a handful of ways to deconstruct compound objects like [sequences](https://realpython.com/python-sequences/) and [mappings](https://realpython.com/python-mappings/), such as these:

| Action | Example |
| --- | --- |
| Unpack an iterable | `head, *middle, tail = range(10)` |
| Unpack and merge dictionaries | `{**headers, **cookies}` |
| Access an item by index | `last_item = items[-1]` |
| Access a value by key | `path = os.environ["PATH"]` |
| Access an attribute by name | `date = datetime.date` |

Structural patterns extend this idea by adding a few more destructuring techniques to the list, albeit strictly in the context of pattern matching. This is different from some other programming languages, which allow you to destructure objects without conditional matching.

If you’ve ever dipped your toes into [JavaScript](https://realpython.com/python-vs-javascript/), then you’re probably familiar with [destructuring assignments](https://realpython.com/python-vs-javascript/#destructuring-assignments), which can streamline the extraction of values from arbitrary objects:

Language: JavaScript

~~~
function sayHello({ name, age }) {
    console.log(`My name's ${name}, and I'm ${age} years old.`);
}

sayHello(new Person("Alice", 42, "New York", "Software Engineer"))
~~~

In this example, you extract the values corresponding to the `.name` and `.age` attributes of a user-defined `Person` type. Later, you’ll learn how to take advantage of similar patterns in Python.

Upon closer inspection, a structural pattern is the opposite of object construction. It’s the “left side” of the [assignment statement](https://realpython.com/python-assignment-operator/), conceptually similar to tuple unpacking:

Language: Python

```
>>> a, b, c = range(3)
>>> print(f"Point({a=}, {b=}, {c=})")
Point(a=0, b=1, c=2)

>>> match range(3):
...     case x, y, z:
...         print(f"Point({x=}, {y=}, {z=})")
...
Point(x=0, y=1, z=2)
```

The `a`, `b`, and `c` variables in the code snippet above appear to the left of the assignment operator (`=`), making them the target of that assignment. The `x`, `y`, and `z` variables in the `case` clause serve a similar purpose, acting as placeholders for values matched from the subject.

However, there’s a subtle difference. Unpacking is unconditional, meaning that it can fail, whereas pattern matching is *conditional*, so it’ll only run if the pattern matches the subject. Consider the following example:

Language: Python

```
>>> a, b, c = range(2)
Traceback (most recent call last):
  ...
ValueError: not enough values to unpack (expected 3, got 2)

>>> match range(2):
...     case x, y, z:
...         print(f"Point({x=}, {y=}, {z=})")
...
```

The unpacking operation fails with an error this time because there aren’t enough values to assign to the variables. The [`range()`](https://realpython.com/python-range/) function generates only two numbers, while the unpacking expects three values, resulting in a `ValueError`. An attempt to destructure the same object into too many variables never runs because the corresponding pattern doesn’t succeed, letting your program continue without interruption.

At this point, you should have a rough idea of how structural pattern matching works. But, if you’re new to this concept, then it still might not be entirely clear how to apply pattern matching in the wild and what use cases it fits best.

[ Remove ads](/account/join/)

### When to Use Structural Pattern Matching?[](#when-to-use-structural-pattern-matching "Permanent link")

The answer to when to use pattern matching is right there in its name: *structural* pattern matching. In short, you should use pattern matching when you want to make a decision based on the **structure of complex data** and possibly **destructure** it at the same time. This approach can help you adopt a more declarative coding style, which is especially beneficial if you’re following the functional [programming paradigm](https://en.wikipedia.org/wiki/Programming_paradigm):

Language: Python

```
from pathlib import Path
from urllib.request import urlretrieve

def fetch(resource):
    match resource:
        case {"protocol": "http" | "ftp", "full_url": url}:
            match urlretrieve(url):
                case file_path, _:
                    return Path(file_path).read_text("utf-8")
        case _:
            raise ValueError("Unsupported protocol")
```

Although not purely functional in style, this example leverages two `match` statements nested one in another to handle different types of resources based on their structure. If the first `resource` is a [Python dictionary](https://realpython.com/python-dicts/) with a `"protocol"` key equal to either `"http"` or `"ftp"` and has a `"full_url"` key, then you retrieve the file from that URL. Upon successful retrieval, you read and return the content of the resulting temporary file.

In contrast, if you’re making a decision based on complex [business rules](https://en.wikipedia.org/wiki/Business_rule) that require a lot of computation, especially if the conditions are non-exclusive or incremental, then you may be better off choosing a different language construct. There are some well-established and usually more appropriate idioms in Python for such scenarios, like a chain of `if...elif...` statements:

Language: Python

```
def get_shipping_cost(order):
    if (
        order.priority is Priority.STANDARD and
        order.domestic and
        any(order.shipping_address.close_to(x) for x in WAREHOUSES)
    ):
        cost = 5 if order.weight <= MAX_WEIGHT_SMALL_PACKAGE else 10
    elif (
        order.priority is Priority.STANDARD and
        order.international
    ):
        cost = 20 if order.weight <= MAX_WEIGHT_SMALL_PACKAGE else 40
    # ...
    else:
        raise ValueError("Invalid order")

    if not order.shipping_address.country.is_vat_exempt:
        cost *= order.shipping_address.country.vat_rate

    return cost
```

This function calculates the shipping cost based on several factors, including the order’s priority, whether it’s domestic or international, the delivery distance, and the weight of the package. It also adjusts the cost based on the [VAT](https://en.wikipedia.org/wiki/Value-added_tax) rate of the destination country if it applies. Codifying this logic with pattern matching would prove cumbersome.

As a rule of thumb, try to avoid using pattern matching as a `switch` statement replacement. A popular method to [emulate the `switch` statement](https://realpython.com/lessons/emulating-switchcase-full-example/) in Python involves a dictionary-based [jump table](https://en.wikipedia.org/wiki/Branch_table), which you can use to implement [dynamic dispatch](https://en.wikipedia.org/wiki/Dynamic_dispatch):

Language: Python

```
from operator import add, sub, mul, truediv as div

def apply(operator, left, right):
    return {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div,
    }.get(operator, lambda *args: None)(left, right)
```

Here, you use a Python dictionary to map string representations of [binary operators](https://en.wikipedia.org/wiki/Binary_operation) to their corresponding functions from the [`operator`](https://realpython.com/python-operator-module/) module. If the provided operator isn’t defined in the dictionary, then you default to a [lambda expression](https://realpython.com/python-lambda/) that always returns [`None`](https://realpython.com/null-in-python/). This method lets you extend the dictionary with additional operators if necessary.

By the end of this tutorial, you’ll have discovered numerous [practical use cases](#finding-practical-uses-for-pattern-matching) for pattern matching through concrete examples. Some of them include parsing deeply nested hierarchical data like [JSON](https://realpython.com/python-json/), processing user input, or traversing recursive data structures, such as [abstract syntax trees (AST)](https://en.wikipedia.org/wiki/Abstract_syntax_tree). But, before diving into these examples, you should first have a better understanding of the syntax and semantics of pattern matching.

## Understanding the New Syntax and Semantics[](#understanding-the-new-syntax-and-semantics "Permanent link")

The syntax of structural pattern matching in Python was heavily inspired by languages like [Scala](https://www.scala-lang.org/) and [Rust](https://www.rust-lang.org/). This was intentional so that developers who are familiar with popular programming languages can immediately feel at home. Take a look at the following image to compare the syntactical differences and similarities between these languages:

[![The Pattern Matching Syntax in Scala, Rust, and Pyhon](https://files.realpython.com/media/scala_rust_python.d359460dae70.png)](https://files.realpython.com/media/scala_rust_python.d359460dae70.png)

The Pattern Matching Syntax in Scala, Rust, and Python

You can also expand the collapsible section below to reveal the sample [factorial implementation](https://realpython.com/python-recursion/#calculate-factorial) in text format, as shown in the screenshot:

Factorial Calculation in Scala, Rust, and PythonShow/Hide

Scala implementation of the factorial function:

Language: Scala

```
def factorial(n: Int): Int =
    n match {
        case 0 | 1 => 1
        case _     => n * factorial(n - 1)
    }
```

Rust implementation of the factorial function:

Language: Rust

```
fn factorial(n: u64) -> u64 {
    match n {
        0 | 1 => 1,
        _ => n * factorial(n - 1),
    }
}
```

Python implementation of the factorial function:

Language: Python

```
def factorial(n):
    match n:
        case 0 | 1:
            return 1
        case _:
            return n * factorial(n - 1)
```

Note that these different implementations are all equivalent.

Besides drawing inspiration from other programming languages, Python’s pattern matching builds on top of the existing syntax for sequence unpacking. In this section, you’ll examine the new keywords and concepts introduced in this feature.

### Soft Keywords in Python 3\.10 and Later[](#soft-keywords-in-python-310-and-later "Permanent link")

To facilitate the use of pattern matching in Python, the interpreter itself had to undergo significant changes. [Python 3\.9](https://realpython.com/python39-new-features/) introduced the concept of [soft keywords](https://docs.python.org/3/reference/lexical_analysis.html#soft-keywords), and Python 3\.10 delivered their first implementation. Standard [keywords](https://realpython.com/python-keywords/) like [`with`](https://realpython.com/python-with-statement/) or [`return`](https://realpython.com/python-return-statement/) are reserved, meaning that you can’t use them as identifiers for your [variables](https://realpython.com/python-variables/), [functions](https://realpython.com/defining-your-own-python-function/), and other elements in your code. As soon as you try, you’ll encounter a [syntax error](https://realpython.com/python-built-in-exceptions/#syntax-errors):

Language: Python

```
>>> ticket.class = "business"
  File "<input>", line 1
    ticket.class = "business"
           ^^^^^
SyntaxError: invalid syntax
```

In this case, `.class` isn’t allowed as an attribute name because it’s a keyword reserved for defining Python classes only. To circumvent this limitation, you can rename the attribute by appending a trailing underscore (`_`), which is a common practice in Python.

On the other hand, **soft keywords** are contextual. They act as keywords only in specific contexts. This new capability was made possible thanks to the introduction of the [PEG parser](https://realpython.com/python39-new-features/#a-more-powerful-python-parser) in Python 3\.9, which changed how the interpreter reads the source code. For instance, since [Python 3\.12](https://realpython.com/python312-new-features/), `type` becomes a keyword when you use it as a [type alias](https://realpython.com/python312-typing/#type-aliases) definition, but it behaves as a regular identifier everywhere else:

Language: Python

```
>>> type String = str

>>> type(42)
<class 'int'>

>>> Blood = type("Blood", (), {
...         "__init__": lambda self, group: setattr(self, "group", group),
...         "__repr__": lambda self: f"Blood(group={self.group!r})",
...     },
... )

>>> type = Blood("AB+")
```

Although [`type()`](https://docs.python.org/3/library/functions.html#type) also happens to be a [built-in function](https://realpython.com/python-built-in-functions/), which you can use for [type checking](https://realpython.com/python-type-checking/) or making new data types at runtime, it’s technically a valid identifier for user-defined symbols as well.

**Note:** While you can reuse the names of built-in functions in your code, doing so will lead to [masking](https://en.wikipedia.org/wiki/Name_resolution_\(programming_languages\)#Name_masking) of their original functionality. It’s usually better to come up with unique names in order to avoid potential issues.

This lenient naming policy allows new keywords to be added into the language without breaking existing code. Back in Python 3\.5, when `async def` syntax ([PEP 492](https://peps.python.org/pep-0492/)) was introduced, the language tokenizer had to be modified to treat `async` and `await` as keywords only in certain contexts. This ensured [backward compatibility](https://en.wikipedia.org/wiki/Backward_compatibility) with [legacy code](https://en.wikipedia.org/wiki/Legacy_system) that used these common words as identifiers, like so:

Language: Python

```
from concurrent.futures import ThreadPoolExecutor
import requests

executor = ThreadPoolExecutor()

def fetch(urls, async=True):
    if async:
        return [executor.submit(requests.get, url) for url in urls]
    else:
        return [requests.get(url) for url in urls]
```

When the `async` parameter is equal to `True`, this function returns immediately with a list of [future objects](https://en.wikipedia.org/wiki/Futures_and_promises) that you can await by calling [`as_completed()`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.as_completed). Otherwise, the function works synchronously by blocking the current [thread of execution](https://realpython.com/intro-to-python-threading/) until all requests are completed.

The change in Python’s tokenizer was a one-time workaround to allow for an interim [deprecation period](https://en.wikipedia.org/wiki/Deprecation#Software) before `async` and `await` finally became reserved keywords in [Python 3\.7](https://realpython.com/python37-new-features/). This resulted in making the above code syntactically incorrect going forward.

The idea behind soft keywords aims to achieve similar benefits without resorting to dirty hacks. The authors of pattern matching in Python picked the `match` keyword because it was widely used for that purpose in many other programming languages.

Unfortunately, the standard-library module for [regular expressions](https://realpython.com/regex-python/) already contained a function named [`match()`](https://docs.python.org/3/library/re.html#re.match), which wouldn’t be allowed anymore, necessitating breaking changes. Additionally, it’s become idiomatic to assign the result of `re.match()` to a variable called `match`. This is a common pattern, so making `match` a [hard keyword](https://peps.python.org/pep-0622/#use-a-hard-keyword) would cause widespread disruption in existing codebases. So, it was decided to make `match` a soft keyword instead.

With soft keywords in place, you can reuse the same name more than once on a single line of code without ambiguity. Depending on the color theme of your choice, most [IDEs and code editors](https://realpython.com/python-ides-code-editors-guide/) should display each instance of `match` using distinct colors to differentiate their meaning:

[![Pattern Matching and Regular Expressions](https://files.realpython.com/media/match_match_match.7dbeeb17aa7e.png)](https://files.realpython.com/media/match_match_match.7dbeeb17aa7e.png)

Pattern Matching and Regular Expressions

The screenshot above depicts a fragment of code in [PyCharm](https://realpython.com/pycharm-guide/) with the [Xcode Light](https://plugins.jetbrains.com/plugin/15727-xcode-theme) theme selected. The first occurrence of `match` is in purple to indicate it’s a keyword, followed by a `match` variable in black, and a `match` function call in teal. You can expand the collapsible section below to reveal the code snippet in text format:

Pattern Matching and Regular ExpressionsShow/Hide

Language: Python

```
from re import match

match match := match(r"([^@]+)@.*", "alice@email.com").group(1):
    case "alice":
        print("Welcome, Alice!")
    case "bob":
        print("Welcome, Bob!")
    case _:
        print("Welcome, stranger!")
```

Although this is perfectly valid Python, it might look confusing even to those familiar with the nuances of pattern matching, regular expressions, and the Walrus operator. In general, you should find ways to avoid such “clever” code.

If you’re unsure whether a particular word is a reserved keyword in your current Python version, then you can always check by using the standard-library [`keyword`](https://docs.python.org/3/library/keyword.html) module:

Language: Python

```
>>> import keyword

>>> keyword.iskeyword("match")
False

>>> keyword.issoftkeyword("match")
True

>>> keyword.kwlist
['False', 'None', ..., 'while', 'with', 'yield']

>>> keyword.softkwlist
['_', 'case', 'match', 'type']
```

As of Python 3\.12, there are thirty-five reserved keywords and only **four soft keywords** in Python, three of which are related to pattern matching. The underscore character (`_`) is one of them.

**Note:** The first soft keywords ever introduced were `match`, `case`, and `_`, all of which facilitate pattern matching.

The underscore is a valid identifier that has had many [conventional meanings](https://realpython.com/python-double-underscore/#other-usages-of-underscores-in-python) in Python, including:

- Unused variables that [linters](https://realpython.com/python-code-quality/#linters) should ignore without complaining

- Throwaway variables in loops and other constructs

- The last evaluated expression in a [Python REPL](https://realpython.com/python-repl/)

- Alias of the multilingual translation function like [`gettext()`](https://docs.python.org/3/library/gettext.html#gettext.gettext)

Now, it’s adopted yet another meaning. In the context of pattern matching, an underscore represents the wildcard pattern typically used as a **default catch-all** case. The other two keywords associated with pattern matching are `match` and `case`, which you’ll learn about next.

[ Remove ads](/account/join/)

### Match Statement and Case Clauses[](#match-statement-and-case-clauses "Permanent link")

Imagine you wanted to build a bare-bones [Python REPL](https://realpython.com/python-repl/), which takes [user input](https://realpython.com/python-keyboard-input/) and interprets the entered line of code. Pattern matching is the perfect tool for such a task. To keep things simple, you’ll only allow statements that can fit on a single line. However, for a more complete solution that offers multiline code block support, scroll down and expand the collapsible section at the end of the next section.

**Note:** The script that you’re about to write is intended for illustrative purposes only. If you’d like to implement a fully-featured Python REPL, then you can leverage the [`code`](https://docs.python.org/3.12/library/code.html) module from the standard library, which provides more convenient building blocks.

Okay. Define your first [`match` statement](https://docs.python.org/3/reference/compound_stmts.html#match) followed by an expression, which is called the **subject value**, and a colon (`:`) to start a new block of code:

Language: Python Filename: `repl.py`

```
PROMPT = "\N{snake} "

match input(PROMPT):
```

In this case, you call the built-in [`input()`](https://docs.python.org/3/library/functions.html#input) function with the [snake emoji](https://www.fileformat.info/info/unicode/char/1f40d/index.htm) prompt represented as a [Unicode](https://realpython.com/python-encodings-guide/) escape sequence. The value returned from the function is your subject.

**Note:** It sometimes helps to store the evaluated subject in a variable before passing it to the `match` statement. Alternatively, you can use the Walrus operator to combine the best of both worlds:

Language: Python

```
match subject := input(PROMPT):
```

Binding the subject to a named variable is preferable when you anticipate the need to refer to it later. For example, you may want to append user input to a file containing the command history of your REPL.

The body of the `match` statement can only consist of a non-empty sequence of **case clauses**. You’re not allowed to use *any* other types of [statements](https://docs.python.org/3/glossary.html#term-statement) inside the `match` code block. That includes the [`pass` statement](https://realpython.com/python-pass/) and the [ellipsis literal (`...`)](https://realpython.com/python-ellipsis/). Furthermore, you must place at least one `case` clause followed by a **structural pattern** and a colon, which starts another nested block of code:

Language: Python Filename: `repl.py`

```
import sys

PROMPT = "\N{snake} "

match input(PROMPT):
    case "help":
        message = f"Python {sys.version}"
        print(message)
```

Here, you use a **literal pattern**, which matches the exact string `"help"`. If the user types the *help* command at the prompt, then you display a message indicating their current Python version in response:

Language: Shell

```
$ python repl.py
🐍 help
Python 3.12.4 (main, Jun 10 2024, 12:47:23) [GCC 13.2.0]
```

More often than not, you’ll collapse each block belonging to a `case` clause into a single line of code while calling some function to delegate the execution:

Language: Python Filename: `repl.py`

```
import sys

PROMPT = "\N{snake} "

match input(PROMPT):
    case "help":
        print(f"Python {sys.version}")
```

This practice can make your code look more concise and easier to follow.

Note that you’re not restricted to the [global scope](https://realpython.com/python-scope-legb-rule/#modules-the-global-scope) when it comes to using pattern matching. You can declare the `match` statement anywhere in your code, for example, within a nested code block in a function:

Language: Python Filename: `repl.py`

```
import sys
import traceback

PROMPT = "\N{snake} "

def main():
    while True:
        try:
            match input(PROMPT):
                case "help":
                    print(f"Python {sys.version}")
        except:
            traceback.print_exc(file=sys.stdout)

if __name__ == "__main__":
    main()
```

The code above follows the [name-main idiom](https://realpython.com/if-name-main-python/) by calling the `main()` function at the bottom of the file. This function runs an [infinite loop](https://realpython.com/python-while-loop/#infinite-loops), which continuously prompts the user for input without the possibility to gracefully terminate the program, not even by raising an exception.

To let the user break out of the loop, you must handle another command, such as *exit* or *quit*. You should also avoid a bare `except:` clause to allow the built-in system exceptions to propagate:

Language: Python Filename: `repl.py`

```
import sys
import traceback

PROMPT = "\N{snake} "

def main():
    print('Type "help" for more information, "exit" or "quit" to finish.')
    while True:
        try:
            match input(PROMPT):
                case "help":
                    print(f"Python {sys.version}")
                case "exit" | "quit":
                    break
        except Exception:
            traceback.print_exc(file=sys.stdout)

if __name__ == "__main__":
    main()
```

You use the [vertical bar (`|`)](https://en.wikipedia.org/wiki/Vertical_bar) to combine two **subpatterns** into a union, which is a neat way to avoid code duplication. By having Python match one of the alternatives, you reuse a code block common to multiple patterns. In this case, they’re both literal patterns.

Now, you have a basic program that your users can interact with. It’ll continue running until the user types either *exit* or *quit*:

Language: Shell

```
$ python repl.py
Type "help" for more information, "exit" or "quit" to finish.
🐍 help
Python 3.12.4 (main, Jun 10 2024, 12:47:23) [GCC 13.2.0]
🐍 EXIT
🐍 exit
```

Notice, however, that your commands are [case-sensitive](https://en.wikipedia.org/wiki/Case_sensitivity). If the user types *EXIT* instead of *exit*, then nothing happens. One way to address this issue is by having a cascade of nested `match` statements:

Language: Python Filename: `repl.py`

```
import sys
import traceback

PROMPT = "\N{snake} "
COMMANDS = ("help", "exit", "quit")

def main():
    print('Type "help" for more information, "exit" or "quit" to finish.')
    while True:
        try:
            match input(PROMPT):
                case command if command.lower() in COMMANDS:
                    match command.lower():
                        case "help":
                            print(f"Python {sys.version}")
                        case "exit" | "quit":
                            break
        except Exception:
            traceback.print_exc(file=sys.stdout)

if __name__ == "__main__":
    main()
```

The outer `match` statement has only one `case` clause, which matches a string as long as it’s in the list of recognized commands. On the other hand, the subject of the inner `match` statement is the matched command converted to lowercase so that you can handle input regardless of its original casing. The `if` statement after the pattern is an **optional guard**, which you’ll take a closer look at later.

**Note:** Patterns are static, while guards can express arbitrary logical conditions that are checked dynamically at runtime.

The default Python REPL intercepts the [`KeyboardInterrupt`](https://realpython.com/python-built-in-exceptions/#keyboardinterrupt) exception raised in response to pressing Ctrl\+C. Additionally, it lets you quickly close the current session by pressing Ctrl\+D, which sends the [end-of-file (EOF)](https://en.wikipedia.org/wiki/End-of-file) control character. You can handle both situations as shown below:

Language: Python Filename: `repl.py`

```
import sys
import traceback

PROMPT = "\N{snake} "
COMMANDS = ("help", "exit", "quit")

def main():
    print('Type "help" for more information, "exit" or "quit" to finish.')
    while True:
        try:
            match input(PROMPT):
                case command if command.lower() in COMMANDS:
                    match command.lower():
                        case "help":
                            print(f"Python {sys.version}")
                        case "exit" | "quit":
                            break
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt")
        except EOFError:
            print()
            exit()
        except Exception:
            traceback.print_exc(file=sys.stdout)

if __name__ == "__main__":
    main()
```

Okay. Your script is slowly shaping up into a decent Python REPL. But, since you haven’t executed any Python code yet, it’s time to fix that now. Along the way, you’ll learn how Python chooses a `case` clause to execute for a given subject.

[ Remove ads](/account/join/)

### Precedence of Structural Patterns[](#precedence-of-structural-patterns "Permanent link")

So far, you’ve mainly encountered **mutually exclusive patterns** that correspond to [disjoint sets](https://en.wikipedia.org/wiki/Disjoint_sets) of subject values. As a result, you were free to arrange these patterns in any order without causing ambiguity in the matching process. However, Python also allows you to specify **overlapping patterns** that will simultaneously match the same subject. That’s where order starts to matter, as it can change the behavior of your program if you’re not careful.

Go ahead and add another `case` clause to your outer `match` statement, which will execute a Python statement:

Language: Python Filename: `repl.py`

```
import ast
import sys
import traceback

PROMPT = "\N{snake} "
COMMANDS = ("help", "exit", "quit")

def main():
    print('Type "help" for more information, "exit" or "quit" to finish.')
    while True:
        try:
            match input(PROMPT):
                case command if command.lower() in COMMANDS:
                    match command.lower():
                        case "help":
                            print(f"Python {sys.version}")
                        case "exit" | "quit":
                            break
                case statement if valid(statement):
                    exec(statement)
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt")
        except EOFError:
            print()
            exit()
        except Exception:
            traceback.print_exc(file=sys.stdout)

def valid(code):
    try:
        ast.parse(code)
        return True
    except SyntaxError:
        return False

if __name__ == "__main__":
    main()
```

If the user input doesn’t match one of your predefined commands, then you assume it might represent a line of Python code. To be sure, you define a **capture pattern**, which binds the entered value to a variable named `statement`. Next, you pass that statement to a [helper function](https://en.wikipedia.org/wiki/Wrapper_function#Helper_function) called `valid()`, which you defined below, right after the `main()` function.

This function uses the [`ast`](https://docs.python.org/3/library/ast.html) module to parse the source code and determine if it’s valid. Finally, you call [`exec()`](https://realpython.com/python-exec/) to execute the provided code snippet upon a successful match.

**Note:** Using `exec()` is considered highly unsafe because it allows for [arbitrary code execution](https://en.wikipedia.org/wiki/Arbitrary_code_execution). In practice, you should avoid calling it against user-supplied data and only use it with code that you trust!

When you give your REPL another spin, this is what you’ll get:

Language: Shell

```
$ python repl.py
Type "help" for more information, "exit" or "quit" to finish.
🐍 print("Hello, World!")
Hello, World!
🐍 name = "John Doe"
🐍 print(f"My name's {name}.")
My name's John Doe.
🐍 2 + 2
🐍 exit
```

When you call the [`print()`](https://realpython.com/python-print/) function, it works as expected, writing the provided [*Hello, World!*](https://en.wikipedia.org/wiki/%22Hello,_World!%22_program) text to the [standard output](https://en.wikipedia.org/wiki/Standard_streams#Standard_output_\(stdout\)) stream. Similarly, defining a variable seems to be working fine, as you can retrieve its current value with an [f-string](https://realpython.com/python-f-strings/) literal. At the same time, the result of the arithmetic addition, two plus two, is nowhere to be seen. Can you guess why?

It’s because `exec()` doesn’t return any value. Although your code gets executed under the curtain, it has no visible [side effects](https://en.wikipedia.org/wiki/Side_effect_\(computer_science\)). Such code represents a special kind of statement known as an [expression](https://docs.python.org/3/glossary.html#term-expression), which you can evaluate using the built-in [`eval()`](https://realpython.com/python-eval-function/) function. Unlike `exec()`, this function returns the evaluated object, which you can process further.

**Note:** The `eval()` function is equally insecure as its `exec()` counterpart, so the same rules apply.

Because **expressions** are also **statements**, but not the other way around, you can’t append another `case` clause with a suitable pattern after the existing case that is meant for handling statements. If you did, the first pattern would always succeed regardless of whether the subject is a statement or an expression, preventing the subsequent cases from running. Therefore, you must place the `case` clause for expressions *before* the `case` clause for statements.

In addition to this, you have to modify your helper function so that it can discern between statements and expressions:

Language: Python Filename: `repl.py`

```
import ast
import sys
import traceback

PROMPT = "\N{snake} "
COMMANDS = ("help", "exit", "quit")

def main():
    print('Type "help" for more information, "exit" or "quit" to finish.')
    while True:
        try:
            match input(PROMPT):
                case command if command.lower() in COMMANDS:
                    match command.lower():
                        case "help":
                            print(f"Python {sys.version}")
                        case "exit" | "quit":
                            break
                case expression if valid(expression, "eval"):
                    _ = eval(expression)
                    if _ is not None:
                        print(_)
                case statement if valid(statement, "exec"):
                    exec(statement)
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt")
        except EOFError:
            print()
            exit()
        except Exception:
            traceback.print_exc(file=sys.stdout)

def valid(code, mode):
    try:
        ast.parse(code, mode=mode)
        return True
    except SyntaxError:
        return False

if __name__ == "__main__":
    main()
```

The extra parameter, which you now must pass explicitly to your `valid()` function, lets you parse the code in either the `"exec"` or `"eval"` mode:

> The *mode* argument specifies what kind of code must be compiled; it can be `'exec'` if *source* consists of a sequence of statements, `'eval'` if it consists of a single expression, \[…\] ([Source](https://docs.python.org/3/library/functions.html#compile))

Also notice that you assign the result of `eval()` to an underscore (`_`) variable, which you print only when the associated expression evaluates to anything other than `None`. This is consistent with the standard REPL, which automatically stores the last evaluated expression in a [special variable](https://realpython.com/python-repl/#using-the-_-special-variable) for your convenience:

Language: Shell

```
$ python repl.py
Type "help" for more information, "exit" or "quit" to finish.
🐍 print(None)
None
🐍 (lambda: None)()
🐍 2 + 2
4
🐍 _ * 2
8
🐍 _ * 2
16
```

You can still execute statements as before, like calling the `print()` function, as well as evaluate expressions. If an expression evaluates to `None`, such as the `lambda` expression above, then you don’t show it. Additionally, the special variable (`_`) allows you to reuse the value of the last expression.

It was briefly mentioned before that the underscore is a soft keyword, which plays a role in pattern matching. Now, it’s time to delve deeper into its use.

[ Remove ads](/account/join/)

### Default Case and the Wildcard Pattern[](#default-case-and-the-wildcard-pattern "Permanent link")

Unlike many other programming languages, Python allows the `case` clauses in pattern matching to remain **non-exhaustive**. In other words, you don’t have to handle all possible cases in a `match` statement. It’s up to you whether you want to catch unmatched patterns in a **default case** or not. For example, if a user of your custom REPL types an unknown command that isn’t a valid statement or expression, then nothing gets executed:

Language: Shell

```
$ python repl.py
Type "help" for more information, "exit" or "quit" to finish.
🐍 This is not a known command or valid Python.
🐍 exit
```

The REPL ignores syntactically incorrect Python and moves on because none of the patterns in your `case` clauses matches the subject. However, it’d be more considerate to the user to let them know about a syntax error in their input.

For this purpose, you can specify the **catch-all case** by using a **wildcard pattern** (`_`) that will *always* match unless one of your earlier patterns already matched the subject. Because it serves the purpose of a fallback case, it has to go last in the sequence of `case` clauses:

Language: Python Filename: `repl.py`

```
# ...

def main():
    print('Type "help" for more information, "exit" or "quit" to finish.')
    while True:
        try:
            match input(PROMPT):
                case command if command.lower() in COMMANDS:
                    match command.lower():
                        case "help":
                            print(f"Python {sys.version}")
                        case "exit" | "quit":
                            break
                case expression if valid(expression, "eval"):
                    _ = eval(expression)
                    if _ is not None:
                        print(_)
                case statement if valid(statement, "exec"):
                    exec(statement)
                case _:
                    print("Please type a command or valid Python")
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt")
        except EOFError:
            print()
            exit()
        except Exception:
            traceback.print_exc(file=sys.stdout)

# ...
```

With this small change, you made your pattern matching exhaustive. In other words, you now cover all possible cases, even if there are infinitely many. This guarantees that at least one of the clauses will run, irrespective of the subject.

**Note:** If you include the default `case _:` clause, then it must go at the bottom of the corresponding `match` block. Failing to do so will make the remaining clauses unreachable, resulting in a syntax error.

Remember that the underscore (`_`) behaves like a **keyword** within a structural pattern. Therefore, it *never* binds the subject to a name, so you won’t be able to refer to it inside or outside the respective `case` clause. That’s good news because the wildcard pattern won’t collide with your special variable bearing the same name, which your REPL manages.

Furthermore, because of the lack of name binding in the wildcard pattern, you can reuse the underscore several times as a **subpattern** to discard certain elements of other patterns. Take a look at this hypothetical example:

Language: Python

```
for user in fetch_users():
    match user:
        case User(_, _, age) if age < 18:
            print(f"Underage: {user}")
        case User(_, "Smith", _):
            print(f"Smith family member: {user}")
```

Here, the underscores are another incarnation of the wildcard pattern. As you can see, the wildcard pattern doesn’t always have to appear in the default catch-all case at the end of a `match` statement. Instead, it tells Python to ignore specific values without binding them to any variable while letting you reuse the underscore. That isn’t the case with regular capture patterns, which don’t allow repeated variables in their definition.

Alright. That wraps up this example. If you’d like to improve your Python REPL, then consider adding support for **multiline code blocks**. You can also integrate [readline-like](https://en.wikipedia.org/wiki/GNU_Readline) editing capabilities, [command history](https://en.wikipedia.org/wiki/Command_history), and contextual [autocomplete](https://en.wikipedia.org/wiki/Autocomplete) triggered by pressing the Tab key. Below, you’ll find a sample implementation of these features:

Complete Source Code for the Python REPLShow/Hide

Language: Python Filename: `repl_enhanced.py`

```
import ast
import atexit
import readline
import rlcompleter
import sys
import traceback
from dataclasses import dataclass, field
from pathlib import Path
from typing import Literal

STANDARD_PROMPT = ">>> "
INDENTED_PROMPT = "... "
TAB_WIDTH = 4
TAB = TAB_WIDTH * " "
COMMANDS = ("help", "exit", "quit")
PYTHON_HISTORY = Path.home() / ".python_history"

@dataclass
class Console:
    indentation_level: int = 0

    def __post_init__(self) -> None:
        readline.parse_and_bind("tab: complete")
        readline.set_completer(rlcompleter.Completer().complete)
        if PYTHON_HISTORY.exists():
            readline.read_history_file(PYTHON_HISTORY)
        atexit.register(readline.write_history_file, PYTHON_HISTORY)

    @property
    def prompt(self) -> str:
        if self.indentation_level > 0:
            return INDENTED_PROMPT
        else:
            return STANDARD_PROMPT

    @property
    def indentation(self) -> str:
        return TAB * self.indentation_level

    def indent(self) -> None:
        self.indentation_level += 1

    def dedent(self) -> None:
        if self.indentation_level > 0:
            self.indentation_level -= 1

    def reindent(self, line: str) -> None:
        num_leading_spaces = len(line) - len(line.lstrip())
        new_indentation_level = num_leading_spaces // TAB_WIDTH
        if new_indentation_level < self.indentation_level:
            self.indentation_level = new_indentation_level

    def input(self) -> str:
        def hook():
            readline.insert_text(self.indentation)
            readline.redisplay()

        try:
            readline.set_pre_input_hook(hook)
            result = input(self.prompt)
            return result
        finally:
            readline.set_pre_input_hook()

@dataclass
class CodeBlock:
    lines: list[str] = field(default_factory=list)

    def execute(self) -> None:
        exec("\n".join(self.lines), globals())
        self.lines = []

def main() -> None:
    print('Type "help" for more information, "exit" or "quit" to finish.')
    console = Console()
    block = CodeBlock()
    while True:
        try:
            match console.input():
                case command if command.lower() in COMMANDS:
                    match command.lower():
                        case "help":
                            print(f"Python {sys.version}")
                        case "exit" | "quit":
                            break
                case line if line.endswith(":"):
                    block.lines.append(line)
                    console.reindent(line)
                    console.indent()
                case line if line.lstrip() == "":
                    console.reindent(line)
                    console.dedent()
                    if console.indentation_level == 0 and block.lines:
                        block.execute()
                case line if console.indentation_level > 0:
                    block.lines.append(line)
                case expression if valid(expression, "eval"):
                    _ = eval(expression)
                    if _ is not None:
                        print(_)
                case statement if valid(statement, "exec"):
                    exec(statement)
                case _:
                    print("Please type a command or valid Python")
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt")
            console.indentation_level = 0
            block.lines = []
        except EOFError:
            print()
            sys.exit()
        except Exception:
            traceback.print_exc(file=sys.stdout)
            console.indentation_level = 0
            block.lines = []

def valid(code: str, mode: Literal["eval", "exec"]) -> bool:
    try:
        ast.parse(code, mode=mode)
        return True
    except SyntaxError:
        return False

if __name__ == "__main__":
    main()
```

Now you’re ready to dive deeper into various types of structural patterns in Python. You’ll start by taking a look at some basic patterns to whet your appetite.

## Exploring Basic Pattern Types Supported by Python[](#exploring-basic-pattern-types-supported-by-python "Permanent link")

In previous sections of this tutorial, you were briefly introduced to different types of structural patterns without exploring them in detail. In this section, you’ll delve deeper into some of the fundamental pattern types that Python supports, including literal patterns, value patterns, and capture patterns.

### Literal Pattern[](#literal-pattern "Permanent link")

The first type of structural pattern that you’ll look at is the [literal pattern](https://peps.python.org/pep-0635/#literal-patterns), which is arguably the most straightforward of them all. It generally lets you restrict the *value* of the subject instead of its type or structure. Consequently, literal patterns alone can be suitable for emulating the `switch` statement in Python if you don’t mind deviating from earlier recommendations.

For example, here’s a sample implementation of a [custom interpreter](https://realpython.com/python-shebang/#how-can-you-use-a-shebang-with-a-custom-interpreter-in-python) of a certain [esoteric programming language](https://en.wikipedia.org/wiki/Esoteric_programming_language), which is based on literal patterns:

Language: Python

```
>>> import sys

>>> def interpret(code, num_bytes=2**10):
...     stack, brackets = [], {}
...     for i, instruction in enumerate(code):
...         match instruction:
...             case "[": stack.append(i)
...             case "]": brackets[i], brackets[j] = (j := stack.pop()), i
...     memory = bytearray(num_bytes)
...     pointer = ip = 0
...     while ip < len(code):
...         match code[ip]:
...             case ">": pointer += 1
...             case "<": pointer -= 1
...             case "+": memory[pointer] += 1
...             case "-": memory[pointer] -= 1
...             case ".": print(chr(memory[pointer]), end="")
...             case ",": memory[pointer] = ord(sys.stdin.buffer.read(1))
...             case "[" if memory[pointer] == 0: ip = brackets[ip]
...             case "]" if memory[pointer] != 0: ip = brackets[ip]
...         ip += 1
...
>>> interpret("""
...   +++++++++++[>++++++>+++++++++>++++++++>++++>+++>+<<<<<<-]>+++
...   +++.>++.+++++++..+++.>>.>-.<<-.<.+++.------.--------.>>>+.>-.
... """)
Hello, World!
```

All patterns in both `match` statements are analogous to [string literals](https://en.wikipedia.org/wiki/String_literal) that correspond to different instructions, such as moving the pointer to the next memory cell (`">"`) in this particular programming language. Python compares the subject against each of your patterns to determine which branch of code to execute. The subject must match a given pattern *exactly* to make it succeed.

Strings aren’t the only [literals](https://en.wikipedia.org/wiki/Literal_\(computer_programming\)) you can use in this kind of structural pattern. Python supports a few more data types, including numbers and [Boolean values](https://realpython.com/python-boolean/). Here’s a more detailed breakdown of the available literal patterns:

| Data Type | Literal Pattern Example | Matched By |
| --- | --- | --- |
| `bytes` | `b"\xf0\x9f\x90\x8d"` | Equality |
| `str` | `"admin"` | Equality |
| `int` | `-42` | Equality |
| `float` | `4.2` | Equality |
| `complex` | `4.2 + 2.3j` | Equality |
| `bool` | `True`, `False` | Identity |
| `NoneType` | `None` | Identity |

These are the only data types with corresponding literal patterns in Python. The counterparts of other kinds of literals, such as the [list literal](https://realpython.com/python-list/#creating-lists-through-literals), are considered separate types of patterns, which you’ll get familiar with soon.

Notice that [f-strings](https://realpython.com/python-f-strings/) are missing from the list because they don’t represent exact values known upfront. Instead, f-strings typically involve [string interpolation](https://realpython.com/python-string-interpolation/), which must be done at runtime. So, when you try to make a literal pattern out of an f-string, you’ll encounter a syntax error:

Language: Python

```
>>> command = "read"
>>> match input("Type the command: "):
...     case f"help {command}":
...         print("Showing help on the 'read' command")
...
  File "<stdin>", line 2
SyntaxError: patterns may only match literals and attribute lookups
```

Fortunately, this isn’t an issue, as you’ll discover other types of structural patterns that can fill this gap.

When you look closely at the table above, you’ll notice a slight inconsistency. While most literal patterns use the **equality test operator** (`==`) to compare the *values* of the subject and the pattern, there are a few notable exceptions. In particular, the three [singletons](https://realpython.com/primer-on-python-decorators/#creating-singletons), `True`, `False`, and `None`, use **identity comparison** (`is`) instead of value comparison to avoid surprising behavior, which could lead to subtle defects.

**Note:** You can read the tutorial on [comparing objects in Python](https://realpython.com/python-is-identity-vs-equality/) to learn more about the differences between equality and identity checks.

When you compare objects by value in Python, their data types are sometimes ignored. Take the following as an example:

Language: Python

```
>>> 1 == "1"
False

>>> 1 == 1.0 == 1.0 + 0.0j == True
True
```

In the first case, you’re trying to compare a number to a string, which fails because both objects have drastically different internal representations. However, in the second case, you’re dealing with four objects of compatible types that share the same value. For instance, even though the internal representation of a [complex number](https://realpython.com/python-complex-numbers/), such as `1.0 + 0.0j`, is different than that of an integer `1`, they contain the same numeric value.

As a result of that, literal patterns may succeed even if they aren’t exactly of the same type as the subject:

Language: Python

```
>>> def is_adult(age):
...     match age:
...         case 18:
...             return True
...         case _:
...             return False
...
>>> is_adult(18)
True
>>> is_adult(18.0)
True
>>> is_adult(18.0 + 0.0j)
True
```

This function takes an age as an argument and checks if it’s eighteen, returning `True` if it is and `False` otherwise. Notice how calling the function with different numeric types still results in a match.

If you want to ensure **strict type checking**, then use a **class pattern** by explicitly wrapping your literal pattern in a relevant type constructor:

Language: Python

```
>>> def is_adult(age):
...     match age:
...         case int(18):
...             return True
...         case _:
...             return False
...
>>> is_adult(18)
True
>>> is_adult(18.0)
False
>>> is_adult(18.0 + 0.0j)
False
```

Now, only an integer matches the structural pattern even though the other two numbers carry the same value.

It could be argued that comparing numbers by value is a sensible thing to do. On the other hand, with `True` and `1` being considered equal in Python, this could lead to unexpected results. Therefore, literal patterns `True`, `False`, and `None` always compare the subject by identity:

Language: Python

```
>>> def get_http_status(is_admin):
...     match is_admin:
...         case True:
...             return "200 OK"
...         case False:
...             return "403 Forbidden"
...         case None:
...             return "302 Found"
...         case _:
...             return "400 Bad Request"
...

>>> for is_admin in 1, 1.0, 1.0 + 0.0j, True:
...     print(f"{is_admin!r:>6}:", get_http_status(is_admin))
...
     1: 400 Bad Request
   1.0: 400 Bad Request
(1+0j): 400 Bad Request
  True: 200 OK
```

The `bool` data type is a subclass of `int` in Python, making all four subject values in the [`for` loop](https://realpython.com/python-for-loop/) above equal. But, because Boolean literal patterns use identity checks, none of the provided numeric subjects matches the `True` pattern, causing the function to return the [HTTP status 400](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/400).

Note that the reverse isn’t true! If a subject happens to be a Boolean value but your pattern is a numeric literal like `1.0`, then the match will succeed on the grounds of value equality:

Language: Python

```
>>> age = 21
>>> match age > 18:
...     case 1.0:
...         print("You're an adult.")
...
You're an adult.
```

Here, the subject is a Boolean expression evaluating to `True`, which matches the literal pattern `1.0` since their values are equal.

So far in this section, you’ve seen literal patterns of the same type used exclusively, effectively working as an analog to the `switch` statement. However, you can mix and match different types of literal patterns in a single `match` statement if you want to:

Language: Python

```
>>> def describe(value):
...     match value:
...         case "\u03c0":
...             print("Greek letter Pi")
...         case 3:
...             print("A rough approximation of Pi")
...         case 3.14:
...             print("A slightly better approximation of Pi")
...

>>> describe("π")
Greek letter Pi

>>> describe(3)
A rough approximation of Pi

>>> describe(3.14)
A slightly better approximation of Pi
```

This function uses literal patterns of three distinct types: string, integer, and float. Such a construct more closely resembles the idea behind structural patterns since it matches the subject based on its type *and* value rather than just specific values.

Literal patterns are fairly intuitive and quick to start with, but they suffer from poor readability and fragility. Because literals aren’t always associated with human-readable names and can’t be reused, they essentially fit the definition of the [magic number](https://en.wikipedia.org/wiki/Magic_number_\(programming\)) anti-pattern, including all the downsides that come with it. In the next section, you’ll learn about another structural pattern that addresses some of these issues.

[ Remove ads](/account/join/)

### Value Pattern[](#value-pattern "Permanent link")

In principle, you can represent values in a programming language using **literals**, **variables**, **constants**, or **expressions** that need evaluation. You’ve seen literals in the previous section, and you’ll cover variables in the next one when you read about the capture pattern. At the same time, you know that structural patterns aren’t expressions in Python, so that leaves only constants.

That said, Python doesn’t allow for defining true [constants](https://en.wikipedia.org/wiki/Constant_\(computer_programming\)) in the traditional sense. Although several idioms for [mimicking constants in Python](https://realpython.com/python-constants/) have emerged over the years, they rely on naming conventions rather than enforced language rules. As a result, there’s no syntactical difference between variables and constants in Python:

Language: Python

```
PI = 3.14  # This is intended as a global constant. Please don't modify it!
pie = "apple"  # This is a short-lived variable, so it's okay to change it.
```

You often declare constants using uppercase letters as a visual cue to make them stand out, but otherwise, there’s no safety mechanism to prevent anyone from changing their values at runtime. Python programmers rely on mutual trust by respecting the conventions and unwritten rules.

Because of this syntactical limitation, you shouldn’t use previously declared variables or constants as structural patterns, as they won’t behave as you might expect them to. Recall the custom Python REPL that you built earlier. Say you wanted to follow good programming practices and keep the individual commands in separate constants to improve code readability and maintainability. You start by specifying the `help` command:

Language: Python

```
>>> HELP_COMMAND = "help"

>>> match input("Type your command: "):
...     case HELP_COMMAND:
...         print("Showing help.")
...
Type your command: exit
Showing help.

>>> HELP_COMMAND
'exit'
```

Although this piece of code looks syntactically correct, it doesn’t work as intended. Notice how your pattern succeeds even though you typed an unrecognized `exit` command, which isn’t supposed to match. To make matters worse, you’ve just overwritten `HELP_COMMAND` with the string `"exit"`.

The root cause of the problem becomes clearer when you add a second `case` clause with another command:

Language: Python

```
>>> HELP_COMMAND = "help"
>>> EXIT_COMMAND = "exit"

>>> match input("Type your command: "):
...     case HELP_COMMAND:
...         print("Showing help.")
...     case EXIT_COMMAND:
...         exit()
...
  File "<stdin>", line 2
SyntaxError: name capture 'HELP_COMMAND' makes remaining patterns unreachable
```

There’s a syntax error now. Both patterns are examples of capture patterns, which will match any subject. Since the first pattern always matches, the second one has no chance of ever running. Additionally, the first pattern *captures* or binds the subject’s value to the specified name, effectively redeclaring your original constant.

You can work around this limitation by using **guards**, which you’ll dive into in more detail later:

Language: Python

```
>>> HELP_COMMAND = "help"
>>> EXIT_COMMAND = "exit"

>>> match input("Type your command: "):
...     case command if command == HELP_COMMAND:
...         print("Showing help.")
...     case command if command == EXIT_COMMAND:
...         exit()
...     case _:
...         print("Unknown command")
...
Type your command: quit
Unknown command
```

You still use capture patterns, but you augment them with conditional statements to ensure that the patterns only match when their respective guard condition is true.

This works fine but leads to overly verbose code. Fortunately, there’s a better way involving a **value pattern**, which lets you recognize variables that should be treated as constants. These typically belong to some [namespace](https://realpython.com/python-namespaces-scope/), such as a [class](https://realpython.com/python-classes/), [enum](https://realpython.com/python-enum/), or a Python [module](https://realpython.com/python-modules-packages/), which you can access with the dot operator:

Language: Python

```
>>> import enum
>>> import module  # Some user-defined module in the current directory

>>> class ClassCommand:
...     HELP = "help"
...
>>> class EnumCommand(enum.StrEnum):
...     EXIT = "exit"
...
>>> match input("Type your command: "):
...     case ClassCommand.HELP:
...         print("Showing help.")
...     case EnumCommand.EXIT:
...         exit()
...     case module.DebugPlugin.RELOAD:
...         print("Reloading the current session.")
...
Type your command: reload
Reloading the current session.
```

As long as you refer to a member by its [fully qualified name](https://en.wikipedia.org/wiki/Fully_qualified_name), which includes at least one instance of the dot operator, then it’s clear that you’re defining a [value pattern](https://peps.python.org/pep-0635/#value-patterns) instead of a capture one. However, had you imported a member into the global namespace by using the [`from ... import ...`](https://realpython.com/python-modules-packages/#from-module_name-import-names) syntax, you’d be back at square one with a capture pattern.

**Note:** In this case, you’ve defined your `EnumCommand` class as a descendant of [`StrEnum`](https://docs.python.org/3/library/enum.html#enum.StrEnum), which is a specialized form of enumeration. Unlike regular enums, which compare their members by identity, `StrEnum` allows you to compare its members by value against strings. This makes the above example a bit cleaner.

Remember that a value pattern looks like **attribute access**. If you tried calling a function or a method using its fully qualified name, then you’d no longer be specifying a value pattern:

Language: Python

```
>>> class Commands:
...     @staticmethod
...     def help(self):
...         return "help"
...
>>> match input("Type your command: "):
...     case Commands.help():
...         print("Showing help.")
...
Type your command: help
Traceback (most recent call last):
  File "<input>", line 2, in <module>
    case Commands.help():
         ^^^^^^^^^^^^^^^
TypeError: called match pattern must be a class
```

You might think that the above code would define a value pattern based on the value returned from the [static method](https://realpython.com/instance-class-and-static-methods-demystified/#static-methods), `.help()`. However, the trailing pair of parentheses always indicates a **class pattern**, which expects a class constructor instead. That makes sense. After all, you’re defining a structural pattern rather than invoking a callable object!

Okay. You’ve seen literal patterns, value patterns, and a few examples of capture patterns. Now, it’s time to systematize what you know about capture patterns before moving on to more advanced patterns.

[ Remove ads](/account/join/)

### Capture Pattern[](#capture-pattern "Permanent link")

A [capture pattern](https://peps.python.org/pep-0635/#capture-patterns) resembles the typical variable declaration. It must be a valid and preferably unique Python identifier that shouldn’t mask existing symbols in your enclosing [scopes](https://realpython.com/python-scope-legb-rule/). It’ll always match the subject, binding its value to the designated name, which you can access as a variable in the current scope.

By default, a capture pattern defines its own **local variable**, which means that the captured name will continue to live outside your `match` block:

Language: Python

```
>>> match input("Type your command: "):
...     case command:
...         print(f"Calling the {command!r} command.")
...
Type your command: help
Calling the 'help' command.
>>> command
'help'
```

Notice how pattern matching defined a new variable, `command`, named after your capture pattern. This variable holds the value of the subject captured by your pattern.

**Note:** If a capture pattern shares its name with a variable declared with either the [global](https://realpython.com/python-use-global-variable-in-function/) or [nonlocal](https://realpython.com/python-scope-legb-rule/#the-nonlocal-statement) keyword, then it won’t create a local variable. Instead, it’ll overwrite the corresponding variable living in the outer scope.

Simultaneously, if a capture pattern doesn’t succeed—for example, because a previous pattern already matched the subject—then it won’t define any new variables. So, you won’t be able to refer to it afterward:

Language: Python

```
>>> match input("Type your command: "):
...     case "help":
...         print("Showing help.")
...     case command:
...         print(f"Calling the {command!r} command.")
...
Type your command: help
Showing help.
>>> command
Traceback (most recent call last):
  ...
NameError: name 'command' is not defined
```

You should be prepared for this scenario, for example, by defining the variable in each `case` clause with relevant values or initializing it beforehand.

A plain capture pattern will make the subsequent `case` clauses unreachable because it matches the subject unconditionally:

Language: Python

```
>>> match input("Type your command: "):
...     case command:
...         print(f"Calling the {command!r} command.")
...     case "help":
...         print("Showing help.")
  File "<input>", line 2
SyntaxError: name capture 'command' makes remaining patterns unreachable
```

To fix this, consider introducing guards to narrow down the set of values that would make your capture pattern match the subject. When you do, you can reuse the same name for capture patterns across multiple `case` clauses as long as the logical conditions remain unambiguous:

Language: Python

```
>>> match input("Type your command: "):
...     case command if command in ("help", "exit"):
...         print("Calling a predefined command.")
...     case command:
...         print(f"Calling the {command!r} command.")
...
Type your command: quit
Calling the 'quit' command.
```

Both capture patterns use the same variable name, `command`, but the first one is qualified with a conditional statement. The second pattern will succeed only when the logical expression next to the first pattern evaluates to `False`.

As a quick reminder, be sure to avoid capture patterns that share their name with a variable you defined previously:

Language: Python

```
>>> command = input("Type your command: ")
Type your command: exit
>>> command
'exit'
>>> match command.upper():
...     case command:
...         print(f"Calling the {command!r} command.")
...
Calling the 'EXIT' command.
>>> command
'EXIT'
```

Here, you store the raw user input in a variable named `command`, which initially holds the string `"exit"`. Later, you use the same name as a capture pattern, which leads to overwriting your original variable with the string `"EXIT"` in all caps. Note that this only happens when the pattern succeeds.

Capture patterns are the cornerstone of **destructuring**. You’ll often use them as **subpatterns** to extract pieces of information from complex objects that you want to decompose. Here’s an example that illustrates the deconstruction of an object representing a common [Git](https://realpython.com/python-git-github-intro/) command:

Language: Python

```
>>> from dataclasses import dataclass
>>> from typing import Self

>>> @dataclass
... class Command:
...     name: str
...     options: tuple[str, ...]
...     subcommand: None | Self = None
...
>>> command = Command(
...     name="git",
...     options=(),
...     subcommand=Command(
...         name="commit",
...         options=("-a", "-m", "'Initial commit'"),
...     )
... )

>>> match command:
...     case Command("git", _, Command(subcommand, options)):
...         print(f"{subcommand=}\n{options=}")
...
subcommand='commit'
options=('-a', '-m', "'Initial commit'")
```

You define the `Command` [data class](https://realpython.com/python-data-classes/) and its concrete `command` instance, which describes the [`git commit`](https://git-scm.com/docs/git-commit) subcommand. The highlighted line combines several patterns in one compound pattern comprised of the following:

- **Literal pattern:** `"git"`

- **Wildcard pattern:** `_`

- **Class pattern:** `Command()`

- **Capture patterns:** `subcommand`, `options`

When the entire pattern succeeds, then both of your capture patterns will define local variables that you can use to decide how you want to handle the command.

Suppose you wanted to specify a pattern that will only match when the main command and the subcommand are identical. Your first attempt at doing so may look like this:

Language: Python

```
>>> match command:
...     case Command(subcommand, _, Command(subcommand, options)):
...         print("The main command and subcommand are the same")
  File "<input>", line 2
SyntaxError: multiple assignments to name 'subcommand' in pattern
```

You declare two capture patterns with the same name, `subcommand`, in a single `case` clause. Unfortunately, this doesn’t work because structural patterns in Python can’t do runtime evaluation. To determine if two attributes are equal, you should define a guard with the desired condition next to your pattern:

Language: Python

```
>>> match command:
...     case Command(main, _, Command(subcommand, _)) if main == subcommand:
...         print("The main command and subcommand are the same")
```

Once a capture pattern binds some value to a name, you can’t reuse that name within the same pattern, or else you’ll get a syntax error. This doesn’t apply to the wildcard pattern (`_`), which doesn’t bind any names, letting you reuse it to discard multiple values.

Alright. You now have a few structural patterns under your belt. While they can help you in basic scenarios, you’ll need to expand your toolkit to tackle more demanding projects. Next up, you’ll delve into some advanced structural patterns.

[ Remove ads](/account/join/)

## Digging Into More Advanced Structural Patterns[](#digging-into-more-advanced-structural-patterns "Permanent link")

The patterns that you’ll examine in this section will let you match and destructure popular collection types, as well as instances of classes. More specifically, you’ll learn about the sequence and mapping patterns. You’ll also learn that Python doesn’t support their [set](https://realpython.com/python-sets/) counterparts.

### Sequence Pattern[](#sequence-pattern "Permanent link")

You’ll take a look at the [sequence pattern](https://peps.python.org/pep-0635/#sequence-patterns) first, which closely resembles **iterable unpacking**. With this kind of structural pattern, you can assign values from a list or tuple to multiple variables in a single line of code while controlling your execution flow.

Say you wanted to model the Git commands from the previous section as a sequence of strings comprising the subcommand as well as the optional parameters. Here’s a utility function that can parse user input using a [regular expression](https://realpython.com/regex-python/), which turns a line of text into a list of substrings:

Language: Python

```
>>> import re

>>> def parse(command):
...     return re.split(r"\s+(?=(?:[^']*'[^']*')*[^']*$)", command)
...

>>> parse("git commit -a -m 'Initial commit'")
['git', 'commit', '-a', '-m', "'Initial commit'"]
```

You can ignore the regular expression above, which only serves as an example. The main point of this function is to split a string at every occurrence of one or more spaces (`\s+`) unless that space is enclosed within single quotes.

**Note:** You can alternatively use [`shlex.split()`](https://docs.python.org/3/library/shlex.html#shlex.split) in the standard library to parse the command. This gives a similar but not identical result.

With this function in place, parsing commands and their arguments becomes straightforward when you use pattern matching:

Language: Python

```
>>> match parse(input("Type your command: ")):
...     case ["git"]:
...         print("Showing the list of available Git subcommands.")
...     case ["git", "--version"]:
...         print("Showing the version of your Git client.")
...     case [_, subcommand, *options]:
...         print(f"{subcommand=}, {options=}")
...
Type your command: git status --long --verbose
subcommand='status', options=['--long', '--verbose']
```

You can quickly recognize a sequence pattern by the presence of square brackets around the comma-delimited list of items. As with other types of compound patterns, you can nest subpatterns in a sequence pattern, including literal patterns, wildcard patterns, capture patterns, other sequence patterns, and more.

While using square brackets works best, there are three alternative notations for sequence patterns, which in most cases you can use interchangeably. They all mimic the iterable unpacking syntax:

1. **Square brackets:** `["git", "--version"]`

2. **Round brackets:** `("git", "--version")`

3. **No brackets:** `"git", "--version"`

There are some exceptions. To denote an **empty sequence**, you *must* use one of the two forms of brackets, as it’s not possible to express zero elements without them:

Language: Python

```
match subject:
    case []:
        print("This will match the subject if it's an empty sequence.")
    case ():
        print("This is equivalent to the above.")
```

Additionally, when the sequence contains only **one item**, then you can omit the brackets, but you also have to append a trailing comma, just like with the tuple notation:

Language: Python

```
match subject:
    case item,:
        print("This will extract the only element of a sequence subject.")
    case item:
        print("This will bind the entire subject to the capture pattern.")
```

Notice how the first pattern ends with a comma, whereas the second pattern doesn’t. This distinction is necessary to indicate whether you want to match a sequence with just one element—and extract it into a variable—or if you prefer to capture the whole subject regardless of whether it’s a sequence or not.

On the other hand, if you do want to surround the only item with brackets, then you have to use square brackets. If you used round brackets, then you’d be defining a regular capture pattern and not a sequence one:

Language: Python

```
match subject:
    case [item]:
        print("This is a sequence pattern.")
    case (item):
        print("This is a capture pattern. It'll match everything!")
```

In other words, the round brackets wrapping a single item are completely ignored. That’s intentional in order to keep the sequence pattern notation consistent with tuples.

**Note:** If you’re wondering which notation to follow, then stick to the square brackets one. It’ll cause you the least amount of headaches down the line.

So, which objects can become the subject of a sequence pattern? Despite some similarities to iterable unpacking, sequence patterns don’t play well with all [iterables](https://realpython.com/python-iterators-iterables/#getting-to-know-python-iterables). They only match a small set of [Python sequences](https://realpython.com/python-sequences/), including the following built-in types and classes from the standard library:

- [`tuple()`](https://realpython.com/python-tuple/)

- [`list()`](https://realpython.com/python-list/)

- [`range()`](https://realpython.com/python-range/)

- [`memoryview()`](https://docs.python.org/3/library/stdtypes.html#memoryview)

- [`array.array()`](https://realpython.com/python-array/)

- [`collections.deque()`](https://realpython.com/python-deque/)

- [`collections.namedtuple()`](https://realpython.com/python-namedtuple/)

You can also use a sequence pattern to match instances of user-defined derivatives of [`Sequence`](https://realpython.com/python-sequences/#using-the-abstract-base-class-collectionsabcsequence) and [`MutableSequence`](https://realpython.com/python-sequences/#requirements-for-defining-a-user-defined-mutable-sequence) abstract base classes. Additionally, sequence patterns will match objects that you built with a [list comprehension](https://realpython.com/list-comprehension-python/).

At the same time, you’ll find `str()`, `bytes()`, and [`bytearray()`](https://realpython.com/python-bytearray/#the-bytearray-constructor) among the **unsupported sequence types**. This may surprise you, given that all of them satisfy the sequence protocol, and you can unpack their instances into separate bytes or characters:

Language: Python

```
>>> first, *_, last = "¿Cómo estás hoy?"
>>> first
'¿'
>>> last
'?'
```

However, they’re also standalone objects, which you could consider [scalars](https://en.wikipedia.org/wiki/Scalar_processor#Scalar_data_type). Due to this dual nature, sequence patterns never match these few data types to avoid potential ambiguity:

Language: Python

```
>>> match "¿Cómo estás hoy?":
...     case first, *_, last:
...         print(f"{first=}, {last=}")
...     case default:
...         print("Not matched:", type(default))
...
Not matched: <class 'str'>
```

Even though the syntax of an unpacking assignment and destructuring are identical, they behave differently. The sequence pattern doesn’t succeed in this case because the subject is a string.

Notice how sequence patterns support **extended unpacking** through the use of the star operator (`*`). In the example above, you ignore elements located between the first and the last index by using a wildcard pattern (`_`). If you wanted to bind them to a variable, then you’d use a capture pattern instead:

Language: Python

```
>>> match list("¿Cómo estás hoy?"):
...     case first, *middle, last:
...         print(f"{first=}")
...         print(f"{middle=}")
...         print(f"{last=}")
...
first='¿'
middle=['C', 'ó', 'm', 'o', ' ', 'e', 's', 't', 'á', 's', ' ', 'h', 'o', 'y']
last='?'
```

The `middle` variable contains a list of characters that were captured. Note that you can have at most one starred expression in your sequence pattern, allowing you to capture multiple elements. Simultaneously, you don’t need any other capture patterns if you just want to capture *all* items of a sequence:

Language: Python

```
>>> match list("¿Cómo estás hoy?"):
...     case [*all_items]:
...         print(all_items)
...
['¿', 'C', 'ó', 'm', 'o', ' ', 'e', 's', 't', 'á', 's', ' ', 'h', 'o', 'y', '?']
```

This is different from a plain capture pattern, which would match any data type.

Going back to the wildcard pattern again, it can also help when you don’t know the exact size of your sequence:

Language: Python

```
match subject:
    case [first, second, *_]:
        print("This will match sequences of length two or more.")
```

Here, you bind the first two elements and ignore the rest as necessary. Otherwise, if your sequence pattern didn’t use the star-underscore syntax (`*_`) at the end, then it’d only match *pairs* while disregarding longer sequences:

Language: Python

```
>>> cursor_position = (765, 432, 0)
>>> match cursor_position:
...     case [x, y]:
...         print(f"{x=}, {y=}")
...     case _:
...         print("Cursor position is not a two-tuple.")
...
Cursor position is not a two-tuple.
```

The pattern `[x, y]` expects exactly two values in the sequence, but your cursor coordinates have three, so the pattern fails.

**Note:** For the record, it’s worth noting a few widely used iterables that aren’t sequences, but that you might intuitively expect to match against a sequence pattern. They include:

- Iterators like [`enumerate()`](https://realpython.com/python-enumerate/), [`map()`](https://realpython.com/python-map-function/), [`filter()`](https://realpython.com/python-filter-function/), and [`zip()`](https://realpython.com/python-zip-function/)

- [Generators](https://realpython.com/introduction-to-python-generators/), such as [`itertools.cycle()`](https://realpython.com/python-itertools/#itertoolscycle-example), and [generator expressions](https://realpython.com/introduction-to-python-generators/#building-generators-with-generator-expressions)

- User-defined iterables and iterators unless they’re sequences

Remember that sequence patterns can only match a few sequence types listed earlier.

A sequence pattern will match *any* of the supported sequences. If you want to impose additional restrictions on the sequence type, then use a class pattern as you did before to ensure stricter type checking of literal patterns:

Language: Python

```
>>> def flip(pair):
...     match pair:
...         case list([x, y]):
...             return [y, x]
...         case tuple([x, y]):
...             return y, x
...         case _:
...             raise TypeError("Unsupported type")
...
>>> flip([1, 2])
[2, 1]
>>> flip((1, 2))
(2, 1)
```

Writing a concrete sequence type around the pattern requires additional effort but makes your code a bit more explicit.

Sequence patterns have a few quirks but are undoubtedly a powerful tool. Next up, you’ll learn about the mapping pattern, which is another advanced structural pattern.

[ Remove ads](/account/join/)

### Mapping Pattern[](#mapping-pattern "Permanent link")

Dictionaries, along with other [Python mappings](https://realpython.com/python-mappings/), are among one of the most important data types, offering instant access to values based on unique keys. Python uses them everywhere, from tracking object attributes and implementing namespaces to organizing imported modules. You often use dictionaries in your own code to store and manage data.

Therefore, it’s essential for Python to support [mapping patterns](https://peps.python.org/pep-0635/#mapping-patterns) in structural pattern matching. They can be especially helpful in consuming [REST APIs](https://realpython.com/api-integration-in-python/) that serve JSON responses, which you can then [deserialize](https://realpython.com/python-serialize-data/) to Python dictionaries.

Suppose you modeled your Git commands using dictionaries instead of data classes. You can quickly convert the `git commit` command, which you defined previously, to a dictionary with [`asdict()`](https://docs.python.org/3/library/dataclasses.html#dataclasses.asdict):

Language: Python

```
>>> from dataclasses import asdict, dataclass
>>> from typing import Self

>>> @dataclass
... class Command:
...     name: str
...     options: tuple[str, ...]
...     subcommand: None | Self = None
...
>>> command = Command(
...     name="git",
...     options=(),
...     subcommand=Command(
...         name="commit",
...         options=("-a", "-m", "'Initial commit'"),
...     )
... )

>>> asdict(command)
{
    'name': 'git',
    'options': (),
    'subcommand': {
        'name': 'commit',
        'options': ('-a', '-m', "'Initial commit'"),
        'subcommand': None
    }
}
```

Instead of using a hierarchy of objects, you now represent the same command with a Python dictionary, which can become the subject of a `match` statement:

Language: Python

```
>>> match asdict(command):
...     case {"subcommand": {"options": options, "name": "commit"}}:
...         print(options)
...
('-a', '-m', "'Initial commit'")
```

A mapping pattern looks like your typical dictionary literal, leveraging curly brackets, commas, and colons to combine keys with values. Because mappings are **unordered collections** of key-value pairs, it doesn’t matter how you arrange your keys and values in the pattern. Here, you intercept any command whose subcommand is named `"commit"` while capturing its options.

**Note:** Values in a mapping pattern can be almost anything, but the corresponding keys must be either **literal patterns** or **value patterns**. If you try to use capture patterns, for example, then you’ll encounter a syntax error:

Language: Python

```
>>> import math
>>> match dict():
...     case {3.14: "Pi"}:  # Literal pattern
...         ...
...     case {math.pi: "Pi"}:  # Value pattern
...         ...
...     case {pi: "Pi"}:  # Capture pattern
  File "<stdin>", line 6
    case {pi: "Pi"}:  # Capture pattern
            ^
SyntaxError: invalid syntax
```

In other words, you must know your keys beforehand. This is for performance reasons so that matching doesn’t end up being too computationally expensive.

A mapping pattern will match not only the built-in Python `dict` but also other kinds of mappings, including the ones from the [`collections`](https://realpython.com/python-collections-module/) module:

- [`collections.ChainMap`](https://realpython.com/python-chainmap/)

- [`collections.Counter`](https://realpython.com/python-counter/)

- [`collections.OrderedDict`](https://realpython.com/python-ordereddict/)

- [`collections.UserDict`](https://realpython.com/inherit-python-dict/)

- [`collections.defaultdict`](https://realpython.com/python-defaultdict/)

When you use an **empty dictionary literal** `{}`, then your pattern will match just about any mapping:

Language: Python

```
>>> from collections import (
...     ChainMap, Counter, OrderedDict, UserDict, defaultdict
... )
>>> mappings = (
...     d := dict(pi=3.14, e=2.72),
...     ChainMap(d),
...     Counter(d),
...     OrderedDict(d),
...     UserDict(d),
...     defaultdict(float, d),
... )
>>> for subject in mappings:
...     match subject:
...         case {}:
...             print("Matched:", type(subject))
...
Matched: <class 'dict'>
Matched: <class 'collections.ChainMap'>
Matched: <class 'collections.Counter'>
Matched: <class 'collections.OrderedDict'>
Matched: <class 'collections.UserDict'>
Matched: <class 'collections.defaultdict'>
```

Notice that your pattern matches these mappings even though they contain the key-value pairs `pi=3.14` and `e=2.72`, which you haven’t specified in the pattern.

This is an important difference from sequence patterns. Sequence patterns require you to either list all expected items or use the star operator (`*`) to indicate a variable-length sequence. In contrast, mapping patterns ignore any **extra keys** that exist in the subject but that you didn’t explicitly include in your pattern.

Therefore, you don’t need to use a wildcard pattern to ignore the remaining key-value pairs. The `**_` symbol would be redundant, so it’s disallowed. You can, however, use the standard **dictionary unpacking** to capture multiple key-value pairs into their own smaller dictionary:

Language: Python

```
>>> match asdict(command):
...     case {"subcommand": _, **rest}:
...         print(rest)
...
{'name': 'git', 'options': ()}
```

As with sequence patterns, the star pattern (`**`) can appear at most once. If you placed more than one, then it wouldn’t be clear which key-value pairs should be captured by each one.

Structural patterns are designed to avoid side effects as much as possible. To give you an example of a side effect, think of accessing a **missing key** in a `defaultdict` instance. This puts the default value under a new key, mutating your mapping:

Language: Python

```
>>> from collections import defaultdict
>>> histogram = defaultdict(int)
>>> for color in ("#000", "#4b7f9e", "#fff", "#4b7f9e"):
...     histogram[color] += 1
...
>>> dict(histogram)
{'#000': 1, '#4b7f9e': 2, '#fff': 1}
```

In this case, the `int()` function delivers a default value, which is equal to zero, for the initial color count in your histogram. When you read the current value of a color for the first time, Python calls the provided [callback function](https://en.wikipedia.org/wiki/Callback_\(computer_programming\)) and uses its result as the default value before letting you increment it by one.

To avoid adding new key-value pairs into such mappings, Python doesn’t use the square bracket syntax when matching a subject to one of your mapping patterns. Rather than calling [`.__getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__getitem__), which square brackets use under the hood, it invokes [`.get()`](https://docs.python.org/3/library/stdtypes.html#dict.get) on the subject:

Language: Python

```
>>> from collections import defaultdict
>>> histogram = defaultdict(int)
>>> histogram.get("#4b7f9e")  # Returns None without altering the histogram
>>> dict(histogram)
{}
>>> histogram["#4b7f9e"]  # Returns the default value, adding a new entry
0
>>> dict(histogram)
{'#4b7f9e': 0}
```

Calling `histogram.get()` bypasses the standard lookup path, so when your mapping is empty, you won’t put any new entries into it. On the other hand, using the square brackets syntax leads to modifying the histogram if the key doesn’t exist.

You’ve covered a lot of ground, but there’s one more advanced structural pattern to take a closer look at. In the next section, you’ll learn about the class pattern.

[ Remove ads](/account/join/)

### Class Pattern[](#class-pattern "Permanent link")

You’ve already seen a few [class patterns](https://peps.python.org/pep-0635/#class-patterns) in this tutorial. When used in conjunction with literal patterns, they enabled a **stricter type control** at runtime, whereas capture patterns allowed you to extract **attribute values** from objects. If you’re interested in matching the subject solely by its type, then you can use plain class patterns. Here’s an example:

Language: Python

```
>>> from datetime import UTC, datetime

>>> def parse(value):
...     match value:
...         case datetime():
...             return value.astimezone(UTC)
...         case int() | float():
...             return datetime.fromtimestamp(value, UTC)
...         case str():
...             return datetime.fromisoformat(value).astimezone(UTC)
...         case _:
...             raise TypeError(f"Unsupported type: {type(value)}")
...

>>> parse(-14182967.876544)
datetime(1969, 7, 20, 20, 17, 12, 123456, tzinfo=datetime.timezone.utc)

>>> parse("1969-07-20T20:17:12.123456+00:00")
datetime(1969, 7, 20, 20, 17, 12, 123456, tzinfo=datetime.timezone.utc)
```

This function takes a `value` as an argument, which can be one of four supported data types, and returns a timezone-aware [`datetime`](https://realpython.com/python-datetime/) instance. Depending on which type you pass as an actual parameter into the function, it determines the appropriate conversion method using pattern matching.

**Fun Fact:** Does the date in the example above ring a bell to you? If not, then you can read a [related article](https://en.wikipedia.org/wiki/Apollo_11) on Wikipedia about that event.

As you can see, instead of explicitly calling `isinstance()` on the subject, you can check if the subject is an instance of the given type by using a class pattern. This is more compact and gives you the option to destructure an object into its constituent parts.

You can generally use [keyword arguments](https://realpython.com/defining-your-own-python-function/#keyword-arguments) of the [class constructor](https://realpython.com/python-class-constructor/) to extract attribute values:

Language: Python

```
>>> import datetime

>>> def aoc_status(date):
...     match date:
...         case datetime.date(year=_, month=12, day=1):
...             print("Advent of Code starts today!")
...         case datetime.date(year=_, month=12, day=day) if day <= 25:
...             print(f"{25 - day} days until the end of AoC.")
...         case _:
...             print("Sorry, no Advent of Code today.")
...

>>> aoc_status(datetime.date.today())
Sorry, no Advent of Code today.

>>> aoc_status(datetime.date(2024, 12, 1))
Advent of Code starts today!

>>> aoc_status(datetime.date(2024, 12, 2))
23 days until the end of AoC.
```

Your `aoc_status()` function checks if the given date coincides with the [Advent of Code](https://realpython.com/python-advent-of-code/), which is an annual coding puzzle contest that takes place between the first and twenty-fifth of December each year.

In both cases, you pass **keyword subpatterns** to the `datetime.date()` class pattern. The first one includes a wildcard pattern to ignore the year, and two literal patterns to match a specific month and day. The second one additionally captures the day number as long as that day is on or before the twenty-fifth of December when the Advent of Code ends. Alternatively, you could omit the `year` attribute altogether in both class patterns.

**Note:** Remember that you can’t reuse the name of a capture pattern within the same class pattern:

Language: Python

```
match date:
    case datetime.date(year=_, month=same, day=same):
        ...
```

This code is illegal because the month and day arguments must be distinct capture patterns.

Sometimes, you can specify your patterns using **positional subpatterns** instead of keyword ones. Whether it’s possible depends on the data type that you refer to in your class pattern. In this instance, the `datetime.date` class doesn’t accept any positional subpatterns:

Language: Python

```
>>> match datetime.date.today():
...     case datetime.date(_, 12, 1):
...         pass
...
Traceback (most recent call last):
  File "<input>", line 2, in <module>
    case datetime.date(_, 12, 1):
         ^^^^^^^^^^^^^^^^^^^^^^^
TypeError: datetime.date() accepts 0 positional sub-patterns (3 given)
```

When you try to use three consecutive subpatterns without providing the associated argument names, then pattern matching fails.

Compiled languages with static type checking, which support pattern matching, would make this possible with the help of [algebraic data types](https://en.wikipedia.org/wiki/Algebraic_data_type#Pattern_matching). Python’s dynamic nature throws a wrench in the works, making matching by positional arguments a bit trickier. The interpreter can’t always guarantee that the order of your positional subpatterns will correspond to the order of expected attributes defined in the class.

That said, you’ll find a few built-in and standard-library types that support matching by [positional arguments](https://realpython.com/defining-your-own-python-function/#positional-arguments). **Data classes** and **named tuples** are among them since they inherently impose order on their attributes:

Language: Python

```
>>> from typing import NamedTuple

>>> class Date(NamedTuple):
...     year: int
...     month: int
...     day: int
...
>>> match Date(1969, 7, 20):
...     case Date(_, 7, 20):
...         print("Celebrating another moon landing anniversary!")
...
Celebrating another moon landing anniversary!
```

Python can correctly tie the specified subpatterns to the positional arguments of the constructor thanks to the special `.__match_args__` attribute that was generated automatically for you:

Language: Python

```
>>> Date.__match_args__
('year', 'month', 'day')
```

Such an ordered sequence of attribute names allows Python to correctly map positional subpatterns to their keyword counterparts, which are used under the surface.

Most classes, including [`datetime.date`](https://docs.python.org/3/library/datetime.html#datetime.date) that you just used, don’t come with this special attribute, though:

Language: Python

```
>>> datetime.date.today().__match_args__
Traceback (most recent call last):
  ...
AttributeError: 'datetime.date' object has no attribute '__match_args__'
```

You must, therefore, rely on explicit keyword arguments or provide the special `.__match_args__` attribute yourself in user-defined classes. You’ll see examples of this and learn how to customize pattern matching for instances of your classes in the next section.

**Note:** When a class supports matching by positional arguments, you can mix both positional and keyword arguments in a single class pattern for more flexibility.

While the majority of classes only support matching by keyword subpatterns, you can take advantage of a convenient **shorthand notation** for most built-in types. If there’s a version of the constructor that accepts a single value, then it’s possible to [implicitly match the subject](https://peps.python.org/pep-0636/#matching-builtin-classes) using a positional subpattern:

Language: Python

```
>>> def length(value):
...     match value:
...         case str(text):
...             return len(text)
...         case int(number):
...             return number.bit_length()
...
>>> length("255")
3
>>> length(255)
8
```

Neither `str` nor `int` provides the special `.__match_args__` attribute, but they know how to properly interpret the only positional subpattern. This can simplify your code by relieving you from writing an **AS pattern**, such as `str() as text`, which you’ll learn about later.

Note that fields not automatically initialized in a data class are excluded from pattern matching:

Language: Python

```
>>> from dataclasses import dataclass, field
>>> from datetime import date

>>> @dataclass
... class Person:
...     dob: date
...     age: int = field(init=False)
...
...     def __post_init__(self):
...         self.age = date.today().year - self.dob.year
...
>>> person = Person(date(1982, 1, 31))
>>> match person:
...     case Person(_):
...         print(f"This person's {person.age} years old.")
...
This person's 42 years old.
```

You only use one wildcard pattern to match a person’s date of birth (`.dob`). The other attribute, `.age`, isn’t taken into consideration when matching because you haven’t specified it in the constructor. The second attribute was computed dynamically based on the current year and the person’s date of birth.

Matching instances of [nominal subtypes](https://realpython.com/inheritance-composition-python/) as well as [structural subtypes](https://realpython.com/python-protocol/) works as expected:

Language: Python

```
>>> from typing import NamedTuple, Protocol, runtime_checkable

>>> @runtime_checkable
... class Additive(Protocol):
...     def __add__(self, other):
...         ...
...
>>> class Vector(NamedTuple):
...     x: int
...     y: int
...
...     def __add__(self, other):
...         return Vector(self.x + other.x, self.y + other.y)
...
>>> match Vector(3, 4):
...     case Additive():
...         print("Matched an additive object.")
...
Matched an additive object.
```

Since class patterns call the `isinstance()` function on the subject, make sure that any protocol you match against was [decorated](https://realpython.com/primer-on-python-decorators/) with `@runtime_checkable`.

The syntax of class patterns, which you can use to destructure an object, elegantly mirrors the syntax of class instantiation. However, you may sometimes need to take additional steps if you want to make your custom classes play nicely with pattern matching.

## Customizing Pattern Matching of Class Instances[](#customizing-pattern-matching-of-class-instances "Permanent link")

In most cases, you don’t need to do anything extra for your custom data types to support pattern matching. Any class name can become the target of a `match` statement:

Language: Python

```
>>> class User:
...     def __init__(self, email, is_admin=False):
...         self.email = email
...         self.is_admin = is_admin
...
>>> def contact_details(user):
...     match user:
...         case User():
...             return f"The user can be reached at <{user.email}>."
...
>>> contact_details(User("jdoe@company.com"))
'The user can be reached at <jdoe@company.com>.'
```

First, you define a plain old Python class, which is neither a descendant of a named tuple nor a data class. As such, it lets you match `User` instances by specifying the `User()` pattern. Remember that you must always include a trailing pair of parentheses to indicate a class pattern. After all, it resembles class instantiation.

Unfortunately, you can’t avoid using keyword subpatterns when you want to be more specific, for example, by narrowing down the user type. If you provide positional subpatterns instead, then Python won’t know how to map their indices to attribute names:

Language: Python

```
>>> def contact_details(user):
...     match user:
...         case User(email, True):
...             return f"The user can be reached at <{email}>."
...
>>> contact_details(User("jdoe@company.com"))
Traceback (most recent call last):
  ...
TypeError: User() accepts 0 positional sub-patterns (2 given)
```

To fix that, you can tell Python about the expected order of object attributes by specifying a special `.__match_args__` field in your class:

Language: Python

```
>>> class User:
...     __match_args__ = ("is_admin",)
...
...     def __init__(self, email, is_admin=False):
...         self.email = email
...         self.is_admin = is_admin
...
```

Note that it has to be a **tuple of strings** and it mustn’t contain **duplicates**! If you define a list, for example, then you’ll cause a `TypeError`. Also, notice how you can reorder or even skip some of your attributes when you define this special field.

With your updated class definition, you can now match users through positional subpatterns that correspond to the attributes specified in `.__match_args__`. Here’s an example of how you can leverage this in a `case` clause:

Language: Python

```
>>> def contact_details(user):
...     match user:
...         case User(True):
...             return f"Admin can be reached at <{user.email}>."
...         case User():
...             return f"Not an admin: <{user.email}>"
...

>>> contact_details(User("admin@company.com", is_admin=True))
'Admin can be reached at <admin@company.com>.'

>>> contact_details(User("jdoe@company.com"))
'Not an admin: <jdoe@company.com>'
```

Under the hood, Python converts each positional pattern at index `i` to a keyword pattern using the `.__match_args__[i]` syntax.

That concludes the overview of basic and advanced structural patterns in Python. Coming up next, you’ll explore a few final types of patterns that will allow you to compose multiple patterns in various ways. Don’t worry, though, as you briefly touched upon most of them before!

## Composing Complex Structural Patterns[](#composing-complex-structural-patterns "Permanent link")

Most structural patterns are composable, meaning you can build complex patterns made of simpler subpatterns. Python will evaluate them from left to right and top to bottom within the hierarchy. The success or failure of these subpatterns determines the outcome of the entire pattern.

The only **standalone patterns** that can’t contain any subpatterns are the following:

- Wildcard pattern

- Literal pattern

- Value pattern

- Capture pattern

These patterns either match values directly or act as their placeholders. On the other hand, you can nest any subpattern within the remaining patterns, including the ones you’re about to explore in this section.

### OR Pattern: Union of Multiple Patterns[](#or-pattern-union-of-multiple-patterns "Permanent link")

If you’ve been following along, then you’ll remember the [OR pattern](https://peps.python.org/pep-0635/#or-patterns) from when you built your rudimentary Python REPL earlier in this tutorial. You used this pattern to break out of an infinite loop in response to one of two commands, *exit* or *quit*:

Language: Python

```
PROMPT = "\N{snake} "

while True:
    match input(PROMPT):
        case "exit" | "quit":
            break
```

Here, you use the [bitwise OR](https://realpython.com/python-bitwise-operators/#bitwise-or) operator denoted by a pipe symbol (`|`) to combine several structural patterns into a union of **alternative subpatterns**. If at least one of them matches the subject, then the corresponding code block will run.

**Note:** The bitwise OR operator also serves as a shorthand notation for [merging dictionaries](https://peps.python.org/pep-0584/), [performing set unions](https://peps.python.org/pep-0218/), and [defining union types](https://docs.python.org/3/library/stdtypes.html#types-union) in type hinting.

This kind of structural pattern can help you avoid code duplication by letting you reuse a block of code that’s common to more than one pattern. Without the OR pattern, you’d have to repeat the same logic for each individual case, leading to more cluttered and brittle code.

If your OR pattern contains at least one **capture pattern**, then *all* of the alternative subpatterns must also include one with precisely the same variables to bind in arbitrary order. You can’t have a mix of capture and non-capture patterns, and you can’t use different variable names across your alternative capture patterns. For example, the following OR patterns are invalid:

Language: Python

```
match subject:
    case Option("--input", in_path) | Option("--output", out_path):
        ...
    case Option(name, value) | Flag(name) | "exit":
        ...
```

The first `case` clause defines an OR pattern that combines two alternative class patterns, each having a pair of subpatterns comprised of a literal and a capture pattern. However, the capture patterns bind to two different names, `in_path` and `out_path`. That’s not allowed because you wouldn’t know which variable to use in the subsequent code block when one of the alternative class patterns succeeded.

Conversely, the second `case` clause mixes different types of subpatterns. Two of them contain capture patterns, but they bind values to different sets of names. The third subpattern is a literal pattern, so it can’t bind any names at all, causing an inconsistency in the matching logic.

You use the OR pattern to make a union of alternative patterns. Note that there’s no explicit **AND pattern** in Python because it’s impossible for a subject to have two different structures at the same time. However, you can combine multiple matching conditions through guards, which you’ll cover later.

Another way to compose your patterns is to combine structural matching with binding the matched value to an alias. This is what you’ll explore next.

### AS Pattern: Alias of a Matched Subpattern[](#as-pattern-alias-of-a-matched-subpattern "Permanent link")

Standalone patterns listed at the beginning of this section match the subject expression without binding its value to a name. For example, a wildcard pattern always matches anything but won’t let you refer to the matched value. Similarly, when you have a few alternative literal patterns combined with an OR pattern, then you won’t know which one was matched. Finally, some class patterns don’t allow you to specify a capture pattern within them.

That’s where [AS patterns](https://peps.python.org/pep-0635/#as-patterns) come in handy. They become useful when you need to express a structural constraint while simultaneously binding the matched value to a variable so that you can refer to it in the subsequent code block. Consider the following example:

Language: Python

```
>>> while True:
...     match eval(input("\N{snake} ")):
...         case int() | float() | complex() as number:
...             print(f"Number: {number:.2f}")
...         case ["N" | "S" | "W" | "E" as hemisphere, coordinate]:
...             names = {"N": "North", "S": "South", "W": "West", "E": "East"}
...             print(f"{names[hemisphere]}ern hemisphere")
...         case _ as unknown:
...             print(f"Unsupported value: {unknown}")
...
🐍 3.14
Number: 3.14
🐍 ["N", 50.061389]
Northern hemisphere
🐍 tuple()
Unsupported value: ()
🐍 exit()
```

You run an infinite loop that reads user input and evaluates it as a Python expression until receiving the EOF character or calling the [`exit()`](https://docs.python.org/3/library/constants.html#exit) function.

If the provided value is a number of one of the built-in numeric types, then you [format that number](https://realpython.com/how-to-python-f-string-format-float/) to two decimal places. Notice how you assign the value matched by your pattern to a variable named `number` using the [`as` keyword](https://realpython.com/python-keywords/#the-as-keyword). It looks as if you’d only bind the last subpattern, which is a complex number, but you actually bind *any* value that matches the entire OR pattern: `int() | float() | complex()`.

The sequence pattern right below it demonstrates how you can nest AS patterns within other patterns. In this case, you use it to bind one of four alternative string literals to a variable named `hemisphere`. This is probably the best use case for this kind of pattern.

The third `case` clause features a wildcard pattern, which matches any value that didn’t fit the previous patterns. In this example, you use the AS pattern to additionally bind this unmatched value to a variable named `unknown`. This lets you handle unsupported input gracefully.

**Note:** In some cases, you can get away with not using the AS pattern even when your primary structural pattern doesn’t bind the matched value.

As mentioned previously, some built-in class patterns let you specify a single capture pattern inside them, such as `int(number)` or `float(number)`. The `number` pattern acts as an alias of the respective value. Other class patterns may require the AS pattern when they only accept keyword subpatterns like `complex(real=re, imag=im)`.

Moreover, when you match the entire subject rather than a part of it, and you have its reference stored in a variable, then you can use that reference directly instead of binding the matched value to another variable.

Just like capture patterns, a successful AS pattern defines a variable that will be visible after your `match` block. However, you should expect such a variable *not* to exist if the pattern doesn’t succeed. Also, your aliases should never conflict with other variables defined in the same or enclosing scope.

By now, you’ve seen almost all of the structural patterns supported by Python. There’s one more, which you’ll get familiar with now to give you the complete picture.

### Group Pattern: Visual Grouping of Subpatterns[](#group-pattern-visual-grouping-of-subpatterns "Permanent link")

The last structural pattern that you’ll learn about in this tutorial is a [group pattern](https://peps.python.org/pep-0634/#group-patterns), which allows you to put parentheses around any pattern to improve its readability. It can be particularly helpful around a nested union to make it visually stand out from an otherwise crowded pattern:

Language: Python

```
match subject:
    case [(latitude), (("N" | "S") | ("W" | "E")) as hemisphere]:
        ...
```

You can safely omit the parentheses around the class and OR patterns above because they make no syntactical difference. On the other hand, they can help to visually separate the individual subpatterns, making them easier to understand.

**Note:** Don’t confuse group patterns with sequence patterns, which can also use parentheses. Keep in mind that a sequence pattern typically contains at least one comma inside the parentheses unless it represents an empty sequence.

That was the last structural pattern you’ll find in Python. But it doesn’t exhaust the whole topic. Next, you’ll take a closer look at guards.

### Guard: Logical Condition on Top of a Pattern[](#guard-logical-condition-on-top-of-a-pattern "Permanent link")

[Guards](https://peps.python.org/pep-0635/#guards) aren’t technically structural patterns, but they work hand in hand with them. While patterns express the static structure of your data, allowing for a declarative style, guards let you branch on non-structural conditions, such as the relationships between the individual subpatterns.

To add a bit of dynamism, you can specify an **arbitrary logical condition**, called a guard, to be checked at runtime when your pattern succeeds. Syntactically, each `case` clause can be followed by an optional `if` statement representing the guard, next to the pattern definition.

Take a look at the following function, which makes an [HTTP request](https://realpython.com/urllib-request/) to the specified URL and uses structural patterns with guards to handle the response object:

Language: Python

```
>>> from http.client import HTTPConnection, HTTPResponse, HTTPSConnection
>>> from sys import stderr
>>> from urllib.parse import ParseResult, urlparse

>>> def fetch(url):
...     print(f"Fetching URL: {url}", file=stderr)
...     connection = make_connection(url)
...     try:
...         connection.request("GET", "/")
...         match connection.getresponse():
...             case HTTPResponse(status=code) if code >= 400:
...                 raise ValueError("Failed to fetch URL")
...             case HTTPResponse(status=code) as resp if (
...                 code >= 300 and (redirect := resp.getheader("Location"))
...             ):
...                 return fetch(redirect)
...             case HTTPResponse(status=code) as resp if code >= 200:
...                 return resp.read()
...             case _:
...                 raise ValueError("Unexpected response")
...     finally:
...         connection.close()
...
>>> def make_connection(url):
...     match urlparse(url):
...         case ParseResult("http", netloc=host):
...             return HTTPConnection(host)
...         case ParseResult("https", netloc=host):
...             return HTTPSConnection(host)
...         case _:
...             raise ValueError("Unsupported URL scheme")
...
>>> fetch("http://realpython.com/")
Fetching URL: http://realpython.com/
Fetching URL: https://realpython.com/
b'\n\n<!doctype html>\n<html lang="en">\n (...) </body>\n</html>\n'
```

The highlighted condition exemplifies a fairly complicated guard that references both a capture subpattern, `code`, and the whole subject aliased as `resp`. The guard checks if the status code of the HTTP response is greater than or equal to 300, indicating a [URL redirect](https://en.wikipedia.org/wiki/URL_redirection). Additionally, the guard verifies if the [Location header](https://en.wikipedia.org/wiki/HTTP_301#Location_header) is present while simultaneously binding its value to a variable called `redirect` using the Walrus operator (`:=`).

**Note:** Guards are powerful but can quickly turn your carefully crafted structural pattern matching into unintelligible [spaghetti code](https://en.wikipedia.org/wiki/Spaghetti_code) if overused, so use them wisely.

A guard is *not* a part of the pattern! It’s a part of the `case` clause, and it’s only checked when the associated pattern matches the subject. Conversely, when a pattern fails to match the subject, the logical condition won’t be evaluated, which can influence potential side effects of the guard. Moreover, a `case` clause with a guard will succeed only when both the pattern matches the subject and the corresponding guard condition is true.

When you augment an OR pattern with a guard, then the conditional statement applies equally to all alternative subpatterns rather than just to the last one on the far right. This is analogous to the AS pattern that you saw in the previous section, which you often place close to the last subpattern. Here’s a toy example to illustrate this:

Language: Python

```
>>> flag = True
>>> while True:
...     match eval(input(">>> ")):
...         case int() | float() if flag:
...             print("Matched a number!")
...         case "toggle":
...             flag = not flag
...         case _:
...             print("That's not a number.")
...
>>> 42
Matched a number!
>>> 4.2
Matched a number!
>>> "toggle"
>>> 42
That's not a number.
>>> 4.2
That's not a number.
>>> "toggle"
>>> 42
Matched a number!
>>> 4.2
Matched a number!
```

This code snippet repeatedly prompts the user for a Python expression to evaluate. When the user types either an integer or a floating-point number, then an appropriate message prints on the screen, but only when the Boolean variable `flag` is true. The user can toggle this variable by typing `"toggle"` at the prompt. Notice how this affects the guard’s behavior for both `int()` and `float()` subpatterns.

Whew! That was a lot to take in, but you made it through. Structural pattern matching is a surprisingly deep rabbit hole of a topic, so mastering it can take some time. You can review a few hands-on examples in the following section to solidify your understanding.

## Finding Practical Uses for Pattern Matching[](#finding-practical-uses-for-pattern-matching "Permanent link")

In this section, you’ll explore various real-world applications of pattern matching and learn how to implement them effectively. Along the way, you’ll retrieve and display comments on GitHub issues, create a guessing game, develop a Python code optimizer, enforce runtime type checking, simulate function overloading, and replicate the switch statement in Python.

### Read Deeply Nested Hierarchical Data[](#read-deeply-nested-hierarchical-data "Permanent link")

Structural pattern matching is an excellent tool for parsing objects deserialized from **hierarchical data formats** like [XML](https://realpython.com/python-xml-parser/), [JSON](https://realpython.com/python-json/), or [YAML](https://realpython.com/python-yaml/). These data formats are prevalent in [web development](https://realpython.com/learning-paths/become-python-web-developer/), facilitating data interchange between clients and servers, particularly through [REST APIs](https://realpython.com/api-integration-in-python/). They’re also commonly used in event-driven [socket](https://realpython.com/python-sockets/) communication delivering real-time updates, such as live flight information or sports scores.

For example, the [GitHub REST API](https://docs.github.com/en/rest) exposes several endpoints for querying various kinds of information available publicly, such as the events related to a particular repository. Say you wanted to fetch the latest comments left by [CPython](https://realpython.com/products/cpython-internals-book/) contributors on open issues:

Language: Shell

```
$ curl -s 'https://api.github.com/repos/python/cpython/events' | jq
[
  {
    "id": "40620926634",
    "type": "PullRequestEvent",
    "actor": {
      "id": 10796600,
      "login": "picnixz",
      "display_login": "picnixz",
      "gravatar_id": "",
      "url": "https://api.github.com/users/picnixz",
      "avatar_url": "https://avatars.githubusercontent.com/u/10796600?"
    },
    "repo": {
      "id": 81598961,
      "name": "python/cpython",
      "url": "https://api.github.com/repos/python/cpython"
    },
    ⋮
  },
  ⋮
]
```

You execute [`curl`](https://en.wikipedia.org/wiki/CURL) in the command line to fetch recent events about the [`python/cpython`](https://github.com/python/cpython) repository. Since the server replies with a JSON payload, you format it nicely using the [`jq`](https://en.wikipedia.org/wiki/Jq_\(programming_language\)) tool. Note that you don’t need to authenticate against GitHub using a token or API key to access this endpoint.

In Python, you can fetch data from such an endpoint using [`urlopen()`](https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen) from the `urllib.request` module:

Language: Python Filename: `issue_comments.py`

```
import json
import urllib.request

def fetch_github_events(org, repo):
    url = f"https://api.github.com/repos/{org}/{repo}/events"
    with urllib.request.urlopen(url) as response:
        return json.loads(response.read())
```

The function that you defined above takes the name of a GitHub organization and one of the repositories it owns, such as `python` and `cpython`, respectively. Then, your function deserializes the response’s body from JSON to a Python list containing the individual events represented as Python dictionaries.

When you look closely at the event types returned by the server, you’ll notice there are several kinds, each with distinct attributes and structure. So, you can use a **mapping pattern** to filter these events, keeping only those with the `"IssueCommentEvent"` type. You can also destructure events into only a few properties of interest, binding their values to variables using **capture patterns**:

Language: Python Filename: `issue_comments.py`

```
# ...

def filter_comments(events):
    for event in events:
        match event:
            case {
                "type": "IssueCommentEvent",
                "created_at": when,
                "actor": {
                    "display_login": user,
                },
                "payload": {
                    "action": "created",
                    "issue": {
                        "state": "open",
                        "title": issue_title,
                    },
                    "comment": {
                        "body": body,
                        "html_url": url,
                        "user": {
                            "html_url": user_url,
                        },
                    },
                },
            }:
                yield Comment(when, body, url, user, user_url, issue_title)
```

Notice how your pattern reflects the structure of a segment of the JSON document retrieved from GitHub. At the same time, you can remain highly selective about the fields to extract from the document, even those nested multiple levels deep. When your pattern matches the subject, you [`yield`](https://realpython.com/introduction-to-python-generators/) an instance of the `Comment` data class, which you’ll define now.

This class lets you conveniently collect the necessary information in one place, and it knows how to render itself in [Markdown](https://realpython.com/django-markdown/) using the third-party [Rich](https://realpython.com/python-rich-package/) library:

Language: Python Filename: `issue_comments.py`

```
import json
import urllib.request
from dataclasses import dataclass

from rich.markdown import Markdown
from rich.panel import Panel

@dataclass
class Comment:
    when: str
    body: str
    url: str
    user: str
    user_url: str
    issue_title: str

    @property
    def footer(self):
        return (
            f"Comment by [{self.user}]({self.user_url})"
            f" on [{self.when}]({self.url})"
        )

    def render(self):
        return Panel(
            Markdown(f"{self.body}\n\n---\n_{self.footer}_"),
            title=self.issue_title,
            padding=1,
        )

# ...
```

You can now connect the dots by making a request to GitHub and printing the rendered Markdown in the console:

Language: Python

```
import json
import urllib.request
from dataclasses import dataclass

from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

# ...

def main():
    console = Console()
    events = fetch_github_events("python", "cpython")
    for comment in filter_comments(events):
        console.clear()
        console.print(comment.render())
        console.input("\nPress [b]ENTER[/b] for the next comment...")

if __name__ == "__main__":
    main()
```

At the bottom of the file, you use the [name-main idiom](https://realpython.com/if-name-main-python/) to define the [entry point](https://en.wikipedia.org/wiki/Entry_point) to your script. When you give your code a spin by [running the script](https://realpython.com/run-python-scripts/), you’ll be able to navigate through the issue comments by pressing the Enter key:

[![A comment on a GitHub issue in the CPython repository](https://files.realpython.com/media/cpython_github_issue_comment.354c0d068a84.png)](https://files.realpython.com/media/cpython_github_issue_comment.354c0d068a84.png)

A Comment on a GitHub Issue in the CPython Repository

The mapping patterns can also prove especially useful when you’re dealing with alternate formats of the same entity. For example, you may be asked to support both the new and legacy versions of a certain API. Or maybe you’re processing a schemaless collection of documents obtained from a NoSQL database like [MongoDB](https://realpython.com/introduction-to-mongodb-and-python/). Because such documents have no schema, some document fields can be reused for different purposes or have different types or structures.

### Parse and Process User Input[](#parse-and-process-user-input "Permanent link")

At the beginning of this tutorial, you saw the perfect application of structural pattern matching when you implemented a basic Python REPL. To solidify your knowledge, you’ll build a simple **guessing game** to interact with the user as an exercise. The player’s goal is to guess a [randomly generated](https://realpython.com/python-random/) number between 1 and 100\. Here’s what a sample gameplay might look like:

Language: Shell

```
$ python guessing_game.py
Welcome to the game! Type 'q' or 'quit' to exit.
🧙 Guess a number between 1 and 100: 50
Too low! 4 tries left.
🧙 Try again: 75
Too high! 3 tries left.
🧙 Try again: 63
You won 🎉
Do you want to play again? [Y/N] n
Bye 👋
```

The player has at most five attempts to guess the number. Each time, they’ll receive feedback on whether their guess is too high, too low, or correct.

As before, you’ll use pattern matching to handle user input. Start by outlining the structure of your Python script, which will include importing the [`random`](https://docs.python.org/3/library/random.html) module, specifying various constants, and creating a few functions:

Language: Python Filename: `guessing_game.py`

```
import random

MIN, MAX = 1, 100
MAX_TRIES = 5
PROMPT_1 = f"\N{mage} Guess a number between {MIN} and {MAX}: "
PROMPT_2 = "\N{mage} Try again: "
BYE = "Bye \N{waving hand sign}"

def main():
    print("Welcome to the game! Type 'q' or 'quit' to exit.")
    while True:
        play_game()
        if not want_again():
            bye()

def play_game():
    ...

def want_again():
    while True:
        match input("Do you want to play again? [Y/N] ").lower():
            case "y": return True
            case "n": return False

def bye():
    print(BYE)
    exit()

if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print()
        bye()
```

The `main()` function greets the player and displays instructions on how to exit the game. It then enters an infinite loop, repeatedly calling `play_game()` and asking the player if they want to give the game another try after each completed round, regardless of its outcome.

The `want_again()` function prompts the user to decide if they want to play again. It uses literal patterns to check the player’s response against letters *y* and *n*, ensuring that only valid inputs are accepted.

You can now implement the `play_game()` function, which is the heart of your program:

Language: Python Filename: `guessing_game.py`

```
16# ...
17
18def play_game():
19    drawn_number = random.randint(MIN, MAX)
20    num_tries = MAX_TRIES
21    prompt = PROMPT_1
22    while num_tries > 0:
23        match input(prompt):
24            case command if command.lower() in ("q", "quit"):
25                bye()
26            case user_input:
27                try:
28                    user_number = int(user_input)
29                except ValueError:
30                    print("That's not a number!")
31                else:
32                    match user_number:
33                        case number if number < drawn_number:
34                            num_tries -= 1
35                            prompt = PROMPT_2
36                            print(f"Too low! {num_tries} tries left.")
37                        case number if number > drawn_number:
38                            num_tries -= 1
39                            prompt = PROMPT_2
40                            print(f"Too high! {num_tries} tries left.")
41                        case _:
42                            print("You won \N{party popper}")
43                            return
44    print("You lost \N{pensive face}")
45
46    # ...
```

This function may seem somewhat obscure at first, so here’s a line-by-line breakdown:

- **Lines 19 to 21** initialize variables that represent the game’s current state, including the drawn random number, the remaining number of tries, and the prompt.

- **Line 22** starts a [`while`](https://realpython.com/python-while-loop/) loop that will run until the player runs out of tries.

- **Lines 24 and 25** terminate the game when the player types one of the predefined commands.

- **Lines 27 to 30** convert the user’s answer into an integer number that you can compare to the drawn number. If the conversion fails, then you print an error message.

- **Lines 32 to 43** use pattern matching to resolve and update the game’s status, showing a relevant message to the player.

- **Line 44** executes if the loop ends without the player guessing the correct number. It prints a message indicating that the player has lost the game.

Expressing the game rules with pattern matching looks arguably more elegant and readable when compared to traditional conditional statements.

### Traverse Recursive Data Structures[](#traverse-recursive-data-structures "Permanent link")

The combination of branching and destructuring makes pattern matching particularly powerful in traversing [recursive data structures](https://en.wikipedia.org/wiki/Recursive_data_type), such as an [abstract syntax tree (AST)](https://en.wikipedia.org/wiki/Abstract_syntax_tree) of a code snippet. Therefore, you can leverage structural patterns to implement the [visitor pattern](https://en.wikipedia.org/wiki/Visitor_pattern) efficiently and concisely.

Suppose you were developing an **intelligent code optimizer** for Python aimed at enhancing performance and maintainability:

Language: Python Filename: `optimizer.py`

```
import ast
import inspect
import textwrap

def main():
    source_code = inspect.getsource(sample_function)
    source_tree = ast.parse(source_code)
    target_tree = optimize(source_tree)
    target_code = ast.unparse(target_tree)

    print("Before:")
    print(ast.dump(source_tree))
    print(textwrap.indent(source_code, "| "))

    print("After:")
    print(ast.dump(target_tree))
    print(textwrap.indent(target_code, "| "))

def sample_function():
    return 40 + 2

def optimize(node):
    ...

if __name__ == "__main__":
    main()
```

Your tool takes a piece of Python source code as input. In this case, you supply a reference to a `sample_function()`, which returns the result of an arithmetic expression, forty plus two.

Next, the program obtains this function’s source code as text using the [`inspect`](https://docs.python.org/3/library/inspect.html) module and translates the resulting string into a hierarchy of objects with the [`ast`](https://docs.python.org/3/library/ast.html) module’s help. Such an abstract representation of source code is convenient to traverse and transform, so your program calls `optimize()`, which you’ll implement in a bit, with the tree of nodes as an argument.

Once your function returns with an optimized abstract syntax tree, you translate it back into Python and display both versions on the screen for comparison. This is what you’ll see when you run the finished program:

Language: Shell

```
$ python optimizer.py
Before:
Module(body=[FunctionDef(..., body=[Return(value=BinOp(...))], ...)], ...)
| def sample_function():
|     return 40 + 2

After:
Module(body=[FunctionDef(..., body=[Return(value=Constant(...))], ...)], ...)
| def sample_function():
|     return 42
```

Clearly, your optimizer has successfully identified a bottleneck and simplified the function’s body by evaluating the expression into a constant. This makes the code more readable and reduces the number of operations to execute at runtime.

How does the `optimize()` function work? It traverses the abstract syntax tree from the root, replacing nodes that it can recognize with equivalent but simplified representations:

Language: Python Filename: `optimizer.py`

```
23# ...
24
25def optimize(node):
26    match node:
27        case ast.Module(body, type_ignores):
28            return ast.Module(
29                [optimize(child) for child in body],
30                type_ignores
31            )
32        case ast.FunctionDef():
33            return ast.FunctionDef(
34                name=node.name,
35                args=node.args,
36                body=[optimize(child) for child in node.body],
37                decorator_list=node.decorator_list,
38                returns=node.returns,
39                type_comment=node.type_comment,
40                type_params=node.type_params,
41                lineno=node.lineno,
42            )
43        case ast.Return(value):
44            return ast.Return(value=optimize(value))
45        case ast.BinOp(ast.Constant(left), op, ast.Constant(right)):
46            match op:
47                case ast.Add():
48                    return ast.Constant(left + right)
49                case ast.Sub():
50                    return ast.Constant(left - right)
51                case _:
52                    return node
53        case _:
54            return node
55
56# ...
```

The highlighted lines recursively call `optimize()` with subnodes to replace in the tree. The wildcard patterns let you return nodes intact if they’re unsupported. However, at the moment, only two binary operators can be simplified.

This was a fairly minimal example, but it should give you an idea of how you can use pattern matching effectively to traverse recursive data structures while performing interesting operations.

### Enforce Types at Runtime to Validate Data[](#enforce-types-at-runtime-to-validate-data "Permanent link")

Because **class patterns** allow you to match the subject by its type, you can effectively use structural pattern matching as a form of the [runtime type-checking](https://en.wikipedia.org/wiki/Run-time_type_information) mechanism. This can be particularly useful for [validating](https://en.wikipedia.org/wiki/Data_validation) function arguments or object attributes in the class constructor.

Take a look at the following example, which uses pattern matching to implement the validation logic:

Language: Python

```
>>> class PositiveNumber:
...     def __init__(self, value):
...         match value:
...             case Decimal() | Fraction():
...                 self.__init__(float(value))
...             case int() | float() if value > 0:
...                 self.value = float(value)
...             case int() | float():
...                 raise ValueError("number must be positive")
...             case complex():
...                 raise TypeError("number must be real")
...             case _:
...                 raise TypeError("value must be a number")
...
...     def __repr__(self):
...         return f"PositiveNumber({self.value!r})"
...
```

The initializer method in this class branches on the type of the input argument. If the argument is an instance of the [`Decimal`](https://realpython.com/python-fractions/#decimal-floating-point-and-fixed-point-decimal) or [`Fraction`](https://realpython.com/python-fractions/) class, then you call `.__init__()` with the same value converted to a float. When passed a positive integer or a floating-point number, the initializer stores that number in an attribute. Otherwise, if the value isn’t positive or isn’t a real number, then you raise an appropriate exception.

Here’s how your new data type behaves in practice:

Language: Python

```
>>> from decimal import Decimal
>>> from fractions import Fraction

>>> PositiveNumber(1)
PositiveNumber(1.0)

>>> PositiveNumber(3.14)
PositiveNumber(3.14)

>>> PositiveNumber(Fraction(3, 4))
PositiveNumber(0.75)

>>> PositiveNumber(Decimal("0.33"))
PositiveNumber(0.33)

>>> PositiveNumber(0)
Traceback (most recent call last):
  ...
ValueError: number must be positive

>>> PositiveNumber(3 + 2j)
Traceback (most recent call last):
  ...
TypeError: number must be real

>>> PositiveNumber("not a number")
Traceback (most recent call last):
  ...
TypeError: value must be a number
```

These examples demonstrate how you can use structural pattern matching to validate data types and values at runtime. Validation makes your code more robust and less prone to errors, so it’s a good idea to incorporate it into your development practice.

**Note:** Instead of rolling your own validation, you should check out [Pydantic](https://realpython.com/python-pydantic/) which is a powerful library for data validation in Python.

You can extend this technique to simulate function overloading in Python, which you’ll learn about now.

### Overload a Callable Based on Its Arguments[](#overload-a-callable-based-on-its-arguments "Permanent link")

Overloading is a programming concept where a [callable](https://docs.python.org/3/glossary.html#term-callable), such as a function, method, lambda expression, or a function object (functor), behaves differently depending on the number and types of arguments passed into it. The built-in `int()` function is a prime example of this:

Language: Python

```
>>> int()
0

>>> int(3.14)
3

>>> int("+42")
42

>>> int("ff", 16)
255

>>> int("0xff", 0)
255
```

Notice how you call the same function with different arguments, as if `int()` had alternative [signatures](https://en.wikipedia.org/wiki/Type_signature):

- When you call it without any arguments, the function always returns zero. This makes `int()` a popular choice for the [default factory](https://docs.python.org/3/library/collections.html#collections.defaultdict.default_factory) of missing keys in `defaultdict` objects.

- Calling `int()` with a floating-point number truncates the decimal part.

- Calling `int()` on a string converts it into an integer, provided that the string looks like a number.

- You can also call `int()` with two arguments to convert a number expressed in a non-decimal base to base-ten. The first argument must be a string, and the second argument must be an integer between two and thirty-six.

- Additionally, when you specify the second argument as zero, the function will look for a prefix like `0x`, which stands for the hexadecimal system, in order to determine the source base.

In statically typed languages, the [compiler](https://en.wikipedia.org/wiki/Compiler) decides which of the overloaded versions of the same function to choose based on the [actual parameters](https://en.wikipedia.org/wiki/Parameter_\(computer_programming\)#Parameters_and_arguments). In dynamic languages like Python, this decision has to be made at runtime by dispatching a function call to another function or by modifying its behavior in place.

**Note:** Don’t confuse function overloading with [method overriding](https://realpython.com/python312-typing/#model-inheritance-with-override), which involves redefining a method in a subclass that already exists in the parent class.

Although Python supports [overloading most of its operators](https://realpython.com/operator-function-overloading/) through [special methods](https://realpython.com/python-magic-methods/), it doesn’t natively support overloading user-defined functions or methods. Since the last definition overwrites all previous function definitions with the same name, you can only emulate overloading in Python to some extent. A popular method entails using a chain of `if isinstance()` checks, like so:

Language: Python

```
>>> def double(value):
...     if isinstance(value, str):
...         return f"{value} {value}"
...     if isinstance(value, int | float | complex):
...         return 2 * value
...     elif hasattr(value, "__iter__"):
...         return [double(x) for x in value]
...     else:
...         raise TypeError("invalid argument")
...

>>> double("bye")
'bye bye'

>>> double(3)
6

>>> double(3.14)
6.28

>>> double(3 + 14j)
(6+28j)

>>> double(range(5))
[0, 2, 4, 6, 8]

>>> double(object())
Traceback (most recent call last):
  ...
TypeError: invalid argument
```

Technically, you’re calling one function, but it changes its behavior based on the type or interface of the supplied argument.

Because this kind of check is done at runtime when you have additional information, you’re no longer constrained to just the number and types of arguments. You can overload your function based on any condition, including parameter values and shapes, such as their length or dimensions. This is where pattern matching fits in perfectly.

For example, you can elegantly implement a [variadic function](https://en.wikipedia.org/wiki/Variadic_function) that will accept a variable-length list of arguments and convert them into a tuple of [RGB color](https://en.wikipedia.org/wiki/RGB_color_model) values:

Language: Python

```
>>> def color(*args):
...     match args:
...         case int(c), int(m), int(y), int(k) if bounded(0, 100, args):
...             r = 255 * (1 - c / 100) * (1 - k / 100)
...             g = 255 * (1 - m / 100) * (1 - k / 100)
...             b = 255 * (1 - y / 100) * (1 - k / 100)
...             return round(r), round(g), round(b)
...         case int(r), int(g), int(b) if bounded(0, 255, args):
...             return r, g, b
...         case float(r), float(g), float(b) if bounded(0.0, 1.0, args):
...             return round(r * 255.0), round(g * 255.0), round(b * 255.0)
...         case [str(s)] if s.startswith("#") and len(s) == 7:
...             return int(s[1:3], 16), int(s[3:5], 16), int(s[5:7], 16)
...         case [str(s)] if s.startswith("#") and len(s) == 4:
...             return int(s[1] * 2, 16), int(s[2] * 2, 16), int(s[3] * 2, 16)
...         case _:
...             raise TypeError(f"unsupported arguments: {args}")
...
>>> def bounded(min_value, max_value, values):
...     return all(min_value <= x <= max_value for x in values)
```

When you pass exactly four integer arguments, all bounded to a range between zero and one hundred, they must represent [CMYK](https://en.wikipedia.org/wiki/CMYK_color_model) percentages that you convert to the RGB color space. If there are only three integers in the range of 0 to 255, they’re assumed to be the RGB triplet itself. However, three floating-point numbers between 0\.0 and 1\.0 imply RGB values in a normalized form.

If you pass a string that starts with a hash (`"#"`) and is either seven or four characters long, then you interpret it as a [hexadecimal color](https://en.wikipedia.org/wiki/Web_colors#Hex_triplet) code in full or shorthand notation. Finally, if the arguments match none of these patterns, then you raise a `TypeError` to indicate unsupported arguments.

Go ahead and test your `color()` function with various types of inputs:

Language: Python

```
>>> color(0, 50, 75, 0)
(255, 128, 64)

>>> color(255, 128, 64)
(255, 128, 64)

>>> color(1.0, 0.5, 0.25)
(255, 128, 64)

>>> color("#ff8040")
(255, 128, 64)

>>> color("#ff0")
(255, 255, 0)

>>> color("red")
Traceback (most recent call last):
  ...
TypeError: unsupported arguments: ('red',)
```

Notice how the function correctly interprets different numbers of arguments, as well as their types and value ranges.

Structural pattern matching eliminates the verbosity that comes with explicit `isinstance()` calls that you’d typically use instead. If you just want to overload a callable based on the argument *types*, then there are more idiomatic patterns to follow. You can check them out by expanding the collapsible sections below:

**Idiom \#1:** Named ConstructorsShow/Hide

If you want to support a few alternative ways to initialize an object, then you can [provide multiple constructors](https://realpython.com/python-multiple-constructors/) in your custom data type:

Language: Python

```
from typing import NamedTuple

class Color(NamedTuple):
    red: int
    green: int
    blue: int

    @classmethod
    def from_cmyk(cls, c, m, y, k):
        r = 255 * (1 - c / 100) * (1 - k / 100)
        g = 255 * (1 - m / 100) * (1 - k / 100)
        b = 255 * (1 - y / 100) * (1 - k / 100)
        return cls(round(r), round(g), round(b))

    @classmethod
    def from_rgb(cls, r, g, b):
        if all(isinstance(x, int) and 0 <= x <= 255 for x in (r, g, b)):
            return cls(r, g, b)
        elif all(isinstance(x, float) and 0 <= x <= 1 for x in (r, g, b)):
            return cls(round(r * 255), round(g * 255), round(b * 255))
        raise ValueError("invalid RGB value")

    @classmethod
    def from_hex(cls, code):
        if code.startswith("#"):
            if len(code) == 7:
                return cls(
                    red=int(code[1:3], 16),
                    green=int(code[3:5], 16),
                    blue=int(code[5:7], 16),
                )
            elif len(code) == 4:
                return cls(
                    red=int(code[1] * 2, 16),
                    green=int(code[2] * 2, 16),
                    blue=int(code[3] * 2, 16),
                )
        raise ValueError("malformed hex code")
```

You can decide how to initialize a `Color` instance by choosing one of your named constructors.

**Idiom \#2:** Single DispatchShow/Hide

If you just want to overload a callable based on the type of its *first* argument, then use the [`@singledispatch`](https://docs.python.org/dev/library/functools.html#functools.singledispatch) or [`@singledispatchmethod`](https://docs.python.org/3/library/functools.html#functools.singledispatchmethod) decorator, which defines a [generic function](https://docs.python.org/3/glossary.html#term-generic-function):

Language: Python

```
from functools import singledispatch

@singledispatch
def pretty_print(*args, **kwargs):
    print(*args, **kwargs)

@pretty_print.register(complex)
def _(number, *args, **kwargs):
    print(f"{number.real} + {number.imag}i", *args, **kwargs)

@pretty_print.register(tuple)
@pretty_print.register(list)
def _(items, *args, **kwargs):
    pretty_print(*items, *args, **kwargs, sep=", ")
```

The first function encapsulates a fallback behavior, whereas the following ones trigger when the type of the first argument matches the type declared in the decorator.

**Idiom \#3:** Multiple DispatchShow/Hide

When you need to branch on types of multiple arguments, then you can install and use the third-party [`multipledispatch`](https://pypi.org/project/multipledispatch/) library:

Language: Python

```
from multipledispatch import dispatch

@dispatch(int, int)
def add(x, y):
    return x + y

@dispatch(object, object)
def add(x, y):
    return f"{x} + {y}"
```

This library allows you to define so-called multimethods based on the types of arguments, which is a form of [polymorphism](https://en.wikipedia.org/wiki/Polymorphism_\(computer_science\)).

Up to this point, you’ve seen legitimate uses of structural pattern matching in Python. Next up, you’ll take a look at a use case that ventures into a sort of gray zone, making some Python developers frown upon it.

### Emulate a C-Style Switch Statement in Python[](#emulate-a-c-style-switch-statement-in-python "Permanent link")

This is arguably one of the most basic use cases for pattern matching in Python, which is why it’s sometimes confused with a C-style `switch` statement. You can use this statement instead of a cascade of `if` statements to select one of many code blocks to execute.

The classic `switch` statement in C expects the expression following it to evaluate to an integer value, a character, or an enumeration member, which are numbers in disguise. [Java](https://realpython.com/java-vs-python/) has additionally allowed strings to be used as `case` labels for a while now:

Language: Java

```
String dayOfWeek = "Monday";

switch (dayOfWeek) {
    case "Saturday":
    case "Sunday":
        System.out.println("It's the weekend!");
        break;
    case "Monday":
    case "Tuesday":
    case "Wednesday":
    case "Thursday":
    case "Friday":
        System.out.println("It's a work day.");
        break;
    default:
        System.out.println("It's not a day at all.");
}
```

In contrast, you can use any data type with Python’s pattern matching. When you employ literal, value, or class patterns, then you can branch your code on the value using exact matching similar to the traditional `switch` statement.

Python’s counterpart to the above code, which is based on literal patterns, would look as follows:

Language: Python

```
day_of_week = "Monday"

match day_of_week:
    case "Saturday" | "Sunday":
        print("It's the weekend!")
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("It's a work day.")
    case _:
        print("It's not a day at all.")
```

Alternatively, if you want to use structural pattern matching against enumeration members, then you can combine value and class patterns instead:

Language: Python

```
import enum

class DayOfWeek(enum.Enum):
    (MONDAY, TUESDAY, WEDNESDAY, THURSDAY,
     FRIDAY, SATURDAY, SUNDAY) = range(7)

day_of_week = DayOfWeek.MONDAY

match day_of_week:
    case DayOfWeek.SATURDAY | DayOfWeek.SUNDAY:
        print("It's the weekend!")
    case DayOfWeek():
        print("It's a work day.")
    case _:
        print("It's not a day at all.")
```

A notable difference between the C-style `switch` statement and Python’s `match` statement is that, in Python, there’s no [fallthrough behavior](#case-clauses-dont-fall-through). Since at most one `case` block will ever run, you don’t need to explicitly stop the processing by putting the `break` statement after each `case` clause. To handle multiple cases with a common branch, you combine your subpatterns using the OR pattern (`|`).

When you use this kind of pattern matching to dispatch a function based on the values of its arguments, then a common idiom is to use a [lookup table (LUT)](https://realpython.com/python310-new-features/#matching-literal-patterns) based on a Python dictionary, as you saw earlier.

However, since this isn’t about branching on the structure, consider using more idiomatic approaches, like a chain of `if..elif...` clauses, which has been the traditional way of emulating the `switch` statement in Python:

Language: Python

```
day_of_week = "Monday"

if day_of_week in ("Saturday", "Sunday"):
    print("It's the weekend!")
elif day_of_week in ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday"):
    print("It's a work day.")
else:
    print("It's not a day at all.")
```

This will look more familiar to Python developers, and it saves you some indentation space as a bonus.

Now that you’ve seen the strengths of structural pattern matching in Python, it’s time to examine its weaknesses and limitations.

## Recognizing Python’s Pattern Matching Limitations[](#recognizing-pythons-pattern-matching-limitations "Permanent link")

In this section, you’ll learn about the several potential surprises to watch out for when you work with Python’s pattern matching. If you’ve gone through this whole tutorial, then consider this a helpful reminder, as most of these points have been mentioned before. You’ll revisit them now for a quick summary of Python’s pattern matching limitations.

### Match Is a Statement, Not an Expression[](#match-is-a-statement-not-an-expression "Permanent link")

If you’re coming from Scala, then you might be accustomed to using `match` as an expression. The language’s syntax allows you to evaluate a matched pattern and assign the result to a variable. Here’s an example:

Language: Scala

```
def numberToText(number: Int): String = {
  val suffix = number % 100 match {
    case 11 | 12 | 13 => "th"
    case _ => number % 10 match {
      case 1 => "st"
      case 2 => "nd"
      case 3 => "rd"
      case _ => "th"
    }
  }
  s"$number$suffix"
}
```

This function takes a number as an argument and returns the corresponding string representation with an appropriate ordinal suffix, such as `"42nd"`. Notice how you conveniently assign the result of the outer `match` expression to the variable `suffix`. Similarly, your nested `match` expression bubbles up with the evaluated string.

Recent versions of Java also support pattern matching through [`switch` expressions](https://openjdk.org/jeps/325), which look as follows:

Language: Java

```
String dayOfWeek = "Monday";
String message = switch (dayOfWeek) {
    case "Saturday", "Sunday" -> "It's the weekend!";
    case "Monday",
         "Tuesday",
         "Wednesday",
         "Thursday",
         "Friday" -> "It's a work day.";
    default -> "It's not a day at all.";
};
```

Here, you assign the value of the `switch` expression to a variable named `message`. You could also pass the entire expression as an argument to [`System.out.println()`](https://docs.oracle.com/en/java/javase/22/docs/api/java.base/java/lang/System.html#out) or another method.

In contrast, Python’s `match` remains a **statement**, so you can’t evaluate it and assign the result to a variable, pass it around, or return it from a function. This was a conscious design decision to keep the syntax consistent with other Python constructs that introduce a block of code with a colon (`:`).

That being said, you can wrap your `match` statement inside a function to achieve a similar effect:

Language: Python

```
>>> def http_status(code):
...     match code:
...         case 200: return "OK"
...         case 400: return "Bad Request"
...         case 401: return "Unauthorized"
...         case 403: return "Forbidden"
...         case 404: return "Not Found"
...         case 405: return "Method Not Allowed"
...         case 500: return "Internal Server Error"
...
>>> http_status(404)
'Not Found'
```

Your function translates numeric HTTP status codes into their respective standard message strings. This can be useful for [logging](https://realpython.com/python-logging/) or in any context where you need human-readable status messages. Note that Python already ships with the [`http.HTTPStatus`](https://docs.python.org/3/library/http.html#http.HTTPStatus) enumeration, which provides a convenient way to work with these codes.

### Case Clauses Aren’t Exhaustive[](#case-clauses-arent-exhaustive "Permanent link")

In languages like Rust, Scala, and Java, the `match` and `switch` statements are exhaustive, meaning they always cover all possible cases or values of the subject. If you fail to cover *every* single case, or if you don’t provide a default one, then you’ll get a syntax error, and your program won’t compile:

Language: Shell

```
$ javac Main.java
Main.java:8: error:
⮑ the switch expression does not cover all possible input values
        String message = switch (dayOfWeek) {
                         ^
1 error
```

The compiler ensures that your program handles every possible scenario, preventing potential runtime errors.

Python is different, letting you decide whether you want your cases to be exhaustive or not. For instance, the following code snippet covers only two out of seven members of an enumeration that you defined previously:

Language: Python

```
>>> match DayOfWeek.MONDAY:
...     case DayOfWeek.SATURDAY | DayOfWeek.SUNDAY:
...         weekend = True
...
>>> weekend
Traceback (most recent call last):
  ...
NameError: name 'weekend' is not defined
```

Because the subject doesn’t match any of the subpatterns, your `case` clause never runs, leaving the `weekend` variable undefined.

Although you’re not required to include a default case, it’s usually a good idea to define one at the bottom of your `match` block using the wildcard pattern (`case _:`). Naturally, you should implement the appropriate fallback logic there to handle any unmatched cases.

### Case Clauses Don’t Fall Through[](#case-clauses-dont-fall-through "Permanent link")

Another surprising quirk of Python’s `case` clauses is that they don’t [fall through](https://en.wikipedia.org/wiki/Switch_statement#Fallthrough) like the `switch` cases in C and Java. In those languages, you must explicitly include the `break` statement after each `case` block to prevent the execution from continuing into the next case. However, a fall-through behavior may occasionally be desirable.

By skipping the `break` statement, you allow your program to execute multiple `case` blocks sequentially until it encounters the first `break` statement. Most commonly, the blocks without a `break` statement will be empty so that you can apply the same logic to multiple values like in the example you saw earlier:

Language: Java

```
String dayOfWeek = "Monday";

switch (dayOfWeek) {
    case "Saturday":
    case "Sunday":
        System.out.println("It's the weekend!");
        break;
    case "Monday":
    case "Tuesday":
    case "Wednesday":
    case "Thursday":
    case "Friday":
        System.out.println("It's a work day.");
        break;
    default:
        System.out.println("It's not a day at all.");
}
```

Several case labels fall through to a common block of code, allowing you to group days of the week into weekends and workdays without repeating yourself.

In rare cases, you’ll have a chain of non-empty `case` blocks without the `break` statements, which can be helpful in performing incremental computations like these:

Language: Java

```
private List<DayOfWeek> getDaysRemaining(int dayNumber) {
    final List<DayOfWeek> daysRemaining = new ArrayList<>();
    switch (dayNumber) {
        case 1:  daysRemaining.add(DayOfWeek.SUNDAY);
        case 2:  daysRemaining.add(DayOfWeek.MONDAY);
        case 3:  daysRemaining.add(DayOfWeek.TUESDAY);
        case 4:  daysRemaining.add(DayOfWeek.WEDNESDAY);
        case 5:  daysRemaining.add(DayOfWeek.THURSDAY);
        case 6:  daysRemaining.add(DayOfWeek.FRIDAY);
        case 7:  daysRemaining.add(DayOfWeek.SATURDAY);
                 break;
        default:
            throw new IllegalArgumentException("Invalid day number");
    }
    return daysRemaining;
}
```

This method returns a list of remaining days until the end of the week. It takes a day number as an argument and translates it into a `DayOfWeek` instance. Note that the lack of `break` statements means that the `switch` statement will include all subsequent days up to Saturday due to the fallthrough behavior.

On the other hand, when you use Python’s pattern matching as a form of the C-style `switch` statement, you’ll notice that each case is independent. In other words, you never use `break` statements because at most one `case` clause will ever run. This saves you some typing, makes your code more readable, and keeps you from worrying about accidentally omitting a `break` statement.

At the same time, you can group multiple cases with an OR pattern to avoid code duplication if you need to.

### Case Clauses Can Overlap[](#case-clauses-can-overlap "Permanent link")

As mentioned previously, structural patterns can overlap with each other, making the same subject match a few of them simultaneously. When they do, their order matters because Python evaluates them from top to bottom, and only one `case` clause in a `match` block can run.

As a rule of thumb, you should start with the most specific pattern, gradually moving to more general patterns. This is similar to how you handle [exceptions](https://realpython.com/python-exceptions/) in Python. If you don’t follow this rule, then you risk causing a surprising behavior or making the remaining cases unreachable, resulting in a syntactical error.

Consider the following example of the popular [fizz buzz](https://en.wikipedia.org/wiki/Fizz_buzz) problem, which is implemented incorrectly:

Language: Python

```
for x in range(1, 101):
    match x:
        case _ if x % 3 == 0:
            print("fizz")
        case _ if x % 5 == 0:
            print("buzz")
        case _ if x % 15 == 0:
            print("fizzbuzz")
        case _:
            print(x)
```

When you run this code, you’ll notice that the word *fizzbuzz* never appears on the screen. Can you spot where the problem lies?

It’s because the third `case` clause never succeeds since either the first or second one is matched before. After all, any number divisible by fifteen is also divisible by three and five. Therefore, the third pattern is effectively ignored. To fix this, you should check for divisibility by fifteen first:

Language: Python

```
for x in range(1, 101):
    match x:
        case _ if x % 15 == 0:
            print("fizzbuzz")
        case _ if x % 3 == 0:
            print("fizz")
        case _ if x % 5 == 0:
            print("buzz")
        case _:
            print(x)
```

A number that’s *not* divisible by fifteen can still be divisible by three or five. That’s the correct implementation of fizz buzz using pattern matching in Python.

Here’s another example illustrating a slightly different situation:

Language: Python

```
>>> match input("Type your command: "):
...     case command:
...         print(f"You typed: {command}")
...     case _:
...         print("Not a command")
  File "<input>", line 2
SyntaxError: name capture 'command' makes remaining patterns unreachable
```

Here, the first pattern is a capture pattern without any guards, so it’ll *always* succeed, rendering the remaining patterns unreachable. You can sometimes fix this by reordering your `case` clauses. However, in this case, both patterns will match any subject, so you must make the capture pattern more specific by augmenting it with a conditional expression.

### Case Clauses Can’t Have Assignment Expressions[](#case-clauses-cant-have-assignment-expressions "Permanent link")

It’s okay to use the Walrus operator (`:=`) in your `match` statements, which can be convenient when you need to refer to the evaluated subject within the same code block. However, Python explicitly forbids using these assignment expressions in `case` clauses, as they could easily be confused with matching keyword subpatterns in class patterns:

Language: Python

```
match (path := Path(__file__)).suffix:
    case ".exe":
        print(f"Binary executable: {path.name!r}")
    case ".zip":
        print(f"Python ZIP package: {path.name!r}")
    case file_extension if file_extension in (".py", ".pyc", ".pyw"):
        print(f"Python module: {path.name!r}")
    case _ as file_extension:
        print(f"Unknown file type: {file_extension!r}")
```

If you need to access the matched pattern, then you can always define a capture pattern or make an alias with an AS pattern, as shown above.

### Not All Patterns Are Made Equal[](#not-all-patterns-are-made-equal "Permanent link")

Although most built-in types, such as `int` and `float`, have the corresponding **class patterns** that allow you to destructure them using a single value, others don’t. For example, Python’s `complex` type consists of two separate values, which must be destructured using the **keyword patterns** rather than positional capture patterns:

Language: Python

```
>>> match 3 + 2j:
...     case complex(real=re, imag=im):
...         print(f"{re=}, {im=}")
...
re=3.0, im=2.0
```

When you omit the complex number constructor’s argument names, then you’ll end up with an error:

Language: Python

```
>>> match 3 + 2j:
...     case complex(re, im):
...         print(f"{re=}, {im=}")
...
Traceback (most recent call last):
  ...
TypeError: complex() accepts 0 positional sub-patterns (2 given)
```

This makes sense, given what you learned previously about class patterns, but it may be a little surprising if you’re used to working with integers and floating-point numbers:

Language: Python

```
>>> match 3.14:
...     case float(real):
...         print(f"{real=}")
...
real=3.14
```

This works as expected because the floating-point number’s constructor takes only one argument, leaving no room for ambiguity.

### Matching a Python Set Requires a Guard[](#matching-a-python-set-requires-a-guard "Permanent link")

While sequence and mapping patterns allow you to match lists and tuples, among other data structures, there’s no dedicated syntax for matching [Python sets](https://realpython.com/python-sets/), which require a different approach. Sets and [frozen sets](https://realpython.com/python-sets/#frozen-sets) are merely unordered collections of elements that don’t have an inherent *structure* to match on. Instead, you can match them by value.

One way to do this is to use a **class pattern** combined with a **guard**. For example, you can check if a set contains one or more of the specified elements:

Language: Python

```
def is_authorized(user):
    match user.roles:
        case set(roles) if roles & {"admin", "staff"}:
            return True
        case _:
            return False
```

This function checks if the given user has the necessary roles to be considered authorized. By using the ampersand operator (`&`), you find the [intersection](https://en.wikipedia.org/wiki/Intersection_\(set_theory\)) of the user’s roles with the set of authorizing roles. If the user has either an `"admin"` or `"staff"` role or both, then you return `True`. Otherwise, you return `False`.

Alternatively, to match a Python set exactly, you can use the equality test operator (`==`) or wrap your set in some kind of namespace to leverage the **value pattern**:

Language: Python

```
class Roles:
    AUTHORIZED = {"admin", "staff"}

def is_authorized(user):
    match user.roles:
        case Roles.AUTHORIZED:
            return True
        case _:
            return False
```

Here, you placed the expected set of roles under a class so that you can reference it using the dot operator, as in `Roles.AUTHORIZED`. The difference is that now, the user must have both `"admin"` and `"staff"` roles to be authorized.

To learn more about matching Python sets, you can read a [StackOverflow answer](https://stackoverflow.com/questions/67828095/structural-pattern-matching-python-matching-a-set-frozenset/67893188#67893188) by [Brandt Bucher](https://github.com/brandtbucher), who is the author of the structural pattern matching specification ([PEP 634](https://peps.python.org/pep-0634/)).

### Most Literal Patterns Match by Equality[](#most-literal-patterns-match-by-equality "Permanent link")

Python compares most literal patterns to the subject by means of **value equality**. In other words, you can have two independent objects, potentially of different data types, stored in distinct areas of computer memory, and they’ll still have equal values.

For instance, the integer `1` is considered equal to the floating-point number `1.0`, the complex number `1 + 0j`, and the Boolean value `True`:

Language: Python

```
>>> 1 == 1.0 == 1 + 0j == True
True
```

Because of this equality, you can sometimes observe surprising effects in pattern matching. Here’s an example demonstrating a **literal pattern** that matches several different subjects:

Language: Python

```
>>> for subject in [1, 1.0, 1 + 0j, True]:
...     match subject:
...         case 1:
...             print(f"Matched: {subject!r}")
...
Matched: 1
Matched: 1.0
Matched: (1+0j)
Matched: True
```

If that’s an undesirable behavior, then you can wrap your literal value in an appropriate class pattern for a stricter type control:

Language: Python

```
>>> for subject in [1, 1.0, 1 + 0j, True]:
...     match subject:
...         case int(1):
...             print(f"Matched: {subject!r}")
...
Matched: 1
Matched: True
```

Now, the floating-point and complex numbers no longer match your pattern. Still, the Boolean value slipped through the cracks since `bool` is a subtype of `int` in Python. You can use a guard or ignore Boolean subjects to have an even more strict control:

Language: Python

```
>>> for subject in [1, 1.0, 1 + 0j, True]:
...     match subject:
...         case bool():
...             pass
...         case int(1) if not isinstance(subject, bool):
...             print(f"Matched: {subject!r}")
...
Matched: 1
```

Either of the highlighted patterns would do the trick to filter out the unwanted subjects.

Having said that, there are three literal patterns that use **identity equality** instead of the ordinary value equality to determine if they match the subject. More specifically, they’re the two Boolean values, `True` and `False`, as well as the empty value of `None`.

Here’s another example showing that only the last subject matches the literal pattern `True`:

Language: Python

```
>>> for subject in [1, 1.0, 1 + 0j, True]:
...     match subject:
...         case True:
...             print(f"Matched: {subject!r}")
...
Matched: True
```

Even though other subjects represent the same value, only one of them has exactly the same identity as your pattern.

### Floating-Point Patterns Are Imprecise[](#floating-point-patterns-are-imprecise "Permanent link")

Languages like Rust completely disallow floating-point literals in pattern matching due to the [representation error](https://docs.python.org/3/tutorial/floatingpoint.html#representation-error), which makes comparing them by value tricky. Python doesn’t impose such a restriction, but that can sometimes lead to unexpected results like what’s shown below:

Language: Python

```
>>> for value in (0.3, 0.1 + 0.2):
...     match value:
...         case 0.3:
...             print("Matched: 3/10")
...         case _:
...             print("Didn't match:", value)
...
Matched: 3/10
Didn't match: 0.30000000000000004
```

Notice how your pattern matched the floating-point literal `0.3` but didn’t match the corresponding arithmetic expression, which should theoretically evaluate to the same value. Unfortunately, unlike the floating-point value `0.3`, the other two numbers don’t have an exact binary representation in computer memory, introducing a tiny but noticeable error.

**Note:** This example isn’t specific to Python. You’ll observe identical behavior in practically any programming language that supports the [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754) standard.

To avoid such surprises, consider replacing floating-point numbers with alternative representations based on other data types, such as `int` or `Decimal`. Alternatively, if you absolutely must use floating-point numbers, then build your patterns around guards that call [`math.isclose()`](https://realpython.com/python-math-module/#find-the-closeness-of-numbers-with-python-isclose).

### String Patterns Are Not Sequences[](#string-patterns-are-not-sequences "Permanent link")

Strings, bytes, and byte arrays are among the sequence data types in Python that share similar properties and behavior. They’re data containers of a fixed length that you can iterate over or access their individual elements by index. You may also destructure such sequences into variables using the iterable unpacking syntax:

Language: Python

```
>>> first, *_, last = "¿Cómo estás hoy?"
>>> first
'¿'
>>> last
'?'
```

However, strings and their binary counterparts are more commonly treated as standalone **scalar values** rather than sequences. To avoid ambiguity, Python’s sequence patterns exclude strings, bytes, and byte arrays from matching. Instead, you must use literal patterns to match them by value or wrap the subject in another sequence type like a Python list beforehand:

Language: Python

```
>>> match "¿Cómo estás hoy?":
...     case str(text) if text.startswith("¿") and text.endswith("?"):
...         print(f"Matched a question: {text[1:-1]}")
...
Matched a question: Cómo estás hoy

>>> match list("¿Cómo estás hoy?"):
...     case [first, *_, last]:
...         print(f"Matched {first=} {last=}")
...
Matched first='¿' last='?'
```

In the first case, you use a class pattern with a capture pattern augmented with a guard. In the second case, you convert the string subject to a list of separate characters.

### Captured Names May Wind Up Undefined[](#captured-names-may-wind-up-undefined "Permanent link")

Because `case` clauses in Python are non-exhaustive, it’s possible that none of them will run at all. Even if you ensure exhaustiveness by specifying a default catch-all case, you may still fail to initialize the variables expected after your `match` block. That’s what happens here:

Language: Python

```
>>> event = {"type": "mouse", "cursor": [823, 375]}

>>> match event:
...     case {"type": "keyboard", "key": key_code}:
...         print("Detected a keyboard event")
...     case _:
...         print("Ignoring an unknown event")
...
Ignoring an unknown event

>>> key_code
Traceback (most recent call last):
  ...
NameError: name 'key_code' is not defined
```

If the mapping pattern succeeds, then it’ll define a `key_code` variable through a capture pattern. However, the wildcard pattern below doesn’t define such a variable. As a result, the `key_code` variable remains undefined since the actual event object isn’t of the keyboard type. This leads to a `NameError` when you try to access `key_code` afterward.

To prevent this potential issue, you should ensure that all variables expected after the `match` block are initialized beforehand or in each `case` block, including the default one. Here’s an example of how you can do this:

Language: Python

```
>>> event = {"type": "mouse", "cursor": [823, 375]}
>>> key_code = None

>>> match event:
...     case {"type": "keyboard", "key": key_code}:
...         print("Detected a keyboard event")
...     case _:
...         print("Ignoring an unknown event")
...
Ignoring an unknown event

>>> if key_code is not None:
...     print(f"{key_code=}")
... else:
...     print("No key code available")
...
No key code available
```

By initializing `key_code` to `None` before the `match` block, you guarantee that the variable will exist, regardless of whether the pattern that defines it is executed.

### Capture Patterns Can’t Reuse Variables[](#capture-patterns-cant-reuse-variables "Permanent link")

When you have more than one capture pattern in your `case` clause, then each must bind the corresponding value to a different name. Otherwise, you’ll end up with a syntax error:

Language: Python

```
match (42, 42):
    case [x, x]:  # SyntaxError: multiple assignments to name 'x' in pattern
        print(f"The point lies on the diagonal at ({x}, {x})")
    case _:
        print("Not on the diagonal")
```

Here, your sequence pattern uses two capture subpatterns, both named `x`, to match points that lie on the diagonal. Unfortunately, this is illegal syntax in Python because the same variable can’t be the target of two assignments.

To circumvent this limitation, you should use **distinct names** and introduce a guard to compare both coordinates as follows:

Language: Python

```
match (42, 42):
    case [x, y] if x == y:
        print(f"The point lies on the diagonal at ({x}, {y})")
    case _:
        print("Not on the diagonal")
```

This approach avoids the syntax error and correctly identifies points on the diagonal. On the other hand, it’s perfectly fine to reuse the same capture pattern across separate alternatives:

Language: Python

```
>>> for point in (42, 0), (0, 42), (42, 42):
...     match point:
...         case [x, 0] | [0, x]:
...             print(f"The {point=} lies on an axis")
...         case _:
...             print(f"The {point=} is not on an axis")
...
The point=(42, 0) lies on an axis
The point=(0, 42) lies on an axis
The point=(42, 42) is not on an axis
```

Even though `x` can refer to either the horizontal or vertical coordinate, there’s no conflict here because that name is always the target of at most one assignment. However, union patterns impose a different limitation around class subpatterns, which you’ll learn about next.

### Union Patterns Bind the Same Names[](#union-patterns-bind-the-same-names "Permanent link")

Whenever you combine multiple class patterns using the **OR pattern**, then each must define *precisely* the same set of names to bind to, although they can be listed in arbitrary order. For example, you can’t have a sequence pattern with two nested class patterns followed by a literal pattern that doesn’t bind any names:

Language: Python

```
match point:
    case [x, y] | 0:  # Alternative patterns bind different names
        print("Matched a point or zero")
    case _:
        print("Matched something else")
```

In the example above, the first alternative, `[x, y]`, binds the names `x` and `y`, while the second alternative, `0`, doesn’t bind any names, leading to a syntax error.

Moreover, you’re not allowed to use different names for the same target in your alternatives:

Language: Python

```
match point:
    case [1, x] | [2, y]:  # Alternative patterns bind different names
        ...
```

Notice that `x` and `y` essentially bind the same value. However, based on the first element in the sequence, only one of these variables will be defined at any given time, leaving the other variable undefined. Therefore, you must use `x` in both alternatives to avoid ambiguity.

### Matching Constant Values Is Tricky[](#matching-constant-values-is-tricky "Permanent link")

Python has no way of differentiating between variables and constants because there’s no syntactical difference between them. The distinction is purely semantic, so when you try to [match a constant value](https://peps.python.org/pep-0622/#note-about-constants), you’re inadvertently creating a **capture pattern** that matches everything:

Language: Python

```
>>> import random

>>> RANDOM_NUMBER = random.randint(1, 100)
>>> RANDOM_NUMBER
77

>>> match int(input("Guess a number between 1 and 100: ")):
...     case RANDOM_NUMBER:
...         print("You won!")
...
Guess a number between 1 and 100: 50
You won!

>>> RANDOM_NUMBER
50
```

In this example, Python randomly picked a number equal to seventy-seven. However, your capture pattern, `RANDOM_NUMBER`, always matches any subject, wrongly indicating that the player guessed the number and overwriting the original constant.

Moreover, when you try to add subsequent cases, you’ll notice they’re unreachable because the first pattern always matches the subject:

Language: Python

```
>>> match int(input("Guess a number between 1 and 100: ")):
...     case RANDOM_NUMBER:
...         print("You won!")
...     case number if number > RANDOM_NUMBER:
...         print("Too low!")
  File "<input>", line 2
SyntaxError: name capture 'RANDOM_NUMBER' makes remaining patterns unreachable
```

In short, there’s no way to match constant values by their unqualified names since they become capture patterns that bind the corresponding values to variables. The only way to match constants in Python is to put them under a namespace—for example, inside a class, enum, or module—and refer to them through dotted **value patterns** or use guards accordingly.

## Conclusion[](#conclusion "Permanent link")

Congratulations! You’ve now acquired a thorough understanding of structural pattern matching in Python. By mastering the `match` statement and `case` clauses, you’ve unlocked powerful tools for writing more concise and readable code.

Along the way, you explored a wide variety of pattern types, from simple literals and value patterns to more complex sequences, mappings, and class patterns. You’ve also learned how to customize pattern matching for user-defined classes so you can extend this powerful feature to your own types.

**In this tutorial, you’ve:**

- Mastered the **syntax** of the `match` statement and `case` clauses

- Explored various **types of patterns** supported by Python

- Learned about **guards**, **unions**, **aliases**, and **name binding**

- Extracted values from deeply nested **hierarchical data structures**

- Customized pattern matching for **user-defined classes**

- Identified and avoided **common pitfalls** in Python’s pattern matching

With this knowledge in your toolkit, you can now leverage structural pattern matching to make your Python code more declarative and expressive. Whether you’re validating data, implementing control flow, or just aiming to write cleaner, more maintainable code, pattern matching can be a powerful ally.

**Get Your Free Code:** [Click here to download the free sample code](https://realpython.com/bonus/structural-pattern-matching-code/) that shows you how to use structural pattern matching in Python.

 **Take the Quiz:** Test your knowledge with our interactive “Structural Pattern Matching” quiz. You’ll receive a score upon completion to help you track your learning progress:

---

[](/quizzes/structural-pattern-matching/)

![Structural Pattern Matching in Python](https://files.realpython.com/media/Structural-Pattern-Matching-in-Python-3.10_Watermarked-2.085d2bfb1940.jpg)

**Interactive Quiz**

[Structural Pattern Matching](/quizzes/structural-pattern-matching/)

In this quiz, you'll test your understanding of structural pattern matching in Python. This powerful control flow construct, introduced in Python 3\.10, offers concise and readable syntax while promoting a declarative code style.

Mark as Completed

[](/feedback/survey/article/structural-pattern-matching/liked/?from=article-footer "Liked it") [](/feedback/survey/article/structural-pattern-matching/disliked/?from=article-footer "Disliked it")

Share

Recommended Course

[Using Structural Pattern Matching in Python](/courses/structural-pattern-matching/) (53m)

🐍 Python Tricks 💌

Get a short & sweet **Python Trick** delivered to your inbox every couple of days. No spam ever. Unsubscribe any time. Curated by the Real Python team.

![Dictionary merging in Python 3.5+](https://files.realpython.com/media/pytrick-dict-merge.4201a0125a5e.png)

Send Me Python Tricks »

About **Bartosz Zaczyński**

Bartosz is an experienced software engineer and Python educator with an M.Sc. in Applied Computer Science.

[» More about Bartosz](/team/bzaczynski/)

---

*Each tutorial at Real Python is created by a team of developers so that it meets our high quality standards. The team members who worked on this tutorial are:*

[](/team/asantos/)

Aldren

[](/team/bweleschuk/)

Brenda

[](/team/gahjelle/)

Geir Arne

Master Real-World Python Skills With Unlimited Access to Real Python

![Locked learning resources](/static/videos/lesson-locked.f5105cfd26db.svg)

**Join us and get access to thousands of tutorials, hands-on video courses, and a community of expert Pythonistas:**

[Level Up Your Python Skills »](/account/join/?utm_source=rp_article_footer&utm_content=structural-pattern-matching)

Master Real-World Python Skills
With Unlimited Access to Real Python

![Locked learning resources](/static/videos/lesson-locked.f5105cfd26db.svg)

**Join us and get access to thousands of tutorials, hands-on video courses, and a community of expert Pythonistas:**

[Level Up Your Python Skills »](/account/join/?utm_source=rp_article_footer&utm_content=structural-pattern-matching)

What Do You Think?

**Rate this article:**

[](/feedback/survey/article/structural-pattern-matching/liked/?from=article-comments "Liked it") [](/feedback/survey/article/structural-pattern-matching/disliked/?from=article-comments "Disliked it")

[LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Frealpython.com%2Fstructural-pattern-matching%2F) [Twitter](https://twitter.com/intent/tweet/?text=Interesting%20Python%20article%20on%20%40realpython%3A%20Structural%20Pattern%20Matching%20in%20Python&url=https%3A%2F%2Frealpython.com%2Fstructural-pattern-matching%2F) [Bluesky](https://bsky.app/intent/compose?text=Interesting%20Python%20article%20on%20%40realpython.com%3A%20Structural%20Pattern%20Matching%20in%20Python%20https%3A%2F%2Frealpython.com%2Fstructural-pattern-matching%2F) [Facebook](https://facebook.com/sharer/sharer.php?u=https%3A%2F%2Frealpython.com%2Fstructural-pattern-matching%2F) [Email](mailto:?subject=Python%20article%20for%20you&body=Structural%20Pattern%20Matching%20in%20Python%20on%20Real%20Python%0A%0Ahttps%3A%2F%2Frealpython.com%2Fstructural-pattern-matching%2F%0A)

What’s your \#1 takeaway or favorite thing you learned? How are you going to put your newfound skills to use? Leave a comment below and let us know.

**Commenting Tips:** The most useful comments are those written with the goal of learning from or helping out other students. [Get tips for asking good questions](https://realpython.com/python-beginner-tips/#tip-9-ask-good-questions) and [get answers to common questions in our support portal](https://support.realpython.com).

---

Looking for a real-time conversation? Visit the [Real Python Community Chat](/community/) or join the next [“Office Hours” Live Q&A Session](/office-hours/). Happy Pythoning!

Keep Learning

Related Topics: [intermediate](/tutorials/intermediate/) [python](/tutorials/python/)

Related Courses:

- [Using Structural Pattern Matching in Python](/courses/structural-pattern-matching/?utm_source=realpython&utm_medium=web&utm_campaign=related-course&utm_content=structural-pattern-matching)

Related Tutorials:

- [Python while Loops: Repeating Tasks Conditionally](/python-while-loop/?utm_source=realpython&utm_medium=web&utm_campaign=related-post&utm_content=structural-pattern-matching)

- [The Walrus Operator: Python's Assignment Expressions](/python-walrus-operator/?utm_source=realpython&utm_medium=web&utm_campaign=related-post&utm_content=structural-pattern-matching)

- [Data Classes in Python (Guide)](/python-data-classes/?utm_source=realpython&utm_medium=web&utm_campaign=related-post&utm_content=structural-pattern-matching)

- [Build Enumerations of Constants With Python's Enum](/python-enum/?utm_source=realpython&utm_medium=web&utm_campaign=related-post&utm_content=structural-pattern-matching)

- [Regular Expressions: Regexes in Python (Part 1)](/regex-python/?utm_source=realpython&utm_medium=web&utm_campaign=related-post&utm_content=structural-pattern-matching)
