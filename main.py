# Mad libs mini-project
def main():
    print("Welcome to the Mad Libs! (っ•ᴗ•c)")
    print("It's a small game that allows you to create a funny story, using different random variants at your choosing")
    print("Hope this game will make you laugh! (≧◡≦) ♡  #And help learn how to code in Python!")
    print("Let's get started! (ง •̀_•́)ง")
    adjective1 = input("Enter an adjective: ")
    noun1 = input("Enter a noun: ")
    verb1 = input("Enter a verb: ")
    place = input("Enter a place: ")
    
    mad_lib = f"Once upon a time, there was a {adjective1} {noun1} who loved to {verb1} in {place}."
    
    print("\nHere's your Mad Lib:")
    print(mad_lib)

if __name__ == "__main__":
    main()