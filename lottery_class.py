from random import choice


def random_ticket():
    numbers = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E']
    choices = []

    while len(choices) < 4:
        value = choice(numbers)
        choices.append(value)
    return choices



total_list= []
attempts = 5    
def verify_ticket():
    my_ticket = [1,2,'A',0]
    items = random_ticket()
    for item in items:
        while item != my_ticket or attempts != 0:
            total_list.append(item)
            attempts -= 1
        else:
            print("you win")


verify_ticket()