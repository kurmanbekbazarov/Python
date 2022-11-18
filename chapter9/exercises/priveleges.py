class Privelege:
    def __init__(self, privileges = []):
        self.privileges = privileges

    def show_privileges(self):
        print(f"List of priveleges: ")
        for i in self.privileges:
            print(f"\t{i}")

admin = Privelege(privileges=('can add post', 'can delete post', 'can ban user'))

admin.show_privileges()