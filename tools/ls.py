'''
This file contains a function that behaves like the ls program in the shell.
'''

# step 1: create function with the right number of args; write the docstring
# step 2: create the doctests for that function
# step 3: get the function to pass doctest
# step 3b: may have to modify doctests to get them to pass
# step 4: you know you have enough doctests if you have 100% code coverage

import glob


def ls(folder=None):
    '''
    This function behaves just like the ls program in the shell.

    >>> ls()
    'README.md __pycache__ bad_encoding.bin build chat.py
    cmc_cs040_chisatokamakura.egg-info dist htmlcov pyproject.toml
    requirements.txt test_utf16.txt tools tutorial.py venv'
    >>> ls('tools')
    'tools/__pycache__ tools/calculate.py tools/cat.py
    tools/grep.py tools/ls.py'


    '''

    result = ''
    # folder + '/' ==> tools
    # glob is non deterministic; no guarantee about order of glob results
    # need to convert nondeterministic to deterministic
    if folder:
        for path in sorted(glob.glob(folder + '/*')):
            result += path + ' '
    else:
        for path in sorted(glob.glob('*')):
            result += path + ' '
    return result.strip()
