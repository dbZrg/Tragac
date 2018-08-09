import numpy as np

def mapa():
    mapa = np.array(range(36)).reshape(6,6)
    print(mapa)
    mapa_str = np.chararray((6,6))
    mapa_str[:] = ' '
    start = int(input("Upisi broj gdje zelis da bude start:"))
    cilj = int(input("Upisi broj gdje zelis da bude cilj:"))
    zid_lokacija = input("Upisi na kojim brojevima zelis da budu prepreke/zid (npr. :1 7 13 19 25) :").split(" ")

    zid = [int(num) for num in zid_lokacija]
    for i in zid:
        for z in range(6):
            for x in range(6):
                if mapa[z, x] == i:
                    mapa[z, x] = 99
                    mapa_str[z,x] = '*'
                if mapa[z,x] == cilj:
                    mapa_str[z,x] = 'cilj'
                if mapa[z,x] == start:
                    mapa_str[z,x] = 'start'
    print(mapa_str)
    return mapa,zid,cilj,start,mapa_str

def index_u_akciju(izabrani_potez,stanje):
    if izabrani_potez == 0:
        # print ("Lijevo")
        return stanje-1
    if izabrani_potez == 1:
        # print ("Desno")
        return stanje + 1
    if izabrani_potez == 2:
        # print ("Gore")
        return stanje - 6
    if izabrani_potez == 3:
        # print("Dole")
        return stanje + 6

def moguci_potezi(stanje):
    redPoteza = R[stanje,]
    samoDozvoljeni = np.where(redPoteza >= 0)[1]
    return samoDozvoljeni

def izaberi_potez(moguci_potezi):
    akcija = int(np.random.choice(moguci_potezi,1))
    return akcija

def dozvoljeni_potezi_tablica(zid,cilj):
    SA = np.mat(np.zeros(shape=(36,4)))
    st=0

    gore= cilj - 6
    dole = cilj + 6
    lijevo = cilj - 1
    desno = cilj + 1
    if gore < 36:
       SA[gore,3]= 100
    if dole < 36:
       SA[dole, 2] = 100
    if lijevo < 36:
       SA[lijevo, 1] = 100
    if desno < 36:
       SA[desno,0]= 100


    for i in range(6):
        for j in range(6):

            if j == 0:
                SA[st,0] = -1000
            if j == 5:
                SA[st, 1] = -1000
            if i == 0:
                SA[st,2] = -1000
            if i == 5:
                SA[st, 3] = -1000
            st += 1

    for i in zid:
        gore= i - 6
        dole = i + 6
        lijevo = i - 1
        desno = i + 1
        if gore < 36:
            SA[gore,3]= -1000
        if dole < 36:
            SA[dole, 2] = -1000
        if lijevo < 36:
            SA[lijevo, 1] = -1000
        if desno < 36:
            SA[desno,0]= -1000

    

    return SA
def spremiQ(stanje,gamma,akcija,index_akcije):
    max_index = np.where(Q[akcija,] == np.max(Q[akcija,]))[1]       #Daje indekse najvecih vrijednosti u jednom redu Q[akcija,]
    #print ("najvece vrijednosti u Q tablici za next", max_index)
    #print (max_index.shape[0])
    if max_index.shape[0] > 1:                                       #Ako ima vise od 1 max vrijednosti tj njihovih indeksa onda random izaberi jednog od njih
        max_index = int(np.random.choice(max_index, size = 1))

    else:
        max_index = int(max_index)

    max_vrijednost = int(Q[akcija,max_index])
    #print("MAX:",max_vrijednost)
    Q[stanje,index_akcije] = R[stanje,index_akcije] + gamma * max_vrijednost             #algoritam

mapa = mapa()
print (mapa[0])

moguca_stanja = mapa[0][mapa[0]<98]
print(moguca_stanja)
R = dozvoljeni_potezi_tablica(mapa[1],mapa[2])                    #tablica dozvoljenih poteza
Q = R.copy()                                       #tablica za ucenje


cilj = mapa[2]          #Lokacija cilja 
gamma = 0.92
iteracije = 50000   #koraci za ucenje
print (R)

#Ucenje Q tablice
for i in range(iteracije):
    stanje = int(np.random.choice(moguca_stanja,1))
    moguci_pot = moguci_potezi(stanje)
    index_poteza = int(izaberi_potez(moguci_pot))
    akcija = index_u_akciju(index_poteza,stanje)
    spremiQ(stanje,gamma,akcija,index_poteza)

Q=Q/np.max(Q)

print (Q)
print ("Trening gotov")


pocetno_stanje = mapa[3]

while 1 :
    print ("------Mapa-----", "zid:* ")
    print (mapa[0])
    mapa[4]
    
    
    #Koristenje Q tablice
    koraci = 0
    put = [pocetno_stanje]
    while pocetno_stanje != cilj and koraci < 200:
         index_naj = np.where(Q[pocetno_stanje,] == np.max(Q[pocetno_stanje,]))[1]
         if index_naj.shape[0] > 1:
               naj_potez = int(np.random.choice(index_naj, size = 1))
         else:
             naj_potez = int(index_naj)
         sljed_stanje = index_u_akciju(naj_potez,pocetno_stanje)
         pocetno_stanje =  sljed_stanje
         put.append(pocetno_stanje)
         koraci += 1


    print ("Koraka do cilja:",koraci)
    print ("Najkraci put:",put)

    if pocetno_stanje == cilj:
        break










