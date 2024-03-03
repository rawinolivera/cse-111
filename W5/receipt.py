#Meets requirements. 
#I completed the assignment requirements and the test procedure.

import csv
from datetime import datetime

STORE_NAME = 'Savy Shop'
CURRENT_DATETIME = datetime.now()
INDEX_NUMBER = 0

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """

    dictionary = {}

    try:
        with open(filename, "rt") as csv_file:
            reader = csv.reader(csv_file)

            next(reader)
            for row_list in reader:
                if len(row_list) != 0:
                    key = row_list[key_column_index]
                    dictionary[key] = row_list

        
        return dictionary   

    except FileNotFoundError as e:
        print(f"Error: missing file\n{e}")
    except PermissionError as e:
        print(f"Error: You do not have permission to open this file\n{e}")
    except KeyError as e:
        print(f"Error: Non product match the code provided.\n'{e.args[0]}'")

def main():

    number_items = 0
    sub_total = 0.0
    TAX = 0.06
    I_NUMBER_INDEX = 0
    NAME_INDEX = 1
    INDEX_PRICE = 2
    products_dict = read_dictionary("products.csv",INDEX_NUMBER)
    print()
    print("* * * * * * * * * * * * * * *\n")
    print(f"   Welcome to *{STORE_NAME}*\n")
    print("* * * * * * * * * * * * * * *\n")
    print("Ordered Items:")
    print()

    file = "request.csv"

    try:

        with open(file, "rt") as request_file:
            reader = csv.reader(request_file)

            next(reader)
            for item in reader:
                p_key = item[I_NUMBER_INDEX]
                if p_key in products_dict:
                    product_data = products_dict[p_key]
                    product_name = product_data[NAME_INDEX]
                    product_price = float(product_data[INDEX_PRICE])
                    quantity = int(item[1])

                    number_items += quantity
                    sub_total += (float(product_price * quantity))
                    print(f"{product_name}: {quantity} --> {product_price}")
                else:
                        print(f"Error: unknown product ID in the {file} file")
                        print(f"'{p_key}'")

            sales_tax = sub_total * TAX
            total_amount = sub_total + sales_tax
            print()
            print(f"Total of Ordered Items: {number_items}\n")
            print(f"The subtotal: {sub_total:.4}")
            print(f"Sales Tax: {sales_tax:.2}\n")
            print(f"Total Due: {total_amount:.4}\n")
            print(f"Thank you for shopping at {STORE_NAME}!")
            print(f"We're always happy to serve you!")
            print(f"{CURRENT_DATETIME:%A %I:%M %p}\n")
    
    except FileNotFoundError as e:
        print(f"Error: missing file\n{e}")
    except PermissionError as e:
        print(f"Error: permission denied\n{e}")
    except KeyError as e:
        print(f"Error: unknown product ID in the {file} file\n'{e.args[0]}'")

if __name__ == "__main__":
    main()