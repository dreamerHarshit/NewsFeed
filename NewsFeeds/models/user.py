class User:
    id_count = 1
    user_id = 0
    name = None

    def __init__(self, name):
        self.name = name
        self.user_id = User.id_count
        User.id_count += 1