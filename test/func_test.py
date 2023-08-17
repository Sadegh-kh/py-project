def get_formatted_name(first, last, middle=""):
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()


def test_first_last_name():
    """Do names like 'Ali Khoshbayan' work?"""
    formatted_name = get_formatted_name("ali", "khoshbayan", "soltan")
    assert formatted_name == "Ali Khoshbayan"
