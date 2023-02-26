filename = "user_list.txt"
with open(filename, "a") as f:

    #ask user to input the date of their to-do-list
    date = input("Enter the date of your to-do-list 'dd/mm/yyyy': ")
    f.write(f"Date: {date}\nyour To-Do-List for today: \n")

    user_list = []
    while True:
        #ask user to input their to-do-list for that day
        todo_list = input("Enter your to-do-list (type 's' to stop!): ")
        if todo_list == "s":
            break
        else:
            user_list.append(todo_list)
            f.write(f"- {todo_list}\n")
            continue

    f.write("\n")

with open(filename, "r") as r:
    load = r.read()
    print(f"this is my file: \n{load}")

#show the user to-do-list and the date
print(f"\nDate: {date}")
print("Your to-do-list for today:")
for value in user_list:
    print(f"- {value}")
