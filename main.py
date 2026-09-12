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
    print("4. Alien Interview")
    print("5. Cooking Disaster")
    print("6. Day of a Superhero (OnePuchMan style)")

    choice = input("Enter your choice (1-6): ").strip()
    
    # Loop to determine the filename based on the user's choice
    if choice == "1":
        filename = "templates/hospital.txt"
    elif choice == "2":
        filename = "templates/camping.txt"
    elif choice == "3":
        filename = "templates/castle.txt"
    elif choice == "4":
        filename = "templates/alien.txt"
    elif choice == "5":
        filename = "templates/cooking.txt"
    elif choice == "6":
        filename = "templates/superhero.txt"
    else:
        print("Invalid choice (>_<). Please run the program again.")
        return

    # Load the chosen template file
    with open(filename, "r", encoding="utf-8") as file:
        template = file.read()
    
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

    # №4 Alien
    placeholders_alien = [
        "Adjective",
        "Proper Noun (Alien Name)",
        "Color",
        "Vehicle",
        "Food",
        "Noun",
        "Verb",
        "Adjective2",
        "Noun2",
        "Silly Object",
        "Verb2",
        "Plural Noun",
        "Adjective3",
        "Noun3",
        "Silly Word"
    ]

    # №5 Cooking
    placeholders_cooking = [
        "Adjective",
        "Dish Name",
        "Family Member",
        "Number",
        "Plural Food",
        "Kitchen Tool",
        "Liquid",
        "Adjective2",
        "Noun",
        "Animal",
        "Verb in past tense",
        "Smelly Thing",
        "Another Smelly Thing",
        "Verb",
        "Noun2",
        "Plural Noun",
        "Exclamation"
    ]

    # №6 Superhero
    placeholders_superhero = [
        "Overpowered ability",
        "Cool Hero Name",
        "Color",
        "Adjective",
        "Plural Noun",
        "Noun",
        "Verb in past tense",
        "Silly Japanese word",
        "Useless action",
        "Food"
    ]

    # Choosing the correct list of placeholders
    if choice == "1":
        placeholders = placeholders_hospital
    elif choice == "2":
        placeholders = placeholders_camping
    elif choice == "3":
        placeholders = placeholders_castle
    elif choice == "4":
        placeholders = placeholders_alien
    elif choice == "5":
        placeholders = placeholders_cooking
    elif choice == "6":
        placeholders = placeholders_superhero

    # Simple mapping for user-friendly questions
    nice_names = {
        # 0 Common templates
        "Number": "a number",
        "Number2": "another number",
        "Measure of time": "a measure of time (e.g. days, weeks, years)",
        "Measure of Time": "a measure of time (e.g. hours, days)",
        "Mode of Transportation": "a mode of transportation",
        "Adjective": "an adjective",
        "Adjective2": "another adjective",
        "Adjective3": "one more adjective",
        "Adjective4": "yet another adjective",
        "Adjective5": "one final adjective",
        "Noun": "a noun",
        "Noun2": "another noun",
        "Noun3": "one more noun",
        "Noun4": "yet another noun",
        "Noun5": "one final noun",
        "Color": "a color",
        "Part of the Body": "a body part",
        "Part of the Body 2": "another body part",
        "Verb": "a verb",
        "Verb2": "another verb",
        "Silly Word": "a silly word",
        "Proper Noun (Person's Name)": "a person's name",
        "Adjective (Feeling)": "an adjective that describes a feeling",
        "Adjective (Feeling) 2": "another feeling adjective",
        "Animal": "an animal",
        "Verb (ending in ing)": "a verb ending in -ing",
        "Adverb (ending in ly)": "an adverb ending in -ly",
        "Place": "a place",
        "Magical Creature (Plural)": "a plural magical creature (e.g. unicorns)",
        "Magical Creature (Plural)2": "another plural magical creature",
        "Room in a House": "a room in a house",
        "Noun (Plural)3": "a plural noun",
        "Noun (Plural)4": "another plural noun",

        # 4 Alien template
        "Proper Noun (Alien Name)": "an alien name",
        "Vehicle": "a vehicle",
        "Food": "a food",
        "Silly Object": "a silly object",
        "Plural Noun": "a plural noun",

        # 5 Cooking template
        "Dish Name": "a dish name",
        "Family Member": "a family member",
        "Plural Food": "a plural food (e.g. potatoes)",
        "Kitchen Tool": "a kitchen tool",
        "Liquid": "a liquid",
        "Verb in past tense": "a verb in past tense",
        "Smelly Thing": "something that smells bad",
        "Another Smelly Thing": "another smelly thing",
        "Exclamation": "an exclamation (e.g. Oh no!, Yikes!)",

        # 6 OnePunchMan template
        "Overpowered ability": "an overpowered ability (e.g. punch with the force of a thousand suns)",
        "Cool Hero Name": "a cool hero name",
        "Silly Japanese word": "a silly Japanese-sounding word",
        "Useless action": "a completely useless action",
    }

    # Empty dictionary for storing the answers
    answers = {}

    # Loop through every placeholder and ask the user for input
    for placeholder in placeholders:
        # Making nice questions for the user input prompt
        question = nice_names.get(placeholder, placeholder) # Fallback to original name
        user_input = input(f"Give me {question}: ").strip()
        answers[placeholder] = user_input

    # Fill in the template with the user's answers
    story = template.format(**answers)

    # Prompt the user for inputs based on placeholders
    print("\n----- Here is your Mad Lib story (๑˃ᴗ˂) -----")
    print(story)

if __name__ == "__main__":
    main()