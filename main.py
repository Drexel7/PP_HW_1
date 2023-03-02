if __name__ == "__main__":
    f = open(r"D:\PP\LABORATOR\LAB1\Tema\readme.txt","r")
    x = f.read();

    x = x.replace('!', '')
    x = x.replace('?', '')
    x = x.replace('.', '')
    x = x.replace(',', '')
    x = x.replace(':', '')
    x = x.replace(';', '')
    x = x.replace('\'', '')
    x = x.replace('\"', '')

    sir= ""
    for a in x:
        if not a.islower():
            sir += a

    sir_final =""
    for i in range(len(sir)-1):
        if sir[i] != ' ' or sir[i + 1] != ' ':  #daca avem 3 spatii consecutive apoi un alt caracter, primele doua spatii se vor sterge
            sir_final += sir[i]

    print(sir_final)
    f.close()