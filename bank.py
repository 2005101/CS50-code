def main():
    y = input("Greeting: ")
    print(value(y))

def value(greeting):
    greeting_new = greeting.lower().strip()
    if greeting_new.startswith("hello"):
        return "$0"
    elif greeting_new.startswith("h"):
        return "$20"
    else:
        return "$100"

if __name__ == "__main__":
    main()
