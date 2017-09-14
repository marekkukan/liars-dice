<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-MML-AM_CHTML'></script>

## Výsledky
![image](https://marekkukan.github.io/liars-dice/graph-2017-08-21.svg)

### Výsledky duelov
<div style="overflow-x: auto;">
<table style="margin-left: auto; margin-right: auto; text-align: center;">
<tr><th></th><th>marek</th><th>majka</th><th>matus</th><th>nukeman</th><th>andrej</th><th>player_smart.py</th></tr>
<tr><th>marek</th><td>-</td><td>560:440</td><td>769:231</td><td>887:113</td><td>823:177</td><td>934:66</td></tr>
<tr><th>majka</th><td>440:560</td><td>-</td><td>675:325</td><td>798:202</td><td>807:193</td><td>808:192</td></tr>
<tr><th>matus</th><td>231:769</td><td>325:675</td><td>-</td><td>479:521</td><td>956:44</td><td>921:79</td></tr>
<tr><th>nukeman</th><td>113:887</td><td>202:798</td><td>521:479</td><td>-</td><td>947:53</td><td>802:198</td></tr>
<tr><th>andrej</th><td>177:823</td><td>193:807</td><td>44:956</td><td>53:947</td><td>-</td><td>465:535</td></tr>
<tr><th>player_smart.py</th><td>66:934</td><td>192:808</td><td>79:921</td><td>198:802</td><td>535:465</td><td>-</td></tr>
</table>
</div>

---
---
---

## Všeobecné pravidlá
* súťažiť sa môže aj v tímoch
* deadline je 20.8.2017 23:59:59
* 1\. a 15. deň v mesiaci budú zverejňované priebežné [výsledky](#results)

## Pravidlá hry
* bude sa hrať naša verzia Kociek, ktorú asi všetci poznáte
* poradie hráčov je na začiatku každej hry náhodne určené
* prvé kolo začína prvý hráč v poradí, ďalšie kolá začína vždy hráč, ktorý naposledy prehral (príp. ak vypadol, tak hráč za ním)
* ak niekto spraví neplatný ťah, alebo nespraví ťah v časovom limite, tak vypadáva z hry a hra pokračuje ďalej novým kolom (v [protokole](https://github.com/marekkukan/liars-dice/blob/master/protocol.txt) sú uvedené všetky možné neplatné ťahy)
* turnaj bude mať $$10^4$$ hier, ak na konci nebude nikto *nespochybniteľný* víťaz, tak sa bude hrať nový turnaj, ktorý bude mať $$10^5$$ hier, ak ani potom nebude *nespochybniteľný* víťaz, tak nový turnaj o $$10^6$$ hier, atď. až kým nebude *nespochybniteľný* víťaz, alebo kým turnaj nebude trvať dlhšie ako 24 hodín
* víťaz je *nespochybniteľný*, ak je veľmi nepravdepodobné, že vyhral len vďaka šťastiu
  * presná definícia:  
Nech $$n$$ je počet hráčov a nech $$p_1, p_2$$ sú počty vyhratých hier prvého a druhého hráča.
Ak $$(p_1 - p_2)^2 / (p_1 + p_2) > q_{\chi^2(n-1)}(0.95)$$, tak víťaz je *nespochybniteľný*.  
(Tá podmienka je zamietacie kritérium pre [test dobrej zhody](https://cs.wikipedia.org/wiki/Test_dobr%C3%A9_shody) hypotézy, že druhý hráč je rovnako dobrý ako prvý.)  
(Napr. ak sú výsledky [500, 400, 100], tak víťaz je nespochybniteľný. Ak sú výsledky [50, 30, 20], tak nie je.)

## Ako má vyzerať bot
* môže byť nakódený v ľubovoľnom programovacom jazyku
* submit-uje sa tak, že mi pošleš mailom zdroják a ja si to u seba skompilujem (keďže ja tiež súťažím, zdrojáky si nebudem pozerať (takže dúfam, že mi nepodstrčíš dáky vírus :-P))
* v [git-repozitári](https://github.com/marekkukan/liars-dice) sú ukážky jednoduchých hráčov v jazykoch C, Java, JavaScript, Python, Scheme
* bot dostáva info o hre na štandardný vstup a píše svoje ťahy na štandardný výstup, podľa [tohto protokolu](https://github.com/marekkukan/liars-dice/blob/master/protocol.txt) (na pochopenie protokolu odporúčam použiť [tento skript](https://github.com/marekkukan/liars-dice/blob/master/play.sh), pomocou ktorého si môžeš zahrať manuálne v príkazovom riadku proti botom)
* po každom ťahu treba flush-núť stdout (ale možno sa to flush-uje automaticky, ako napr. v Jave, príp. Python s prepínačom `-u` to tiež robí automaticky)
* boti musia hrať rýchlo, aby bolo možné odohrať veľa hier .. neviem dobre odhadnúť, ako rýchlo/pomaly to bude bežať, ale chcel by som, aby to zvládlo aspoň 10000 hier za 24 hodín .. takže časový limit je max. 0.1 sekundy na ťah (ale možno sa zmení)
* pamäťový limit je 100MB (to je asi nekonečno, ale keby niekto náhodou potreboval viac, tak sa to môže zmeniť)

## Ceny
* každý kto porazí hráča [player_smart.py](https://github.com/marekkukan/liars-dice/blob/master/player_smart.py) má u mňa pivo/kofolu/tekvicový džús/prostedakydrink
* víťaz súťaže okrem toho vyhrá aj večnú slávu a (s jeho dovolením) jeho bot bude použitý v appke, ktorú možno raz spravím

## <a name="results"></a>Výsledky cvičných kôl
![image](https://marekkukan.github.io/liars-dice/graph-2017-08-15.svg)
![image](https://marekkukan.github.io/liars-dice/graph-2017-07-19.svg)
![image](https://marekkukan.github.io/liars-dice/graph-2017-07-01.svg)
![image](https://marekkukan.github.io/liars-dice/graph-2017-06-15.svg)
![image](https://marekkukan.github.io/liars-dice/graph-2017-06-01.svg)
![image](https://marekkukan.github.io/liars-dice/graph-2017-05-01.svg)

