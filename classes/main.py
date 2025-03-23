class nation:
    def __init__(self,name, language,CF):
        self.name = name
        self.language = language
        self.CF = CF
nation1 = nation("france","french","europe")
nation2 =nation("greece","greek","europe")
nation3 =nation("egypt","arabic","africa")

print(nation1.CF)
    
