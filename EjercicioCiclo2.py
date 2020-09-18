def multiplos(a,b,x):

    if a<b:
        c=0
        for i in range(a,b+1):
            if i%x== 0:
                c=c+1
             
        print (c)
    else:
        print ("El valor del rango es incorrecto")