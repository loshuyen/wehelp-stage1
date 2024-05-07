import urllib.request as request
import json

# ===== TASK 1 =====

spot_url = 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1'
mrt_url = 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-2'

spot_data = {}
mrt_data = {}

with request.urlopen(spot_url) as response:
    spot_data = response.read()
    spot_data = json.loads(spot_data)
    spot_data = spot_data['data']['results']
with request.urlopen(mrt_url) as response:
    mrt_data = response.read()
    mrt_data = json.loads(mrt_data)
    mrt_data = mrt_data['data']

no_vs_spot = {x['SERIAL_NO']:x['stitle'] for x in spot_data}
no_vs_mrt = {x['SERIAL_NO']:x['MRT'] for x in mrt_data}
mrt_vs_spot = {x['MRT']:'' for x in mrt_data}

for key, val in no_vs_mrt.items():
    if not mrt_vs_spot[val]:
        mrt_vs_spot[val] += no_vs_spot[key]
    else:
        mrt_vs_spot[val] += f",{no_vs_spot[key]}"

no_vs_district = {x['SERIAL_NO']:x['address'].split()[1][:3] for x in mrt_data}
with open('spot.csv', mode='w', newline='') as file:
    for spot in spot_data:
        district = no_vs_district[spot['SERIAL_NO']]
        file.write(f"{spot['stitle']},{district},{spot['longitude']},{spot['latitude']},https{spot['filelist'][5:].split('https')[0]}\n")

with open('mrt.csv', mode='w', newline='') as file:
    for mrt in mrt_vs_spot:
        file.write(f"{mrt},{mrt_vs_spot[mrt]}\n")

# ===== TASK 2 =====

from bs4 import BeautifulSoup

def get_data (page_url):
    url = page_url
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'Cookie':'over18=1'
    }
    ptt_req = request.Request(url, headers=headers)

    with request.urlopen(ptt_req) as response:
        ptt_data = response.read().decode('utf-8')
    root = BeautifulSoup(ptt_data, 'html.parser')
    articles = root.find_all('div', class_='r-ent')
    with open('article.csv', mode='a', newline='') as file:
        for article in articles:
            title = article.find('div', class_='title')
            like = article.find('div', class_='nrec')
            if title.a != None:
                article_title = title.a.string
                article_href = 'https://www.ptt.cc' + title.a['href']
                article_like = like.span.string if like.span else 0
                article_req = request.Request(article_href, headers=headers)
                with request.urlopen(article_req) as response:
                    article_data = response.read().decode('utf-8')
                article_root = BeautifulSoup(article_data, 'html.parser')
                article_info = article_root.find_all('span', class_='article-meta-value')
                pub_time_list = []
                for info in article_info:
                    pub_time_list.append(info.string)
                pub_time = pub_time_list[3] if len(pub_time_list) > 3 else ''
                file.write(f"{article_title},{article_like},{pub_time}\n")
    next_link = 'https://www.ptt.cc' + root.find('a', string='‹ 上頁')['href']
    return next_link

ptt_url = 'https://www.ptt.cc/bbs/Lottery/index.html'
count = 0
while count < 3:
    ptt_url = get_data(ptt_url)
    count+=1