class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.name = username
        self.followers = 0 ## default value
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User(username = "Giop", user_id = "001")

