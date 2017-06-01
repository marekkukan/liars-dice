<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-MML-AM_CHTML'>
</script>

## Všeobecné pravidlá
* súťažiť sa môže aj v tímoch
* deadline je 1.8.2017 23:59:59
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

## <a name="results"></a>Výsledky
![image](https://marekkukan.github.io/liars-dice/graph-2017-06-01.svg)

### Staré výsledky
![image](https://marekkukan.github.io/liars-dice/graph-2017-05-01.svg)

