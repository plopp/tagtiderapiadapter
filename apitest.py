import base64
import urllib2
import json



def main():
    #print getStations()
    getDepartures(getIdFromName('Hovmantorp'))

def auth(url):
    passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
    passman.add_password(None, url, "tagtider", "codemocracy")
    opener = urllib2.build_opener(urllib2.HTTPBasicAuthHandler(passman),
                         urllib2.HTTPDigestAuthHandler(passman))
    urllib2.install_opener(opener)
    pagehandle = urllib2.urlopen(url)
    return pagehandle

def getStations():
    pagehandle = auth("http://api.tagtider.net/v1/stations.json")    
    stations = json.load(pagehandle)
    return stations['stations']['station']

def getIdFromName(name):
    for stations in getStations():
        if(stations['name'] == name):
            return stations['id']
    return -1

def getDepartures(stationId):    
    if stationId > -1:
        url = "http://api.tagtider.net/v1/stations/%s/transfers/departures.json" %(stationId)
        pagehandle = auth(url)    
        deps = json.load(pagehandle)
        print deps
        for transfer in deps['station']['transfers']['transfer']:
            print transfer['destination'],' ',transfer['departure'],' Track:',transfer['track']

if  __name__ =='__main__':main()
