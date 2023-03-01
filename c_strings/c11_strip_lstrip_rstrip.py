url = 'https://google.com'

url = url.lstrip('https://')
url = url.rstrip('.com')
url = url.capitalize()

print(url)