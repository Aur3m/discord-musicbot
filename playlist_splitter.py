from bs4 import BeautifulSoup
import requests

url = 'https://www.youtube.com/playlist?list=PLMIlze7aeTnvS3IREzmPR376iyzTUxnNk'

def Splitter(url):
    try:
        ch4 = []
        sourceCode = requests.get(url).text
        soup = BeautifulSoup(sourceCode, 'html.parser')
        domain = 'https://www.youtube.com'
        for link in soup.find_all("a", {"dir": "ltr"}):
            href = link.get('href')
            if href.startswith('/watch?'):
                ch1 = domain + href
                ch2 = ch1.split('&list=')
                ch3 = ch2[0]
                ch4.append(ch3)
        return ch4
    except Exception as err:
        print('ERREUR DE PLAYLIST SPLITTER:\n' + str(type(err)) + str(err))