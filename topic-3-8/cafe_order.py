

def drink_price(size, shot):
    price = 0
    if size == "S":
        price += 3
    else:
        if size == "M":
            price += 4
        else:
            if size == "L":
                price += 5
    if shot == "Y":
        price += 1
    else:
        price += 0
    return price 

def serve_customer(customer_number, drink_count):
    bill = 0
    
    drink_count = input("Drink count: ")
    for i in range (0, int(drink_count), 1):
            size =(input("Size: ").upper())
            extra = (input("Extra: ").upper())
            bill += int(drink_price(size, extra))
    return bill 


    


def main():
    customer_number = int(input("Customer number: "))
    sales = 0
    for i in range(0, customer_number, 1):
    
    print(serve_customer((), ()))
    
main()