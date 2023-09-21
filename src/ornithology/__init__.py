"""
Produces thoughtful and provoking modern art
"""

from textwrap import dedent

def bird() -> str:
    artwork = (
        r"""
          _____
         /     \
        |     o |
        |        >
        |  V    |
        |       |
        |_______|
          |   |
          +<  +<
        """
    )
    return dedent(artwork[1:])

