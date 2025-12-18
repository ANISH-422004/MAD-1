def funA(func):
    def inner_wrapper():
        print("Wrapper function of funA")
        res1 = func()
        res2 = func()
        return res1, res2
    return inner_wrapper

@funA
def funB():
    return "I am from funB"

print(funB())