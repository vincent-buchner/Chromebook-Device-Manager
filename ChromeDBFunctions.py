import json
import art
import datetime
import os


# Should these functions be within a class?

# Clears the command prompt
def clear():
    os.system("cls" if os.name == "nt" else "clear")


# A function that writes to the .json file
def write_json(data, filename="backup_config.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


# Start up ASCII
def start_up():
    art.tprint("THE    DATABASE")
    print("\t * ~ *    C R E A T E D    B Y :   V I N C E N T   B U C H N E R    * ~ *\n")


# Displays the options the users have
def choices():
    print("\n\n\t\t\t~ + + \t(1) View Data\t + + ~")
    print("\t\t\t~ + + \t(2) Append Data\t + + ~")
    print("\t\t\t~ + + \t(3) Delete Data\t + + ~")
    print("\t\t\t~ + + \t(4) Exit\t + + ~")


# Prints the data to the screen
def view_data(file: str):
    with open(file, "r") as f:
        data = json.load(f)
        for i, item in enumerate(data):
            name = item["name"]
            chromebook = item["chromebook"]
            check_out = item["time&date"]
            print(f"Index Number: {i}")
            print(f"Name : {name}")
            print(f"Chromebook : {chromebook}")
            print(f"Time Of Checkout: {check_out} ")
            print("\n\n")


# Deletes an index from the .json file
def delete_data(file: str):
    clear()
    view_data(file)
    new_data = []
    with open(file, "r") as f:
        data = json.load(f)
        data_length = len(data) - 1
    print("Which index number would you like to delete?")
    delete_option = input(f"Select a number 0-{data_length}: ")
    i = 0
    for entry in data:
        if i == int(delete_option):
            i = i + 1
            pass
        else:
            new_data.append(entry)
            i = i + 1

    with open(file, "w") as f:
        json.dump(new_data, f, indent=4)

    print("Index was deleted!")


# Appends the .json file
def appending_the_list(file: str):
    clear()
    start_up()
    print("\nPress Ctrl + C to quit application")
    username = input("Please enter the name: ")
    password = input("Please enter the Chromebook's ID: ")
    check_out = time_and_date()

    with open(file) as json_file:
        data = json.load(json_file)
        keys = {"name": username, "chromebook": password, "time&date": check_out}
        data.append(keys)

    write_json(data)
    print("\nIndex was added!\n")


# Returns the current time and date
def time_and_date():
    temp_date = datetime.date.today()
    date = temp_date.strftime("%b-%d-%Y")

    temp_time = datetime.datetime.now()
    time = temp_time.strftime("%H:%M:%S")

    return f"Check Out Time: {time} {date}"


# Logs the th info on to a .txt file
def logging_data(file: str, data_choice: int):
    with open(file, "a") as f:
        if data_choice == 1:
            f.write(time_and_date() + "\n")
            f.write("Viewing database...\n")
        elif data_choice == 2:
            f.write(time_and_date() + "\n")
            f.write("Appending database...\n")
        elif data_choice == 3:
            f.write(time_and_date() + "\n")
            f.write("Removing index from database...\n")
        elif data_choice == 4:
            f.write(time_and_date() + "\n")
            f.write("Exiting program...\n\n")
        elif data_choice == 5:
            f.write(time_and_date() + "\n")
            f.write("Running program...\n")

        else:
            print(f"There was an issue logging the data to {file}")
