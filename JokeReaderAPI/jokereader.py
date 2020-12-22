import requests as req

# Get a joke from jokeapi and print to console.
# Not using 3rd party api wrappers.

# Settings Constants
JOKE_CAT_PROGRAMMING = 'Programming'
JOKE_CAT_DARK = 'Dark'
JOKE_CAT_PUN = 'Pun'
JOKE_CAT_SPOOKY = 'Spooky'
JOKE_CAT_CHRISTMAS = 'Christmas'

# Settings class to handle persistent flags
class settings():
    def __init__(self):
        self.nsfw = False
        self.religious = False
        self.political = False
        self.racist = False
        self.sexist = False
    def getSettings(self):
        string = "Joke settings: \n"
        string += "No NSFW: "+str(self.nsfw)+'\n'
        string += "No Religious: " + str(self.religious)+'\n'
        string += "No Political: "+str(self.political)+'\n'
        string += "No Racist: "+str(self.racist)+'\n'
        string += "No Sexist: "+str(self.sexist)+'\n'
        return string

jokeSettings = settings()

# jokeapi endpoint https://sv443.net/jokeapi/v2/joke/[Category/-ies]
def quickJoke():
    url = "https://sv443.net/jokeapi/v2/joke/any"
    jokeJson = req.get(url)
    if jokeJson.status_code!=200:
        print('ERROR'+str(jokeJson.status_code))
        return
    joke = jokeJson.json()
    if joke['type']=='single':
        print(joke["joke"])
    else:
        print(joke['setup'])
        print(joke['delivery'])
    print("Joke number: "+str(joke['id']))

def getJokeSpecific(id=0):
    url = "https://sv443.net/jokeapi/v2/joke/any"
    url+='?idRange=%s-%s' %(str(id),str(id))
    jokeJson = req.get(url)
    joke = jokeJson.json()
    if joke['error']:
        print("HTTP ERROR "+str(joke['code']))
        return
    if joke['type']=='single':
        print(joke["joke"])
    else:
        print(joke['setup'])
        print(joke['delivery'])
    print("This is joke number: "+str(joke['id']))

def setJokeFilters(no_nsfw=jokeSettings.nsfw, no_religious=jokeSettings.religious, no_political=jokeSettings.political, no_racist=jokeSettings.racist, no_sexist=jokeSettings.sexist):
    jokeSettings.nsfw = no_nsfw
    jokeSettings.religious = no_religious
    jokeSettings.political = no_political
    jokeSettings.racist = no_racist
    jokeSettings.sexist = no_sexist
    print(jokeSettings.getSettings())

def getJoke(category='any'):
    url = "https://sv443.net/jokeapi/v2/joke"
    url += "/"+category
    numFlags = 0
    blacklist = "?blacklistflags="

    if jokeSettings.nsfw:
        numFlags+=1
        blacklist += 'nsfw'
    if jokeSettings.religious:
        numFlags+=1
        blacklist += ',religious' if numFlags>1 else 'religious'
    if jokeSettings.political:
        numFlags+=1
        blacklist += ',political' if numFlags>1 else 'political'
    if jokeSettings.racist:
        numFlags+=1
        blacklist += ',racist' if numFlags>1 else 'racist'
    if jokeSettings.sexist:
        numFlags+=1
        blacklist += ',sexist' if numFlags>1 else 'sexist'
    if numFlags !=0:
        url+=blacklist
    jokeJson = req.get(url)
    joke = jokeJson.json()
    if joke['error']:
        print("HTTP ERROR "+str(joke['code']))
        return
    print("\nThis is joke number: "+str(joke['id'])+"\n")
    if joke['type']=='single':
        print(joke["joke"]+'\n')
    else:
        print(joke['setup'])
        print(joke['delivery']+'\n')
