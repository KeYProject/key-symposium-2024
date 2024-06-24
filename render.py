import os
import os.path
import sys
import shutil
import markdown2
import yaml 

from path import Path 

from jinja2 import Environment, FileSystemLoader, select_autoescape
env = Environment(
    loader=FileSystemLoader("_layouts"),
    autoescape=select_autoescape()
)

def _read(handle):
    meta_str = ""
    content = ""
    lines = list(handle)
    start = 0
    if lines[0] == '---':
        stop = lines.find('---',1)
        meta_str = '\n'.join( lines[1:stop])
        start = stop + 1
    content = '\n'.join(lines[start:])

    meta = yaml.loads(meta_str)

    return (meta, content)


def render_index():
    index = "index.html"
    template = env.get_template(index)

    with open(CONTENT / "index.md") as fh:
        (meta, content) = read(handle)

    with open(PUBLIC / index,'w') as fh: 
        fh.write(template.render(content=content, meta=meta))

def main():
    os.rmdir("public/")
    os.mkdir("public/")
    os.system("cp -R _static public")

    render_index()
    render_locations()
    render_program()


if __name__ == '__main__': main()