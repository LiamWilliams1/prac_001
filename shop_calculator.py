def main():

    number_of_items = int(input("enter number of items:"))
    total_price_of_items = 0
    while number_of_items <= 0:
        print ("invalid input")
        number_of_items = int(input("enter number of items:"))
    for i in range(number_of_items):
        price_of_item = float(input("price of item:"))
        total_price_of_items += price_of_item
        if total_price_of_items > 100:
            total_price_of_items= total_price_of_items * 0.9

    print("total Price is {:.2f}".format( total_price_of_items ))

main()