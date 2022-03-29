import ChromeDBFunctions as chromedb

try:
    chromedb.clear()
    chromedb.start_up()
    chromedb.logging_data("log.txt", 5)
    while True:
        chromedb.choices()
        choice = input("\nPlease enter one of the corresponding numbers: ")
        if choice == "1":
            chromedb.view_data("backup_config.json")
            chromedb.logging_data("log.txt", 1)
        elif choice == "2":
            chromedb.appending_the_list("backup_config.json")
            chromedb.logging_data("log.txt", 2)
        elif choice == "3":
            chromedb.delete_data("backup_config.json")
            chromedb.logging_data("log.txt", 3)
        elif choice == "4":
            chromedb.logging_data("log.txt", 4)
            break
        else:
            print("You did not press a corresponding number, please try again.")


except KeyboardInterrupt:
    pass
