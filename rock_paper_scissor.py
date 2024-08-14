import random
import mysql.connector
from datetime import datetime

def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host="localhost", 
            user="root",      
            password="root",  
            database="game_db"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS game_results (
                id INT AUTO_INCREMENT PRIMARY KEY,
                winner VARCHAR(255) NOT NULL,
                date_time DATETIME NOT NULL
            )
        """)
        connection.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

def insert_result(connection, winner):
    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO game_results (winner, date_time) VALUES (%s, %s)", (winner, datetime.now()))
        connection.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

# Display the game result
def display_result(user_choice, computer_choice, winner):
    print(f"User choice: {user_choice}")
    print(f"Computer choice: {computer_choice}")
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win!")
    else:
        print("Computer wins!")

def main():
    connection = connect_to_db()
    if connection is None:
        print("Failed to connect to the database.")
        return

    create_table(connection)
    
    user_name = input("Enter your name: ").capitalize()
    user_score = 0
    computer_score = 0

    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        while user_choice not in ["rock", "paper", "scissors"]:
            user_choice = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()

        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        
        if winner == "user":
            user_score += 1
            insert_result(connection, user_name)
        elif winner == "computer":
            computer_score += 1
            insert_result(connection, "Computer")

        display_result(user_choice, computer_choice, winner)
        print(f"Scores - {user_name}: {user_score}, Computer: {computer_score}")

        play_again = input("Do you want to play another round yes/no: ").lower()
        if play_again != "yes":
            break

    print("Thank you for playing!!!")
    connection.close()

if __name__ == "__main__":
    main()
