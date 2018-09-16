import os
from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/keyboard')
def Keyboard():
 
    dataSend = {
        "type" : "buttons",
        "buttons" : ["시작하기"]
    }

    return jsonify(dataSend)


@app.route('/message', methods=['POST'])
def Message():
    
    dataReceive = request.get_json()
    content = dataReceive['content']
 
    if content == u"시작하기":
        dataSend = {
            "message": {
                "text": "아직 개발중이라 대답을 잘 못해도 이해해줘^^;"

            }
        }
    elif content == u"실시간검색어":
        url = 'https://www.naver.com'
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')
        tag_list = soup.select('.PM_CL_realtimeKeyword_list_base .ah_item')
        item = ''
        for idx, tag in enumerate(tag_list, 1):
            realtime_url = 'https://search.naver.com/search.naver?where=nexearch&query={}'.format(tag.select('span')[1].text.replace(' ', '+'))
            item_, link_ =  tag.select('span')[1].text,  realtime_url
            item = item + '\n' + item_
        dataSend = {
            "message": {
                "text": item
            }
        }
    else:
        dataSend = {
            "message": {
                "text": "아직 배우는 중이에요!"
            }
        }


 
    return jsonify(dataSend)
 
 
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 80)
