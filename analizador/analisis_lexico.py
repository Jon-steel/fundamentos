import ply.lex as lex

tokens =(
    "num",
    "suma",
    "resta",
    "multiplicacion",
    "divicion",
    "pal"
    )
t_num=r'([0-9])'
t_suma=r'(\+)'
t_resta=r'(\-)'
t_multiplicacion=r'(\*)'
t_divicion=r'(\/)'
t_pal=r'([a-z]+)'
t_ignore_space=r'\s+'
def t_error(t):
    print"error: simbolo ilegal '%s' en linea... %s"%(t.value[0],t.lexer.lineno)
    t.lexer.skip(1)

def prueba(entrada):
    lexico = lex.lex()
    lexico.input(entrada)
    while True:
        token=lexico.token()
        if not token:
            break
        print token

if __name__ == "__main__":
    while True:
        entrada = raw_input('entrada:')
        prueba(entrada)
