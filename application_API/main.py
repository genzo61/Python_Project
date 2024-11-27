import requests
url = "http://api.weatherapi.com/v1/current.json"
api_key = "89e40be99a8a4c23bbb170814242611"

konum = input("konum : ")
response = requests.get(url,params={
    "key": api_key,
    "q": konum,
    "lang": "tr"
})
sonuc = response.json()
sehir = sonuc["location"]["name"]
havadurumu = sonuc["current"]["temp_c"]
text = sonuc["current"]["condition"]["text"]
print(str(sehir) + " " + str(havadurumu) + " " + str(text))