# This is the code that will be run from the second file

def greet(name):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    greet(user_name)
