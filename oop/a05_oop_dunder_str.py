class Invoice:
    def __init__(self, client, total):
        self.client = client
        self.total = total

    def __str__(self):
        return f'Invoice from {self.client} for ${self.total}'

inv = Invoice('Google', 500)
print(str(inv))
