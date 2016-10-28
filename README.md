# Generátor kódu pro systém pøesunù z šifrovaèky Podzimní 2016

Použití (Python 3.0+): `python codewords_generator.py LETTER-TABLE-FILE DICTIONARY-FILE [MAX-WORD-LENGTH]`

kde:
* LETTER-TABLE-FILE je soubor obsahující kódovací tabulku ve formátu: PÍSMENO X Y, každé písmeno na vlastním øádku. X a Y vyjadøují posun v pøíslušné souøadnici, x roste smìrem doprava a y roste smìrem nahoru (napø. A -1 1 znaèí posun o 1 pole doleva a o 1 pole nahoru). Pøíklad tabulky:
  A -1 1
  B 1 2
  C 2 2
  ...
  Tabulka z Podzimní 2016 je k dispozici v souboru letter_table.txt.
  
* DICTIONARY-FILE je soubor se slovníkem, každé slovo na vlastním øádku. Diakritika bude zahozena a všechna písmena pøevedena na velká. Použitelný slovník èeských podstatných jmen (nekompletní) je v souboru dict.txt

* MAX-WORD-LENGTH je nepovinný parametr omezující délku použitých slov. Není-li pøítomen, je maximální délka nastavena na 100 (tedy prakticky neomezena).

## Výstup
 
Výstupem je soubor codewords.txt, v nìmž je pro každý vektor (x,y) dosažitelný pomocí nìjakého slova ze slovníku vypsán seznam slov, kterými lze tohoto vektoru dosáhnout, a to v sestupném poøadí podle "robustnosti" slova. Robustností se rozumí minimální hammingovská vzdálenost daného slova k libovolnému jinému slovu ze slovníku. Má-li tedy slovo robustnost aspoò 2, pak pøi øešení šifry chyba v jediném písmenu nikdy nedá jiné smysluplné slovo (resp. jiné slovo ze slovníku). Formát výstupu:

`X, Y [(SLOVO1, ROBUSTNOST1), (SLOVO2, ROBUSTNOST2), ...]` 

Pøiložený soubor 'codewords.txt' byl vygenerován pøíkazem `python 
codewords_generator.py letter_table.txt dict.txt 10`


POZN.:
Kvùli poèítání hammingovských vzdáleností má program èasovou složitost O(n^2), bìh tedy mùže nìjakou chvíli trvat (v závislosti na velikosti slovníku).



