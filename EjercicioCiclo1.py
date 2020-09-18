def palindroma(palabra):
    reves=""
    for i in reversed(range(0,len(palabra))):
        reves+=palabra[i]
    if palabra==reves:
        print ("Es palindroma")
    else:
        print("No es palindroma")
        
