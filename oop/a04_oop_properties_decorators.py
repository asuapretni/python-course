class Invoice:
    def __init__(self, client, total):
        self._client = client
        self._total = total

    def formatter(self):
        return f'{self._client} owes: ${self._total}'

    @property
    def client(self):
        return self._client

    @client.setter
    def client(self, client):
        self._client = client

    @property
    def total(self):
        return self._total

google = Invoice('Google', 100)

print(google.client)
print(google.__dict__)

google.client = 'yahoo'

print(google.client)


# exercise solved
class Garage:
  def __init__(self, size):
    #   Protect the size attribute
    self._size = size
    self.cars = []

  @property
  def size(self):
      return self._size

  # @size.setter
  # def size(self, size):
  #     self._size = size

  def open_door(self):
    return "The door opens"

# proof = Garage(4)
# print(proof.size)  # works fine
# proof.size = 6   # without the setter gives an error
# print(proof.size)