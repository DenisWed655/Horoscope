import requests

from bs4 import BeautifulSoup

def data_ignio(): #   ignio.com
    html = requests.get('http://ignio.com/r/export/utf/xml/weekly/cur.xml')
    soup = BeautifulSoup(html.text, 'lxml').find('cancer')

    alist = [item.string for item in soup]

    for i in range(len(alist)-4):
        print(alist[i].strip())

    return '='*50

def data_oculus(): #   oculus.ru
    html = requests.get('http://www.oculus.ru/goroskop_na_nedelyu/rak.html')
    soup = BeautifulSoup(html.text, 'lxml').find('article').find_all('p')

    for i in soup:
        print(i.string)

    return soup


def main():
    print(data_ignio())
    print(data_oculus())

if __name__ == '__main__':
    main()