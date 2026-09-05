import requests

class AudioTag():
    def __init__(self, apikey):
        self.apikey = apikey

        self.APILINK = "https://audiotag.info/api"
    

    def identify(self, file):
        r = requests.post(self.APILINK, data={
            'apikey': self.apikey, 'action': 'identify'},
            files={'file': file})
        print(r.text)
       
        if (not r.json()['success']):
            return None

        return r.json()


    def getResult(self, token):
        if (token == None): return None

        while True:
            r = requests.post(self.APILINK, data={
                'apikey': self.apikey, 'action': 'get_result',
                'token': token})

            if (r.json()['result'] != 'wait'):
                break

        if (r.json()['result'] != 'found'):
            return None

        return r.json()


    def identifyAndGetResult(self, file):
        identify = self.identify(file)
        if (identify == None): return None
        return self.getResult(identify['token'])
