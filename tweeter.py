import PySimpleGUI as sg

import json
from requests_oauthlib import OAuth1Session #OAuthライブラリの読み込み

url = "https://api.twitter.com/1.1/statuses/update.json" #ツイートポストエンドポイント

# Option設定とLayout
sg.theme('Dark Teal 12')

layout = [
    [sg.Text('Tweet From Python')],
    [sg.Text('CONSUMER_KEY', size=(21, 1)), sg.InputText('',size=(40, 1))],
    [sg.Text('CONSUMER_SECRET', size=(21, 1)), sg.InputText('',size=(40, 1))],
    [sg.Text('ACCESS_TOKEN', size=(21, 1)), sg.InputText('',size=(40, 1))],
    [sg.Text('ACCESS_TOKEN_SECRET', size=(21, 1)), sg.InputText('',size=(40, 1))],
    [sg.Text('Description', size=(21, 1)), sg.Multiline('', size=(40,5))],
    [sg.Text('', size=(21, 1)), sg.Submit(button_text='Tweet!!', size=(35, 1))]
]

# Window生成
window = sg.Window('Tweeter', layout)

#Event
while True:
    event, values = window.read()

    if event is None:
        break

    if event == 'Tweet!!':  #ボタンが押されたら認証+Tweet

        CK =  values[0]
        CS =  values[1]
        AT =  values[2]
        ATS = values[3]
        twitter = OAuth1Session(CK, CS, AT, ATS)  #認証処理

        tweet =  values[4]
        params = {"status" : tweet}
        res = twitter.post(url, params = params) #post送信

        if res.status_code == 200: #正常投稿:200
            print("Success.")
        else:  #200じゃなかったら失敗
            sg.Popup('Tweet Failed. ', 'Code : %d' %res.status_code,
            title='tweeter',
            button_type=0)
    

#終了処理
window.close()
