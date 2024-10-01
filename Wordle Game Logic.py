import pandas as pd
import random

# Load Wordle words from a CSV file or a URL (replace with actual URL)
url = "https://example.com/wordle_words_2024.csv"
df = pd.read_csv(url)

# Assume the CSV has a column called 'word' that contains the list of words
wordle_words_2024 = df['word'].str.upper().tolist()  # Convert to uppercase and then to a list

# Function to select a random word
def choose_random_word(word_list):
    return random.choice(word_list).upper()

# Function to play Wordle
def wordle():
    solution = choose_random_word(wordle_words_2024)  # Random word selection
    attempts = 6  # You can adjust the number of attempts
    
    print("Welcome to Wordle! Guess the 5-letter word.")
    
    for attempt in range(attempts):
        guess = input(f"Attempt {attempt + 1}/{attempts}: ").upper()
        
        if len(guess) != 5:
            print("Please enter a 5-letter word.")
            continue
        
        # Provide feedback to the user
        feedback = []
        for i in range(len(guess)):
            if guess[i] == solution[i]:
                feedback.append(f"*{guess[i]}*")  # Correct letter in correct place
            elif guess[i] in solution:
                feedback.append(guess[i])  # Correct letter in wrong place
            else:
                feedback.append("_")  # Incorrect letter
        
        print("Feedback:", " ".join(feedback))
        
        # Check if the guess is correct
        if guess == solution:
            print("Congratulations! You've guessed the word.")
            break
    else:
        print(f"Sorry, you've run out of attempts. The word was {solution}.")

# Play the game
wordle()


