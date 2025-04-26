import glob

def CreatePage():
    page_title = input("Enter Name Of New Note Page:  ").upper()
    page = open(f"{page_title}.txt","w")
    page.close()
    print(f"New file '{page_title}' created!\n")

def ListNotes():
    for i in glob.glob('*.txt'):
        print(i)

def EditFiles(name):
    test = glob.glob('*.txt')
    name = str(name) + ".txt"
    working = True
    while working:
        if name not in test:
            print("Sorry File entered does not exist!\n")
            name = input("Enter Name of file:   ").upper() + ".txt"
        else:
            print(name)
            working = False