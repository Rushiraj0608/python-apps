# LEXING

from typing import Any


with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

for i in range(len(lines)):
    if '#' in lines[i]:
        lines[i] = lines[i].split('#', 1)[0]
    if '/*' in lines[i]:
        lines[i] = lines[i].split('/*', 1)[0]
        for j in range(i,len(lines)):
            if '*/' in lines[i]:
                lines[i] = lines[i].split('/*', 1)[1]
            else:
                lines.remove(lines[i])

    


class token():
    typ: str
    val: str

    def __init__(self, typ, val):
        """
        >>> token('sym', '(')
        token('sym', '(')
        """
        self.typ = typ
        self.val = val

    def __repr__(self):
        return f'token({self.typ!r}, {self.val!r})'

def lex(s: str) -> list[token]:
    """
    >>> lex('')
    []
    >>> lex('x=3')
    [token('var', 'x'), token('asg', '='), token('int', '3')]
    """

    tokens = []
    i = 0

    while i < len(s):
        if s[i].isspace():
            i += 1
        elif s[i].isalpha():
            end = i + 1
            while end < len(s) and (s[end].isalnum() or s[end] == '_'):
                end += 1
            assert end >= len(s) or not (s[end].isalnum() or s[end] == '_')

            word = s[i:end]

            if word in ['print']:
                tokens.append(token('kw', word))
            else:
                tokens.append(token('var', word))
            i = end
        elif s[i].isdigit():
            end = i + 1
            while end < len(s) and (s[end].isdigit()):
                end += 1
            assert end >= len(s) or not (s[end].isdigit())

            word = s[i:end]

            if word.isdigit():
                tokens.append(token('int', word))
            i = end
        elif s[i] == '(':
            tokens.append(token('sym', '('))
            i += 1
        elif s[i] == ')':
            tokens.append(token('sym', ')'))
            i += 1
        elif s[i:i+1] == '+':
            tokens.append(token('opr', '+'))
            i += 1
        elif s[i:i+1] == '-':
            tokens.append(token('opr', '-'))
            i += 1
        elif s[i:i+1] == '*':
            tokens.append(token('opr', '*'))
            i += 1
        elif s[i:i+1] == '/':
            tokens.append(token('opr', '/'))
            i += 1
        elif s[i:i+1] == '%':
            tokens.append(token('opr', '%'))
            i += 1
        elif s[i:i+1] == '^':
            tokens.append(token('opr', '^'))
            i += 1
        elif s[i:i+2] == '++':
            tokens.append(token('un', '++'))
            i += 2
        elif s[i:i+2] == '--':
            tokens.append(token('un', '--'))
            i += 2
        elif s[i:i+1] == '=':
            tokens.append(token('asg', '='))
            i += 1
        elif s[i:i+2] == '+=':
            tokens.append(token('opeq', '+='))
            i += 2
        elif s[i:i+2] == '-=':
            tokens.append(token('opeq', '-='))
            i += 2
        elif s[i:i+2] == '*=':
            tokens.append(token('opeq', '*='))
            i += 2
        elif s[i:i+2] == '/=':
            tokens.append(token('opeq', '/='))
            i += 2
        elif s[i:i+2] == '%=':
            tokens.append(token('opeq', '%='))
            i += 2
        elif s[i:i+2] == '^=':
            tokens.append(token('opeq', '^='))
            i += 2
        elif s[i:i+2] == '||':
            tokens.append(token('sym', '||'))
            i += 2
        elif s[i:i+2] == '&&':
            tokens.append(token('sym', '&&'))
            i += 2
        elif s[i] == '!':
            tokens.append(token('sym', '!'))
            i += 1
        elif s[i:i+2] == '==':
            tokens.append(token('relop', '=='))
            i += 2
        elif s[i:i+2] == '<=':
            tokens.append(token('relop', '<='))
            i += 2
        elif s[i:i+2] == '>=':
            tokens.append(token('relop', '>='))
            i += 2
        elif s[i:i+2] == '!=':
            tokens.append(token('relop', '!='))
            i += 2
        elif s[i:i+1] == '>':
            tokens.append(token('relop', '>'))
            i += 1
        elif s[i:i+1] == '<':
            tokens.append(token('relop', '<'))
            i += 1
        else:
            raise SyntaxError(f'unexpected character {s[i]}')

    return tokens


# PARSING

class ast():
    typ: str
    children: tuple[Any, ...]

    def __init__(self, typ: str, *children: Any):
        self.typ = typ
        self.children = children

    def __repr__(self):
        return f'ast({self.typ!r}, {", ".join([repr(c) for c in self.children])})'

# INTERPRETER

def interp(a: ast, env: set[str]) -> bool:
    try:
        if a.typ == 'val':
            return a.children[0]
        elif a.typ == 'var':
            return a.children[0] in env
        elif a.typ == '!':
            return not interp(a.children[0], env)
        elif a.typ == '+':
            return interp(a.children[0], env) + interp(a.children[1], env)
        elif a.typ == '-':
            return interp(a.children[0], env) - interp(a.children[1], env)
        elif a.typ == '*':
            return interp(a.children[0], env) * interp(a.children[1], env)
        elif a.typ == '/':
            return interp(a.children[0], env) / interp(a.children[1], env)
        elif a.typ == '%':
            return interp(a.children[0], env) % interp(a.children[1], env)
        elif a.typ == '^':
            return interp(a.children[0], env) ^ interp(a.children[1], env)
        elif a.typ == '--':
            return interp(a.children[0], env)-1
        elif a.typ == '++':
            return interp(a.children[0], env)+1
        elif a.typ == '+=':
            return interp(a.children[0], env) + interp(a.children[1], env)
        elif a.typ == '-=':
            return interp(a.children[0], env) - interp(a.children[1], env)
        elif a.typ == '*=':
            return interp(a.children[0], env) * interp(a.children[1], env)
        elif a.typ == '/=':
            return interp(a.children[0], env) / interp(a.children[1], env)
        elif a.typ == '%=':
            return interp(a.children[0], env) % interp(a.children[1], env)
        elif a.typ == '^=':
            return interp(a.children[0], env) ^ interp(a.children[1], env)
        elif a.typ == '==':
            return interp(a.children[0], env) == interp(a.children[1], env)
        elif a.typ == '<=':
            return interp(a.children[0], env) <= interp(a.children[1], env)
        elif a.typ == '>=':
            return interp(a.children[0], env) >= interp(a.children[1], env)
        elif a.typ == '!=':
            return interp(a.children[0], env) != interp(a.children[1], env)
        elif a.typ == '<':
            return interp(a.children[0], env) < interp(a.children[1], env)
        elif a.typ == '>':
            return interp(a.children[0], env) > interp(a.children[1], env)
        elif a.typ == '!':
            return not interp(a.children[0], env)
        elif a.typ == '&&':
            return interp(a.children[0], env) and interp(a.children[1], env)
        elif a.typ == '||':
            return interp(a.children[0], env) or interp(a.children[1], env)
        
    except ZeroDivisionError:
        return 'divide by zero'

