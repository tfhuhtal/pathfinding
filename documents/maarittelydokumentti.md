# Määrittelydokumentti

- Aineopintojen harjoitustyö tietorakenteet ja algoritmit aineopintojen harjoitustyö -kurssille. 
- Harjoitustyössäni käytän ohjelmointikielenä Pythonia, mutta osaan myös itse Javaa ja Javscriptiä.
- Harjoitustyön dokumentaatio kielenä käytetään markdownia ja dokumenttien kieli on Suomi, kuitenkin Pyhton -koodin muuttujien ja funktioiden nimet ovat englanniksi. 
- Toteutan tämän kurssin opintosuuntani (TKT) toisena harjoitustyönä.

## Algoritmit ja tietorakenteet

- Toteutan työssäni Dijkstran algoritmin, A-star hakualgoritmin ja Jump Point Search algoritmin.
- Syötteinä ohjelmani saa matriisin jonka jokaisella solmulla on joko arvo 0 tai 1, sekä lähtö- ja maalikoordinaatit. 0-solmut tarkoittavat käveltävää solmua ja 1-solmut esteitä joiden kautta ei voi edetä.

## Aika- ja tilavaativuus

- Aikavaativuus Dijkstran algoritmille on O(V²)
- A-star algoritmin aikavaativuus on wikipedian mukaan (A-star, 2023) f(n) = g(n) + h(n), n on polun seuraava solmu, g(n) on polun hinta aloitussolmusta solmuun n ja h(n) heurestiikka funktio joka arvioi halvimman reitin solmusta n maaliin.
- Jump Point Search algoritmin aikavaativuus on parempi kuin A-star algoritmin, sillä se on optimoitu muunnos A-star algoritmista.

### Lähteet

- A-star (27.2.2023). [Wikipedia](https://en.wikipedia.org/wiki/A*_search_algorithm), luettu 19.3.2023.
- Dijkstra (3.3.2023). [Wikipedia](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm), luettu 19.3.2023. 
- Jump Point Search (27.2.2023). [Wikipedia](https://en.wikipedia.org/wiki/Jump_point_search), luettu 19.3.2023.
