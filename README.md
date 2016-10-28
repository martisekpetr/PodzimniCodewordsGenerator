# Gener�tor k�du pro syst�m p�esun� z �ifrova�ky Podzimn� 2016

Pou�it� (Python 3.0+): `python codewords_generator.py LETTER-TABLE-FILE DICTIONARY-FILE [MAX-WORD-LENGTH]`

kde:
* LETTER-TABLE-FILE je soubor obsahuj�c� k�dovac� tabulku ve form�tu: P�SMENO X Y, ka�d� p�smeno na vlastn�m ��dku. X a Y vyjad�uj� posun v p��slu�n� sou�adnici, x roste sm�rem doprava a y roste sm�rem nahoru (nap�. A -1 1 zna�� posun o 1 pole doleva a o 1 pole nahoru). P��klad tabulky:
  A -1 1
  B 1 2
  C 2 2
  ...
  Tabulka z Podzimn� 2016 je k dispozici v souboru letter_table.txt.
  
* DICTIONARY-FILE je soubor se slovn�kem, ka�d� slovo na vlastn�m ��dku. Diakritika bude zahozena a v�echna p�smena p�evedena na velk�. Pou�iteln� slovn�k �esk�ch podstatn�ch jmen (nekompletn�) je v souboru dict.txt

* MAX-WORD-LENGTH je nepovinn� parametr omezuj�c� d�lku pou�it�ch slov. Nen�-li p��tomen, je maxim�ln� d�lka nastavena na 100 (tedy prakticky neomezena).

## V�stup
 
V�stupem je soubor codewords.txt, v n�m� je pro ka�d� vektor (x,y) dosa�iteln� pomoc� n�jak�ho slova ze slovn�ku vyps�n seznam slov, kter�mi lze tohoto vektoru dos�hnout, a to v sestupn�m po�ad� podle "robustnosti" slova. Robustnost� se rozum� minim�ln� hammingovsk� vzd�lenost dan�ho slova k libovoln�mu jin�mu slovu ze slovn�ku. M�-li tedy slovo robustnost aspo� 2, pak p�i �e�en� �ifry chyba v jedin�m p�smenu nikdy ned� jin� smyslupln� slovo (resp. jin� slovo ze slovn�ku). Form�t v�stupu:

`X, Y [(SLOVO1, ROBUSTNOST1), (SLOVO2, ROBUSTNOST2), ...]` 

P�ilo�en� soubor 'codewords.txt' byl vygenerov�n p��kazem `python 
codewords_generator.py letter_table.txt dict.txt 10`


POZN.:
Kv�li po��t�n� hammingovsk�ch vzd�lenost� m� program �asovou slo�itost O(n^2), b�h tedy m��e n�jakou chv�li trvat (v z�vislosti na velikosti slovn�ku).



