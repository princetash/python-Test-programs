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