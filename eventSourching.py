class Event:
    def __init__(self, event_type, data):
        self.event_type = event_type
        self.data = data

class Account:
    def __init__(self, id):
        self.id = id
        self.balance = 0
        self.events = []

    def deposit(self, amount):
        self.balance += amount
        event = Event("DEPOSIT", {"amount": amount})
        self.events.append(event)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            event = Event("WITHDRAW", {"amount": amount})
            self.events.append(event)
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.balance

    def get_events(self):
        return self.events


# Hesap oluştur
account = Account("123")

# Para yatır
account.deposit(100)
print("Hesap bakiyesi:", account.get_balance())

# Para yatır
account.deposit(150)
print("Hesap bakiyesi:", account.get_balance())

# Para çek
account.withdraw(50)
print("Hesap bakiyesi:", account.get_balance())

# Para yatır
account.deposit(20)
print("Hesap bakiyesi:", account.get_balance())

# Hareketleri al
events = account.get_events()
print("Hareketler:")
for event in events:
    print(event.event_type, event.data)
    
