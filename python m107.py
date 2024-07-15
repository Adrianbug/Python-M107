import random

# Define a list of video games with their clues and answers
video_games = [
    {
        'name': 'The Legend of Zelda: Breath of the Wild',
        'clue': 'Explore the vast world of Hyrule in this open-world action-adventure game.',
        'options': ['The Legend of Zelda: Breath of the Wild', 'Super Mario Odyssey', 'Dark Souls III', 'Skyrim'],
        'answer': 'The Legend of Zelda: Breath of the Wild'
    },
    {
        'name': 'Grand Theft Auto V',
        'clue': 'This game features an open-world environment where players can engage in various criminal activities.',
        'options': ['Red Dead Redemption 2', 'Grand Theft Auto V', 'Watch Dogs 2', 'Saints Row IV'],
        'answer': 'Grand Theft Auto V'
    },
    {
        'name': 'The Witcher 3: Wild Hunt',
        'clue': 'Play as Geralt of Rivia in this critically acclaimed RPG based on a series of Polish novels.',
        'options': ['Dark Souls III', 'Dragon Age: Inquisition', 'The Witcher 3: Wild Hunt', 'Final Fantasy XV'],
        'answer': 'The Witcher 3: Wild Hunt'
    }
    # Add more video games with clues and answers as needed
]

def play_game():
    print("Welcome to the Video Game Guessing Game!")
    score = 0
    random.shuffle(video_games)  # Shuffle the order of games
    
    for game in video_games:
        print("\nClue: " + game['clue'])
        print("Choose from the following options:")
        for i, option in enumerate(game['options']):
            print(f"{i + 1}. {option}")
        
        # Get user's guess
        while True:
            try:
                guess = int(input("Enter your choice (1-4): "))
                if 1 <= guess <= 4:
                    break
                else:
                    print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        user_choice = game['options'][guess - 1]
        
        # Check if the user's guess is correct
        if user_choice == game['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {game['answer']}")
    
    print(f"\nGame Over! Your final score is: {score}/{len(video_games)}")

# Start the game
play_game() 