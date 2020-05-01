import math
while True:
    import re
    expresion = r'([0-9]+|[\w]+)\s([-|+|*|/|^|#]|[\w]+)\s([0-9]+|[\w]+)'
    expresion1 = r'([\w]+)\s([0-9]+|[\w]+)'
    resultado = re.compile(expresion)
    resultado1 = re.compile(expresion1)
    prueba = raw_input("entrada: ")
    busqueda=re.search(resultado,prueba)
    busqueda1=re.search(resultado1,prueba)
    if busqueda:
        print busqueda.group(1)
        n1=busqueda.group(1)
        print busqueda.group(2)
        op=busqueda.group(2)
        print busqueda.group(3)
        n2=busqueda.group(3)
        
        if n1 == "cero":
            n1 = 0
        if n1 == "uno":
            n1 = 1
        if n1 == "dos":
            n1 = 2
        if n1 == "tres":
            n1 = 3
        if n1 == "cuatro":
            n1 = 4
        if n1 == "cinco":
            n1 = 5
        if n1 == "seis":
            n1 = 6
        if n1 == "siete":
            n1 = 7
        if n1 == "ocho":
            n1 = 8
        if n1 == "nueve":
            n1 = 9
        if op == "mas":
            op = "+"
        if op == "menos":
            op = "-"
        if op == "por":
            op = "*"
        if op == "entre":
            op = "/"
        if n2 == "cero":
            n2 = 0
        if n2 == "uno":
            n2 = 1
        if n2 == "dos":
            n2 = 2
        if n2 == "tres":
            n2 = 3
        if n2 == "cuatro":
            n2 = 4
        if n2 == "cinco":
            n2 = 5
        if n2 == "seis":
            n2 = 6
        if n2 == "siete":
            n2 = 7
        if n2 == "ocho":
            n2 = 8
        if n2 == "nueve":
            n2 = 9
        try:
            n1=int(n1)
            n2=int(n2)

            if op=="+" or "-" or "*" or "/":
                if op=="+":
                    r=n1+n2
                          
                elif op=="-":
                    r=n1-n2
                            
                elif op=="*":
                    r=n1*n2
                           
                elif op=="/":
                    r=n1/n2

                elif op=="^":
                    r=n1**n2

                elif op=="#":
                    r=n1**(1.0/n2)
                print ("el resultado es:  %s %s %s = %s" % (n1, op, n2, r)) 

        except:
            print"qr";
        
            
    elif busqueda1:
        print busqueda1.group(1)
        op=busqueda1.group(1)
        print busqueda1.group(2)
        n2=busqueda1.group(2)

        
        try:
            n2=int(n2)

            if op=="sen" or "cos" or "tan":
                if op=="sen":
                    r=math.sin(n2)
                    
                elif op=="cos":
                    r=math.cos(n2)
                    
                elif op=="tan":
                    r=math.tan(n2)

          
            
                print ("el resultado es: %s %s = %s" % (op, n2, r))
        except:  
            print"qr";
            
   
