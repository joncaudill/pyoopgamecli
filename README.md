# pyoopgamecli

A simple text-based escape room game written in Python using object-oriented programming principles.

## Purpose

A simple experiment to test writing simple text based games.   To be used as a personal reference for later

## Features

- Explore a room filled with interactive objects.
- Inspect objects by looking, touching, or smelling them for clues.
- Guess the escape code to win the game.
- Basic test suite for core classes.

## Getting Started

### Prerequisites

- Python 3.x

### Running the Game

Clone the repository:

```sh
git clone https://github.com/joncaudill/pyoopgamecli.git
cd pyoopgamecli
```

Run the game:

```sh
python main.py
```

### How to Play

- You will be presented with a list of objects and prompted to enter a 3-digit code or choose an object to inspect.
- Enter the number corresponding to an object to interact with it.
- Choose how to interact: look, touch, or smell.
- Use the clues to guess the correct escape code.

## Project Structure

- `main.py` - Main game logic and class definitions.

## Testing

Basic tests for the `Room` class are included at the bottom of `main.py` (commented out). Uncomment to run:

```python
room_tests = RoomTests()
room_tests.test_check_code()
room_tests.test_get_game_object_names()
```

## License

This was created for educational purposes