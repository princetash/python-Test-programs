def read_dict_file(input_file):
   
    try:
        with open(input_file, "r") as rf:
            data = {}
            
            for line in rf:
                if '=' in line:
                    key, value = line.strip().split("=")
        
                    key = key.strip()
        
                    value = value.strip().split(", ")
                    data[key] = value
            return data
    except FileNotFoundError:
        print("Input file not found.") 
    except Exception as e:
        print(f"An error occurred: {e}")

def invert_dict(original_dict):
    inverted_dict = {}

    for key, value in original_dict.items():
        if isinstance(value, list):
            for v in value:
                if v not in inverted_dict:
                    inverted_dict[v] = [key]
                else:
                    inverted_dict[v].append(key)
        else:
            if value not in inverted_dict:
                inverted_dict[value] = [key]
            else:
                inverted_dict[value].append(key)
    return inverted_dict


input_file = "intry.txt"
output_file = "outtry.txt"


original_dict = read_dict_file(input_file)
print("Original Dictionary:")
print(original_dict)

# Inverting the dictionary
inverted_dict = invert_dict(original_dict)
print("Inverted Dictionary:")
print(inverted_dict)