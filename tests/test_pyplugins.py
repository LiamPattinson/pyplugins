from pyplugins import ArtPrinter

def test_default():
    """
    Tests that the default string is registered with the ArtPrinter. It contains
    a '0' somewhere inside, so we simply check for that.
    """
    result = ArtPrinter.get("default")
    assert "0" in result

def test_bird():
    """
    Tests that the bird string is registered with the ArtPrinter. This is not
    explicitly imported anywhere, and is instead handled using entry points. We check
    for the presence of its eye, its beak, and its wings using very sophisticated
    feature recognition technology.
    """
    result = ArtPrinter.get("bird")
    assert "o" in result
    assert ">" in result
    assert "V" in result
