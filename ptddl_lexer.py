from sly import Lexer

class PTDDLLexer(Lexer):
    #Lista dos possíveis tokens que podem ser reproduzidos pelo Lexer
    tokens = { 'NOMEENTIDADE', 'TIPOCOLUNA', 'TIPO', 'CRIAR', 'ALTERAR', 'APAGAR','E' ,'RENOMEAR',
     "COLUNA", "TABELA", "BANCO", "ADICIONAR", "COM", "CONSTRAINT", 'IDENT', 'PARA', 'START'}
    
    #Especificação de cada token através de uma expressão regular
    E = r'e'
    START = r'#'

    NOMEENTIDADE = r'[A-Z][a-zA-Z0-9_]*'
    TIPOCOLUNA = r'int|varchar \([0-9]+\)|timestamp|data|float|char \([0-9]+\)'
    TIPO = r'tipo'
    CONSTRAINT = r'nulo|nao nulo|chave primaria'
    IDENT = r'[a-z_][a-z0-9_]*'
    IDENT['apagar'] = 'APAGAR'
    IDENT['alterar'] = 'ALTERAR'
    IDENT['criar'] = 'CRIAR'
    IDENT['tabela'] = 'TABELA'
    IDENT['alterar'] = 'ALTERAR'
    IDENT['criar'] = 'CRIAR'
    IDENT['banco'] = 'BANCO'
    IDENT['com'] = 'COM'
    IDENT['coluna'] = 'COLUNA'
    IDENT['renomear'] = 'RENOMEAR'
    IDENT['para'] = 'PARA'
    IDENT['adicionar'] = 'ADICIONAR'


    literals = [',']

    # Ignorar este caracter
    ignore = ' \t'

    # Rastreamento do numero de linhas
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')
    
    # Error handling rule
    def error(self, t):
        print("Illegal character '%s'" % t.value[0])
        self.index += 1


if __name__ == '__main__':
    data = "criar tabela Pessoa com coluna Nome tipo varchar chave primaria e coluna Idade tipo int e coluna Sexo tipo char"

    lexer = PTDDLLexer()
    for tok in lexer.tokenize(data):
        print(tok)