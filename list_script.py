import unicodedata

class Inventory:
    def __init__(self):
        self.items = []
        self.load_initial_items()

    def load_initial_items(self):
        initial_items = [
            {'name': 'Mechanical Keyboard', 'quantity': 15, 'price': 250.00, 'category': 'Peripherals'},
            {'name': 'Gaming Mouse', 'quantity': 30, 'price': 150.00, 'category': 'Peripherals'},
            {'name': '24" Monitor', 'quantity': 10, 'price': 800.00, 'category': 'Monitors'},
            {'name': 'Gaming Chair', 'quantity': 5, 'price': 1200.00, 'category': 'Furniture'},
            {'name': 'Headset', 'quantity': 25, 'price': 200.00, 'category': 'Peripherals'},
            {'name': '1TB SSD', 'quantity': 20, 'price': 500.00, 'category': 'Storage'},
            {'name': 'Intel i7 Processor', 'quantity': 8, 'price': 1500.00, 'category': 'Hardware'},
            {'name': 'RTX 3060 Graphics Card', 'quantity': 6, 'price': 2500.00, 'category': 'Hardware'},
            {'name': '650W Power Supply', 'quantity': 12, 'price': 400.00, 'category': 'Hardware'},
            {'name': '16GB RAM', 'quantity': 18, 'price': 350.00, 'category': 'Hardware'}
        ]
        self.items.extend(initial_items)
        print("Initial items loaded successfully.")

    def add_item(self, name, quantity, price, category):
        item = {
            'name': name,
            'quantity': quantity,
            'price': price,
            'category': category
        }
        self.items.append(item)
        print(f"Item '{name}' added successfully.")

    def remove_item(self, name):
        for item in self.items:
            if item['name'].lower() == name.lower():
                self.items.remove(item)
                print(f"Item '{name}' removed successfully.")
                return
        print(f"Item '{name}' not found.")

    def update_item(self, name, new_quantity=None, new_price=None):
        for item in self.items:
            if item['name'].lower() == name.lower():
                if new_quantity is not None:
                    item['quantity'] = new_quantity
                if new_price is not None:
                    item['price'] = new_price
                print(f"Item '{name}' updated successfully.")
                return
        print(f"Item '{name}' not found.")

    def list_items(self, page=1, items_per_page=5):
        total_pages = (len(self.items) + items_per_page - 1) // items_per_page

        while True:
            start = (page - 1) * items_per_page
            end = start + items_per_page
            paginated_items = self.items[start:end]

            if not paginated_items:
                print("Inventory is empty.")
            else:
                for item in paginated_items:
                    print(f"Name: {item['name']}, Quantity: {item['quantity']}, Price: {item['price']}, Category: {item['category']}")

                print(f"Page {page} of {total_pages}")

            if page > 1:
                print("A. Previous page")
            if page < total_pages:
                print("B. Next page")
            print("C. Exit listing")

            option = input("Choose an option: ").strip().upper()

            if option == 'A' and page > 1:
                page -= 1
            elif option == 'B' and page < total_pages:
                page += 1
            elif option == 'C':
                break
            else:
                print("Invalid option. Try again.")

    def normalize_text(self, text):
        normalized_text = unicodedata.normalize('NFKD', text)
        return ''.join(c for c in normalized_text if not unicodedata.combining(c)).lower()

    def search_items(self, name=None, category=None, min_price=None, max_price=None):
        name = self.normalize_text(name) if name else None
        category = self.normalize_text(category) if category else None

        results = [item for item in self.items if
                   (name is None or name in self.normalize_text(item['name'])) and
                   (category is None or category == self.normalize_text(item['category'])) and
                   (min_price is None or item['price'] >= min_price) and
                   (max_price is None or item['price'] <= max_price)]

        if results:
            for item in results:
                print(f"Name: {item['name']}, Quantity: {item['quantity']}, Price: {item['price']}, Category: {item['category']}")
        else:
            print("No items found with the provided criteria.")

def menu():
    inventory = Inventory()
    while True:
        print("\nInventory Management")
        print("1. Add item")
        print("2. Remove item")
        print("3. Update item")
        print("4. List items")
        print("5. Search items")
        print("6. Exit")
        option = input("Choose an option: ")

        if option == '1':
            name = input("Item name: ")
            quantity = int(input("Quantity: "))
            price = float(input("Price: "))
            category = input("Category: ")
            inventory.add_item(name, quantity, price, category)
        elif option == '2':
            name = input("Name of the item to remove: ")
            inventory.remove_item(name)
        elif option == '3':
            name = input("Name of the item to update: ")
            new_quantity = input("New quantity (press Enter to keep current): ")
            new_price = input("New price (press Enter to keep current): ")
            new_quantity = int(new_quantity) if new_quantity else None
            new_price = float(new_price) if new_price else None
            inventory.update_item(name, new_quantity, new_price)
        elif option == '4':
            page = 1
            items_per_page = int(input("Enter the number of items per page: "))
            inventory.list_items(page, items_per_page)
        elif option == '5':
            print("\nSearch options:")
            print("1. Search by name")
            print("2. Search by category")
            print("3. Search by price range")
            print("4. Combine filters")
            search_option = input("Choose a search option: ")

            if search_option == '1':
                name = input("Enter the item name or part of it: ")
                inventory.search_items(name=name)
            elif search_option == '2':
                category = input("Enter the category: ")
                inventory.search_items(category=category)
            elif search_option == '3':
                min_price = float(input("Enter minimum price: "))
                max_price = float(input("Enter maximum price: "))
                inventory.search_items(min_price=min_price, max_price=max_price)
            elif search_option == '4':
                name = input("Item name (press Enter to skip): ")
                category = input("Category (press Enter to skip): ")
                min_price = input("Minimum price (press Enter to skip): ")
                max_price = input("Maximum price (press Enter to skip): ")
                min_price = float(min_price) if min_price else None
                max_price = float(max_price) if max_price else None
                inventory.search_items(name or None, category or None, min_price, max_price)
            else:
                print("Invalid search option. Try again.")
        elif option == '6':
            print("Exiting...")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    menu()
