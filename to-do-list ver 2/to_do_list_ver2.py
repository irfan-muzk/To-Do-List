import json

#load json data into a python object
filename1 = "user_list.json"
with open(filename1, "r") as fp:
    load1 = json.load(fp)

#ask user to input the date
date1 = input("Enter the date of your to-do-list 'dd/mm/yyyy': ")

#add list if to-do-list doesn't exist
if date1 not in load1:
    load1[date1] = []
#display the existing list
else:
    result = load1[date1]
    print(
        "\nyou have already make to-do-list for this day."
        f"\nDate: {date1}"
        "\nto-do-list:"
        )
    for value in result[0]:
        print(f"- {value}")

    #ask user if they want to change their list
    while True:
        ask_user = input("do you want to change this list?"
                        "\nenter 'y' as yes or 'n' as no! ")
        if ask_user == "y":
            load1[date1] = []
            break
        elif ask_user == "n":
            print("thanks fo your input, you can access your list anytime")
            break
        else:
            print("please enter 'y' if you want to change your list, "
                  "or enter 'n' if you don't.")
            continue

#make new list to store user to-do-list input temporarily
new_list = []
#ask user to input their to-do-list for that day
while load1[date1] == []:
        todo_list = input("Enter your to-do-list (type 's' to stop!): ")
        if todo_list != "s":
            new_list.append(todo_list)
        else:
            break

#store user input to json file
if new_list != []:
    load1[date1].append(new_list)
    with open(filename1, "w") as json_file:
        json.dump(load1, json_file,
                indent=4,)
        
    #show the user their to-do-list and the date input
    print("\nYour to-do-list have been saved!")
    print(f"Date: {date1}")
    print("to-do-list:")
    for value in new_list:
        print(f"- {value}")