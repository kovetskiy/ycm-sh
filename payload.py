import ycmd
import ycmd.identifier_utils
import re
import os

regex = re.compile(r"[:_a-zA-Z0-9-]+", re.UNICODE)

ycmd.identifier_utils.FILETYPE_TO_IDENTIFIER_REGEX["sh"] = regex
ycmd.identifier_utils.FILETYPE_TO_IDENTIFIER_REGEX["bash"] = regex
ycmd.identifier_utils.FILETYPE_TO_IDENTIFIER_REGEX["zsh"] = regex

os.unlink(__file__)
os.unlink(__file__ + "c")
