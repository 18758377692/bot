# coding=gbk
"""
���ߣ�����
ʱ�䣺2021/8/22
˽�˽���Ⱥ��970353786
"""
# pip install baidu-aip
from aip import AipSpeech

""" ��� APPID AK SK """
APP_ID = '24734236'
API_KEY = 'KnmsgdYdL4v9enp2iuD5e6OS'
SECRET_KEY = 'HGhMchOle5sbzRdFqOoHkRu5P1jZR1NM'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

result = client.synthesis('��ɽ���������������', 'zh', 1, {
    'vol': 5,  # ����
    'spd': 3,  # ����
    'pit': 9,  # ���
    'per': 3,  # 0��Ů 1���� 3����ң 4��С����
})
# ʶ����ȷ�������������� �����򷵻�dict �������������
if not isinstance(result, dict):
    with open('auido.mp3', 'wb') as f:
        f.write(result)
