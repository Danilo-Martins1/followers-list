from datetime import datetime
import instaloader

L = instaloader.Instaloader()
L.login('username', 'password')

followers = instaloader.Profile.from_username(L.context, 'username').get_followers()
followees = instaloader.Profile.from_username(L.context, 'username').get_followees()

print('\n')
print('Seguidores: ' + str(followers._data['count']))
print('Seguindo: ' + str(followees.data['count']))
print('\n\n')
print('Lista e Informações de Seguidores:')
print('\n')
print(followees._data['edges'])