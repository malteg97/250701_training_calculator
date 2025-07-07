""" Testproject for a calculator with some basic functionality """


def add(num1, num2):
    """Add two numbers
    """
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
    return result

def subtract(num1, num2):
    """Subtract num2 from num1"""
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
    return result


def is_number(value):
    try:
        float(value)
    except ValueError:
        return False
    return True


def get_number_from_user():
    """Get input from user and return as float number

    :return: Input as float if the user entered a number. Otherwise return None
    """
    try:
        return float(input("Bitte Zahl eingeben: "))
    except ValueError:
        return None


def switch_operator(operator):
    """Map the users input (operator) to the function that needs to be executed

    :return: The function to execute.
    If there is no function defined for the given operator return 'invalid'.
    If an empty string is given return None.
    """
    switcher = {
        "+": add,
        "-": subtract,
        "": None
    }
    return switcher.get(operator, "invalid")


def calculator():
    """Main function of the calculator app
    """
    cont = True
    while cont:
        operator = input("Bitte den Rechenoperator eingeben:\n"
                         "'+' für Addition\n"
                         "'-' für Subtraktion\n"
                         "'/' für Division\n"
                         "'*' für Multiplikation\n"
                         "'**' für Potenzieren\n"
                         "Enter ohne Eingabe zum Abbrechen\n"
                         "Eingabe: ")
        operating_function = switch_operator(operator)
        if not operating_function:
            print("Auf Wiedersehen")
            cont = False
        elif operating_function == "invalid":
            print(f"Der Operator {operator} ist nicht bekannt oder noch nicht implementiert.")
        else:
            num1 = get_number_from_user()
            num2 = get_number_from_user()
            if is_number(num1) and is_number(num2):
                operating_function(num1, num2)


if __name__ == "__main__":
    calculator()
