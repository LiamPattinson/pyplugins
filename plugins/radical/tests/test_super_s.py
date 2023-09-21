from pyplugins import ArtPrinter

def test_super_s():
    result = ArtPrinter.get("s")
    assert r"\ ".strip() in result
    assert "/" in result
    assert "_" in result
    assert "|" in result
