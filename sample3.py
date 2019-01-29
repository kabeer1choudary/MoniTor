import http.client

websites = ["skytorrents.lol","torrentznew.top","yts.ag","www.skidrowreloaded.com","torrents.me/site/btscene","isohunts.to","rarbg.to/index8.php","www.toorgle.com","torrents.me/site/torrent-downloads"]

def URL_check_http(url_now):
    r1 = http.client.HTTPConnection(url_now)
    # r1.request("GET","/")
    r1.request("HEAD","/")
    res1 = r1.getresponse()
    print(url_now, res1.status, res1.reason)

def URL_check_https(url_now):
    r2 = http.client.HTTPSConnection(url_now)
    # r2.request("GET","/")
    r2.request("HEAD","/")
    res2 = r2.getresponse()
    print(url_now, res2.status, res2.reason)

for i in websites:
    try:
        URL_check_http(i)
        URL_check_https(i)
    except:
        http.client.HTTPException
