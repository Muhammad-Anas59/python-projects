class IceCream:
    def __init__(self,name,price):
        self.name=name
        self.price=price
class Order:
    def __init__(self):
        self.items=[]
    def additem(self,iceCream):
        self.items.append(iceCream)
        print(f"Added {iceCream.name} to your menu :\n")
    def total(self):
        total=0
        for item in self.items:
            total=total+item.price
        return total
    def show(self):
        if not self.items:
            print("No items in order :")
            return
        
        print("\nYour ordered IceCream : ")
        for i,item in enumerate(self.items,1):
            print(f"{i}.{item.name}  ${item.price}")
        print(f"Total : ${self.total()}\n")
    
    def checkout(self):
        if not self.items:
            print("\nYour order is empty")
            return
        self.show()
        done=input("\nProceed to check out ?(Yes/No) :").strip().lower()
        if done=='yes':
            print("\nYou order is confirmed! Thanks a lot")
            self.items.clear()
        else:
            print("\nOrder is Cancelled : ")
def main():
        menu=[
            IceCream("Strawberry",1.5),
            IceCream("Chocolate",2.5),
            IceCream("Pista",1.5),
            IceCream("Vanilla",2),
            IceCream("Tooty Fruity",3),
            IceCream("Mango",2),

        ]
        order=Order()
        while True:
            print("\n___ICECREAM MENU___")
            for i,item in enumerate(menu,1):
                print(f"{i}.{item.name} ${item.price}")
            print("7.View Order ")
            print("8.Checkout ")
            print("9.EXit")
            done=input("Choose any Option :\n")
            if done in ['1','2','3','4','5','6']:
                order.additem(menu[int(done)-1])
            elif done=='7':
                order.show()
            elif done=='8':
                order.checkout()
            elif done=='9':
                print("\nThanks for coming.Take Care")
                break
            else :
                print("\nInvalid Choice :")
if __name__=="__main__":
    main()
