import telebot
class Bot(telebot.TeleBot):

    def __init__(self, token):
        super().__init__(token)
        self.active = False
        self.counter = 0

    def increment_counter(self):
        self.counter = self.counter+1

    def is_active(self):
        return self.active

    def toggle_status(self):
        self.active = not self.active
        pass