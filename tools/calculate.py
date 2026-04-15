'''
This file contains a function that evaluates a string math expression.
'''

# always one python function and one tool schema

import json


def calculate(expression):
    '''
    This function evaluates a string math expression.

    >>> calculate("5 + 8")
    '{"result": 13}'

    >>> calculate('5*')
    '{"error": "Invalid expression"}'
    '''
    try:
        result = eval(expression)
        return json.dumps({"result": result})
    except Exception:
        return json.dumps({"error": "Invalid expression"})


tool_schema = {
    "type": "function",
    "function": {
        "name": "calculate",
        "description": "Evaluate a mathematical expression",
        "parameters": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "The mathematical expression to evaluate",
                }
            },
            "required": ["expression"],
        },
    },
}
