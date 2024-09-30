The **KBC (Kaun Banega Crorepati) Game** in Python is a fun, quiz-based project that mimics the popular Indian TV show. The game consists of a series of multiple-choice questions with increasing difficulty, where each correct answer leads to a higher reward. It provides players with lifelines like **50-50**, **Ask the Audience**, and **Phone a Friend**, making the game engaging and interactive.

### Key Features:
1. **Question Bank**: The game uses a pre-defined set of questions from various categories such as General Knowledge, Science, Sports, and more. The questions can be stored in a text file or a database, from which they are randomly selected.
   
2. **Lifelines**:
   - **50-50**: Eliminates two incorrect answers, making it easier to choose the correct one.
   - **Ask the Audience**: Provides a percentage distribution of audience votes for each answer, simulating the TV show experience.
   - **Phone a Friend**: Gives a pre-defined hint or suggests a possible answer, replicating the "help from a friend" concept.

3. **Levels and Rewards**: As in the real show, the game has multiple levels, with each correct answer moving the player to a higher reward tier. The difficulty of questions increases with each level. A player can also "quit" after any correct answer to take their accumulated winnings.

4. **Game Flow**:
   - The player is asked a question with four possible answers (A, B, C, D).
   - After answering correctly, they proceed to the next round.
   - If they choose the wrong answer, the game ends, and they lose their accumulated money (or fall to a predefined safety net).
   
5. **User Interface**: The game runs in a simple command-line interface, where questions, options, and game progress are displayed. Players interact by typing the letter corresponding to their answer or choosing a lifeline.

6. **Python Concepts Used**:
   - **Control structures**: `if-else` for decision making, `while` for looping through questions.
   - **File Handling**: To load questions from a file or store player data.
   - **Functions**: For organizing the game logic (e.g., question display, checking answers, applying lifelines).
   - **Random Module**: To shuffle questions and randomly provide answers for lifelines like 50-50.

This project is an excellent way to practice Python concepts like loops, conditionals, and file handling, while also creating a fun and interactive game that can be played by friends and family for entertainment.
