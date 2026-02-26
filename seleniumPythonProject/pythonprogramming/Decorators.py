#decorators - wrapper function around the functions are called as decorators

def make_pretty(func):
    def inner():
        print("i got decorator")
        func()
    return inner

@make_pretty
def vanillacake():
    print("i am the cake")
@make_pretty
def strawberrycake():
    print("i am the strawberry cake")

vanillacake()
strawberrycake()
