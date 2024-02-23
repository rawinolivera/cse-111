import csv
from datetime import datetime

def read_dictionary(products, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters:
        products: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    products_dict = {}
    with open(products, "rt") as products_file:
        reader = csv.reader(products_file)
        next(reader)
        for row in reader:
            key = row[key_column_index]
            products_dict[key] = row
    return products_dict

def calculate_totals(order, products_dict):
    """Calculate the number of items, subtotal, sales tax,
    and total for the given order.

    Parameters:
        order: the name of the CSV file containing the order.
        products_dict: the dictionary containing product information.
    """
    try:
        with open(order, "rt") as order_file:
            items_count = 0
            subtotal = 0.0
            sales_tax_rate = 0.06 
            
            for row in csv.reader(order_file):
                product_number = row[0]
                
                if product_number in products_dict:
                    product_info = products_dict[product_number]
                    quantity = int(row[1])
                    price = float(product_info[2])
                    
                    items_count += quantity
                    subtotal += quantity * price
                else:
                    print(f"Error: unknown product ID in the {order} file")
                    print(f"'{product_number}'")

            sales_tax = subtotal * sales_tax_rate
            total = subtotal + sales_tax

            return items_count, subtotal, sales_tax, total

    except FileNotFoundError as e:
        print(f"Error: missing file\n{e}")
    except PermissionError as e:
        print(f"Error: permission denied\n{e}")
    except KeyError as e:
        print(f"Error: unknown product ID in the {order} file\n'{e.args[0]}'")

def print_receipt(items_count, subtotal, sales_tax, total):
    """Print the receipt with the given details.

    Parameters:
        items_count: the number of items in the order.
        subtotal: the subtotal amount.
        sales_tax: the sales tax amount.
        total: the total amount.
    """
    print("\nInkom Emporium\n")

    
    with open('products.csv', "rt") as products_file:
        store_name = csv.reader(products_file).__next__()[1]
        print(store_name)

    print("\nOrdered Items:")
    

    print("\nNumber of Items:", items_count)
    print("Subtotal: ${:.2f}".format(subtotal))
    print("Sales Tax: ${:.2f}".format(sales_tax))
    print("Total: ${:.2f}".format(total))
    
    print("\nThank you for shopping at the Inkom Emporium.")
    
    current_date_and_time = datetime.now()
    print(current_date_and_time.strftime("%a %b %d %H:%M:%S %Y"))

def main():
    try:
        products_dict = read_dictionary('products.csv', 0)
        order_totals = calculate_totals('request.csv', products_dict)

        if order_totals:
            items_count, subtotal, sales_tax, total = order_totals
            print_receipt(items_count, subtotal, sales_tax, total)

    except FileNotFoundError as e:
        print(f"Error: missing file\n{e}")
    except PermissionError as e:
        print(f"Error: permission denied\n{e}")

if __name__ == "__main__":
    main()
