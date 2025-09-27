from .text import Line
from .input import Input
from .inventory import AddItem, RemoveItem
from .redirect import Redirect
import json

def load_lines_from_file(file_name: str):
    lines = []
    data = json.load(open(file_name))
    for line in data:
        match line["type"]:
            case "input": _type = Input
            case "line": _type = Line
            case "add_item": _type = AddItem
            case "remove_item": _type = RemoveItem
            case "redirect": _type = Redirect
            case _: 
                print(f"Type {line['type']} not found!")
                _type = Line
        lines.append(_type(line))
    return lines