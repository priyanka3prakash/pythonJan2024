"""
Purpose: create decorator for retry for n times
"""


# decorator with one argument
def repeat(func):
    def inner(*args, **kwargs):
        for _ in range(3):
            func(*args, **kwargs)

    return inner

@repeat
def hello_world(name):
    print(f"Hello {name}!!!")


hello_world("Python")
print()
# ================================
def retry(func):
    def inner(*args, **kwargs):
        for _ in range(5):
            try:
                return func(*args, **kwargs)
            except Exception as ex:
                print(ex)

    return inner


@retry
def hello_world(name):
    # print(f"Hello {name}!!!")
    for i in range(2):
        raise ZeroDivisionError("error")
    print(f"Hello {name}!!!")


hello_world("Python")


# decorator with TWO arguments
def retry(environment, count):
    def inner1(func):
        def inner2(*args, **kwargs):
            print(f"{environment = }")
            for _ in range(count):
                func(*args, **kwargs)

        return inner2

    return inner1


@retry(environment="dev", count=3)
def hello_world(name):
    print(f"Hello {name}!!!")


hello_world("Python")



@retry(environment="uat", count=5)
def hello_world(name):
    print(f"Hello {name}!!!")


hello_world("Python")