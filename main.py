from Chat import *

if __name__ == '__main__':
    c = Chat("Minou")
    print(f"The cat's name is {c.name}")
    print(f"cat is {c.state}")
    c.sleep()
    print(f"cat is {c.state}")