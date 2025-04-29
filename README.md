# Word Sort Project

This project is a simple Python application that manages a SQLite database of words. It allows users to insert words into the database and display them in alphabetical order.

## Files

- **sorted.py**: Contains the main logic for managing the SQLite database. It includes functions to initialize the database, insert words, and display words in alphabetical order.
  
- **Dockerfile**: Contains instructions to build a Docker image for the project. It sets up the working directory, installs dependencies, and defines the command to run the application.

- **requirements.txt**: Lists the Python dependencies required for the project.

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd wordsort
   ```

2. **Install dependencies**:
   You can install the required dependencies using pip:
   ```
   pip install -r requirements.txt
   ```

3. **Run the application**:
   Execute the following command to run the application:
   ```
   python sorted.py
   ```

## Docker Instructions

To build and run the Docker container, follow these steps:

1. **Build the Docker image**:
   ```
   docker build -t wordsort .
   ```

2. **Run the Docker container**:
   ```
   docker run -it wordsort
   ```

## Usage

- When prompted, enter a word to add it to the database.
- Type 'exit' to finish entering words and display all words in alphabetical order.