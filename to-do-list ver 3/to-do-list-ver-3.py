import json

class ToDoList:
    def __init__(self, date):
        self.date = date
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def save_to_file(self, filename):
        with open(filename, "r") as fp:
            data = json.load(fp)
        data[self.date] = self.items
        with open(filename, "w") as fp:
            json.dump(data, fp, indent=4)

class User:
    def __init__(self, filename):
        self.filename = filename
        with open(filename, "r") as fp:
            self.data = json.load(fp)

    def get_todo_list(self, date):
        if date not in self.data:
            self.data[date] = []
        return self.data[date]

    def display_todo_list(self, date):
        todo_list = self.get_todo_list(date)
        if todo_list:
            print(f"\nYou have already made a to-do list for this day."
                   "\nDate: {date}\nTo-do list:")
            for item in todo_list:
                print(f"- {item}")
        else:
            print(f"\nYou have not made a to-do list for this day yet."
                   "\nDate: {date}")

    def edit_todo_list(self, date):
        while True:
            response = input("Do you want to change this list? (y/n): ")
            if response.lower() == "y":
                self.data[date] = []
                break
            elif response.lower() == "n":
                print("Thanks for your input. "
                      "You can access your list anytime.")
                break
            else:
                print("Please enter 'y' if you want to change your list, "
                      "or enter 'n' if you don't.")

    def make_todo_list(self, date):
        todo_list = self.get_todo_list(date)
        if todo_list:
            print(f"\nYou have already made a to-do list for this day."
                   "\nDate: {date}\nTo-do list:")
            for item in todo_list:
                print(f"- {item}")
            self.edit_todo_list(date)
        else:
            print(f"\nYou have not made a to-do list for this day yet."
                   "\nDate: {date}")
        new_items = []
        while True:
            item = input("Enter your to-do-list (type 's' to stop!): ")
            if item == "s":
                break
            else:
                new_items.append(item)
        if new_items:
            todo_list.extend(new_items)
            todo_list_obj = ToDoList(date)
            for item in todo_list:
                todo_list_obj.add_item(item)
            todo_list_obj.save_to_file(self.filename)
            print("\nYour to-do list has been saved!")
            print(f"Date: {date}\nTo-do list:")
            for item in new_items:
                print(f"- {item}")

# Example usage:
filename = "user_list.json"
user = User(filename)
date = input("Enter the date of your to-do-list 'dd/mm/yyyy': ")
user.make_todo_list(date)