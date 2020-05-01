import re

expresion = r'(712)(\-)([0-9]{3})(\-)([0-9]{4})'
resultado = re.compile(expresion)
prueba = raw_input("entrada: ")
busqueda=re.search(resultado,prueba)
if busqueda:
    print busqueda.group()
else:
    print"qr"

