import requests
print('Enter your Website Url:')
x = input()

URL = x
page = requests.get(URL)

print('\x1b[6;30;42m' + 'Scan....!' + '\x1b[0m')

    
print(page.text)
