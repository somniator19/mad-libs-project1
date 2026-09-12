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
    
    # Choosing the correct list of placeholders
    if choice == "1":
        placeholders = placeholders_hospital
    elif choice == "2":
        placeholders = placeholders_camping
    elif choice == "3":
        placeholders = placeholders_castle

    # №1 Hospital
    placeholders_hospital = [
        "Number",
        "Measure of time",
        "Mode of Transportation",
        "Adjective",
        "Adjective2",
        "Noun",
        "Color",
        "Part of the Body",
        "Verb",
        "Number2",
        "Noun2",
        "Noun3",
        "Part of the Body 2",
        "Noun4",
        "Adjective3",
        "Silly Word"
    ]

    # №2 Camping
    placeholders_camping = [
        "Proper Noun (Person's Name)",
        "Noun",
        "Adjective (Feeling)",
        "Verb",
        "Adjective (Feeling) 2",
        "Animal",
        "Verb2",
        "Color",
        "Verb (ending in ing)",
        "Adverb (ending in ly)",
        "Number",
        "Measure of Time",
        "Silly Word",
        "Noun2"
    ]

    # №3 Castle
    placeholders_castle = [
        "Proper Noun (Person's Name)",
        "Adjective",
        "Color",
        "Animal",
        "Place",
        "Adjective2",
        "Magical Creature (Plural)",
        "Adjective3",
        "Magical Creature (Plural)2",
        "Room in a House",
        "Noun",
        "Noun2",
        "Noun (Plural)3",
        "Adjective4",
        "Noun (Plural)4",
        "Number",
        "Measure of time",
        "Verb (ending in ing)",
        "Adjective5",
        "Noun5"
    ]

    # Empty dictionary for storing the answers
    answers = {}

    # Loop through every placeholder and ask the user for input
    for placeholder in placeholders if choice == "1" else placeholders_camping if choice == "2" else placeholders_castle:
        # Making nice questions for the user input prompt
        question = placeholder.replace("_", " ").title()
        user_input = input(f"Enter a {question}: ").strip()
        answers[placeholder] = user_input

    # Fill in the template with the user's answers
    story = template.format(**answers)

    # Prompt the user for inputs based on placeholders
    print("\n----- Here is your Mad Lib story -----")
    print(story)

if __name__ == "__main__":
    main()