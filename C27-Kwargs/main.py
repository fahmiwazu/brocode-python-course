############ kwargs
def hello(**names):
    # print("Hello "+kwargs['first']+" "+kwargs['last'])
    print("Hello", end=" ")
    for key,value in names.items():
        print(value, end=" ")

hello(tittle="Mr.",first="Fahmi",last="Wazza",middle="Calma")