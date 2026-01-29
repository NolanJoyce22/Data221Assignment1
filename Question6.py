def dictionary_from_list_of_integers(list_of_integers):
    unique_values_paired_with_percentage = {}
    total_amount_of_ints = len(list_of_integers)

    sorted_list_of_integers = sorted(list_of_integers)

# Iterate through each value in list. If integer is not in the dictionary create a key for it, and the value is the
    #percentage of numbers less than that key
    for integer in sorted_list_of_integers:
        if integer not in unique_values_paired_with_percentage:
            count = 0
            for n in sorted_list_of_integers:
                if n <= integer:
                    count += 1
            unique_values_paired_with_percentage[integer] = (count / total_amount_of_ints) * 100

    return (unique_values_paired_with_percentage)

print(dictionary_from_list_of_integers([3,1,2,3,4,2]))



