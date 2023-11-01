# this is really old code that I am ashamed of :(

import os
import json
from time import sleep as wait

from numberFormatter import formatNum

def printWithSpace(args=""):
    print(f"    {args}")


hello = """
    ████████╗ ██████╗       ██████╗  ██████╗     ██╗     ██╗███████╗████████╗    
    ╚══██╔══╝██╔═══██╗      ██╔══██╗██╔═══██╗    ██║     ██║██╔════╝╚══██╔══╝    
       ██║   ██║   ██║█████╗██║  ██║██║   ██║    ██║     ██║███████╗   ██║   
       ██║   ██║   ██║╚════╝██║  ██║██║   ██║    ██║     ██║╚════██║   ██║   
       ██║   ╚██████╔╝      ██████╔╝╚██████╔╝    ███████╗██║███████║   ██║   
       ╚═╝    ╚═════╝       ╚═════╝  ╚═════╝     ╚══════╝╚═╝╚══════╝   ╚═╝
       
    ████████████████████████████████████████████████████████████████████████║
    ╚═══════════════════════════════════════════════════════════════════════╝
"""
printWithSpace(hello)

filename = "todo.json"
todos = []
todosDone = []

def listTodos():
    os.system("cls")
    printWithSpace(hello)
    if len(todos) == 0 and len(todosDone) == 0:
        printWithSpace("There are currently no To-Do's in your To-Do list.")
    else:
        if len(todos) != 0:
            printWithSpace("Unfinished To-Do's:")
            for num, todo in enumerate(todos, 1):
                printWithSpace(f"{formatNum(num, 'lz', len(str(len(todos))) - len(str(num)))}. {todo}")
        if len(todosDone) != 0:
            printWithSpace()
            printWithSpace("Finished To-Do's:")
            for todoDone in todosDone:
                printWithSpace(f"· {todoDone}")

def prepareFile():
    # Prepare file to store data if there is no file "todo.json" yet
    with open(filename, "w") as f:
        json.dump(
            {
                "todo": [],
                "done": []
            }, f, indent=4)


def loadFile():
    with open(filename) as f:
        data = json.load(f)
        for todo in data["todo"]:
            todos.append(todo)
        for todoDone in data["done"]:
            todosDone.append(todoDone)
    wait(.5)

if os.path.exists(filename):
    printWithSpace("Loading your saved To-Do's...")
    # load file and make sure that it isn't corrupted
    try:
        loadFile()
        listTodos()
    except:
        prepareFile()
        printWithSpace()
        printWithSpace(f"WARNING: The file '{filename}' has been reset because it was corrupted or incorrectly modified.")
else:
    prepareFile()

def save():
    with open(filename, "w") as f:
        # Dump everything into file
        json.dump(
            {
                "todo": todos,
                "done": todosDone
            }, f, indent=4)

done = False
changes = False
while not done:
    printWithSpace()
    printWithSpace("[List] To-Do's, Add <todo>, Remove <todo>, Finish <todo>, [Delete] list, Quit")
    action = input("    > ")
    
    if action.lower() in ("quit", "q"):
        if changes:
            printWithSpace("Saving your To-Do's...")
            save()
            wait(.5)
        printWithSpace("Bye!")
        input()
        done = True
    
    elif action.lower() in ("list", "l"):
        listTodos()
    
    elif action.lower() in ("delete", "del"):
        if os.path.exists(filename):
            done2 = False
            while not done2:
                confirmation = input("    Do you want to delete all your To-Do's? (yes/no) ")
                if confirmation.lower() in ("yes", "y"):
                    todos, todosDone = [], []
                    os.remove(filename)
                    printWithSpace("Your To-Do list has been cleared.")
                    done2 = True
                    changes = False
                else:
                    break
        else:
            printWithSpace("You cannot delete your To-Do list, because it does not exist yet.")
            
    elif action.lower() in ("open", "o"):
        printWithSpace(f"Opening '{filename}'...")
        printWithSpace(f"WARNING: Only modify this, if you know what you are doing!")
        wait(1)
        os.system(f"notepad {filename}")
        todos = []
        todosDone = []
        loadFile()
        
    elif action.lower() != "":
        try:
            command, todo = action.split(maxsplit=1)
            command = command.lower()
            
            if command in ("add", "a"):
                todos.append(todo)
                printWithSpace(f"'{todo}' has been added to your To-Do list.")
                
            elif command in ("remove", "rem", "r"):
                try:
                    num = int(todo)
                    if 0 < num <= len(todos):
                        printWithSpace(f"'{todos[num - 1]}' has been removed from your To-Do list.")
                        todos.remove(todos[num - 1])
                    else:
                        printWithSpace(f"There is no To-Do with the index {num} in your To-Do list.")
                        
                except:
                    if todo in todos:
                        todos.remove(todo)
                        printWithSpace(f"'{todo}' has been removed from your To-Do list.")
                    elif todo in todosDone:
                        todosDone.remove(todo)
                        printWithSpace(f"'{todo}' has been removed from your To-Do list.")
                    else:
                        printWithSpace(f"'{todo}' could not be found in your To-Do list.")
                
            elif command in ("finish", "fin", "f"):
                try:
                    num = int(todo)
                    if 0 < num <= len(todos):
                        toChange = todos[num - 1]
                        printWithSpace(f"You have finished '{toChange}'.")
                        todos.remove(toChange)
                        todosDone.append(toChange)
                    else:
                        printWithSpace(f"There is no To-Do with the index {num} in your To-Do list.")
                        
                except:
                    if todo in todos:
                        todos.remove(todo)
                        todosDone.append(todo)
                        printWithSpace(f"You have finished '{todo}'.")
                    else:
                        printWithSpace(f"'{todo}' could not be found in your To-Do list.")
            else:
                printWithSpace("Error: Unknown command '%s'." % command)

            changes = True
            save()
            
        except:
            printWithSpace("Error: Unknown command '%s' or incorrect use of command." % action)
