from utils import process_item, is_float


if __name__ == '__main__':
    print("🧮 Least prime number greater than a user input. \nType some numbers or type 'q' to quit.")
    while 1:
        user_input = input("Choose a number: ")
        if user_input == "q":
            break
        elif is_float(user_input):
            print(f"Least prime number greater than {user_input} is: {process_item(user_input)}")
        else:
            print("User input should be numerical.")
