# Generátor kódových slov pro systém přesunů z šifrovačky Podzimní 2016
Více o systému zde: http://www.sifrovacihra.cz/informace.aspx (credits: Martin Mach)

## Requirements
Python 3.0+

## Formát vstupu
`python codewords_generator.py LETTER-TABLE-FILE DICTIONARY-FILE [MAX-WORD-LENGTH]`

kde:
* LETTER-TABLE-FILE je soubor obsahující kódovací tabulku ve formátu: PÍSMENO X Y, každé písmeno na vlastním řádku. X a Y vyjadřují posun v příslušné souřadnici, x roste směrem doprava a y roste směrem nahoru (např. A -1 1 značí posun o 1 pole doleva a o 1 pole nahoru). Příklad tabulky:  
  A -1 1  
  B 1 2  
  C 2 2  
  ...  
  Tabulka z Podzimní 2016 je k dispozici v souboru **letter_table.txt**.
  
* DICTIONARY-FILE je soubor se slovníkem, každé slovo na vlastním řádku. Diakritika bude zahozena a všechna písmena převedena na velká. Použitelný slovník českých podstatných jmen (nekompletní) je v souboru **dict.txt**

* MAX-WORD-LENGTH je nepovinný parametr omezující délku použitých slov. Není-li přítomen, je maximální délka nastavena na 100 (tedy prakticky neomezena).

## Výstup
 
Výstupem je soubor **codewords.txt**, v němž je pro každý vektor (x,y) dosažitelný pomocí nějakého slova ze slovníku vypsán seznam slov, kterými lze tohoto vektoru dosáhnout, a to v sestupném pořadí podle *robustnosti* slova. Robustností se rozumí minimální hammingovská vzdálenost daného slova k libovolnému jinému slovu ze slovníku. Má-li tedy slovo robustnost aspoň 2, pak při řešení šifry chyba v jediném písmenu nikdy nedá jiné smysluplné slovo (resp. jiné slovo ze slovníku). Formát výstupu:

`X, Y [(SLOVO1, ROBUSTNOST1), (SLOVO2, ROBUSTNOST2), ...]` 

Přiložený soubor **codewords.txt** byl vygenerován příkazem `python codewords_generator.py letter_table.txt dict.txt 10`


***

POZN.:
Kvůli počítání hammingovských vzdáleností má program časovou složitost O(n^2), běh tedy může nějakou chvíli trvat (v závislosti na velikosti slovníku).



