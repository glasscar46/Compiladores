from sly import Parser
from ptddl_lexer import PTDDLLexer

class CalcParser(Parser):
    # Get the token list from the lexer (required)
    tokens = PTDDLLexer.tokens
    debugfile = 'parser.out'

    #Produções da Gramática
    @_('APAGAR apexp')
    def start(self, p):
        return f'DROP {p.apexp};'

    @_('BANCO NOMEENTIDADE')
    def apexp(self, p):
        return f"DATABASE {p[1]}"

    @_('TABELA NOMEENTIDADE') 
    def apexp(self, p): 
        return f"TABLE {p[1]}"

    @_('CRIAR criarexp')
    def start(self, p):
        return f"CREATE {p[1]};"
    
    @_('TABELA NOMEENTIDADE COM cd')
    def criarexp(self, p):
        return f'TABLE {p[1]}' + '(' + '\n' + f' {p[3]}'  + '\n' + ')'
    
    #Traducao para PT-Br
    def translate_constraint(self, constraint: str) -> str:
        if constraint == 'nao nulo':
            return 'NOT NULL'
        elif constraint == 'chave primaria':
            return "PRIMARY KEY"    
        return 'NULL'

    @_('COLUNA NOMEENTIDADE TIPO TIPOCOLUNA CONSTRAINT acd')
    def cd(self, p):
        return f'{p[1]} {p[3]} {self.translate_constraint(p[4])}{p[5]}'

    @_('COLUNA NOMEENTIDADE TIPO TIPOCOLUNA acd')
    def cd(self, p):
        return f'{p[1]} {p[3]} {p[4]}'

    @_('E cd')
    def acd(self, p):
        return ',' + '\n' + p[1]
    @_('')
    def empty(self, p):
        return ''

    @_('empty')
    def acd(self, p):
        return ''

    @_('ALTERAR altexp')
    def start(self, p):
        return 'ALTER ' +  p[1] + ';'

    @_('TABELA NOMEENTIDADE z')
    def altexp(self, p):
        return 'TABLE ' + p[1] + p[2]
    
    @_('addcmd')
    def z(self, p):
        return p[0]

    @_('APAGAR COLUNA NOMEENTIDADE')
    def z(self, p):
        return '\n'+ ' DROP COLUMN ' + p[2]

    @_('RENOMEAR COLUNA NOMEENTIDADE PARA NOMEENTIDADE')
    def z(self, p):
        return '\n' ' RENAME COLUMN ' + p[2] + ' to ' +  p[4]
    
    @_("ADICIONAR addcd maddcmd")
    def addcmd(self, p):
        return '\n' +" ADD " + p[1] + p[2]

    @_('COLUNA NOMEENTIDADE TIPO TIPOCOLUNA CONSTRAINT')
    def addcd(self, p):
        return f'COLUMN {p[1]} {p[3]} {self.translate_constraint(p[4])} '

    @_('COLUNA NOMEENTIDADE TIPO TIPOCOLUNA')
    def addcd(self, p):
        return f'COLUMN {p[1]} {p[3]} '

    @_('E addcmd')
    def maddcmd(self, p):
        return ',' + p[1]
    
    @_('empty')
    def maddcmd(self, p):
        return ''

if __name__ == '__main__':
    lexer = PTDDLLexer()
    parser = CalcParser()
    print("Bem vindo ao conversor de linguagem natural (pt-Br) ao SQL(DDL)")
    while True:
        try:
            text = input('> ')
            if text == 'close':
                break
            if text == 'help':
                print("O conversor reconhece os comandos 'APAGAR', 'CRIAR' e 'ALTERAR'.")
                continue
            result = parser.parse(lexer.tokenize(text))
            print(result)
        except EOFError:
            break