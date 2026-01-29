

def computing_powers_of_specified_integers(list_of_paired_integers):
    list_of_powers = []
# Iterate through each pair in the list and compute the power
    for x,y in list_of_paired_integers:
        if y >= 0:
            power = x**y
            list_of_powers.append(power)
    return list_of_powers

print(computing_powers_of_specified_integers([[5,2], [3,-1], [4,3], [2,0]]))
