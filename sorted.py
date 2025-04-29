import sqlite3

# Function to initialize the database
def initialize_database():
    conn = sqlite3.connect('words.db')  # Connect to the database (or create it if it doesn't exist)
    cursor = conn.cursor()
    # Create a table to store words if it doesn't already exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS words (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word TEXT NOT NULL UNIQUE
        )
    ''')
    conn.commit()
    conn.close()

# Function to insert a word into the database
def insert_word(word):
    conn = sqlite3.connect('words.db')
    cursor = conn.cursor()
    # Insert the word into the database
    cursor.execute('INSERT OR IGNORE INTO words (word) VALUES (?)', (word,))
    conn.commit()
    conn.close()

# Function to retrieve and display all words in alphabetical order
def display_words():
    conn = sqlite3.connect('words.db')
    cursor = conn.cursor()
    # Retrieve all words sorted alphabetically
    cursor.execute('SELECT word FROM words ORDER BY word ASC')
    words = cursor.fetchall()
    conn.close()

    # Display the words
    if words:
        print("\nSorted words:")
        for word in words:
            print(word[0])
    else:
        print("\nNo words in the database.")

# Main function
def main():
    initialize_database()  # Ensure the database is set up

    while True:
        # Ask the user to input a word
        word = input("Enter a word (or type 'exit' to finish): ").strip()

        # Exit the loop if the user types 'exit'
        if word.lower() == 'exit':
            break

        # Insert the word into the database
        insert_word(word)

    # Display all words in alphabetical order
    display_words()

if __name__ == "__main__":
    main()
