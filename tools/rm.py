'''
This tool removes one or more files using a
path or glob pattern, then commits the change.
'''

import os
import glob
from git import Repo

PROTECTED_FILES = {
    'README.md',
    'AGENTS.md',
    'requirements.txt',
    'pyproject.toml',
    '.gitignore',
}


def rm(path):
    '''
    This tool removes one or more files using a
    path or glob pattern, then commits the change.

    >>> with open('tmp_rm1.txt', 'w', encoding='utf-8') as f:
    ...     _ = f.write('hello')
    >>> rm('tmp_rm1.txt')
    'Removed the file tmp_rm1.txt'
    >>> os.path.exists('tmp_rm1.txt')
    False

    >>> with open('tmp_rm2.txt', 'w', encoding='utf-8') as f:
    ...     _ = f.write('a')
    >>> with open('tmp_rm3.txt', 'w', encoding='utf-8') as f:
    ...     _ = f.write('b')
    >>> rm('tmp_rm*.txt')
    'Removed 2 files'
    >>> os.path.exists('tmp_rm2.txt') or os.path.exists('tmp_rm3.txt')
    False

    >>> rm('/etc/passwd')
    'Invalid path'

    >>> rm('../secret.txt')
    'Invalid path'

    >>> rm('file_that_does_not_exist.txt')
    'Error: file not found'
    '''
    if (
        not isinstance(path, str)
        or os.path.isabs(path)
        or '..' in path
    ):
        return 'Invalid path'

    if path in PROTECTED_FILES:
        return 'Invalid path'

    if '*' in path and not path.startswith('tmp'):
        return 'Invalid path'

    try:
        matches = glob.glob(path)

        if not matches:
            return 'Error: file not found'

        removed_files = []
        for match in matches:
            if os.path.isdir(match):
                continue
            if (
                os.path.isabs(match)
                or '..' in match
                or os.path.basename(match) in PROTECTED_FILES
            ):
                return 'Invalid path'
            os.remove(match)
            removed_files.append(match)

        if not removed_files:
            return 'Error: file not found'

        repo = Repo('.')
        repo.git.add(all=True)
        repo.index.commit(f'[docchat] rm {path}')

        if len(removed_files) == 1:
            return f"Removed the file {removed_files[0]}"

        return f"Removed {len(removed_files)} files"

    except Exception as e:
        return f'Error: {e}'


tool_schema = {
    "type": "function",
    "function": {
        "name": "rm",
        "description": (
            "Remove one or more files using a path or glob.\n"
            "Commit deletion with git."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "The file path or glob pattern to remove."
                }
            },
            "required": ["path"]
        }
    }
}
