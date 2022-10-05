from collections import deque

graph = {}
searched = []

graph['olufunmi'] = ['deola', 'wale', 'florence', 'shola']
graph['deola'] = ['joy', 'mike']
graph['wale'] = ['ayo', 'funke']
graph['florence'] = ['dolapom']
graph['shola'] = []
graph['joy'] = []
graph['mike'] = []
graph['ayo'] = []
graph['funke'] = []
graph['dolapom'] = []


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person[-1] == 'm':
                print(person, "is a mango seller")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
                print(person, "is not a mango seller")
    return False


print(search("olufunmi"))
