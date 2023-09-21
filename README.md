# pyplugins

This is a toy library used to understand how plugins and entry points work in Python.

## Installation

To install, clone this package and create a new virtual environment (recommended to use 
a new terminal to avoid accidentally messing up your current environment!).

```bash
$ git clone https://github.com/LiamPattinson/pyplugins
$ cd pyplugins
$ python3 -m venv venv 
$ source venv/bin/activate # Linux
$ venv/bin/Activate.ps1 # Windows
```

To install:

```bash
$ python3 -m pip install --upgrade pip
$ python3 -m pip install .
```

To run the tests:

```bash
$ python3 -m pip install .[test]
$ python3 -m pytest tests
```

## Usage

There are three component Python packages:

- `pyplugins`: A library that can be extended with plugins. It provides a class
  `ArtPrinter` that generates ASCII 'art'. Other package maintainers can extend this
  class with new templates.
- `ornithology`: A plugin for `pyplugins` that comes packages alongside `pyplugins` in
  the `src` directory.
- `radical`: A plugin for `pyplugins` that is packaged separately, with its own
  `pyproject.toml` file. This is located within the `plugins` directory.

The `ArtPrinter` can be used as so:

```python
>>> from pyplugins import ArtPrinter
>>> ArtPrinter.print("default")
```

As `ornithology` is packaged alongside `pyplugins`, the following call will also work:

```python
>>> ArtPrinter.print("bird")
```

Note that there is no need to explicitly import this library, nor is it imported within
`pyplugins`.

The `radical` library provides 'artwork' with the key `"s"`, but if we try to call the
following, we should receive a `KeyError`:

```python
>>> ArtPrinter.print("s")
```

To make this work, we need to install the `radical` library:

```bash
$ python3 -m pip install plugins/radical
```

The above call should now work.

To understand how this code works, see the `__init__.py` file within `pyplugins` and the
`[project.entry-points."pyplugins.templates"]` heading in the `pyproject.toml` files.
