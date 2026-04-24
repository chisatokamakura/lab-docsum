'''
This tool writes multiple files, git adds them, commits them,
and runs doctests on any Python files.
'''

import os
from git import Repo
from tools.doctests import doctests


def write_files(files, commit_message):
    '''
    Write multiple files, git add them, commit them, and run doctests
    on any Python files.

    >>> isinstance(write_files(
    ...     [{'path': 'tmp1.txt', 'contents': 'hello'}],
    ...     'add tmp1'
    ... ), str)
    True

    >>> write_files(
    ...     [{'path': '/etc/passwd', 'contents': 'x'}],
    ...     'bad write'
    ... )
    'Invalid path'
    '''
    try:
        for file_info in files:
            path = file_info['path']
            contents = file_info['contents']

            if (
                not isinstance(path, str)
                or os.path.isabs(path)
                or '..' in path
                or os.path.basename(path) == 'README.md'
            ):
                return 'Invalid path'

            with open(path, 'w', encoding='utf-8') as f:
                f.write(contents)

        repo = Repo('.')
        for file_info in files:
            repo.git.add(file_info['path'])

        repo.index.commit(f'[docchat] {commit_message}')

        for file_info in files:
            path = file_info['path']
            if path.endswith('.py'):
                doctests(path)

        if len(files) == 1:
            return f"Wrote the file {files[0]['path']}"

        return f"Wrote {len(files)} files"

    except Exception as e:
        return f'Error: {e}'


tool_schema = {
    "type": "function",
    "function": {
        "name": "write_files",
        "description": (
            "Write multiple files.\n"
            "Commit them with git and run doctests on Python files."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "files": {
                    "type": "array",
                    "description": "A list of files to write.",
                    "items": {
                        "type": "object",
                        "properties": {
                            "path": {
                                "type": "string",
                                "description": (
                                    "The path of the file to write."
                                )
                            },
                            "contents": {
                                "type": "string",
                                "description": (
                                    "The contents to write into the file."
                                )
                            }
                        },
                        "required": ["path", "contents"]
                    }
                },
                "commit_message": {
                    "type": "string",
                    "description": "The git commit message to use."
                }
            },
            "required": ["files", "commit_message"]
        }
    }
}
