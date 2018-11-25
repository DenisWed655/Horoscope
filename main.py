import requests

from bs4 import BeautifulSoup

def data_ignio(): #   ignio.com
    html = requests.get('http://ignio.com/r/export/utf/xml/weekly/cur.xml')
    soup = BeautifulSoup(html.text, 'lxml').find('cancer')

    alist = [item.string for item in soup]

    for i in range(len(alist)-4):
        print(alist[i].strip())

    return ' ======================================== '

def main():
    print(data_ignio())

if __name__ == '__main__':
    main()