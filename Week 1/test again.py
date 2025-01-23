def my_decorator(func):
    def wrapper():
        print("Something before the function runs.")
        func()
        print("Something after the function runs.")
    wrapper()

def say_hello():
    print("Hello!")

say_hello = my_decorator(say_hello)
#say_hello
#say_hello
print (say_hello)