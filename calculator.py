def calculator(x = None):

    result = x

    def nInput():
        n = input()
        if n == "n":
            reset()
        if n == "r":
            if result == None:
                print("Error: Missing result")
                reset()
            else:
                n = result
                print(n)
        if is_number(n):
            return float(n)
        else:
            print("Error: Invalid input")
            reset()

    def is_number(n):
        try:
            float(n)
            return True
        except ValueError:
            return False

    def sum():
        z = x + y
        return z

    def subs():
        z = x - y
        return z

    def mult():
        z = x * y
        return z

    def div():
        z = x / y
        return z

    def reset():
        print("Reseting")
        calculator()

    operators: dict = {
        "+": sum,
        "-": subs,
        "*": mult,
        "/": div
    }

    if x == any:
        pass
    else:
        x = nInput()

    operator: str = input()

    if operator == "n":
        reset()
    elif operator in operators:
        y = nInput()
        z = operators[operator]()
        print(f"{x} {operator} {y} = {z}")
    else:
        print("El operador no existe, prueba con: (+/-)")

    calculator(float(z))
    
calculator()