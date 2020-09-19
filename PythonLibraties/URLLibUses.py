import urllib.request as urlreq
import webbrowser

#weburl = urlreq.urlopen('https://www.google.com/')
weburl = urlreq.urlopen('https://www.bbc.com/hindi')
html = weburl.read()
data = weburl.getcode()
url = weburl.geturl()
hd = weburl.headers
info = weburl.info()

print('The url is -  ', url)
print("HTTP Status is - ", data)
print("Header return --\n", hd)
print("Info() return --\n", info)
print("Now opening the url - ", url)
#webbrowser.open_new(url)
