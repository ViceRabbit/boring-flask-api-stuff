
import requests

jsonobj = {'bruhman': 'Anti-Cringe Rabbit', 'bruh': "Rabbits that aren't cringe; unlike Gavin42307 *cough*"}
post = requests.post('https://5000-vicerabbit-boringflaska-ynpqm2mfflk.ws-us70.gitpod.io/rabbits', json = jsonobj)
print(post.json())
print('Succesfully posted.')

