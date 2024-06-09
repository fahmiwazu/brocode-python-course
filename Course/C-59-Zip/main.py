############# zip (iterable)
usernames = ["Dude","Bro","Mister"]
password = ("1234","5678","qwert")
login_date = ["1/1/2021","1/2/2021","1/3/2021"]

users = zip(usernames, password,login_date)

print(type(users))

for i in users:
    print(i)