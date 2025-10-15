#메가박스는 스크랩을 막아놓음
# import requests

# url='https://www.megabox.co.kr/movie'
# headers={'user-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36'}
# res=requests.get(url, headers=headers)

# file_name=f'data/megabox.html'
# with open(file_name,'w',encoding='utf-8') as file:
#     file.write(res.text)


import requests

url='https://www.cineq.co.kr/Movie/BoxOffice'
res=requests.get(url)

file_name=f'data/씨네큐.html'
with open(file_name,'w',encoding='utf-8') as file:
    file.write(res.text)
