# Mad libs mini-projectn >> A fun game to kill your time `^_^`

def main():
    # Welcome message and instructions
    print("Welcome to the Mad Libs! (っ•ᴗ•c)")
    print("It's a small game that allows you to create a funny story, using different random variants at your choosing")
    print("Hope this game will make you laugh! (≧◡≦)")
    print("Let's get started! (ง •̀_•́)ง")

    # Menu for choosing a template
    print("Please choose a template:")
    print("1. Hospital Adventure")
    print("2. Camping Trip")
    print("3. Castle Quest")

    choice = input("Enter your choice (1-3): ").strip()
    
    # Loop to determine the filename based on the user's choice
    if choice == "1":
        filename = "templates/hospital.txt"
    elif choice == "2":
        filename = "templates/camping.txt"
    elif choice == "3":
        filename = "templates/castle.txt"
    else:
        print("Invalid choice (>_<). Please run the program again.")
        return

    # Load the chosen template file
    with open(filename, "r", encoding="utf-8") as file:
        template = file.read()

    # Prompt the user for inputs based on placeholders
    print("\n----- Here is the template you've chosen -----")
    print(template)

if __name__ == "__main__":
    main()