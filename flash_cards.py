Deck = [("hat","gorro"),("dog","perro")]
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
    Deck.append(new_card)
    print(f"New Card {new_card} Added!")

def ReviewCards():
    global Deck
    for i in Deck:
        print(i)

def Main():
    global User_Response, Running
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
        else:
            print("Sorry Wrong input")
            User_Response = User_Input()


Main()