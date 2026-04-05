# Rock-Paper-Scissors-Game

A simple command-line based Rock, Paper, Scissors game built using Python. This project allows users to play against the computer while keeping track of their scores in a local file.

📌 Features
Interactive CLI (Command Line Interface)
Personalized user experience (name input)
Randomized computer choices
Score tracking using a file system
Option to play multiple rounds
Clear game rules and results display
🕹️ How the Game Works
The user enters their name.
The computer randomly selects one option: Rock, Paper, or Scissor.
The user selects their option.
The game compares both choices and determines:
✅ Win
❌ Loss
🤝 Draw
The result is saved in a scoreboard file.
The user can choose to play again.
📂 Project Structure
project-folder/
│
├── main.py
├── Muzammil/
│   └── score_board.txt
└── README.md
⚙️ Requirements
Python 3.x

No external libraries are required (uses built-in random module).

▶️ How to Run
Clone or download this repository.
Make sure the folder Muzammil exists.
Create a file named score_board.txt inside the Muzammil folder.
Run the script:
python main.py
📝 Scoreboard System
Scores are stored in:
Muzammil/score_board.txt
Each user has their own entry:
Ali: 1, -1, 0, 1
Ahmed: 0, 1

Where:
1 = Win
0 = Draw
-1 = Loss

⚠️ Known Issues / Improvements
Input validation condition needs improvement (currently always triggers invalid input).
File path uses mixed slashes (\ and /) which may cause issues on some systems.
No exception handling for file operations.
Score calculation is not summarized (only raw values stored).
UI can be improved with better formatting.
🚀 Future Enhancements
Add score summary (total wins/losses/draws)
Improve input validation
Add GUI version (Tkinter or PyQt)
Store data using JSON or database
Multiplayer support
🤝 Contribution

Feel free to fork this project and improve it. Suggestions and pull requests are welcome!

📜 License
This project is open-source and available for learning purposes.

Fix your code bugs 🔧
Improve logic (especially that invalid input issue)
Or convert this into a GUI app 😄
