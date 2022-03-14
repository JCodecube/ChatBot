print("!!This is just a prototype i will be updating this when i can!! would you like to start the game? Yes or No")
GameStarter = input()


def Game():
    print("Bot: Hello!")

    PlayerInput1 = input()

    if PlayerInput1 == "Hi" or "Hello" or "Hey": {
        print("Bot: What is your name?")
    }

    PlayerInput2 = input()
    print("Bot: That is a very nice name " + PlayerInput2 + "! My name is Bot. How are you?")
    PlayerInput3 = input()
    if PlayerInput3 == "Good": {
        print("That is nice to hear! But i need to go bye!")
    }
    if PlayerInput3 == "Bad": {
        print("That is sad to hear, but remember! When the day feels like its going bad the only way is up. But i need to go bye!")
    }
    print("Bot has left the chat!")
    print("Game over! Restart or Close?")
    GameCloser = input()
    if GameCloser == "Restart": Game()
    if GameCloser == "Close": pass

if GameStarter == "Yes": Game()
if GameStarter == "No": pass