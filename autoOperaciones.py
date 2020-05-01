while True:
    palabra=raw_input("Ingrese la cadena y al final - ; -    y  x para salir: ") 
    if palabra == "":
        break

    palabra += ";"
    
    estado="q0"
    n1 = "0"
    n2 = "0"
    op = ""

    for en in palabra:
        if estado == "q0":
            if en=="0" or en=="1" or en=="2" or en=="3" or en=="4" or en=="5" or en=="6" or en=="7" or en=="8" or en=="9":
                estado="q1"
                n1 += en
            if en == ";" or en=="+" or en=="-" or en=="*" or en=="/":
                print "Caracter invalido " + en
                exit
                estado="qr"
        elif estado == "q1":
            if en=="0" or en=="1" or en=="2" or en=="3" or en=="4" or en=="5" or en=="6" or en=="7" or en=="8" or en=="9":
                estado="q1"
                n1 += en
                exit
            if  en=="+" or en=="-" or en=="*" or en=="/":
                estado="q2"
                op += en
            if en == ";":
                print "Caracter invalido " + en
                exit
                estado="qr"
        elif estado == "q2":
            if en=="0" or en=="1" or en=="2" or en=="3" or en=="4" or en=="5" or en=="6" or en=="7" or en=="8" or en=="9":
               estado="q3"
               n2 += en
            if en=="+" or en=="-" or en=="*" or en=="/" or en ==";":
                print "Caracter invalido " + en
                exit
                estado="qr"
        elif estado == "q3":
            if en=="0" or en=="1" or en=="2" or en=="3" or en=="4" or en=="5" or en=="6" or en=="7" or en=="8" or en=="9":
               estado == "q3"
               n2 += en
            if en=="+" or en=="-" or en=="*" or en=="/":
               estado="q2"
            if en==";":
                estado="qa"

    if estado <> "qr":
       
        n1=int(n1)
        n2=int(n2)
        op=(op)

        if op=="+" or op=="-" or op=="*" or op=="/":
            if op=="+":
                r=n1+n2
              
            elif op=="*":
                r=n1*n2
                
            elif op=="-":
                r=n1-n2
               
            elif op=="/":
                r=n1/n2

        print estado
        print ("el resultado de es:  %s %s %s = %s" % (n1, op, n2, r))

