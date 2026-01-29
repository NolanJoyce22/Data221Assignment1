from random import random
#Create list of random values and a random key value
list_of_random_values = [random() for i in range(20)]
random_key_value = random()

list_of_random_values.sort()

indices_where_random_value_is_greater_than_or_equal_to_random_key_value = []
#Iterate through each value and append the value to the list if it is greater than the key value
for i in range(len(list_of_random_values)):
    if list_of_random_values[i] >= random_key_value:
        indices_where_random_value_is_greater_than_or_equal_to_random_key_value.append(i)


print(f"Sorted list: {list_of_random_values}")
print(f"x = {random_key_value}")

if indices_where_random_value_is_greater_than_or_equal_to_random_key_value:
    print(f"First index where list value >= x {indices_where_random_value_is_greater_than_or_equal_to_random_key_value[0]}")
else:
    pass








