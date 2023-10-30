def read_dict_file(input_file):
    # Read a dictionary from the input file and return it as a Python dictionary.
    try:
        with open(input_file, "r") as rf:
            data = {}
            #iterating through all lines in opened file
            for line in rf:
        #checking the lines that have : in them and splitting them then removing spaces and {}
        #after splitting each side is assigned to either the key or the value
                if ':' in line:
                    key, value = line.strip().strip("{}").split(":")
        #removing all spaces in the key
                    key = key.strip()
        #removing all spaces and comams in the value and then splitting them where there is ', '
                    value = value.strip().strip(', ').split(', ')
        #appending the empty dictinary data with the keys and values
                    data[key] = value
            
            return data
        #handling the first error if the file is not found and an empty dictionary
    except FileNotFoundError:
        print("Input file not found.")
    #handling all the other exceptions that might occur
    except Exception as e:
        print(f"An error occurred: {e}")

def invert_dict(original_dict):
    inverted_dict = {}
    try:
        #iterating through the keys and values of the dictionary returned by the read function
        for key, values in original_dict.items():
        #checking whether some of the values are lists
            if isinstance(values, list):
            #if the values is a list, we iterate through the values 
            # then we check whether that value exist in the dictionary
            #if it does not, we insert the value as key and the key as the value
                for value in values:
                    if value not in inverted_dict:
                        inverted_dict[value] = [key]
                    else:
                        inverted_dict[value].append(key)
        #if the values are not a list, we just check whether it exists in the inverted dictionary
        #if it does exist we append the values as the key and the key as the values
        #if it exists, we jst append thet values to the key
            else:
                if values not in inverted_dict:
                    inverted_dict[values] = [key]
                else:
                    inverted_dict[values].append(key)
        return inverted_dict
    except:
        print("An error occured during inverting the dictionary")


def write_dict_to_file(output_file, output_dict):
    #writing the inverted dictionary to the output file
    try:
            with open(output_file, 'w') as wf:
                wf.write(str(output_dict))
    except:
        print("file could not be written")



input_file = "input_dict.txt"
output_file = "output_dict.txt"

# Reading the dictionary from the input_file
original_dict = read_dict_file(input_file)
print("Original Dictionary:")
print(original_dict)

# Inverting the dictionary
inverted_dict = invert_dict(original_dict)
print("Inverted Dictionary:")
print(inverted_dict)

#writing to file
write_dict_to_file(output_file,inverted_dict)