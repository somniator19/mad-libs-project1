# Mad Libs 

A simple and fun Mad Libs game written in Python.

The player chooses a story template, fills in the missing words, and receives a completely ridiculous finished story.

## How to play

1. Make sure you have Python 3 installed.
2. Open a terminal in the project folder.
3. Run the program:

<```bash
python main.py >

1. Choose a template (1–6).
2. Answer the questions.
3. Enjoy your story (つ✧ω✧)つ

## Available templates

1. **Hospital Adventure** – Official template  
2. **Camping Trip** – Official template  
3. **Castle Quest** – Official template  
4. **Alien Interview** – Original  
5. **Cooking Disaster** – Original  
6. **Superhero Fail** – Inspired by One-Punch Man

## Project structure

mad-libs-project1/
├── main.py
├── README.md
├── .gitignore
└── templates/
├── hospital.txt
├── camping.txt
├── castle.txt
├── alien.txt
├── cooking.txt
└── superhero.txt 

## Notes

- All story templates are stored as plain text files.
- The program loads the chosen template, asks for the required words, and fills them in using Python’s `.format()` method.
- Some templates contain small easter eggs (ASCII art and a short Japanese note).

## Future ideas

- Web version
- More chaotic templates
- Ability for players to create their own templates

Made with curiosity and a bit of chaos (=^･ω･^=)