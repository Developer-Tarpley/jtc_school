# main.py
def hello_world():
    return "Welcome to Git!"

def greet_person(name: str) -> str:
    return "Hello, " + name + "!"

if __name__ == "__main__":
    print(hello_world())
    print(greet_person("Corey"))