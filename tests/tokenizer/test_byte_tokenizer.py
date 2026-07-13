from nanoforge.tokenizer import ByteTokenizer


def test_encode_ascii():

    tokenizer = ByteTokenizer()

    assert tokenizer.encode("ABC") == [65, 66, 67]

def test_decode_ascii():

    tokenizer = ByteTokenizer()

    assert tokenizer.decode([65, 66, 67]) == "ABC"

def test_round_trip():

    tokenizer = ByteTokenizer()

    text = "Hello NanoForge!"

    assert tokenizer.decode(
        tokenizer.encode(text)
    ) == text

def test_unicode_round_trip():

    tokenizer = ByteTokenizer()

    text = "Hello 😊 NanoForge 🚀"

    assert tokenizer.decode(
        tokenizer.encode(text)
    ) == text


def test_empty_string():

    tokenizer = ByteTokenizer()

    assert tokenizer.encode("") == []

    assert tokenizer.decode([]) == ""