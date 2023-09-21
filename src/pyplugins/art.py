"""
Simple class that prints ASCII 'art'. Used to demonstrate the use of entry points for
plugins.
"""

from textwrap import dedent
from typing import Callable, Dict


class ArtPrinter:
    """
    Class that prints ASCII art of questionable quality. New art templates can
    be registered using the function ``_register``, though this should be
    handled via plugins. The ``print`` function writes art to screen, while the
    raw string can be accessed using ``get``.

    Uses classmethods entirely -- there is no need to instantiate this class.
    """

    _templates: Dict[str, Callable[[], str]] = dict()

    @classmethod
    def _register(cls, key: str, template: Callable[[], str]) -> None:
        cls._templates[key] = template

    @classmethod
    def get(cls, key: str) -> str:
        return cls._templates[key]()

    @classmethod
    def print(cls, key: str) -> None:
        print(cls.get(key))

def _default_template() -> str:
    default = (
        r"""
         ____    _____  _____     _       _    _   _       _______
        |  _ \  |  __| |  __|    / \     | |  | | | |     |__   __|
        | | \ \ | |__  | |__    / 0 \    | |  | | | |        | |
        | | | | |  __| |  __|  / ___ \   | |  | | | |        | |
        | |_/ / | |__  | |    / /   \ \  | |__| | | |____    | |
        |____/  |____| |_|   /_/     \_\ |______| |______|   |_|
        """
    )
    # First character is a newline. Skip this and remove indentation.
    return dedent(default[1:])

ArtPrinter._register("default", _default_template)
