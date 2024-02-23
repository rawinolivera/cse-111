import csv

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

    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)

        next(reader)
        for row_list in reader:
            if len(row_list) != 0:
                key = row_list[key_column_index]
                dictionary[key] = row_list

    
    return dictionary   

def main():

    I_NUMBER_INDEX = 0
    NAME_INDEX = 1
    INDEX_PRICE = 2
    products_dict = read_dictionary("products.csv",INDEX_NUMBER)

    print(products_dict)

    
    with open("request.csv", "rt") as request_file:
        reader = csv.reader(request_file)

        next(reader)
        print("Request Item List:")
        for item in reader:
            p_key = item[I_NUMBER_INDEX]
            if p_key in products_dict:
                product_data = products_dict[p_key]
                product_name = product_data[1]
                product_price = product_data[2]
                quantity = int(item[1])
                print(f"{product_name}: {quantity} --> {product_price}")

if __name__ == "__main__":
    main()