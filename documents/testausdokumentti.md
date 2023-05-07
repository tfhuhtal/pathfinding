# Testaus dokumentti

## Testaus

### Dijkstran algoritmi

Dijkstran lyhimmän polun algoritmia on testattu yksikkötesteillä mitkä kattavat kaikki kahdeksan suuntaa. Myös kaikki oikeellisuus tarkistukset on tehty sekä testattu, että algoritmi toimii oikein myös silloin kun maali on esteen päällä. Algoritmia on testattu myös kartalla missä on vain yksi mahdollinen reitti.

### A* algoritmi

A* algoritmi on testattu samalla tavalla kuin Dijkstran algoritmi. A* algoritmin testit kattavat myös kaikki kahdeksan suuntaa. Myös kaikki oikeellisuus tarkistukset on tehty sekä testattu, että algoritmi toimii oikein myös silloin kun maali on esteen päällä. Algoritmia on testattu myös kartalla missä on vain yksi mahdollinen reitti. A* algoritmia on myös testattu 

### JPS algoritmi

Jump point search -algoritmia on tällä hetkellä testattu osittain samoilla testeillä kuin A* algoritmia. Tämä johtuu siitä, että JPS algoritmi on A* algoritmin muokkaus.

## Testikattavuus

![image info](./images/test_coverage.png)

Kuten kuvasta näkee testikattavuus on 99%%, vain joitakin jps algoritmin kohtia ei ole testattu kokonaan. Tämä johtuu siitä, että jps algoritmin testaaminen on haastavaa ja vielä en ole löytänyt sopivaa tapaa testata sitä kattavasti.

## Testaus ohjeet

Projekti toimii Python versiolla ^3.8. Voit testata ohjelmaa asentammalla ensin Poetryn riippuvuudet komennolla:
```bash
poetry install
```
Tämän jälkeen testit voi ajaa komennolla:
```bash
poetry run invoke test
```
tai komennolla:
```bash
poetry run invoke coverage
```
Testikattavuusraportin voi generoida komennolla:
```bash
poetry run invoke report
```
tai komennolla:
```bash
poetry run invoke html
```
Tämän jälkeen voi tarkastella testikattavuutta avaamalla tiedoston htmlcov/index.html selaimella:

```bash
firefox htmlcov/index.html
```

