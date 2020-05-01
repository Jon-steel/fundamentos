p11= raw_input("")
p1= raw_input("")
p22= raw_input("")

estadoi="q0"
for entrada in p11:
    if estadoi=="q0":
        if entrada=="0" or entrada=="1" or entrada=="2" or entrada=="3" or entrada=="4" or entrada=="5" or entrada=="6" or entrada=="7" or entrada=="8" or entrada=="9" :
            estado1="qA"
        else:
            estado1="qR"         
    elif estado1=="qR" or estado1=="qA":
        break
for entrada in p22:
    if estadoi=="q0":
        if entrada=="0" or entrada=="1" or entrada=="2" or entrada=="3" or entrada=="4" or entrada=="5" or entrada=="6" or entrada=="7" or entrada=="8" or entrada=="9" :
            estado2="qA"
        else:
            estado2="qR"         
    elif estado2=="qR" or estado2=="qA":
        break
for entrada in p1:
    if estadoi=="q0":
        if entrada=="+" or entrada=="-" or entrada=="*" or entrada=="/":
            estado3="qA"
        else:
            estado3="qR"         
    elif estado3=="qR" or estado3=="qA":
        break
if estado1=="qA" and estado2=="qA" and estado3=="qA":
    estadoF="qA"
else:
    estadoF="qR"
print estadoF

p=int(p11)
p2=int(p22)

if p1=="+" or p1=="-" or p1=="*" or p1=="/":
    if p1=="+":
        r=p+p2
      
    elif p1=="*":
        r=p*p2
        
    elif p1=="-":
        r=p-p2
       
    elif p1=="/":
        r=p/p2
    
        
else:
    estado1="qR"

print ("el resultado de es:  %s %s %s = %s" % (p, p1, p2, r))
    
    
    


 
    
    
    
    

