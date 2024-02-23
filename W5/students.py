import csv

def read_dictionary(filename):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    stundents_dict = {}

    with open("students.csv", "rt") as csv_file:

        reader = csv.reader(csv_file)
        next(reader)

        for row_list in reader:
            id = row_list[0]
            name= row_list[1]
            stundents_dict[id] = [name]

    return stundents_dict


def main():

    dictionary = read_dictionary("students.csv")

    student_number = str(int(input("Please enter the Student Number: ")))    

    if student_number in dictionary:

        student_name = dictionary[student_number]

        print(student_name)

    else:
        print("No such student")

if __name__ == "__main__":
    main()