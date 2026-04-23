'''
This tool writes contents to a file, commits the change with git. 
If it is a Python file, runs doctests and returns output.
'''

from tools.write_files import write_files

def write_file(path, contents, commit_message):
    '''
    Write one file, commit it with git, and run doctests if it is a Python file.

    >>> isinstance(write_file('tmp.txt', 'hello', 'add tmp'), str)
    True

    >>> write_file('/etc/passwd', 'x', 'bad write')
    'Invalid path'
    '''
    return write_files(
        [{'path': path, 'contents': contents}],
        commit_message
    )