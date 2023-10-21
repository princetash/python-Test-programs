employee_names = ['James', 'Mike', 'Smith', 'Peter', 'Rosalia',
         'Emmanuel', 'Abel', 'Benard', 'Daniel', 'Leonard']

# part 1 Splitting the names into two subLists
subList1 = employee_names[:5]
subList2 = employee_names[5:]


# part 2 Adding new employee to subList2
subList2.append('Kriti Brown')


# part 3 Removing second employee from subList1
subList1.pop(1)
# del subList1[1]


# part 4 Merging both lists
merged_names = subList1 + subList2


# part 5 Increasing the salary by 4%
salary_list = [140, 170, 235, 450, 700, 456, 320, 560, 540, 500]

#list to store updated salary
updated_salary_list = []
#calculating the updated salary
for salary in salary_list:
    updated_salary = salary * 1.04
    updated_salary_list.append(updated_salary)

# part 6 sorting the salaries
salary_list.sort()

#top 3 salaries
top_3 = salary_list[-3:]

#Outputs
print("SubList1:", subList1)
print("SubList2:", subList2)
print("Merged List:", merged_names)
print("Updated Salary List:", updated_salary_list)
print("Top 3 Salaries:", top_3)

#part b
#getting the sentence from user
sentence = input("Enter your sentence: ")
#splitting the sentence into words
wordList = sentence.split(' ')
#reversing the wordlist
wordList.reverse()
#joining the wordlist to form a sentence
reversed_sentence = ' '.join(wordList)


#outputs
print("Original Sentence:", sentence)
print("Word List:", wordList)
print("Reversed Sentence:", reversed_sentence)



#adding functions to compute the same values
#comment all the code below to test the code above and vice versa
def give_raise(salary_list, percentage):
  """Gives a raise to every employee in the salary list.

  Args:
    salary_list: A list of salaries.
    percentage: The percentage of the raise.

  Returns:
    A list of salaries with the raise applied.
  """

  new_salary_list = []
  for salary in salary_list:
    new_salary = salary * (1 + percentage)
    new_salary_list.append(new_salary)
  return new_salary_list


def sort_salary_list(salary_list):
  """Sorts the salary list in descending order.

  Args:
    salary_list: A list of salaries.

  Returns:
    A sorted list of salaries in descending order.
  """

  salary_list.sort(reverse=True)
  return salary_list


def get_top_3_salaries(salary_list):
  """Gets the top 3 salaries in the salary list.

  Args:
    salary_list: A list of salaries.

  Returns:
    A list of the top 3 salaries in the salary list.
  """

  top_3_salaries = []
  for i in range(3):
    top_3_salaries.append(salary_list[i])
  return top_3_salaries


# Example usage:

salary_list = [100000, 90000, 80000, 70000, 60000]

# Give a 4% raise to every employee.
new_salary_list = give_raise(salary_list, 0.04)

# Sort the salary list in descending order.
sorted_salary_list = sort_salary_list(new_salary_list)

# Get the top 3 salaries.
top_3_salaries = get_top_3_salaries(sorted_salary_list)

# Print the top 3 salaries.
print(top_3_salaries)
