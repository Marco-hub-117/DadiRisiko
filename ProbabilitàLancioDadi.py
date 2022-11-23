import random

def lista_probabilità_per_faccia(nLanci = 100000):
    lanci = []

    for i in range(0,nLanci):
        lanci.append(random.randint(1,6))

    occorrenzePerValore = [0, 0, 0, 0, 0, 0]

    for lancio in lanci:
        occorrenzePerValore[lancio - 1 ] = occorrenzePerValore[lancio - 1 ] + 1

    print(occorrenzePerValore)

    probabilitàPerValore = []

    for occorrenza in occorrenzePerValore:
        probabilitàPerValore.append(occorrenza/nLanci*100)

    return probabilitàPerValore
    

def stringa_formattata_probabilità(lista_probabilità):   
    
    stringaFormattata = ""
    
    for i in range(1,7):
        stringaFormattata += f"probabilità di {i}: {lista_probabilità[i-1]}% \n"

    return stringaFormattata

def main():

    probabilitàPerFaccia = lista_probabilità_per_faccia(10000)

    stringaFormattata = stringa_formattata_probabilità(probabilitàPerFaccia)

    print(stringaFormattata)



if __name__ == '__main__':
    main()
