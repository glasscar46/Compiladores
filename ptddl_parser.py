from sly import Parser
from ptddl_lexer import PTDDLLexer

class CalcParser(Parser):
    # Get the token list from the lexer (required)
    tokens = PTDDLLexer.tokens

    @_('APAGAR apexp')
    def start(self, p):
        return f'drop {p.apexp};'

    @_('BANCO NOMEENTIDADE')
    def apexp(self, p):
        return f"database {p[1]}"

    @_('TABELA NOMEENTIDADE')
    def apexp(self, p):
        return f"table {p[1]}"

    @_('CRIAR criarexp')
    def start(self, p):
        return f"create {p[1]};"
    
    @_('TABELA NOMEENTIDADE COM cd')
    def criarexp(self, p):
        return f'table {p[1]}' + '('+ f'{p[3]}' + ')'
    
    def translate_constraint(self, constraint: str) -> str:
        if constraint == 'nao nulo':
            return 'NOT NULL'
        return 'NULL'

    @_('COLUNA NOMEENTIDADE TIPO TIPOCOLUNA CONSTRAINT acd')
    def cd(self, p):
        return f'{p[1]} {p[3]} {self.translate_constraint(p[4])}{p[5]}'

    @_('COLUNA NOMEENTIDADE TIPO TIPOCOLUNA acd')
    def cd(self, p):
        return f'{p[1]} {p[3]} {p[4]}'

    @_('E cd')
    def acd(self, p):
        return f', {p[1]}'
    @_('')
    def empty(self, p):
        return ''

    @_('empty')
    def acd(self, p):
        return ''

if __name__ == '__main__':
    lexer = PTDDLLexer()
    parser = CalcParser()

    while True:
        try:
            text = input('> ')
            result = parser.parse(lexer.tokenize(text))
            print(result)
        except EOFError:
            break