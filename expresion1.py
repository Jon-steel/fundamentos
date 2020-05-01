import re

expresion = r'^([a-z]{3,5})$'
resultado = re.compile(expresion)
prueba = raw_input("entrada: ")
busqueda=re.search(resultado,prueba)

if busqueda:
    print busqueda.group()
else:
    print"qr"
