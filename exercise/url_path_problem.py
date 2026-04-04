"""
Docstring for url_path_problem

Problem: URL Path Validator

Write a function that validates and normalizes URL paths.

Rules:
1. Path components are separated by "/"
2. "." means current directory (ignore it)
3. ".." means parent directory (go up one level if possible)
4. Multiple slashes "//" should be treated as single "/"
5. Path should not start or end with "/" (except root "/")
6. Invalid paths return empty string

Examples:
- "/home/user/../documents/./files" → "/home/documents/files"
- "//etc//../var/log//" → "/var/log"
- "../../etc/passwd" → "" (tries to go above root)
- "." → ""
- "/" → "/"

Write function: normalize_path(path: str) -> str
"""



def normalise_path(path):
    components = path.split('/')
    stack = []
    for comp in components:
        if comp == '.' or comp == '':
            continue
        elif comp == '..':
            if stack:
                stack.pop() # go up level
            else:
                return ''
        else:
            stack.append(comp)
    result =  '/'.join(stack) if stack else '/'

    return result
    


def main():
    path = "//etc//../var/log//"
    print(normalise_path(path))

main()