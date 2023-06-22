def get_valid_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculate_total_cost():
    # Get the original price, discount rate, and sales tax rate
    original_price = get_valid_input("Enter the original price of the item: $")
    discount_rate = get_valid_input("Enter the discount rate (%): ")
    sales_tax_rate = get_valid_input("Enter the sales tax rate (%): ")

    # Calculate the sale price
    sale_price = original_price * (1 - discount_rate / 100)
    
    # Calculate total tax
    total_tax = sale_price * (sales_tax_rate / 100)

    # Calculate total cost
    total_cost = sale_price + total_tax

    # Print the sale price, total tax, and total cost
    print(f"The sale price of the item is: ${sale_price:.2f}")
    print(f"The total tax on the item is: ${total_tax:.2f}")
    print(f"The total cost after tax is: ${total_cost:.2f}")

if __name__ == "__main__":
    calculate_total_cost()
