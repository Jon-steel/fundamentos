import ply.yacc as yacc
from analizador.analisis_lexico import tokens
from analizador.analisis_sintactico import *

sintaxis = yacc.yacc()

while 1:
    e = raw_input("entrada")
    sintaxis.parse(e)
