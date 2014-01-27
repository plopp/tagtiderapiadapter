import base64
import urllib2
import json

def main():
    url = "http://api.tagtider.net/v1/stations.json"
    passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
    passman.add_password(None, url, "tagtider", "codemocracy")
    opener = urllib2.build_opener(urllib2.HTTPBasicAuthHandler(passman),
                         urllib2.HTTPDigestAuthHandler(passman))

    urllib2.install_opener(opener)
    pagehandle = urllib2.urlopen(url)
    
    stations = json.load(pagehandle)
    for station in stations['stations']['station']:
        print station['name']

if  __name__ =='__main__':main()
