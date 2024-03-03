from datetime import datetime

current_datetime = datetime.now().strftime("%a %b %d %H:%M:%S %Y")

def add_new_entry(current_datetime, subject, description):
    with open('entries.txt', 'a') as file:
        file.write(f"{current_datetime} -> SUBJECT: {subject} DESCRIPTION: {description}\n")


def main():
    title_entry = str(input("Task Completed: "))
    description_entry = str(input("Describe detaily the achievement completed: "))

    add_new_entry(current_datetime, title_entry, description_entry)

    print(f"The entry was registered, check your file to see the update of your records.")
    


if __name__ == "__main__":
    main()