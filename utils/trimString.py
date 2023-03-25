def trimString(string, length):
    """
    Takes a string and length as input, and if there are less words than given length,
    returns the string as is. If there are more words, it keeps the first length number
    of words and adds "..." at the end.
    """

    words = string.split()
    if len(words)<=length:
        return string
    trimmed = " ".join(words[:length]) + "..."
    return trimmed