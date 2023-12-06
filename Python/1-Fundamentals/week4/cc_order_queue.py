class Queue:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.size() == 0:
            return None
        return self.items.pop(0)

    def show_queue(self):
        print(self.items)


class IceCreamShop:
    def __init__(self, flavors):
        self.flavors = flavors
        self.orders = Queue()

    def take_order(self, customer, flavor, scoops):
        if flavor not in self.flavors:
            raise ValueError("Invalid flavor: {}".format(flavor))
        if scoops < 1 or scoops > 3:
            raise ValueError("Invalid number of scoops: {}".format(scoops))

        print("Order created!")

        order = {"customer": customer, "flavor": flavor, "scoops": scoops}
        self.orders.enqueue(order)

    def show_all_orders(self):
        print("All orders:")
        for order in self.orders.items:
            print("* Customer:", order["customer"])
            print("* Flavor:", order["flavor"])
            print("* Scoops:", order["scoops"])

    def next_order(self):
        next_order = self.orders.dequeue()
        if next_order is None:
            print("No more orders.")
        else:
            print("Next order:")
            print("* Customer:", next_order["customer"])
            print("* Flavor:", next_order["flavor"])
            print("* Scoops:", next_order["scoops"])


shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()
