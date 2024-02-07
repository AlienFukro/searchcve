import requests
import sys
from bs4 import BeautifulSoup

with open(sys.argv[1]) as f:
    for cvelist in f:
        url = 'https://nvd.nist.gov/vuln/detail/' + cvelist
        url2 = url.rstrip()
        print (url2)

        r = requests.get(url2)
        html = r.text

        # BeautifulSoupを使用してHTMLを解析
        soup = BeautifulSoup(html, 'html.parser')

        target_element = soup.find(class_='severityDetail')
        # 要素が見つかった場合、そのテキストを取得して表示
        if target_element:
            target_value = target_element.text
            print("SVSS3のBase score:", target_value)
        else:
            print("SVSS3のBase scoreの値は見つかりませんでした")