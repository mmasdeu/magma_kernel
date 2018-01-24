"""A magma kernel for Jupyter"""

def readfile(filename):
    with open(filename,  encoding='utf-8') as f:
        return f.read()
__version__ = readfile(path.join(path.dirname(__file__), 'VERSION'));
assert __version__ #silence pyflakes
