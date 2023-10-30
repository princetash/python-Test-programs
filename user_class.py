class User:
    def __init__(self, first_name, last_name, age):
        self.fname = first_name 
        self.lname = last_name
        self.age =age
        self.login_attempts = 0

    
    def describe_user(self):
        print(f"This user's first name is {self.fname} and last name is {self.lname}. {self.fname} will be {int(self.age + 5)} in the next five years")


    def greet_user(self):
        print(f"Hello {self.fname}, it's good to see you")

    #increamenting login attempts by 1 if the number of total attempts is less than 3
    def increament_login_attempts(self):
        if self.login_attempts < 3:
            self.login_attempts += 1
            print(f"Login attempts: {self.login_attempts}")
        else:
            print(f"You are out of login attempts. You have tried {self.login_attempts} times. Reset attempts to try again")


    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"Login attempts: {self.login_attempts}")


my_user = User("Mike", "Jones", 5)
my_user.describe_user()
my_user.greet_user()

#calling increament attempt to check whether increament is working
my_user.increament_login_attempts()
my_user.increament_login_attempts()
my_user.increament_login_attempts()
my_user.increament_login_attempts()
my_user.increament_login_attempts()

#calling reset to check whether it is resetting attempts to 0
my_user.reset_login_attempts()
my_user.increament_login_attempts()


class Privilege:
    def __init__(self):
        self.privileges = "can add post", "can delete post", "can ban users"

    
    
    def show_privilege(self):
        print("The privileges of the admin include:")
        for privilege in self.privileges:
            print(f"   - {privilege}")



class Admin(User):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.privilege = Privilege()



admin = Admin("Mike", "Josy", 65)
admin.privilege.show_privilege()