def p_calculadora(p):
    """calculadora : operaciones"""
    pass
def p_operaciones(p):
    """operaciones : operacion"""
    pass
def p_operacion(p):
    """operacion : n1 op n2 """
    print(p)
def p_n1(p):
    """n1 : palabra
          | numero"""
    pass
def p_op(p):
    """op : simbolo
          | palabra"""
    pass
def p_n2(p):
    """n2 : palabra
          | numero"""
    pass
def p_palabra(p):
    """palabra : pal"""
    pass
def p_simbolo(p):
    """simbolo : suma
               | resta
               | divicion
               | multiplicacion"""
    pass
def p_numero(p):
    """numero : num"""
    pass
def p_error(p):
    print"error de sintaxis"
    print p
