import pathlib
from pathlib import Path


cwd = pathlib.Path.cwd()
print(cwd)
print(cwd.parent)
print(cwd.is_dir())
print(cwd.parent.is_fifo())

for child in cwd.parent.iterdir():
    if child.is_dir():
        print(child)


new_file = Path.joinpath(cwd, 'new_file.txt')
print(new_file)
