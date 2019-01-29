import requests

websites = ["https://skytorrents.lol","https://torrentznew.top","https://yts.ag","https://www.skidrowreloaded.com","https://torrents.me/site/btscene","https://isohunts.to","https://rarbg.to/index8.php","http://www.toorgle.com","https://torrents.me/site/torrent-downloads"]

# def url_check(url):
#     try:
#         req = requests.get(url)
#     except:
#         requests.exceptions.RequestException
#     if req.status_code == 200:
#         print("site is working")
#         print(req.headers)
#     else:
#         print("site is not working")

# websites = open("websites.txt", 'r')
for site in websites:
    # url_check(site)
    try:
        req = requests.get(site)
        print(site, req.status_code, " - site is working")
        # print("\n", req.headers, "\n")
    except:
        requests.exceptions.RequestException
        print(site, " - error loading the site")
    # url_check(site)
#     if url_check.status == 200:
#         print("site is working")
#     else:
#         print("site is not working")
