import pandas as pd
import pytube
data = pd.read_json("watch-history.json")
compteur = 0
youtuber = []
pub = 0
compttt = 0

for i in data["details"]:
    if("name" in str(i)):
        #data = data.drop(data.index[compttt])
        pub += 1
    compttt +=1
print("Vous avez regarder "+str(pub)+" pub sur YT")
for i in data["subtitles"]:   
    try:
        for j in i[0]:
            if(j == "name"):
                youtuber.append(i[0]["name"])
    except:
        continue

print("Depuis que tu es sur YT tu as regarder  "+str(len(data))+" vidéos")
video = data["title"]


def enlever_doublons(tableau):
  resultat = []
  for element in tableau:
    if element not in resultat:
      resultat.append(element)
  return resultat


print("Tu as regarder "+str(len(enlever_doublons(youtuber)))+" youtuber différents")
def compter_types(tableau):
  compteurs = {}
  for element in tableau:
    if element not in compteurs:
      compteurs[element] = 1
    else:
      compteurs[element] += 1
  return compteurs
compt = compter_types(youtuber)
def findmaxvalue(tableau):
    max = 0
    res = []
    key = tableau.keys()
    for i in key:
        if(tableau[i]>max):
            max = tableau[i]
            res = [i,tableau[i]]

    return res
vid = compter_types(video)
print("TOP YOUTUBEUR")
for i in range(3):
    dictt = findmaxvalue(compt)
    compt.pop(dictt[0])
    print("Top "+str(i+1)+" : "+str(dictt[0])+" avec "+str(dictt[1])+" vidéos vues")
dictt2 = findmaxvalue(vid)
vid.pop(dictt2[0])
print("TOP VIDEO AVEC PUB")
for i in range(3):
    dictt2 = findmaxvalue(vid)
    vid.pop(dictt2[0])
    print("Top "+str(i+1)+" : "+str(dictt2[0])+" avec "+str(dictt2[1])+" vues")

def seconds_to_time(seconds):
        # Calculer le nombre d'heures, de minutes et de secondes
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60

        # Formater le résultat sous forme de chaîne de caractères HH:MM:SS
        print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")


url = data["titleUrl"]
dureepasse = 0
for i in url:
    try:
        yt = pytube.YouTube(i)

        # Récupérer la première vidéo de la liste des vidéos disponibles
        data = yt.streaming_data
        # Afficher la durée de la vidéo en secondes

        duree = int(data["formats"][0]["approxDurationMs"])
        dure = int(duree/1000- (duree/1000)%1)
        
        dureepasse += dure
    except:
        print("ERREUR")
        continue



print("VOUS AVEZ PASSER "+seconds_to_time(dureepasse)+" sur youtube")

data = pd.read_excel("sortie.xlsx")
video = data["title"]
vid = compter_types(video)
dictt2 = findmaxvalue(vid)
vid.pop(dictt2[0])
print("TOP VIDEO SANS PUB")
for i in range(3):
    dictt2 = findmaxvalue(vid)
    vid.pop(dictt2[0])
    print("Top "+str(i+1)+" : "+str(dictt2[0])+" avec "+str(dictt2[1])+" vues")

