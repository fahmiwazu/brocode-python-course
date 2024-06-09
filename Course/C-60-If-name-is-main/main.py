########## if __name__ == '__main__' in python
def hello():
     print("Hello!")

if __name__ == "__main__":
    hello()
    print("Running this main directly")
else:
    print("Running other module indirectly")