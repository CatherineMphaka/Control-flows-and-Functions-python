#defining the function calculate_discount which has the parameters:price & discount_percent
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price - (price * (discount_percent / 100))
        return discounted_price
    else:
        return price
#return price: When a function encounters a return statement, it immediately exits the function and passes back the specified value (price in this case) to the caller. 
#This means that the function calculate_discount returns the final calculated price to the code that called it. This allows the calling code to store the result in
# a variable or use it in other calculations.
#print(price): On the other hand, print(price) simply displays the value of price to the console. 
#However, it does not pass the value back to the caller like return does.

def main():
    original_price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(original_price, discount_percent)
    
    if final_price != original_price:
        print("Final price after applying discount: ${:.2f}".format(final_price))
    else:
        print("No discount applied. Final price: ${:.2f}".format(final_price))
#${:.2f}this is a format specifier used to format floating-point numbers
if __name__ == "__main__":
    main()
# if __name__ == "__main__": checks whether the script is being run directly by the Python interpreter (i.e., as the main script). If it is, the code block beneath it will be executed.
# This is often used to define a block of code that should only run when the script is executed directly and not when it is imported as a module into another script.
