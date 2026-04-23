import subprocess

def doctests(path):
    '''
    Run doctests on the given file with --verbose and return the output.

    >>> output = doctests('tools/ls.py')
    >>> 'passed' in output or 'OK' in output
    True
    '''
    result = subprocess.run(
        ['python', '-m', 'doctest', '--verbose', path],
        capture_output=True,
        text=True
    )
    return result.stdout + result.stderr

tool_schema = {
    "type": "function",
    "function": {
        "name": "doctests",
        "description": "Run doctests on a file and return verbose output.",
        "parameters": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "The path to the file to run the doctests."
                }
            },
            "required": ["path"]
        }
    }
}