# coding=gbk
"""
���ߣ�����
ʱ�䣺2021/8/22
˽�˽���Ⱥ��970353786
"""
import requests
import pyttsx3
print('����������˵�ģ�')
while True:
    a=input()
    url='https://api.ownthink.com/bot?appid=9ffcb5785ad9617bf4e64178ac64f7b1&spoken=%s'%a
    te=requests.get(url).json()
    data=te['data']['info']['text']
    print(data)
    ini= pyttsx3.init()
    shuo=ini.say(data)
    ini.runAndWait()