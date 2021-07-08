class Place:

    def __init__(self):
        self.name = "name of place"
        self.email = "email"
        self.number = "phone number"


    def save_name(self, name):
        self.name = name

    def save_email(self, email):
        self.email = email
    
    def save_number(self, number):
        self.number = number

    def print_save(self):

        txt = f'{self.name} \n'
        txt += f'{self.email} \n'
        txt += f'{self.number}\n'

        print(txt)

        f = open("saved_data.txt", 'a',encoding='utf8')
        f.write(txt)
        f.close()

   