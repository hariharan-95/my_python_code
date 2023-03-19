from re import X


def func1(funcall):
    def inner():
        print("Hi hari how are you")
        x = funcall()
    return X

@func1
def hai():
    print("machi machi")

hai()