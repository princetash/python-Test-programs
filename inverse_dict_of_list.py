dict_student = {
    'Stud1': ['CS1101', 'CS2402', 'CS2001', 'CS2450'], 
    'Stud2': ['CS2402','CS2001','CS1102'],
    'Stud3': ['CS3450', 'CS1102', 'CS2450'] 
}

#converting values to keys and key to values

def inverted_dict(diction):
    #initializing an empty dictionary where we will store our new values
    inverse = dict()
    #iterating through the dictionary provided to get the key(student) and the value(courses)
    for student, courses in diction.items():
        #iteraing through the courses list in oder to get each individual course
        for course in courses:
        #checking whether the value(course) of a certain key(student) exists in the inverse dictionary
        #if not the value becomes the key
            if course not in inverse:
                inverse[course] = [student]
            #if the value exists as a key in the dictionary, we append to that value
            else:
                inverse[course].append(student)
    return inverse
result_inverse = inverted_dict(dict_student)
print(f"Original dictionary{dict_student}")
print()
print(f"Inverted dictionary{result_inverse}")

