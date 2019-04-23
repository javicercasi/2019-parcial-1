def interfaz(palabra):
    from parcial import codigo

    if not palabra:
        return ('Error')
        print("No ingreso ninguna palabra")

    
    try:
        numero1=int(palabra)
        resultado=codigo(numero1)
        return interfaz(resultado)

    except:
        return('Error')
        print("Disculpe, solo acepto numeros")

def main():
    palabra=input('Ingrese un numero: ')
    result=interfaz(palabra)
    print(result)
main()


