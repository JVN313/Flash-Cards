Deck = {
    "DOG": "PERRO",
    "HAT": "GORRO"
}

Running = True

def User_Input():
    User_Prompt = input("To create a new card type 'NEW' Or Review Your Deck type 'View'?\n").upper()
    return User_Prompt

User_Response = User_Input()

def CreateCard():
    global Deck
    front = str(input("Type Front Word of the Card\n").upper())
    back = str(input("Type Back Word of the Card\n").upper())
    new_card = (front,back)
    Deck.update({front: back})
    print(f"New Card {new_card} Added!")

def ReviewCards():
    global Deck
    for i in Deck:
        print(f"{i}:{Deck.get(i)}")

def RemoveCard(card,deck):
    if card in deck:
        print(f"Card: ({card},{deck.get(card)}) Removed!\n")
        deck.pop(card)
    else:
        print("Sorry the card entered is not in the deck")

def Main():
    global User_Response, Running, Deck
    while Running:
        if User_Response == "NEW":
            CreateCard()
            User_Response = User_Input()
        elif User_Response == "VIEW":
            ReviewCards()
            User_Response = User_Input()
        elif User_Response == "EXIT":
            print("NOW EXITING PROGRAM")
            Running = False
        elif User_Response == "REMOVE":
            remove_input = input("Enter The Front Word Of THe Card You Wish To Remove.   ").upper()
            RemoveCard(remove_input,Deck)
            User_Response = User_Input()
        else:
            print("Sorry Wrong input")
            User_Response = User_Input()


Main()