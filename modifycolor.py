# import modules for replace function
from tempfile import mkstemp
from shutil import move
from os import fdopen, remove

import os
import regexcolors
import shelve


# takes a file and replaces a line with given string
def replace(file_path, pattern, subst):
    # Create temp file
    fh, abs_path = mkstemp()
    with fdopen(fh, 'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                new_file.write(line.replace(pattern, subst))
    # Remove original file
    remove(file_path)
    # Move new file
    move(abs_path, file_path)


# check if .vimrc exists


# if .vimrc exists, open original .vimrc and extract colorscheme line
homedir = os.environ['HOME']
file_path = homedir + '/hitman.txt'
original = ''
file = open(file_path , 'r')
for line in file:
    if 'colorscheme' in line:
        original = line
file.close()

# if .vimrc exists, but there is no colorscheme


# if .vimrc DNE, create .vimrc in users home file and add colorscheme to it


shelf_file = shelve.open('color_data')
try:
    colors_list = shelf_file['color_list']
except TypeError:
    print('Creating scheme list data...')
    colors_list = regexcolors.extract_scheme_names()
    shelf_file['color_list'] = colors_list

# select a color from the list
color = 'colorscheme ' + colors_list[5] + '\n'

# change the colorscheme in vim settings
replace(file_path, original, color)
