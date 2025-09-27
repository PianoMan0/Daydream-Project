from .text import Line

def load_lines_from_txt(file_name: str):
    lines = []
    with open(file_name) as fp:
        for line in fp.readlines():
            line = line.rstrip("\r\n").rstrip("\n")
            lines.append(Line(line))
    return lines