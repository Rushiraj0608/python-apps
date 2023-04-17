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

        elif s[i] == '_':
            end = i + 1
            while end < len(s) and (s[end].isalnum() or s[end] == '_'):
                end += 1
            assert end >= len(s) or not (s[end].isalnum() or s[end] == '_')

            word = s[i:end]

            tokens.append(token('var', word))
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
        """
        x || true
        >>> ast('||', ast('var', 'x'), ast('val', True))
        ast('||', ast('var', 'x'), ast('val', True))
        """
        self.typ = typ
        self.children = children

    def __repr__(self):
        return f'ast({self.typ!r}, {", ".join([repr(c) for c in self.children])})'

def parse(s: str) -> ast:
    ts = lex(s)

    a, i = disj(ts, 0)

    if i != len(ts):
        raise SyntaxError(f"expected EOF, found {ts[i:]!r}")

    return a

def disj(ts: list[token], i: int) -> tuple[ast, int]:
    """
    >>> parse('true || false')
    ast('||', ast('val', True), ast('val', False))
    """
    if i >= len(ts):
        raise SyntaxError('expected conjunction, found EOF')

    lhs, i = conj(ts, i)

    while i < len(ts) and ts[i].typ == 'sym' and ts[i].val == '||':
        rhs, i = conj(ts, i+1)
        lhs = ast('||', lhs, rhs)

    return lhs, i

def conj(ts: list[token], i: int) -> tuple[ast, int]:
    """
    >>> parse('true && false')
    ast('&&', ast('val', True), ast('val', False))
    >>> parse('!x && (a && !false)')
    ast('&&', ast('!', ast('var', 'x')), ast('&&', ast('var', 'a'), ast('!', ast('val', False))))
    >>> parse('!x && a && !false')
    ast('&&', ast('&&', ast('!', ast('var', 'x')), ast('var', 'a')), ast('!', ast('val', False)))
    """
    if i >= len(ts):
        raise SyntaxError('expected conjunction, found EOF')

    lhs, i = assign(ts, i)

    while i < len(ts) and ts[i].typ == 'sym' and ts[i].val == '&&':
        rhs, i = assign(ts, i+1)
        lhs = ast('&&', lhs, rhs)

    return lhs, i

def assign(ts: list[token], i: int) -> tuple[ast, int]:
    
    if i >= len(ts):
        raise SyntaxError('expected assignment, found EOF')

    lhs, i = div(ts,i)
    if i<len(ts) and ts[i].typ == 'asg' and ts[i].val == '=':
        rhs, i = div(ts, i+1)
        lhs =  ast('=', lhs, rhs)

    return lhs, i

def div(ts: list[token], i: int) -> tuple[ast, int]:
    
    if i >= len(ts):
        raise SyntaxError('expected divisiom, found EOF')

    lhs, i = mul(ts,i)
    if i<len(ts) and ts[i].typ == 'opr' and ts[i].val == '/':
        rhs, i = mul(ts, i+1)
        lhs =  ast('/', lhs, rhs)

    return lhs, i

def mul(ts: list[token], i: int) -> tuple[ast, int]:
    
    if i >= len(ts):
        raise SyntaxError('expected multiplication, found EOF')

    lhs, i = add(ts,i)
    if i<len(ts) and ts[i].typ == 'opr' and ts[i].val == '+':
        rhs, i = add(ts, i+1)
        lhs =  ast('*', lhs, rhs)

    return lhs, i

def add(ts: list[token], i: int) -> tuple[ast, int]:
    
    if i >= len(ts):
        raise SyntaxError('expected addition, found EOF')

    lhs, i = sub(ts,i)
    if i<len(ts) and ts[i].typ == 'opr' and ts[i].val == '+':
        rhs, i = sub(ts, i+1)
        lhs =  ast('+', lhs, rhs)

    return lhs, i

def sub(ts: list[token], i: int) -> tuple[ast, int]:
    
    if i >= len(ts):
        raise SyntaxError('expected subtraction, found EOF')

    lhs, i = neg(ts,i)
    if i<len(ts) and ts[i].typ == 'opr' and ts[i].val == '-':
        rhs, i = neg(ts, i+1)
        lhs =  ast('-', lhs, rhs)

    return lhs, i




def neg(ts: list[token], i: int) -> tuple[ast, int]:
    """
    >>> parse('! true')
    ast('!', ast('val', True))
    >>> parse('!! true')
    ast('!', ast('!', ast('val', True)))
    """

    if i >= len(ts):
        raise SyntaxError('expected negation, found EOF')

    if ts[i].typ == 'sym' and ts[i].val == '!':
        a, i = neg(ts, i+1)
        return ast('!', a), i
    else:
        return atom(ts, i)




def atom(ts: list[token], i: int) -> tuple[ast, int]:
    """
    >>> parse('x')
    ast('var', 'x')
    >>> parse('true')
    ast('val', True)
    >>> parse('(((false)))')
    ast('val', False)
    """

    t = ts[i]

    if t.typ == 'var':
        return ast('var', t.val), i+1
    if t.typ == 'int':
        return ast('int', t.val), i+1
    if t.typ == 'opr':
        return ast('opr', t.val), i+1
    elif t.typ == 'kw' and t.val in ['true', 'false']:
        return ast('val', t.val == 'true'), i + 1
    elif t.typ == 'sym' and t.val == '(':
        a, i = disj(ts, i + 1)

        if i >= len(ts):
            raise SyntaxError(f'expected right paren, got EOF')

        if not (ts[i].typ == 'sym' and ts[i].val == ')'):
            raise SyntaxError(f'expected right paren, got "{ts[i]}"')
        
        return a, i + 1

    raise SyntaxError(f'expected atom, got "{ts[i]}"')

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
    

# with open("input.txt") as file:
#     lines = [line.rstrip() for line in file]

# for i in lines:
#     ast = parse(i)


# expr = 'true || false && !x'
expr = 'x=3/4+1'
ast = parse(expr)

print(ast)
# print(ast.children[0])
# print(ast.children[0].children[0])
# print(ast.children[1]) 
# print(ast.children[1].children[0])  

# expr = 'true || false && !x'
# ast = parse(expr)
# print(ast.typ)
# print(ast.children[0].typ)
# print(ast.children[0].children[0])
# print(ast.children[1].typ)
# print(ast.children[1].children[0].typ) 