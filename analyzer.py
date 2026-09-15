import ast

def analyze(code):
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return {
            "error": "Invalid Python code (syntax error detected)",
            "loops": 0,
            "functions": 0
        }

    loops = 0
    functions = 0

    for node in ast.walk(tree):
        if isinstance(node, (ast.For, ast.While)):
            loops += 1
        if isinstance(node, ast.FunctionDef):
            functions += 1

    return {
        "loops": loops,
        "functions": functions
    }