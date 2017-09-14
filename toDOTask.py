print "Welcome to the CreativeWoodpecker TODO app"
'''
tasks = ["Tadej", "Lorber","SmartNinja"]
name= "Tadej"
surname=" Lorber"

user= [name, surname]

print tasks [0]


'''
todo_list = []
todo_dictionary = {}
while True:
    task = raw_input("please enter TODO task")
    todo_list.append(task)

    complete = raw_input("Is this task finished? (yes/no):")

    if complete.lower() == "yes":
        todo_dictionary[task] = True
    else:
        todo_dictionary[task] = False


    print "Your task is " + task

    newTask = raw_input("Would you like to add another task?(yes/no)")

    if newTask.lower() == "no":
        break
todo_file = open("todo.txt" , "w+")
print ( "Zakljuceni taski: \n")
print "" \
      ""

for task in todo_dictionary:
    if todo_dictionary[task] == True:
        print task
        todo_file.write("-" + task + "\n")

print "Nezakljuceni taski"
print "" \
      ""
for task in todo_dictionary:
    if todo_dictionary[task] == False:
        print task
        todo_file.write("-" + task + "\n")

'''
for task in todo_list:
    print task;
'''
print "" \
      ""
print "Goodbay"
