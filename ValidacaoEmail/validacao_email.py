import re

class ValidacaoEmail:
    
    def __init__(self):
        self.caracters = ['_', '.']

    def email_validado(self, email):
        pat = "^[a-z0-9-._]+@[a-z0-9]+\.[a-z]{1,3}$"
    
        if re.match(pat, email.lower()):
            return True

        return False

    def email_validacao_split(self, email):
        separa_email = email.split('@')
        email_valido = len(separa_email) > 1
        
        if not email_valido:
            return False

        for item in separa_email[0]:
            if item.isalpha() or item.isdigit() or self.email_validacao_custom_carater(item):
                email_valido = True
            else:
                return False

        for item in separa_email[1]:
            if item.isalpha() or item.isdigit() or self.email_validacao_custom_carater(item):
                email_valido = True
            else:
                return False

        return email_valido

    def email_validacao_custom_carater(self, caracter):
        return caracter in self.caracters