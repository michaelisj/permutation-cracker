import datetime
import shutil
import os

ENCODING = "UTF8"
NEWLINE = "\r\n"


def read_utf8_encrypted_file(filePath: str) -> str:
    """Reads a UTF8 encoded file, and removes all newlines

    Args:
        filePath (str):

    Returns:
        str: string containing the stripped file content
    """
    import time
    with open(filePath, "rb") as f:
        content = f.read().decode(ENCODING)
    return content.replace(NEWLINE, "")


def protect_file_from_delete(filePath):
    if os.path.isfile(filePath):
        path, end = os.path.splitext(filePath)
        now = datetime.datetime.now().strftime("%H_%M_%S")
        shutil.copy(filePath, f"backups/{path}_{now}{end}")
