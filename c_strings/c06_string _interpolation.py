name ='Kristine'
greeting = f'Hi {name}'
print(greeting)

greeting = f'Hi {{brakets}}'  #the way to print curly brakets
print(greeting)

name ='Kristine'
product = 'Python course'

email_content = f"""
Hi {name},

Thank you for purchasing {product}

Regards,
Sales Team
""".strip()

print(email_content)

