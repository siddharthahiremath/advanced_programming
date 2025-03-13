class Email():
    def __init__(self, name:str, email:list, ccemail:list, subject:str, body:str):
        self.name = name
        self.email = email
        self.ccemail = ccemail
        self.subject = subject
        self.body = body
    def log_data(self):
        print(self.name)
        print(self.email)
        print(self.ccemail)
        print(self.subject)
        print(self.body)