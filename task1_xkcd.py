
import bs4, requests, os

os.makedirs('xkcd', exist_ok = True)

url = 'http://xkcd.com'

while not url.endswith('#'):
    print('Downloading page ' + url)
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    
    try:
        comicURL = 'http:' + soup.select('#comic img')[0].get('src')
        print('Downloading image ' + comicURL)
        res = requests.get(comicURL)
        imageFile = open(os.path.join('xkcd', os.path.basename(comicURL)), 'wb')
        for chunk in res:
            imageFile.write(chunk)
        imageFile.close()
    except Exception as exc:
        print('Could not find image due to ' + str(exc))

    url = 'http://xkcd.com' + soup.select('a[rel="prev"]')[0].get('href')