import requests
dem_html = requests.get('https://www.nytimes.com/interactive/2019/us/politics/2020-presidential-candidates.html')

from bs4 import BeautifulSoup
soup = BeautifulSoup(dem_html.content, 'html.parser')

filtered = soup.find_all(attrs= {'class':'g-name'})

list1 = []

for i in filtered:
    vy = (i.text.replace('\t',''))
    list1.append(vy.replace('\n',''))
print(list1[0:21])

cand_list = list1[0:21]
cand_list
