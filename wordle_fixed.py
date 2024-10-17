import tkinter as tk
import random

# List of five-letter words
tup1 = ("whichtheretheiraboutwouldtheseotherwordscouldwritefirstwaterafterwhererightthinkthreeyears"
        "placesoundgreatagainstilleverysmallfoundthoseneverundermightwhilehouseworldbelowaskedgoing"
        "largeuntilalongshallbeingoftenearthbegansincestudynightlightabovepaperpartsyoungstorypoint"
        "timesheardwholewhitegivenmeansmusicmilesthingtodaylaterusingmoneylinesordergroupamonglearn"
        "knownspacetableearlytreesshorthandsstateblackshownstoodfrontvoicekindsmakescomesclosepower"
        "livedvoweltakenbuiltheartreadyquiteclassbringround")

# Split string into a list of 5-letter words
tup1 = " ".join(tup1[i:i+5] for i in range(0, len(tup1), 5)).split()

# Choose a random word from the list
selected_word = random.choice(tup1).lower()
attempts = 6

# Function to reset the game
def reset_game():
    global selected_word, attempts
    selected_word = random.choice(tup1).lower()
    attempts = 6
    entry_box.delete(0, tk.END)
    result_frame.pack_forget()
    result_label.config(text="New game started. You have 6 attempts.")
    attempts_label.config(text=f"Remaining attempts: {attempts}")

# Function to create colored boxes based on guess results
def display_result(guess, result):
    # Remove previous result boxes
    for widget in result_frame.winfo_children():
        widget.destroy()

    # Display the current result using colored boxes
    for i, letter in enumerate(guess):
        if result[i] == "X":
            color = "#6aaa64"  # Green box
        elif result[i] == "0":
            color = "#c9b458"  # Yellow box
        else:
            color = "#ffffff"  # White box

        label = tk.Label(result_frame, text=letter.upper(), bg=color, width=4, height=2, font=("Helvetica", 18), relief="solid")
        label.grid(row=0, column=i, padx=5)

    result_frame.pack(pady=10)

# Function to process the user's guess
def check_guess():
    global attempts
    guess = entry_box.get().lower()

    if len(guess) != 5:
        result_label.config(text="Please enter a valid 5-letter word.")
        return

    if attempts > 0:
        if guess == selected_word:
            result_label.config(text=f"{guess}, correct guess! You win!")
            display_result(guess, "XXXXX")  # Display all green boxes
            return

        # Generate result string (X for correct position, 0 for wrong position, - for not in the word)
        result = ""
        for i in range(5):
            if selected_word[i] == guess[i]:
                result += "X"
            elif guess[i] in selected_word:
                result += "0"
            else:
                result += "-"
        
        # Display result using colored boxes
        display_result(guess, result)

        attempts -= 1
        attempts_label.config(text=f"Remaining attempts: {attempts}")

        if attempts == 0:
            result_label.config(text=f"Game over! The word was '{selected_word}'.")
    else:
        result_label.config(text=f"Game over! The word was '{selected_word}'.")

# Set up the main application window
root = tk.Tk()
root.title("Unlimited Wordle Bot")
root.geometry("400x400")
root.config(bg="#FDE2E4")  # Light pastel pink background

# Title label
title_label = tk.Label(root, text="Wordle Bot", font=("Helvetica", 24, "bold"), bg="#FDE2E4", fg="#94B3FD")
title_label.pack(pady=10)

# Instructions label
instructions = tk.Label(root, text="Guess the 5-letter word. You have 6 attempts.", font=("Helvetica", 14), bg="#FDE2E4", fg="#333333")
instructions.pack(pady=5)

# Entry box for the word guess
entry_box = tk.Entry(root, font=("Helvetica", 16), width=10, justify="center", bg="#FFF1E6")
entry_box.pack(pady=10)

# Button to submit the guess
submit_button = tk.Button(root, text="Submit", font=("Helvetica", 14), command=check_guess, bg="#D4A5A5", fg="white")
submit_button.pack(pady=10)

# Frame to display colored result boxes
result_frame = tk.Frame(root, bg="#FDE2E4")

# Label to display remaining attempts
attempts_label = tk.Label(root, text=f"Remaining attempts: {attempts}", font=("Helvetica", 14), bg="#FDE2E4", fg="#333333")
attempts_label.pack()

# Label to display additional result messages
result_label = tk.Label(root, text="Enter your guess!", font=("Helvetica", 14), bg="#FDE2E4", fg="#333333")
result_label.pack(pady=20)

# Button to reset the game
reset_button = tk.Button(root, text="Reset Game", font=("Helvetica", 14), command=reset_game, bg="#94B3FD", fg="white")
reset_button.pack(pady=10)

# Start the application
root.mainloop()
