def calculator(x = None):

    def sum():
        z = int(x) + int(y)
        return print(f"= {z}")

    def subs():
        z = int(x) - int(y)
        return print(f"= {z}")


    operators: dict = {
        "+": sum,
        "-": subs
    }
    

    if x == any:
        pass
    
    else:
        x: int = input()
    
    op: str = input()
    

    if op in operators:
        y: int = input()
        z = operators[op]()
    else:
        print("El operador no existe, prueba con: (+/-)")

    calculator()
    
calculator()