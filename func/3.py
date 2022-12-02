def events(price, discount):
    discount_price = (price * discount) / 100
    price_after_discount = price - discount_price
    return price_after_discount


price = 2100000
discount = 70
print(events(price, discount))
