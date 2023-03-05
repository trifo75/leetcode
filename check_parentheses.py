
# %%

class Solution:

    # szótárba felvesszük a vizsgálandó zárójelek
    # nyitó és záró verzióját

    rebraces = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
            
    def isValid(self, s: str) -> bool:

        # verem a zárójelek számára
        stack = []

        # végigjárjuk az input stringet
        for char in s:
            # ha a char egy nyitó zárójel, akkor letesszük a verembe
            if char in self.rebraces.values(): stack.append(char)

            # ha a char egy záró zárójel, akkor...
            if char in self.rebraces.keys():
                # megnézzük, hogy üres-e a verem 
                if stack:
                    # ha nem üres, akkor kiveszünk egyet és megnézzük, hogy
                    # char párja-e. Ha nem, akkor az input hibás
                    if stack.pop() !=  self.rebraces[char]: return False
                else:
                    # ha üres volt a lista, akkor az input hibás
                    return False

        # A srting végére érve, ha a verem üres, akkor a string OK
        # ha nem, akkor hibás
        if not stack:
            return True
        else:
            return False 


        
    braces = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    def isValid_resorcewaste(self, s: str) -> bool:

        if not isinstance(s,str): raise ValueError

        #print("Rekurzió indul. Paraméter: \"{}\"".format(s))

        length = len(s)


        # zárójelpár kereséshez 
        #   openpos: az aktuális nyitó zárójel pozíciója
        #   closepos: az openpos-hoz tartozó záró zárójel helye
        #   braces: a nyitó zárójeltól számolva keressük a kifejezés végét
        #       egy nyitó: +1
        #       egy záró:  -1
        #       ha lemegy nullára, akkor megvan

        openpos = 0
        while openpos < length:
            #print("Külsö ciklus indul. openpos: {}".format(openpos))
            # ha záró zárójellel találkozunk, akkor az biztos rossz 
            if s[openpos] in list(self.braces.values()): return False
            
            # ha nyitó zárójellel találkozunk, akkor megkeressük a záró párját
            if s[openpos] in list(self.braces.keys()):

                # ha a string végén vagyunk és épp kinyitottunk egy zárójelet, akkor az mindenképp rossz
                if openpos >= length -1: return False

                # kikeressük a használandó nyitó és záró zárójelet
                # ez inkább csak az olvashatóság miatt van
                bropen = s[openpos]
                brclose = self.braces[bropen]

                # megkeressük az adott nyitó zárójel záró párját
                closepos = openpos
                bracecount = 0
                for closepos in range(openpos,length):
                    #print("belső ciklus indul. Openpos: {}, closepos: {}, bracecount: {}".format(openpos,closepos,bracecount))
                    if s[closepos] == bropen:  bracecount += 1 # nyitó: +1
                    if s[closepos] == brclose: bracecount -= 1 # záró:  -1

                    if bracecount == 0: 
                        # amikor a braces = 0, akkor megvan a kinyitott zárójel párja
                        # a kettő közti szöveget rekurzívan megvizsgáljuk

                        # ha a megtalált zárójelben lévő szöveg érvénytelen,
                        # akkor nyilván a teljes kifejezés érvénytelen
                        if not self.isValid(s[openpos+1:closepos]): return False

                        # ha érvényes volt a kifejezés, akkor 
                        # megszakítjuk a for ciklust és a záró után 
                        # folytatjuk a keresést a köv. zárójelpárra
                        openpos = closepos + 1
                        break

                    if bracecount != 0 and closepos == length -1: return False
                    
            # ha nem volt zárójel, akkor csak megyünk egyet előre az
            # openpos változóval       
            else:
            
                openpos += 1

        # a ciklusban feldolgoztunk mindent es nem jött vissza hiba
        # akkor jók vagyunk
        return True

                






testcases = [
    '{{}',
    '])}',
    ']',
    '(])',
    '[](',
    '',
    '[(aa){bb}]{ww(qq)}ee',
    '()',
    '([])',
    'ee(()(aa))(eee)',
    '()[]{}',
    '(])',
    '{}'
]

s = Solution()

for case in testcases:
    if s.isValid(case):
        print("\"{c}\" rendben van.".format(c=case))
    else:
        print("\"{c}\" kifejezés hibás.".format(c=case))

# %%