

# LEXING

from typing import Any


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
        elif s[i:i+2] == '++':
            tokens.append(token('un', '++'))
            i += 2
        elif s[i:i+2] == '--':
            tokens.append(token('un', '--'))
            i += 2
        elif s[i:i+1] == '=':
            tokens.append(token('asg', '='))
            i += 1
        else:
            raise SyntaxError(f'unexpected character {s[i]}')

    return tokens


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
        elif a.typ == '--':
            return interp(a.children[0], env)-1
        elif a.typ == '++':
            return interp(a.children[0], env)+1
        
    except ZeroDivisionError:
        return 'divide by zero'

