# pySpaceBremen
# 2024-11-30
# first.py

from fasthtml import common as fh

app, rt = fh.fast_app(live=True)


@rt('/')
def index():
    return fh.P('Hallo Welt!')


fh.serve()
