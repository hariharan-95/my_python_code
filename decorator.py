
def hello(func):
    def wrapper():
        print("Wrapper function to call")
        func()
        print("funciton alled hari")
        
    return wrapper 


@hello
def normalfuntion():
    print("Pda andavane name pakkam")


normalfuntion()

