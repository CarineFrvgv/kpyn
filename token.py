
class Token:
    def __int__(self, token_type, value):
        self.token_type = token_type,
        self.value = value

    def __repr__(self):
        if self.value:
            return f'{self.value}: {self.token_type}'
        return f'{self.token_type}'


# Single character
PLUS = 'PLUS'
MINUS = 'MINUS'
MUL = 'MULTIPLICATION'
DIV = 'DIVISION'
LPAR = 'L_PARENTHESES'
RPAR = 'R_PARENTHESES'
LBRA = 'L_BRACES'
RBRA = 'R_BRACES'
COMMA = 'COMMA'
DOT = 'DOT'
