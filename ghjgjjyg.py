
palabra=raw_input("Ingrese la operacion (para raiz # para elevacion % ): ")
    
for en in palabra:
    if estado=="q0":
        if en in "0123456789":
            estado="q1"
        if en in "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ":
            estado="q7"
        if en == ";" or en=="+" or en=="-" or en=="*" or en=="/" or en==" " or en=="%" or en=="#":
            estado="qr"
            
    elif estado=="q1":
        if en in "0123456789":
            estado="q1"
        if en == ";" or en=="+" or en=="-" or en=="*" or en=="/" or en=="%" or en=="#" or en in "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ":
            estado="qr"
        if en==" ":
            estado="q2"
           
            
    elif estado=="q2":
         if en in "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ":
            estado="q3"
         if en == ";" or en=="+" or en=="-" or en=="*" or en=="/" or en=="%" or en=="#":
            estado="q4"
         if en in "0123456789" or en==";" or en==" ":
            estado="qr"
            
     elif estado=="q3":
         if en in "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ":
            estado="q3"
         if en in "0123456789" or en==";" or en=="+" or en=="-" or en=="*" or en=="/" or en=="%" or en=="#":
            estado="qr"
         if en==" ":
            estado="q5"
            
    elif estado=="q4":
         if en==" ":
                estado="q5"
        if en in "0123456789aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ" or en==";" or en=="+" or en=="-" or en=="*" or en=="/" or en=="%" or en=="#":
                estado="qr"

        elif estado=="q5":
            if en in "0123456789":
                estado="q6"
                n2 = en
            if en in "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ":
                estado="q8"
                n2 = en
            if en== ";" or en=="+" or en=="-" or en=="*" or en=="/" or en==" " or en=="%" or en=="#":
                estado="qr"
            
        elif estado=="q6":
            if en in "0123456789":
                estado="q6"
                n2 += en
            if en==";":
                estado="qa"
            if en in "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ" or en=="+" or en=="-" or en=="*" or en=="/" or en=="%" or en=="#":
                estado="qr"
            
        elif estado=="q7":
            if en in "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ":
                estado="q7"
            if en==" ":
                estado="q2"
            if en== ";" or en=="+" or en=="-" or en=="*" or en=="/" or en in "0123456789" or en=="%" or en=="#" or :
                estado="qr"
            
        elif estado=="q8":
            if en in "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ":
                estado="q8"
            if en==";":
                estado="qa"
            if en == " " or en=="+" or en=="-" or en=="*" or en=="/" or en in "0123456789" or en=="%" or en=="#":
                estado="qr"
            
    

            
        print estado
