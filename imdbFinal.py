import requests
from bs4 import BeautifulSoup

# List of Genre
# If you find any Genre missing please append to this list
genreList = ["Action", "Adventure", "Animation", "Biography", "Comedy", "Crime", "Documentary", "Drama", "Family",
             "Fantasy", "Film-Noir", "History", "Horror", "Music", "Musical", "Mystery", "Romance", "Sci-Fi",
             "Short", "Sport", "Superhero", "Thriller", "War", "Western"]

print "Waiting for your input..."
print "ID in form of ttxxxxx.."

# Get the soup for Movie data
try:
    input = raw_input("Enter IMDB ID: ")
    url = "http://www.imdb.com/title/{}".format(input)
    print "Got the Movie"
    print "Processing..."
    req = requests.get(url)
    cont = req.content
    soup = BeautifulSoup(cont, "html.parser")
    print "Processing is done"

except Exception as exp:
    print exp

posterData = soup.find_all('div', attrs={'class':'poster'})
posterLink = posterData[0].find_all('img')[0]['src']
print "Poster Link"
print posterLink

titleData = soup.find_all('div', attrs={'class':'title_wrapper'})
title = titleData[0].find_all('h1')[0].text
if "(" in title:
    title = titleData[0].find_all('h1')[0].text.split("(", 1)[0]
    print "Movie Title"
    print title
else:
    print "Movie Title"
    print title

ratingsData = soup.find_all('div', attrs={'class':'ratingValue'})
ratings = ratingsData[0].find_all('strong')[0].text
print "Movie Ratings"
print ratings + "/10"

genreData = soup.find_all('div', attrs={'class':'subtext'})
temp = genreData[0].text.split("\n")
print "Movie duration & Movie Genre & Release Date"
for t in temp:
    try:
        t = t.strip()
        int(t[0])
        print t
    except Exception as exp:
        pass

    try:
        t = t.strip().strip(",")
        if t in genreList:
            print t
    except Exception as exp:
        pass

totalRatingsData = soup.find_all('span', attrs={'class':'small'})
totalRatings = totalRatingsData[0].text
print "Total Votes"
print totalRatings

# Get the soup for Credit
try:
    cURL = url + "/fullcredits?ref_=tt_cl_sm#cast"
    print "Got the information for Cast & Crew"
    print "Processing..."
    cReq = requests.get(cURL)
    cCont = cReq.content
    cSoup = BeautifulSoup(cCont, "html.parser")
    print "Processing is done"

except Exception as exp:
    print exp

tableData = cSoup.find_all('table')
lists = []
row = []
for table in tableData:

    row = table.text.split("\n")
    lists.append(row)

dire = lists[0]
writers = lists[1]
actors = lists[2]

print "Director"
print dire[9].strip()

abc = []
for w in writers:
    w = w.strip()
    if "..." in w:
        continue
    else:
        abc.append(w)

xyz = [i for i in abc if i != ""]
print "Writers of the Movie"
print xyz

temp = []
for a in actors:
    a = a.strip()
    if "..." in a:
        continue
    else:
        temp.append(a)

x = [i for i in temp if i != ""]
print "Actor & Movie Name"
print x
