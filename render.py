#!/usr/bin/python

import os
import os.path
import sys
import shutil
import markdown2
import yaml 

from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape
env = Environment(
    loader=FileSystemLoader("_layouts"),
    autoescape=select_autoescape()
)

CONTENT = Path("content/")
PUBLIC = Path("public/")
CFG = Path("config.yml")

if CFG.exists():
    with open(CFG) as fh:
        SITE = yaml.safe_load(fh)
else:
    SITE = {}

class PageRendered:
    def __init__(self,m,c):
        self.meta = m
        self.content = c




def _read(fn):
    with open(fn) as handle:
        meta_str = ""
        content = ""
        lines = list(handle)
        start = 0

        if lines[0] == '---\n':
            try:
                stop = lines.index('---\n',1)
                meta_str = '\n'.join( lines[1:stop])
                start = stop + 1
            except ValueError:
                pass

        content = '\n'.join(lines[start:])

        meta = yaml.safe_load(meta_str)

        if str(fn).endswith(".md"):
            content = markdown2.markdown(content)

        return PageRendered(meta, content)

def _render(md, template, target):
    index = target
    template = env.get_template(template)
    page = _read(CONTENT/md)
    with open(PUBLIC/target, 'w') as fh:
        fh.write(template.render(content=page.content, page=page.meta, site=SITE))


def render_index(): _render("index.md", "index.html", "index.html")
def render_registration(): _render("registration.html", "base.html", "registration.html")
def render_locations(): pass

def render_program():
    template = env.get_template("programme.html")
    talks = []
    bySlot = {}
    p = _read(CONTENT/"programme.md")
    for fn in Path("talks/").rglob("*.md"):
        t = _read(fn)
        talks.append(t)
        try:
            bySlot[t.meta['slot']] = t
        except:
            print(f"No slot given in {fn}")

    talks = sorted(talks, key=lambda x: x.meta.get('order', 50))

    with open(PUBLIC/"programme.html", 'w') as fh:
        fh.write(template.render(content=p.content, page=p.meta, talks=talks, bySlot=bySlot, site=SITE))


def render_css():
    import sass
    content = sass.compile(dirname=("_static","public"), output_style="compressed")
    print(content)
    #with open(PUBLIC/"style.css", 'w') as fh:
    #    fh.write(content)



def main():
    if PUBLIC.exists():
        shutil.rmtree(PUBLIC)
    PUBLIC.mkdir()

    os.system("cp -R _static/* public")

    render_css()
    render_index()
    render_registration()
    render_locations()
    render_program()


if __name__ == '__main__':
    main()
