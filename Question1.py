
threshold = 100
product = 1
current_number_in_loop = 1

while product <= 100:
# Multiplying product by current number in the loop. Stops when product reaches 100
    current_number_in_loop +=1
    product *= current_number_in_loop

print("the product is", product)
print("The nuber that caused the product to exceed the threshold is", current_number_in_loop)
    