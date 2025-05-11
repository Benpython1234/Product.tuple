tup1 = (4, 3, 2, 2, -1, 18)
tup2 = (2, 4, 8, 8, 3, 2, 9)

def tuple_product(tup):
    product = 1
    for num in tup:
        product *= num
    return product

print("Tuple 1:", tup1)
print("Product of Tuple 1:", tuple_product(tup1))

print("\nTuple 2:", tup2)
print("Product of Tuple 2:", tuple_product(tup2))
