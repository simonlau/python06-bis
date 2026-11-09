# Python 201 – All About the TypedDict

> Source: https://blog.pythonlibrary.org/2025/06/17/python-201-all-about-the-typeddict/
> Collected: 2026-11-09
> Published: 2025-06-17

Python has supported the concept of type hinting for quite a while now. However, unlike other programming languages, Python does not enforce type hints. You must use an external tool, such as Mypy, for that.

In this tutorial, you will learn all about [**TypedDict**](https://peps.python.org/pep-0589/), a special way of adding type hinting to **Heterogeneous dictionaries**. A heterogeneous dictionary is a dictionary that has values that are not all the same type.

But before you learn how to use the TypedDict, you should review how to type hint a regular dictionary.

## Type Hinting a Regular Dictionary

A regular Python dictionary is defined as follows:

```python
my_dictionary = {"some_key": "some_value"}
```

You can use any hashable type for the key, such as a string or an integer. The value of a dictionary can be any type whatsoever.

When you want to type hint a dictionary, you would use the following: **dict[key_type, value_type]**

Now let’s apply that to the example above:

```python
my_dictionary: dict[str, str] = {"some_key": "some_value"}
```

If you are using a version of Python before 3.9, you will need to do the following instead:

```python
from typing import Dict

my_dictionary: Dict[str, str] = {"some_key": "some_value"}
```

Fortunately, modern Python no longer requires that extra import.

Now you’re ready to learn about how and why you might want to use the TypedDict

## Creating a TypedDict

The TypedDict was introduced to Python in 3.8. You can read the full details about it in [PEP 589](https://peps.python.org/pep-0589/). The reason you would use a TypedDict over a regular dictionary is when you have a dictionary with values of different types.

Here’s an example:

```python
my_dictionary = {
    "names": ["Mike", "Andrea", "John"],
    "type": "employee",
    "code": 123456,
}
```

Type hinting this type of dictionary is more complex. You can do something like this, though:

```python
my_dictionary: dict[str, list | str | int] = {
    "names": ["Mike", "Andrea", "John"],
    "otype": "employee",
    "code": 123456,
}
```

Depending on how your type checker is configured, this might work. However, if you write code that modifies the list, your type checker may complain that a string doesn’t have an append method or vice versa.

To make the type checker happier, you should use a **TypedDict**.

Here’s how you would use one with this example:

```python
from typing import TypedDict


class MultiTypeDict(TypedDict):
    names: list
    otype: str
    code: int


my_dictionary: MultiTypeDict = {
    "names": ["Mike", "Andrea", "John"],
    "otype": "employee",
    "code": 123456,
}
```

Isn’t that great? There’s just one problem. What if your dictionary’s keys have spaces in them? You cannot create class attributes with spaces!

There’s a workaround for that. Check it out in the next section.

## Creating a TypedDict with Keys that Have Spaces

For this example, you will create a new dictionary with four keys, three of which contain spaces.

To make a TypedDict for this type of dictionary, you need to call the TypedDict constructor instead of subclassing it:

```python
from typing import TypedDict

Results = TypedDict(
    "Results",
    {
        "Animal Habitats": list,
        "Tested": bool,
        "Animal Name": str,
        "Animal Location": str,
    },
)

actual_results: Results = {
    "Animal Habitats": ["Asia", "N. America"],
    "Tested": False,
    "Animal Name": "Tigris",
    "Animal Location": "North Bay",
}
```

When you call TypedDict, you pass in the typename (what you would have named the class) and the fields the dictionary should have. You’ll note that the fields are a dictionary. This is where you will put the keys that contain spaces and those without spaces.

Give it a try and you’ll find it works great!

## Wrapping Up

**TypedDict** is a handy tool for storing a complex dictionary. You will find that sometimes you even have these complex dictionaries inside of lists, tuples or even other dictionaries. Using the TypedDict can make type-hinting these data structures easier and prevent hard-to-detect defects from creeping in.
