from sys import argv
from os.path import exists
script, from_file, to_file = argv

open.write(to_file, 'w',indata=open.read(from_file))