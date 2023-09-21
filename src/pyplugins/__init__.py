from importlib.metadata import entry_points

from .art import ArtPrinter

__all__ = ["ArtPrinter"]

# The following code handles plugin entry points

template_entry_points = entry_points()["pyplugins.templates"]

for ep in template_entry_points:
    ArtPrinter._register(ep.name, ep.load())
