from sly import Lexer

class PTDDLLexer(Lexer):
    
    tokens = { 'IDENT', 'TIPOENT', 'TIPO', 'CRIAR', 'ALTERAR', 'APAGAR', 'PRONOME', 'CMD', 'E' , "TIPOCOLUNA", "TIPOENTIDADE"}
    E = 'E|e'
    IDENT = r'[a-zA-Z_][a-zA-Z0-9_]*'
    IDENT['a'] = 'PRONOME'
    IDENT['o'] = 'PRONOME'
    IDENT['A'] = 'PRONOME'
    IDENT['O'] = 'PRONOME'
    IDENT['apaga'] = 'APAGAR'
    IDENT['altera'] = 'ALTERAR'
    IDENT['cria'] = 'CRIAR'
    IDENT['apagar'] = 'APAGAR'
    IDENT['alterar'] = 'ALTERAR'
    IDENT['criar'] = 'CRIAR'

    # String containing ignored characters
    ignore = ' \t'

    # Line number tracking
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

if __name__ == '__main__':
    data = "apagar a tabela pessoa e a tabela carro e apagar a tabela pessoa e a tabela carro"
    lexer = PTDDLLexer()
    for tok in lexer.tokenize(data):
        print(tok)