# Abbas Salim
# 2026396
class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${int(self.item_price)} = ${self.item_quantity * int(self.item_price)}")

if __name__ == "__main__":
    # Prompt the user for two items
    print("Item 1")
    item_name_1 = input("Enter the item name:\n")
    item_price_1 = float(input("Enter the item price:\n"))
    item_quantity_1 = int(input("Enter the item quantity:\n"))

    print("\nItem 2")
    item_name_2 = input("Enter the item name:\n")
    item_price_2 = float(input("Enter the item price:\n"))
    item_quantity_2 = int(input("Enter the item quantity:\n"))

    # Create two ItemToPurchase objects
    item1 = ItemToPurchase(item_name_1, item_price_1, item_quantity_1)
    item2 = ItemToPurchase(item_name_2, item_price_2, item_quantity_2)

    # Output the total cost
    print("\nTOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()
    total_cost = (item1.item_quantity * int(item1.item_price)) + (item2.item_quantity * int(item2.item_price))
    print(f"\nTotal: ${total_cost}")
