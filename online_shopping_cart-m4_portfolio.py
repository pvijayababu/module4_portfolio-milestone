# Step 1: Define the ItemToPurchase class where attributes are defined and values are initialized
class ItemToPurchase:
    def __init__(self, name="none", price=0.0, quantity=0):
        self.item_name = name
        self.item_price = price
        self.item_quantity = quantity
    
    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"*\t{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total_cost:.2f}\t\t*")
        return total_cost

# Step 2: Main section to prompt the user for two items and create two objects of the ItemToPurchase class
#         and the inputs from prompting is taken and initialized to the variables. Main function to add items to the cart and calculate the total bill
def main():
    # Creating a shopping cart list
    shopping_cart = []

    # Adding two items to the cart
    print("Enter the details of the first item:")
    name = input("Enter the item name: ")
    price = float(input("Enter the item price: "))
    quantity = int(input("Enter the item quantity: "))
    item1 = ItemToPurchase(name, price, quantity)
    shopping_cart.append(item1)

    print("\nEnter the details of the second item:")
    name = input("Enter the item name: ")
    price = float(input("Enter the item price: "))
    quantity = int(input("Enter the item quantity: "))
    item2 = ItemToPurchase(name, price, quantity)
    shopping_cart.append(item2)

    # Displaying items in the cart and calculating the total bill
    print()
    print('*********************************************************')
    print("*\tItems in your cart:\t\t\t\t*")
    total_bill = 0.0
    for item in shopping_cart:
        total_bill += item.print_item_cost()
    
    print('*\t\t\t\t\t\t\t*')
    print(f"*\tTotal bill amount: ${total_bill:.2f}\t\t\t*")
    print('*********************************************************')
if __name__ == "__main__":
    main()

