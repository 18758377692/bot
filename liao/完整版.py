# coding=gbk
"""
���ߣ�����
ʱ�䣺2021/8/22
˽�˽���Ⱥ��970353786
"""
from play import playsound
from aip import AipSpeech
import requests
""" ��� APPID AK SK """
APP_ID = '24734236'
API_KEY = 'KnmsgdYdL4v9enp2iuD5e6OS'
SECRET_KEY = 'HGhMchOle5sbzRdFqOoHkRu5P1jZR1NM'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

print('����������˵�ģ�')

while True:
    a=input()
    url='https://api.ownthink.com/bot?appid=9ffcb5785ad9617bf4e64178ac64f7b1&spoken=%s'%a
    te=requests.get(url).json()
    data=te['data']['info']['text']
    print(data)
    result = client.synthesis(data, 'zh', 1, {
        'vol': 8,  # ����
        'spd': 5,  # ����
        'pit': 9,  # ���
        'per': 4,  # 0��Ů 1���� 3����ң 4��С����
    })
    # ʶ����ȷ�������������� �����򷵻�dict �������������
    if not isinstance(result, dict):
        with open('auido.mp3', 'wb+') as f:
            f.write(result)

    p = playsound()
    voice_path = r"auido.mp3"
    p.play(voice_path)  # ����
    p.close()  # ֹͣ