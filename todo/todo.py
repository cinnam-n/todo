# Equiv. startup program

import os
import time

path = "C:\\cinnastartup\\todo\\"

os.system("C:\\cinnastartup\\todo\\time.bat")
timeFile = open("C:\\cinnastartup\\todo\\time.txt", "r")
listFile = open("C:\\cinnastartup\\todo\\list.txt", "r")
# For some reason, if you don't put the entire path to the file, python goes a little schizo.

time.sleep(0.001)

currentHour = timeFile.read()
if int(currentHour) < 12:
    print("Good morning, James!\n")
else:
    print("Good evening, James!\n")

tasks = listFile.readlines()
    
loop = True
while loop:
    print("Here are your tasks as of now:")
    for l in range(0, len(tasks)):
        string = f"{l+1} : {tasks[l].replace("\n", "")}"
        if l+1 < 10: string = "0" + string
        print(string)

    action = input("\nAdd task, Remove task, or Exit? [a/r/e]: ")
    print("")

    match action:

        case "a":
            index = int(input("Enter list index: "))
            newTask = input("Enter new task: ")
            tasks.pop(index-1)
            tasks.insert(index-1, newTask)
            tasks.append("")

        case "r":
            index = int(input("Enter list index: "))
            confirm = input(f"\n <!> Are you sure you want to remove task {index+1}? \n Type \"DELETE\" to confirm: ")
            print("Deleting index...")
            tasks.pop(index-1)

        case "e":
            print("Exiting...")
            loop = False

        case _:
            print("That command isn't recognised!")

    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

listFile = open("C:\\cinnastartup\\todo\\list.txt", "w")
for j in range(0, 16):
    if tasks[j]:
        listFile.writelines(f"{tasks[j]}")
    else:
        listFile.writelines("\n")
listFile.close()
