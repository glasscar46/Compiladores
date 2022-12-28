from sly import Parser
from ptddl_lexer import PTDDLLexer

class CalcParser(Parser):
    # Get the token list from the lexer (required)
    tokens = PTDDLLexer.tokens

    # Grammar rules and actions
    @_('expr PLUS term')
    def expr(self, p):
        return p.expr + p.term

    @_('expr MINUS term')
    def expr(self, p):
        return p.expr - p.term

    @_('term')
    def expr(self, p):
        return p.term

    @_('term TIMES factor')
    def term(self, p):
        return p.term * p.factor

    @_('term DIVIDE factor')
    def term(self, p):
        return p.term / p.factor

    @_('factor')
    def term(self, p):
        return p.factor

    @_('NUMBER')
    def factor(self, p):
        return p.NUMBER

    @_('LPAREN expr RPAREN')
    def factor(self, p):
        return p.expr

if __name__ == '__main__':
    lexer = PTDDLLexer()
    parser = CalcParser()

    while True:
        try:
            text = input('convert: ')
            result = parser.parse(lexer.tokenize(text))
            print(result)
        except EOFError:
            break