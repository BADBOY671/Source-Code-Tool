import requests, time
print('Enter your Website Url:')
x = input()

URL = x
page = requests.get(URL)

print('\x1b[6;30;42m' + 'Wait....!' + '\x1b[0m')
time.sleep(5)
print(page.text)
