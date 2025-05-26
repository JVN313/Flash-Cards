import glob, os

Decks = {"SPANISH":{"Hello":"Hola", "Cat":"Gato", "Dog":"Perro"},
         "DUTCH":{"Hello":"Hallo", "Car":"Auto", "Home":"Thuis"},
         "FRENCH":{"Yes": "Oui", "Want": "Veux", "Who":"Qui"}}

def CreateDeck():
    global Decks
    working = True
    while working:
        deck_name = str(input("Enter Name Of New Deck:   ").upper())
        if deck_name not in Decks:
            Decks.update({deck_name:{}})
            working = False
        else:
            print("Deck Name Already Exists!")

def CreateCard():#THE DECK TO ADD THE CARD MUST BE SELECTED FIRST
    front = str(input("Type Front Word of the Card\n").upper())
    back = str(input("Type Back Word of the Card\n").upper())
    new_card = (front,back)
    print(f"New Card {new_card} Added!\n")
    return {front:back}

def ReviewCards(deck):#DECK NAME MUST BE IN CAPS
    global Decks
    for i in Decks[deck]:
        print(f"{i}:{Decks[deck].get(i)}")

def RemoveCard(card,deck):
    global Decks
    if deck in Decks and card in Decks[deck]:
        print(f"Card: ({card},{Decks[deck].get(card)}) Removed!\n")
        Decks[deck].pop(card)
    else:
        print("Sorry the card entered is not in the deck, or Deck does not exist\n")

def DeleteDeck(deck):
    global Decks
    if deck in Decks:
        del Decks[deck]
    else:
        print("Deck does not exist\n")

CreateDeck()
print(Decks)