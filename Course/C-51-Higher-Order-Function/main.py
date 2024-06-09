############ higher order function in python
def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text = func("Hello")
    print(text)

hello(loud)
hello(quiet)

def divisor(x):
    def devidend(y):
        return y / x
    return devidend

devide = divisor(2)
print(devide(10))