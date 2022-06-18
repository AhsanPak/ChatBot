import requests
url = 'https://127.0.0.1:5000/talktohelp.herokuapp.com/webhooks/rest/webhook'
myobj = {
"message": "hi",
"sender": 1,
}
x = requests.post(url, json = myobj)
print(x.text)