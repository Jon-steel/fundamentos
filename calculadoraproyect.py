import math
while True:
    palabra=raw_input("Ingrese los datos: \n")
    if palabra == "":
        break
    palabra += ";"
      
    estado="q0"
    n1 = ""
    n2 = ""
    op = ""

    for en in palabra:
        if estado == "q0":
            if en=="a" or en=="b" or en=="c" or en=="d" or en=="e" or en=="f" or en=="g" or en=="h" or en=="i" or en=="j" or en=="k" or en=="l" or en=="m" or en=="n" or en=="ñ" or en=="o" or en=="p" or en=="q" or en=="r" or en=="s" or en=="t" or en=="u" or en=="v" or en=="w" or en=="x" or en=="y" or en=="z":
                estado="q2"
                n1 += en
            if en=="0" or en=="1" or en=="2" or en=="3" or en=="4" or en=="5" or en=="6" or en=="7" or en=="8" or en=="9":
                estado="q1"
                n1 += en
            if en == ";" or en=="+" or en=="-" or en=="*" or en=="/" or en=="^" or en==" " or en=="#":
                estado="qr"
                    
        elif estado == "q1":
            if en=="0" or en=="1" or en=="2" or en=="3" or en=="4" or en=="5" or en=="6" or en=="7" or en=="8" or en=="9":
                estado="q1"
                n1 += en
            if en==" ":
                estado="q3"
            if en==";" or en=="+" or en=="-" or en=="*" or en=="/" or en=="^" or en=="#" or en=="a" or en=="b" or en=="c" or en=="d" or en=="e" or en=="f" or en=="g" or en=="h" or en=="i" or en=="j" or en=="k" or en=="l" or en=="m" or en=="n" or en=="ñ" or en=="o" or en=="p" or en=="q" or en=="r" or en=="s" or en=="t" or en=="u" or en=="v" or en=="w" or en=="x" or en=="y" or en=="z":
                estado="qr"
                    
        elif estado == "q2":
            if en=="a" or en=="b" or en=="c" or en=="d" or en=="e" or en=="f" or en=="g" or en=="h" or en=="i" or en=="j" or en=="k" or en=="l" or en=="m" or en=="n" or en=="ñ" or en=="o" or en=="p" or en=="q" or en=="r" or en=="s" or en=="t" or en=="u" or en=="v" or en=="w" or en=="x" or en=="y" or en=="z":
                estado="q2"
                n1 += en
            if en=="0" or en=="1" or en=="2" or en=="3" or en=="4" or en=="5" or en=="6" or en=="7" or en=="8" or en=="9" or en==";":
                estado="qr"
            if en==" ":
                estado="q3"
                    
        elif estado == "q3":
            if en=="a" or en=="b" or en=="c" or en=="d" or en=="e" or en=="f" or en=="g" or en=="h" or en=="i" or en=="j" or en=="k" or en=="l" or en=="m" or en=="n" or en=="ñ" or en=="o" or en=="p" or en=="q" or en=="r" or en=="s" or en=="t" or en=="u" or en=="v" or en=="w" or en=="x" or en=="y" or en=="z":
                estado = "q4"
                op += en
            if en=="+" or en=="-" or en=="*" or en=="/" or en=="^" or en=="#":
                estado="q5"
                op += en
            if en==" " or en==";" or en=="1" or en=="2" or en=="3" or en=="4" or en=="5" or en=="6" or en=="7" or en=="8" or en=="9":
                estado="qr"
                    
        elif estado == "q4":
            if en=="a" or en=="b" or en=="c" or en=="d" or en=="e" or en=="f" or en=="g" or en=="h" or en=="i" or en=="j" or en=="k" or en=="l" or en=="m" or en=="n" or en=="ñ" or en=="o" or en=="p" or en=="q" or en=="r" or en=="s" or en=="t" or en=="u" or en=="v" or en=="w" or en=="x" or en=="y" or en=="z":
                estado = "q4"
                op += en
            if en==";" or en=="+" or en=="-" or en=="*" or en=="/" or en=="^" or en=="#":
                estado="qr"
            if en==" ":
                estado = "q6"

        elif estado == "q5":
            if en=="a" or en=="b" or en=="c" or en=="d" or en=="e" or en=="f" or en=="g" or en=="h" or en=="i" or en=="j" or en=="k" or en=="l" or en=="m" or en=="n" or en=="ñ" or en=="o" or en=="p" or en=="q" or en=="r" or en=="s" or en=="t" or en=="u" or en=="v" or en=="w" or en=="x" or en=="y" or en=="z":
                estado = "qr"
            if en=="+" or en=="-" or en=="*" or en=="/" or en=="^" or en=="#" or en==" "or en==";" or en==";" or en=="1" or en=="2" or en=="3" or en=="4" or en=="5" or en=="6" or en=="7" or en=="8" or en=="9":
                estado="qr"
            if en==" ":
                estado="q6"
        
        elif estado == "q6":
            if en=="a" or en=="b" or en=="c" or en=="d" or en=="e" or en=="f" or en=="g" or en=="h" or en=="i" or en=="j" or en=="k" or en=="l" or en=="m" or en=="n" or en=="ñ" or en=="o" or en=="p" or en=="q" or en=="r" or en=="s" or en=="t" or en=="u" or en=="v" or en=="w" or en=="x" or en=="y" or en=="z":
                estado="q8"
                n2 += en
            if en=="0" or en=="1" or en=="2" or en=="3" or en=="4" or en=="5" or en=="6" or en=="7" or en=="8" or en=="9":
                estado = "q7"
                n2 += en
            if en==";" or en=="+" or en=="-" or en=="*" or en=="/" or en=="^" or en=="#" or en ==" ":
                estado="qr"
                
        elif estado == "q7":
            if en=="0" or en=="1" or en=="2" or en=="3" or en=="4" or en=="5" or en=="6" or en=="7" or en=="8" or en=="9":
                estado = "q7"
                n2 += en
            if en==";":
                estado="qa"
            if en=="a" or en=="b" or en=="c" or en=="d" or en=="e" or en=="f" or en=="g" or en=="h" or en=="i" or en=="j" or en=="k" or en=="l" or en=="m" or en=="n" or en=="ñ" or en=="o" or en=="p" or en=="q" or en=="r" or en=="s" or en=="t" or en=="u" or en=="v" or en=="w" or en=="x" or en=="y" or en=="z" or en=="+" or en=="-" or en=="*" or en=="/" or en=="^" or en=="#" or en ==" ":
                estado="qr"

        elif estado =="q8":
            if en=="a" or en=="b" or en=="c" or en=="d" or en=="e" or en=="f" or en=="g" or en=="h" or en=="i" or en=="j" or en=="k" or en=="l" or en=="m" or en=="n" or en=="ñ" or en=="o" or en=="p" or en=="q" or en=="r" or en=="s" or en=="t" or en=="u" or en=="v" or en=="w" or en=="x" or en=="y" or en=="z":
                estado="q8"
                n2 += en 
            if en=="0" or en=="1" or en=="2" or en=="3" or en=="4" or en=="5" or en=="6" or en=="7" or en=="8" or en=="9" or en=="+" or en=="-" or en=="*" or en=="/" or en=="^" or en=="#" or en ==" ":    
                estado="qr"
            if en==";":
                estado="qa"

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
        if op == "raiz":
            op = "#"
        if op == "potencia":
            op = "^"
        if op == "seno":
            op = "sen"
        if op == "coseno":
            op = "cos"
        if op == "tangente":
            op = "tan"
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

        if op=="+" or op=="-" or op=="*" or op=="/" or op=="^" or op=="#" or op=="sen" or op=="cos" or op=="tan":
            if op=="+":
               r=n1+n2
                      
            elif op=="*":
                r=n1*n2
                        
            elif op=="-":
                r=n1-n2
                       
            elif op=="/":
                r=n1/n2
                
            elif op=="sen":
                r=math.sin(n2)
                
            elif op=="cos":
                r=math.cos(n2)
                
            elif op=="tan":
                r=math.tan(n2)
                
            elif op=="^":
                r=n1**n2

            elif op=="#":
                r=n1**(1.0/n2)

            print ("el resultado de es:  %s %s %s = %s" % (n1, op, n2, r))
            
    except:
        print "La expresion esta mal"
            
    print estado  
