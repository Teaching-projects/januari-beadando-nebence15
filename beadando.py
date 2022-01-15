nyelv = input("EN/HU?")

def koszones(language="HU"):
    if language == "HU":
        return "Szia, ez egy szókereső játék.(Magyar szavak) Próbáld meg minél kevesebb hibával megoldani!"
    elif language == "EN":
        return "Hi, this is a word search game.(Hungarian words) Try to solve it with as few errors as possible!"

def tudnivalok(language="HU"):
    if language == "HU":
        return "A megadott betubol legalabb 9 szot kell kitalalnod, hogy veget erjen a jatek. Minden rossz valasz utan -1 pontot kapsz, minden jo valasz utan +1 pont jar."
    elif language == "EN":
        return "You must guess at least 9 words from the given letter to play the game. You get -1 point for every bad answer, +1 point for every good answer."





pontok = 0
betu = ["a","m","b","l","k","r"]


megoldas = ["alma","mamba","baba","kar","akar","alkar","lakk","bal","rak","kamra","karma"]



while pontok < 5:
    tipp = input("Add meg a tipped ")
    if tipp in  megoldas:
        pontok += 1
    elif tipp!= megoldas: 
        pontok -= 1
    

print(pontok,"pontot tudtál szerezni.")
