while True:
    palabra= raw_input("ingresa la cadena")+";"
    if palabra=="":
        break
    estado="q0"
    for entrada in palabra:
        if estado=="q0":
            if entrada=="0" or entrada=="1" or entrada=="2" or entrada=="3" or entrada=="4" or entrada=="5" or entrada=="6" or entrada=="7" or entrada=="8" or entrada=="9" :
                estado="q1"
                n1=entrada
            if entrada==";":
                print "Caracter inesperado"
                exit
                estado="qR"
                entrada="l"
            if entrada=="+" or entrada=="-"or entrada=="*" or entrada=="/":
                estado="qR"
                entrada=""   
        elif estado=="q1":
            if entrada=="0" or entrada=="1" or entrada=="2" or entrada=="3" or entrada=="4" or entrada=="5" or entrada=="6" or entrada=="7" or entrada=="8" or entrada=="9" :
                estado="q1"
                n1+=entrada
                exit
            if entrada=="+" or entrada=="-"or entrada=="*" or entrada=="/":
                estado="q2"
                simbol=entrada
            if entrada==";":
                print "Caracter inesperado"
                estado="qR"
                entrada=""   
                exit
        elif estado=="q2":
             if entrada=="0" or entrada=="1" or entrada=="2" or entrada=="3" or entrada=="4" or entrada=="5" or entrada=="6" or entrada=="7" or entrada=="8" or entrada=="9" :
                 estado="q3"
                 n2=entrada
             if entrada=="+" or entrada=="-"or entrada=="*" or entrada=="/" or entrada==";" or entrada=="":
                estado="qR"
                print "Caracter inesperado"
                entrada=""
                exit
             if entrada=="+" or entrada=="-"or entrada=="*" or entrada=="/":
                estado="qR"
                entrada=""
                exit
        elif estado=="q3":
             if entrada=="0" or entrada=="1" or entrada=="2" or entrada=="3" or entrada=="4" or entrada=="5" or entrada=="6" or entrada=="7" or entrada=="8" or entrada=="9" :
                 estado="q3"
                 n2+=entrada
             if entrada=="+" or entrada=="-"or entrada=="*" or entrada=="/":
                 estado="q2"
             if entrada==";":
                 estado="qA"

                 
        elif estado=="qR" or estado=="qA":
            break
    nI=int(n1)
    nI2=int(n2)

    if simbol=="+" or simbol=="-" or simbol=="*" or simbol=="/":
        if simbol=="+":
            r=nI+nI2
          
        elif simbol=="*":
            r=nI*nI2
            
        elif simbol=="-":
            r=nI-nI2
           
        elif simbol=="/":
            r=nI/nI2
        
            
    else:
            estado="qR"
    if estado=="qR":
        print "la operacion esta mal"
        nI=0
        nI2=0
        p=";"
    else:     
        print estado
        print ("el resultado de -> %s %s %s = %s" % (nI, simbol, nI2, r))
nI=0
nI2=0
entrada="";
       

