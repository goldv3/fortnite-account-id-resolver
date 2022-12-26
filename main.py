#source creator: Gold.#8016
#source leaked by: Gold.#8016

import requests

user = input('Epic Name: ')

r=requests.get(f'https://jesseapi.jesseschepers1.repl.co/accountid?user={user}')

print(r.text)

#basicly if you like to add it to your own tool use this code its just an example have fun!!!!!!!!!
