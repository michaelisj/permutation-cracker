ENCODING = "UTF8"
NEWLINE = "\r\n"


def read_utf8_encrypted_file(filePath: str) -> str:
    """Reads a UTF8 encoded file, and removes all spaces 
    and newlines

    Args:
        filePath (str):

    Returns:
        str: string containing the stripped file content
    """

    with open(filePath, "rb") as f:
        content = f.read().decode(ENCODING)
    return content.replace(NEWLINE, "").replace(" ", "")
