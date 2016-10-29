import sys
from unidecode import unidecode
from operator import itemgetter


# odstrani diakritiku a prevede na velka pismena
def convert(s):
    return unidecode(s).upper()


# nacte tabulku pismena ze souboru, format: PISMENO X Y (kazde pismeno na vlastnim radku)
def load_letter_table(filename):
    table = {}
    with open(filename) as f:
        for line in f:
            [letter, x, y] = line.split()
            table[letter] = (int(x), int(y))
    return table


# nacte slovnik ze souboru, kazde slovo na vlastnim radku
def load_dictionary(filename):
    dictionary = []
    with open(filename) as f:
        for line in f:
            if len(line.strip()) <= max_length:
                dictionary.append(convert(line.strip()))
    return dictionary


# spocte cilovy vektor pro slovo
def get_target_vector(word, table):
    target_x, target_y = 0, 0
    for letter in word:
        if letter not in table:
            return None
        (x, y) = table[letter]
        target_x += x
        target_y += y
    return target_x, target_y


# spocte hammingovskou vzdalenost dvou stejne dlouhych slov (= pocet odlisnych pismen)
def hamming(s1, s2):
    return sum(a != b for a, b in zip(s1, s2))


# spocte minimum z hammingovskych vzdalenosti daneho slova ke vsem ostatnim slovum v korpusu
def get_min_hamming_distance(word, dictionary):
    min_distance = len(word) + 1
    for other in dictionary:
        if len(word) == len(other) and word != other:
            dist = hamming(word, other)
            if dist < min_distance:
                min_distance = dist
    return min_distance


# HLAVNI SKRIPT

# parametry prikazove radky: letter_table_file dictionary_file [max_word_length]
if len(sys.argv) < 3:
    exit()
table_file = sys.argv[1]
dict_file = sys.argv[2]

max_length = 100
if len(sys.argv) >= 4:
    max_length = int(sys.argv[3])

# nacti tabulku
table = load_letter_table(table_file)
# nacti slovnik
dictionary = load_dictionary(dict_file)

# codewords obsahuje pro kazdy vektor seznam slov, ktere na nej vedou (serazene sestupne podle robustnosti)
# (robustnost = minimalni hamingovska vzdalenost ke zbytku slovniku)
codewords = {}
for word in dictionary:
    vector = get_target_vector(word, table)
    if vector is not None:
        distance = get_min_hamming_distance(word, dictionary)
        if vector in codewords:
            codewords[vector].append((word, distance))
        else:
            codewords[vector] = [(word, distance)]

# vypise vysledek do souboru
with open("codewords.txt", 'w') as f:
    for key in sorted(codewords):
        sor = sorted(codewords[key], key=itemgetter(1), reverse=True)
        f.write(str(key[0]) + ", " + str(key[1]) + " [")
        for e in sor:
            f.write("(" + str(e[0]) + ", " + str(e[1]) + "), ")
        f.write("]\n")

