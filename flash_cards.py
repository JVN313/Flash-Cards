import glob, os

Deck = {
    "DOG": "PERRO",
    "HAT": "GORRO"
}

Running = True

def User_Input():
    User_Prompt = input("To create a new card type 'NEW' / Review Your Deck type 'View'/ Remove a card type 'REMOVE' / To exit program type 'Exit'\n").upper()
    return User_Prompt

User_Response = User_Input()

def CreateCard():
    global Deck
    front = str(input("Type Front Word of the Card\n").upper())
    back = str(input("Type Back Word of the Card\n").upper())
    new_card = (front,back)
    Deck.update({front: back})
    print(f"New Card {new_card} Added!\n")

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
#Start of note taking mode
def CreatePage():
    page_title = input("Enter Name Of New Note Page:  ").upper()
    page = open(f"{page_title}.txt","w")
    page.close()
    print(f"New File '{page_title}' created!\n")

def ListNotes():
    for i in glob.glob("*.txt"):
        print(i)

def EditFiles(file_name):
    test = glob.glob("*.txt")
    file_name = str(file_name) + ".txt"
    file_edit = ""
    file_choice = ""
    file_append = "a"
    working = True
    
    while working:
        if file_name not in test:
            print("Sorry file does not exist!\n")
            file_name = input("Enter Name Of File:  ").upper() + ".txt"
        else:
            print(f"Accessing File '{file_name}'!\n")
            working = False
    
    working = True
    while working:
        file_choice = input("To Read The File Enter 'R'/To Add to file enter 'A':\n").lower()
        if file_choice == "a":
            file_edit = open(f"{file_name}", "a")
            file_append = input("Enter What You Wish To add To THe file:\n")
            file_edit.write(f"\n{file_append}")
            file_edit.close()
            print("Edits Added!\n")
            working= False
        elif file_choice == "r":
            file_edit = open(f"{file_name}","r")
            print(file_edit.read())
            file_edit.close()
            working= False
        else:
            print("Sorry Incorrect Input!\n")

def RemoveFile(file_name):
    file_name = file_name.upper()
    if os.path.exists(f"{file_name}.txt"):
        os.remove(f"{file_name}.txt")
        print(f"{file_name} Removed!\n")
    else:
        print("The file does not exist\n")

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
            #BEGINNING OF NOTETAKING OPTIONS
        elif User_Response == "NEW NOTE":
            CreatePage()
            User_Response = User_Input()
        elif User_Response == "VIEW NOTES":
            ListNotes()
            User_Response = User_Input()
        elif User_Response == "EDIT":
            file = input("Enter File Name:  ").upper()
            EditFiles(file)
            User_Response = User_Input()
        elif User_Response == "DELETE NOTE":
            file = input("Enter File Name:  ").upper()
            RemoveFile(file)
            User_Response = User_Input()
        else:
            print("Sorry Wrong input")
            User_Response = User_Input()


Main()