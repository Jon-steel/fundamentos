# -*- coding: utf-8 -*-
palabra=raw_input("Ingrese la cadena: ") + ";"
estado="q0"
for en in palabra:
    if estado =="q0":
        if en=="a" or en=="b" or en=="c" or en=="d" or en=="e" or en=="f" or en=="g" or en=="h" or en=="i" or en=="j" or en=="k" or en=="l" or en=="m" or en=="n" or en=="ñ" or en=="o" or en=="p" or en=="q" or en=="r" or en=="s" or en=="t" or en=="u" or en=="v" or en=="w" or en=="x" or en=="y" or en=="z" or en=="0" or en=="1" or en=="2" or en=="3" or en=="4" or en=="5" or en=="6" or en=="7" or en=="8" or en=="9":
            estado="q1"
        if en=="." or en=="@" or en==";":
            estado="qr"
            
    elif estado =="q1":
        if en=="." or en=="a" or en=="b" or en=="c" or en=="d" or en=="e" or en=="f" or en=="g" or en=="h" or en=="i" or en=="j" or en=="k" or en=="l" or en=="m" or en=="n" or en=="ñ" or en=="o" or en=="p" or en=="q" or en=="r" or en=="s" or en=="t" or en=="u" or en=="v" or en=="w" or en=="x" or en=="y" or en=="z" or en=="0" or en=="1" or en=="2" or en=="3" or en=="4" or en=="5" or en=="6" or en=="7" or en=="8" or en=="9":
            estado ="q1"
        if en=="@":
            estado="q2"
        if en==";":
            estado="qr"
            
    elif estado=="q2":
        if en=="a" or en=="b" or en=="c" or en=="d" or en=="e" or en=="f" or en=="g" or en=="h" or en=="i" or en=="j" or en=="k" or en=="l" or en=="m" or en=="n" or en=="ñ" or en=="o" or en=="p" or en=="q" or en=="r" or en=="s" or en=="t" or en=="u" or en=="v" or en=="w" or en=="x" or en=="y" or en=="z" or en=="0" or en=="1" or en=="2" or en=="3" or en=="4" or en=="5" or en=="6" or en=="7" or en=="8" or en=="9":
            estado="q3"
        if en==".":
            estado="qr"
        if en==";" or en=="@":
            estado="qr"
    elif estado=="q3":
         if en=="a" or en=="b" or en=="c" or en=="d" or en=="e" or en=="f" or en=="g" or en=="h" or en=="i" or en=="j" or en=="k" or en=="l" or en=="m" or en=="n" or en=="ñ" or en=="o" or en=="p" or en=="q" or en=="r" or en=="s" or en=="t" or en=="u" or en=="v" or en=="w" or en=="x" or en=="y" or en=="z" or en=="0" or en=="1" or en=="2" or en=="3" or en=="4" or en=="5" or en=="6" or en=="7" or en=="8" or en=="9":
            estado="q3"
         if en==".":
            estado="q4"
         if en=="@" or en==";":
            estado="qr"
    elif estado=="q4":
         if en=="a" or en=="b" or en=="c" or en=="d" or en=="e" or en=="f" or en=="g" or en=="h" or en=="i" or en=="j" or en=="k" or en=="l" or en=="m" or en=="n" or en=="ñ" or en=="o" or en=="p" or en=="q" or en=="r" or en=="s" or en=="t" or en=="u" or en=="v" or en=="w" or en=="x" or en=="y" or en=="z":
            estado="q4"
         if en=="." or en=="@":
            estado="qr"
         if en=="1" or en=="2" or en=="3" or en=="4" or en=="5" or en=="6" or en=="7" or en=="8" or en=="9":
            estado="qr"
         if en==";":
            estado="qa"
        
    
            
    elif estado =="qr" or estado=="qa":
        break 
print estado 
            
