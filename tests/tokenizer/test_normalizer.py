from nanoforge.tokenizer import TextNormalizer

def test_empty_string():

    normalizer = TextNormalizer()

    assert normalizer.normalize("") == ""

def test_strip_whitespace():

    normalizer = TextNormalizer()

    assert (
        normalizer.normalize(
            "   hello  "
        )
        == "hello"
    )

def test_collapse_whitespace():

    normalizer = TextNormalizer()

    assert (
        normalizer.normalize(
            "hello     world"
        )
        == "hello world"
    )

def test_windows_line_endings():

    normalizer = TextNormalizer()

    assert (
        normalizer.normalize(
            "hello\r\nworld"
        )
        == "hello\nworld"
    )


def test_old_mac_line_endings():

    normalizer = TextNormalizer()

    assert (
        normalizer.normalize(
            "hello\rworld"
        )
        == "hello\nworld"
    )

