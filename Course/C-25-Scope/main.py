########## Scope
name = "Fahmi"          # global scope (available inside & outside functions)
def display_name():
    name = "Waz"        # local scope (variable only inside this function)
    print(name)

display_name()
print(name)
