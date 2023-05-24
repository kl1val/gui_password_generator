import random

class PassGen:

    def __init__(self, info_dict) -> None:
        self.info_dict = info_dict
        self.symbols_dict = {"a-z": 'abcdefghijklmnopqrstuvwxyz', 
                              "A-Z": 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 
                              "0-9": '0123456789',
                              "#!$": '#!@$%&?:;'}
        self.strength_dict = {"Simple": 12,
                              "Medium": 17,
                              "Strong": 25,
                              "Unbreakable": 35}
        
    def get_password_symbols(self):
        symbols = ''
        raw_symbols = self.info_dict['symbols']

        for symbol in raw_symbols:
            symbols = symbols + self.symbols_dict[symbol]

        return symbols
    
    def get_password_strength(self):
        raw_strength = self.info_dict['strength']
        return self.strength_dict[raw_strength]
    
    @staticmethod
    def password_validation(password):
        for number in range(1, len(password)-1):
            if password[number].lower() not in (password[number-1].lower(), password[number+1].lower()):
                return password
        return False

    def generate_password(self):
        symbols = self.get_password_symbols()
        strength = self.get_password_strength()
        password = ''

        for _ in range(strength):
            password += random.choice(symbols)
        return self.password_validation(password)
