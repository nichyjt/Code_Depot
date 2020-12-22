import requests as req

# Get a joke from jokeapi and print to console.
# Not using 3rd party api wrappers.

# Setting Variables
JOKE_CAT_PROGRAMMING = 'Programming'
JOKE_CAT_DARK = 'Dark'
JOKE_CAT_PUN = 'Pun'
JOKE_CAT_SPOOKY = 'Spooky'
JOKE_CAT_CHRISTMAS = 'Christmas'
nsfw = False
religious=False
political=False
racist=False
sexist=False

# jokeapi endpoint https://sv443.net/jokeapi/v2/joke/[Category/-ies]
def quickJoke():
    jokeJson = req.get(url+"/any")
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
    return

def getJokeSpecific(id=0):
    url = "https://sv443.net/jokeapi/v2/joke/any"
    url+='?idRange%s-%s' %(str(id),str(id))

def setJokeFilters(no_nsfw=nsfw, no_religious=religious, no_political=political, no_racist=racist, no_sexist=sexist):
    nsfw = no_nsfw
    religious = no_religious
    political = no_political
    racist = no_racist
    sexist = no_sexist

def getJoke(category='any'):
    url = "https://sv443.net/jokeapi/v2/joke/any"
    url += "/"+category
    numFlags = 0
    blacklist = "?blacklistflags="
    if nsfw:
        ++numFlags
        blacklist += 'nsfw'
    if religious:
        ++numFlags
        blacklist += ',religious' if numFlags>1 else 'religious'
    if political:
        ++numFlags
        blacklist += ',political' if numFlags>1 else 'political'
    if racist:
        ++numFlags
        blacklist += ',racist' if numFlags>1 else 'racist'
    if sexist:
        ++numFlags
        blacklist += ',sexist' if numFlags>1 else 'sexist'
    if numFlags !=0:
        url+=blacklist
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