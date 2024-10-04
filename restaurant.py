class Menu:
    items = {
            "pizza ": 3.00,
            "nachos ": 4.50,
            "popcorn ": 6.00,
            "fries ": 2.50,
            "chips ": 1.00,
            "pretzel ": 3.50,
            "soda ": 3.00,
            "lemonade ": 4.25                 
            }   
    
    def menu(self):
        for _ in range(10):
            print("-", end="")
        print("MENU", end="")
        for _ in range(10):
            print("-", end="")   
        print("")
        for key,value in self.items.items():
            print(f"{key}: ${value}")
        for _ in range(25):
            print("-", end="")
        print("")
        
        
class Customer:
    
    price = {
            "pizza": 3.00,
            "nachos": 4.50,
            "popcorn": 6.00,
            "fries": 2.50,
            "chips": 1.00,
            "pretzel": 3.50,
            "soda": 3.00,
            "lemonade": 4.25                 
            } 
    
    def customer_order(self):
        self.items = ["pizza","nachos","popcorn","fries","chips","pretzel","soda","lemonade"]
        self.total = 0
        self.receipt = []
        while True:
            self.order = input("Select an item (q to quit): ")
            if self.order == "q":
                break
            elif self.order in self.items:
                self.receipt.append(self.order)
                for key in self.price:
                    if key == self.order:
                        self.total = self.total + self.price[self.order]
            else:
                print("Choose one of the items from the menu, Invalid input")
        print("------ YOUR ORDER ------")
        for i in self.receipt:
            print(i)
        print(f"Total is: ${self.total}")
            
                
def main():
    m = Menu()
    c = Customer()
    m.menu()
    c.customer_order()
    

if __name__ == "__main__":
    main()
    