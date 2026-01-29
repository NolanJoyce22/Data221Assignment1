def detailed_dictionary_from_list_of_strings(list_of_strings):
    dictionary_with_string_information = {}
# Iterate through list creating the dictionary
    for s in list_of_strings:
        length_of_string = len(s)
        dictionary_with_string_information[s] = {"Length":length_of_string,
                                          "Parity":"Even" if length_of_string % 2 == 0 else "Odd"
                                          }
    return dictionary_with_string_information


