from .text import Line
import json

def load_lines_from_file(file_name: str):
    lines = []
    data = json.load(open(file_name))
    for line in data:
        lines.append(Line(line))
    return lines