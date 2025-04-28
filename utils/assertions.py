def assert_text_contains(text, expected):
    assert expected in text, f"Expected '{expected}' to be in f'{text}'"