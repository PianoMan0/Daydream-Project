from .text import Line
from .input import Input
import json

def load_lines_from_file(file_name: str):
    lines = []
    data = json.load(open(file_name))
    for line in data:
        match line["type"]:
            case "input": _type = Input
            case "line": _type = Line
            case _: _type = Line
        lines.append(_type(line))
    return lines