


def is_palindrome_phrase(String: str):
    punctuation = """
    !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    """
    cleared_string = String.replace(" ", "")
    for i in punctuation:
        cleared_string = cleared_string.replace(i, '')
    if cleared_string == cleared_string[::-1]:
        return True
    else:
        return False


print(is_palindrome_phrase(" me em !# e em"))

