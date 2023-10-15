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
