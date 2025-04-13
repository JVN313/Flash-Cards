Deck = [("hat","gorro"),("dog","perro")]
User_Prompt = input("To create a new card type 'NEW' Or Review Your Deck type 'View'?\n").upper()
Running = True

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
    global User_Prompt, Running
    while Running:
        if User_Prompt == "NEW":
            CreateCard()
            User_Prompt = input("To create a new card type 'NEW' Or Review Your Deck type 'View'?\n").upper()
        elif User_Prompt == "VIEW":
            ReviewCards()
            User_Prompt = input("To create a new card type 'NEW' Or Review Your Deck type 'View'?\n").upper()
        elif User_Prompt == "EXIT":
            print("NOW EXITING PROGRAM")
            Running = False
        else:
            print("Sorry Wrong input")
            User_Prompt = input("To create a new card type 'NEW' Or Review Your Deck type 'View'?\n").upper()


Main()