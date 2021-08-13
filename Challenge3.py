import ast
from typing import List


def parse_imports(code: str) -> List[str]:
    """
    Parse the given Python source code and return the list of full-qualified paths for all imported symbols, sorted in ascending lexicographic order.
    """
    tree = ast.parse(code)
    result = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                result.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            module = node.module
            for alias in node.names:
                result.append(f"{module}.{alias.name}")
    return sorted(result)

# Examples
print(parse_imports('import os'))
print(parse_imports('import os\nfrom typing import List'))