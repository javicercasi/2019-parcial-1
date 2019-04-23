def codigo(numero):

    if numero<=9:
        hexa=str(numero)
        return(hexa)

    division=numero
    listaresto=[]
    sale=[]
    listadivision=[]

    while division>=16:
        division=int(division/16)
        listadivision.append(division)

        resto=division % 16
        listaresto.append(resto)
        sale.append(listaresto[::-1])
    
    i=0
    for number in sale:
        
        if number == 10:
            sale[i]='A'
        
        if number == 11:
            sale[i] ='B'

        if number == 12:
            sale[i] ='C'

        if number  == 13:
            sale[i] = 'D'

        if number == 14:
            sale[i] = 'E'

        if number == 15:
            sale[i] = 'F'
        
        i=i+1

        resultado=resultado+ sale[i]

    if numero == 10:
            return ('A')
        
    if numero == 11:
            return ('B')

    if numero == 12:
            return ('C')

    if numero == 13:
            return ('D')

    if numero == 14:
            return ('E')

    if numero == 15:
            return ('F')
    
    #for number




        



    


    
    




