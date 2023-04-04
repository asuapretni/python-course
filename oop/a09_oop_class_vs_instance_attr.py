# class Website:
#     def __init__(self, title):
#         self.title = title
#
# ws = Website('My website')
# print(ws.__dict__)  # {title: 'My website'}
# print(ws.title)
#
# ws = Website('Other website')
# print(ws.__dict__)
# print(ws.title)


class DifferentWebsite:
    title = 'My class title'

dw = DifferentWebsite()
print(dw.title)
print(dw.__dict__)  # {} we can use __dict__ to distinguise between class and instance attrs
