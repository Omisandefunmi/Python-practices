voted = {}


def check_voters(name):
    if voted.get(name):
        return "Kick them out"
    else:
        voted[name] = True
        return "Let them vote"


print(check_voters("funmi"))
print(check_voters("kunmi"))
print(check_voters("funmi"))
print(voted)


cache = {}


def get_data_from_url(url):
    data = url
    return data


def cache_urls(url):
    if cache.get(url):
        return cache[url]
    else:
        data = get_data_from_url(url)
        cache[url] = data
        return data

