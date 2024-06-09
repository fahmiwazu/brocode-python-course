################## Exception
try:
    numerator = int(input("Numb A : "))
    denomerator = int(input("Numb B : "))
    res = numerator / denomerator
except ZeroDivisionError as e:
    print(e)
    print("can devide by 0")
except ValueError as e:
    print(e)
    print("enter only number please")
except Exception as e:
    print(e)
    print("something when wrong")
else:
    print(res)
finally:
    print("this will always executed")