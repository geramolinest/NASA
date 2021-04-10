import requests as r


key = 'eMgZtSl1bRXcEogBabMmie9ZSvasmw4GMJjRir3N'
urlexample = 'https://api.nasa.gov/planetary/apod?api_key=eMgZtSl1bRXcEogBabMmie9ZSvasmw4GMJjRir3N'


def MarsWeather():
    url  = 'https://api.nasa.gov/insight_weather/?api_key='+key+'&feedtype=json&ver=1.0'
    response = r.get(url).json()
    return response
   
def getURL():
    url  = 'https://api.nasa.gov/insight_weather/?api_key='+key+'&feedtype=json&ver=1.0'
    return url
    
if __name__ == '__main__':
     MarsWeather()
