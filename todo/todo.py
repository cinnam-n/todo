# Equiv. startup program

import os
import time

# Files

tempPath = __file__.split("\\")
dir = ""
for i in range(0, len(tempPath)-1):
    dir += tempPath[i] + "\\"

print(dir)

os.system(f"{dir}time.bat") # Needs to be run in advance of timeFile opening
setupFile = open(f"{dir}setup.txt", "r")
timeFile = open(f"{dir[:-5]}time.txt", "r")
listFile = open(f"{dir}list.txt", "r")

setupContent = setupFile.readlines()
timeContent = timeFile.readlines()
listContent = listFile.readlines()

# Var (idk if this is needed)

name = ""

# Main

if setupContent[0] == "0":

    # Start setup
    print("This is your first run of todo!")
    setupFile = open(f"{dir}setup.txt", "w")

    name = input("Enter name to use: ")
    setupFile.write(f"{name}\n")
    setupContent = setupFile.readlines() # Needed to replace "0" with "{name}"

# Normal run

name = setupContent[0].replace("\n", "")

currentHour = str(timeContent[0])[:-2]
if int(currentHour) < 12:
    print(f"Good morning, {name}!\n")
else:
    print(f"Good evening, {name}!\n")
    
loop = True
while loop:
    print("Your to-do list:")
    for task in range(0, len(listContent)):
        string = f"{task+1} : {listContent[task].replace("\n", "")}"
        if task+1 < 10: string = "0" + string
        print(string)

    action = input("\nAdd task, Remove task, or Exit? [a/r/e]: ")
    print("")

    match action:

        case "a":
            index = int(input("Enter list index: "))
            newTask = input("Enter new task: ")
            listContent.pop(index-1)
            listContent.insert(index-1, newTask+"\n")

        case "r":
            index = int(input("Enter list index: "))
            confirm = input(f"\n <!> Are you sure you want to remove task {index}? \n Type \"DELETE\" to confirm: ")
            print("Deleting index...")
            listContent.pop(index-1)
            listContent.append("\n")

        case "e":
            print("Exiting...")
            loop = False

        case _:
            print("That command isn't recognised!")

    print("\n\n\n")

listFile = open(f"{dir}list.txt", "w")
print(listContent)
for j in range(0, len(listContent)):
    listFile.writelines(f"{listContent[j]}")
listFile.close()
