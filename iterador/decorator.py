def my_decorator(function):
    def wrapper():
        print("Executado ANTES da funcao")
        function()
        print("executado DEPOIS da funcao ")
    return wrapper



def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

def split_string(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper




def decorator_dudu(function):
    def wrapper():
        dudu = input("fala teu nome ai: ")
        function()
        print(dudu[::-1])
    return wrapper


