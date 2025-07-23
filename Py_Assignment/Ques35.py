# Write a function using *args and **kwargs to print any number of arguments.

def show_all(*args, **kwargs):
    print("Positional: ", args)
    print("Keyword: ", kwargs)
show_all(1, 2, 3, name= "Suhani", age= 19)