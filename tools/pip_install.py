'''
This tool lets the agent install
a Python library by running `pip install` from code.
'''

import subprocess


ALLOWED_LIBRARIES = {
    "groq",
    "python-dotenv",
    "GitPython",
}


def pip_install(library_name):
    '''
    Install an allowed Python library using pip3.

    >>> pip_install('/etc/passwd')
    'Invalid library'

    >>> pip_install('not-allowed-package')
    'Invalid library'
    '''
    if library_name not in ALLOWED_LIBRARIES:
        return 'Invalid library'

    result = subprocess.run(
        ['pip3', 'install', library_name],
        capture_output=True,
        text=True
    )
    return result.stdout + result.stderr


tool_schema = {
    "type": "function",
    "function": {
        "name": "pip_install",
        "description": "Install an approved Python package using pip3.",
        "parameters": {
            "type": "object",
            "properties": {
                "library_name": {
                    "type": "string",
                    "description": "The approved library name to install."
                }
            },
            "required": ["library_name"]
        }
    }
}
