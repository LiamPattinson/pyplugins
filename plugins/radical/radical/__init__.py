"""
Create rad images.
"""

from textwrap import dedent

def super_s() -> str:
    result = (
        r"""
            _________
           /         \
          /           \
         /             \
        |       |       |
        |       |       |
         \       \     /
          \       \   /
           \       \ /
            \       \
           / \       \
          /   \       \
         /     \       \
        |       |       |
        |       |       |
         \             /
          \           /
           \_________/
        """
    )
    return dedent(result[1:])
