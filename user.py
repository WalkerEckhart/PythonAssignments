class User:
    def __init__(self, first, last, email, age, points=0, member=False):
        self.first_name = first
        self.last_name = last
        self.email = email
        self.age = age
        self.member = member
        self.points = points
    
    def display_info(self):
        print(f" {self.first_name} , {self.last_name} , {self.email} , {self.age} , {self.member} ; {self.points} .")
        return self
    
    def enroll(self):
        if self.member == True:
            print(f"You're already a member, {self.first_name}! ")
            self.member = False
        else:
            self.member = True
            self.points += 200
        return self
    
    def spend_points(self, amount):
        self.points -= amount
        if self.points < 0:
            self.points += amount
            print(f"Get your bread up, {self.first_name}! You only have {self.points} points! You need {amount - self.points} more points")
        else: 
            print(f"Transcation completed. You now have {self.points} points.")
        return self


user_walker = User("Walker", "Eckhart", "eckhartwalker@gmail.com", 21, 30, True)
user_link = User("Crystal", "Lenk", "clenk@clenk.clenk", 20, 0)
user_micaela = User("Red", "Rover", "redRover@hotmail.com", 21, 0)

user_walker.enroll().spend_points(50)
user_link.enroll().spend_points(300)
user_micaela.enroll().spend_points(40)