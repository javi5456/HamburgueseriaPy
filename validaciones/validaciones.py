def pedirNum():
    while True:
            try:
               return int(input())
            except ValueError:
                    print("Tiene que ingresar un numero valido")