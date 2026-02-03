def save_history(text):
    with open("history.txt", "a") as file:
        file.write(text + "\n")

def view_history():
    try:
        with open("history.txt", "r") as file:
            print("\n--- CONVERSION HISTORY ---")
            print(file.read())
    except FileNotFoundError:
        print("No history found.")
