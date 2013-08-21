import random

s={}
s["Biss"]={"Schild verwenden":0.5,"Ausweichen":0,"Verstecken":1,"Heiltrank trinken":1}
s["Klaue"]={"Schild verwenden":1,"Ausweichen":0.5,"Verstecken":0,"Heiltrank trinken":1}
s["Feuerball"]={"Schild verwenden":0,"Ausweichen":1,"Verstecken":0.5,"Heiltrank trinken":1}
s["Schlaf"]={"Schild verwenden":0,"Ausweichen":0,"Verstecken":0,"Heiltrank trinken":0}
s["Brüllen"]={"Schild verwenden":2,"Ausweichen":2,"Verstecken":2,"Heiltrank trinken":2}
s["Schwefelatem"]={"Schild verwenden":1,"Ausweichen":1,"Verstecken":1,"Heiltrank trinken":1}
s["Ei legen"]={"Schild verwenden":0,"Ausweichen":0,"Verstecken":0,"Heiltrank trinken":0}

#neuer Befehl:
#s["#"]={"Schild verwenden":#,"Ausweichen":#,"Verstecken":#,"Heiltrank trinken":#}

#Schadensmodell:
#Heiltrank: 1
#Schild+Feuer: 0
#Schild+Klaue: 1
#Schild+Biss: 0.5
#Ausweichen+Feuer: 1
#Ausweichen+Klaue: 0.5
#Ausweichen+Biss: 0
#Verstecken+Feuer: 0.5
#Verstecken+Klaue: 0
#Verstecken+Biss: 1
#♥•★

#Geplante Aktionen:
#Drachenei
#Kritischer Treffer lässt den Drachen einmal aussetzten.
#Trank zur Erhöhung der kritischen Trefferchance
#Drache brüllt:


b="Enderdragon" #b=Boss
geg="Creeper"   #geg=Gegner
bhp=200
ghp=20
maxghp=20
maxs=20
mins=10
runde=0
crit=0.5



menu_a=["Aufgeben",
     "Normaler Angriff",
     "Ultimativer Angriff"]

menu_d=["Aufgeben",
     "Schild verwenden",
     "Ausweichen",
     "Verstecken",
     "Heiltrank trinken"]

b_action=["Feuerball",
         "Klaue",
         "Biss",
         "Schlaf",
         "Brüllen",
         "Schwefelatem",
         "Ei legen"]

    #Erster Teil der Runde.
while bhp >0:
    runde=runde+1
    print("★","Runde",runde)
    print()
    print(geg,"ist bereit.",geg,"hat noch",ghp,"Leben übrig.")
    print("♥"*int(ghp))
    print(b,"ist bereit.",b,"hat noch",bhp,"Leben übrig.")
    print("•"*int(bhp))
    while True:
        print()
        for x in menu_a:
            print(menu_a.index(x),":",x)
        print()
        x=input()
        if x < "0" or x > "2" or len(x)>1:
            print("Falsche Eingabe")
            continue
        else:
            print()
            break
    #Angriffsmenu, menu_a.
    if x=="0":
        print("Du rennst weg.")
        break
    elif x=="1":
        print(geg,"greift an!")
        schaden=random.randint(mins,maxs)
        print(b,"erleidet",schaden,"Schaden.")
        bhp=bhp-schaden
    elif x=="2":
        print(geg,"versucht einen ultimativen Angriff!")
        treffer=random.random()
        if treffer<crit:
            print("Ultimativer Angriff ist geglückt! Das war sehr effektiv!")
            schaden=maxs*3
            print(b,"erleidet",schaden,"Schaden.")
            bhp=bhp-schaden
        else:
            print("Ultimativer Angriff gescheitert.")
    if bhp<=0:
        print("Gratulation ,",b,"wurde besiegt!")
        break
    #Zweiter Teil der Runde.
    while True:
        print()
        for x in menu_d:
            print(menu_d.index(x),":",x)
        print()
        x=input()
        if x < "0" or x > "4" or len(x)>1:
            print("Falsche Eingabe")
            continue
        else:
            print()
            break
    #Verteidigungsmenu, menu_d.
    if x=="0":
        print("Du rennst weg.")
        break
    elif x=="1":
        schild=True
        print(geg,"duckt sich hinter seinem Schild!")
    elif x=="2":
        ausweichen=True
        print(geg,"weicht aus!")
    elif x=="3":
        verstecken=True
        print(geg,"versteckt sich!")
    elif x=="4":
        print(geg,"trinkt einen Heiltrank!")
        trank=random.randint(5,10)
        ghp=ghp+trank
        print(geg,"hat",trank,"Leben dazubekommen.")
        if ghp>20:
            ghp=maxghp
        print(geg,"hat jetzt",ghp,"Leben.")
    #Drachenaktionen
    action=random.choice(b_action)
    if action=="Feuerball":
        print(b,"setzt Feuerball ein!")
    elif action=="Klaue":
        print(b,"setzt Klaue ein!")
    elif action=="Biss":
        print(b,"setzt Biss ein!")
    elif action=="Schlaf":
        print(b,"ist eingeschlafen!")
    elif action=="Brüllen":
        print(b,"brüllt",geg,"an!")
    elif action=="Schwefelatem":
        print(b,"gähnt.")
        print("Mit seinem Schwefelatem verbrennt er die Augenbrauen von",geg,"!")
        print("Er sollte sich mal die Zähne putzen!")
    elif action=="Ei legen":
        print(b,"legt ein Ei.")
    #Schadensberechnung
    schaden=s[action][menu_d[int(x)]]
    print(geg,"erleidet",schaden,"Schaden.")
    print()
    ghp=ghp-schaden
    if ghp<=0:
        print(geg,"wurde besiegt.")
        break


