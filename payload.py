import ycmd
import ycmd.identifier_utils
import re

regex = re.compile( r"[_a-zA-Z-][\w:-]*", re.UNICODE)

ycmd.identifier_utils.FILETYPE_TO_IDENTIFIER_REGEX["sh"]   = regex
ycmd.identifier_utils.FILETYPE_TO_IDENTIFIER_REGEX["bash"] = regex
ycmd.identifier_utils.FILETYPE_TO_IDENTIFIER_REGEX["zsh"]  = regex
