def create_price_list(items):
    price_list = []

    items = items.split(", ")
    for item in items:
        item = item.split("=")
        price_list.append([item[0], float(item[1])])

    return price_list


def price_of(price_list, item_name):
    for item in price_list:
        if item[0] == item_name:
            return item[1]


def total(price_list, cart):
    cart_total = 0

    cart = cart.split(" ")
    for item in cart:
        item, quantity = item.split(":")
        quantity = int(quantity)

        if quantity < 1:
            continue

        item_total = price_of(price_list, item) * quantity
        if quantity > 5:
            item_total = item_total * 0.9

        cart_total += item_total
        print(item, quantity, item_total)

    print("total", cart_total)


# -------------------------------

price_list_txt = "milk=5.0, bread=40.0, banana=5.0, egg=5.0, rice=30.0, noodle=12.0"
pricelist = create_price_list(price_list_txt)
purchases = "milk:1 bread:2 egg:12 banana:0"
total(pricelist, purchases)
