class GameObject:
    name = ""
    appearance = ""
    feel = ""
    smell = ""

    def __init__(self, name, appearance, feel, smell):
        self.name = name
        self.appearance = appearance
        self.feel = feel
        self.smell = smell

    def look(self):
        return f"You see a {self.appearance} {self.name}.\n"
    
    def touch(self):
        return f"You feel the {self.feel} {self.name}.\n"
    
    def sniff(self):
        return f"You smell the {self.smell} {self.name}.\n"
    
# test the GameObject class    
""" game_object = GameObject("knife", "sharp", "cold", "metallic")
print(game_object.look())
print(game_object.touch())
print(game_object.sniff()) """

class Room:
    escape_code = 0
    game_objects = []
    def __init__(self, escape_code, game_objects):
        self.escape_code = escape_code
        self.game_objects = game_objects

    def check_code(self, code):
        print(f"Checking code: {code}")
        if code == self.escape_code:
            return "You escaped the room!"
        else:
            return "Wrong code. Try again."
    
    def get_game_object_names(self):
        return [obj.name for obj in self.game_objects]
    
# test the Room class
""" game_object2 = GameObject("key", "rusty", "rough", "metallic")
game_object3 = GameObject("door", "wooden", "smooth", "freshly cut wood")
test_room = Room(1234, [game_object, game_object2, game_object3])
print(test_room.get_game_object_names())
print(test_room.check_code(1233))
print(test_room.check_code(1234)) """

class Game:
    def __init__(self):
        self.attempts = 0
        self.room = Room (234, [])
        """ in reality, to make this game more functional, we would need to have
        a way to add game objects to the room, like from a database. """
    def create_objects(self):
        self.room.game_objects.append(GameObject("knife", 
                                                 "sharp", 
                                                 "cold", "metallic"))
        self.room.game_objects.append(GameObject("key", "rusty", "rough", 
                                                 "suspiciously stinky"))
        self.room.game_objects.append(GameObject("door", "wooden door to room 2", 
                                                 "smooth", "freshly cut wood"))
        self.room.game_objects.append(GameObject("window", 
                                                 "glass with the number 3 written on it in crayon", 
                                                 "smooth", "freshly cut wood"))
        self.room.game_objects.append(GameObject("table", "wooden", 
                                                 "smooth but for 4 large scratches in it", 
                                                 "freshly cut wood"))
    def get_room_prompt(self):
        prompt = "enter the 3 digit code or choose an object to inspect:\n"
        names = self.room.get_game_object_names()
        index = 1
        for name in names:
            prompt += f"{index}. {name}\n"
            index += 1
        return prompt
    
    def take_turn(self):
        prompt = self.get_room_prompt()
        selection = int(input(prompt))
        if selection >= 1 and selection <= 5:
            self.select_object(selection - 1)
            self.take_turn()
        else:
            is_code_correct = self.guess_code(selection)
            if is_code_correct:
                print("Congratulations, you win!")
            else:
                if self.attempts == 3:
                    print("Game over, you ran out of guesses. Better luck next time!")
                else:
                    print(f"Incorrect, you have used {self.attempts}/3 attempts.\n")
                    self.take_turn()

    def get_object_interaction_string(self, name):
        return f"How do you want to interact with the {name}?\n1. Look\n2. Touch\n3. Smell\n"

    def select_object(self, index):
        selected_object = self.room.game_objects[index]
        prompt = self.get_object_interaction_string(selected_object.name)
        interaction = input(prompt)
        clue = self.interact_with_object(selected_object, interaction)
        print(clue)

    def interact_with_object(self, object, interaction):
        if interaction == "1":
            return object.look()
        elif interaction == "2":
            return object.touch()
        else:
            return object.sniff()
    
    def guess_code(self, code):
        if self.room.check_code(code):
            return True
        else:
            self.attempts += 1
        return False
    
class RoomTests:
    def __init__(self):
        self.room_1 = Room(111, [
            GameObject(
                "Sweater",
                "It's a blue sweater that had the number 12 switched on it.",
                "Someone has unstitched the second number, leaving only the 1.",
               "The sweater smells of laundry detergent."),
            GameObject(
                "Chair", 
                "It's a wooden chair with only 3 legs.",
                "Someone had deliberately snapped off one of the legs.",
                "It smells like old wood.")
        ])
        self.room_2 = Room(222, [])

    def test_check_code(self):
        print(self.room_1.check_code(111) == True)
        print(self.room_1.check_code(222) == False)

    def test_get_game_object_names(self):
        print(self.room_1.get_game_object_names() == ["Sweater", "Chair"])
        print(self.room_2.get_game_object_names() == [])

# run the room tests
""" room_tests = RoomTests()
room_tests.test_check_code()
room_tests.test_get_game_object_names() """


game = Game()
game.take_turn()

