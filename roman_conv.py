
# %%
"""
TODO:
* type check - int_to_roman -> int
* try - catch error handling
"""


def roman_to_integer(roman):

    values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    inputlist = list(str(roman))
    out = 0
    prev = 1000
    while len(inputlist) > 0:
        
        if inputlist[0] in values.keys():
            curr = values[inputlist.pop(0)]
            if curr > prev:
                out -= prev * 2
            
            out += curr

            prev = curr
            
        else:
            raise ValueError

    return out


def int_to_roman(i):

    # input csekk - ha az int(i) elhasal, rossz volt az input.
    i = int(i)

    # 3999-ig kezeljük a számokat
    # a 4000-hez 4db 'M' kéne, ami a szabályok szerint nem lehet
    if i >= 4000:
        raise ValueError

    # 1-es számjegyek
    # mivel a 10-es és 100-as ugyanilyen szerkezetben épül fel
    # csak más betűkkel, azokat a translate metódussal állítjuk elő
    r = {
        1: 'I',
        2: 'II',
        3: 'III',
        4: 'IV',
        5: 'V',
        6: 'VI',
        7: 'VII',
        8: 'VIII',
        9: 'IX',
        0: ''
    }

    # 1000-es helyiérték feltöltése 'M'-ekkel
    out = 'M' * (i // 1000)

    # 100-as helyiérték feltöltése
    # 100-as behelyettesítés: IVX -> CDM
    translate_100 = ''.maketrans('IVX','CDM')
    out += r[i // 100 % 10].translate(translate_100)

    # 10-es helyiérték feltöltése
    # 10-es behelyettesítés:  IVX -> XLC

    translate_10 = ''.maketrans('IVX','XLC')
    out += r[i // 10 % 10].translate(translate_10)

    # 1-es helyiérték feltöltése
    out += r[ i % 10 ]

    return out

    

# load sample roman numbers from file
romanlist = []
with open('roman_sample.txt', 'r', encoding='UTF-8') as file:
    while (line := file.readline().rstrip()):
        # sor szétvágása 
        # KÉRDÉS: hogyan lehet több egymást követő NEM SPACE szeparátort
        # egyetlenként kezelni - ahogy a paraméter nélküli .split dolgozik?
        l = line.split()
        if len(l) == 3:
            # kivágjuk csak a számokat és tuple-ként 
            # hozzáadjuk a romanlist-hez
            romanlist.append((int(l[0]),l[2]))


# test int to roman conversion
# print failing items from sample
for l in romanlist:
    r = int_to_roman(l[0])
    if r != l[1]:
        print(l,r)

# test roman to int conversion
# print failing items from sample
for l in romanlist:
    i = roman_to_integer(l[1])
    if i != l[0]:
        print(l,i)


