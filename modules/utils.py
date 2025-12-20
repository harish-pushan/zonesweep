def change_the_url(url):
    if url[:8] == "https://":
        url = url[8:]
    elif url[:7] == "http://":
        url = url[7:]
    return url