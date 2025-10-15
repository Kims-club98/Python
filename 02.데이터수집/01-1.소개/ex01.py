import requests
import os

path=os.getcwd() +'/data' #f'{os.getcwd()} /data'

if not os.path.exists(path):
    os.makedirs(path)

print(path)

name=input('이름>')
url=f'https://www.google.com/search?sca_esv=5d812c3a7137edf1&rlz=1C1FKPE_koKR1177KR1178&udm=2&fbs=AIIjpHyDg0Pef0CibV20xjIa-FRejxCuOmkq074km2sZXr7uqz9_8tiStZcoMiP-q5iAtTZL8-ZdTewwQWlWih-7esbNhKOXKOKa_rCQgz2OtnVKwLY8iOIhasTdsfj99ZIJghBOXKYgC2k20Lxd21MXq8s3D4-LW8OT17wPXxa4OQjtBbAywJeLhaUxOdTwSzEZZe3FJ-afB5J_fsvirH28kAwf9vt79TCw8jQX95DmqK6wyHdLbZU&q={name}&sa=X&sqi=2&ved=2ahUKEwiw3_an67iPAxXbra8BHYxsK7oQtKgLegQIIxAB&biw=1038&bih=706&dpr=1.25'
res=requests.get(url)



file_name=f'data/{name}.html'
with open(file_name, 'w', encoding='utf-8') as file:
    file.write(res.text)


