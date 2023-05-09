# Käyttöohje

## Ohjelman kloonaaminen

1. Avaa komentorivi ja siirry haluamaasi kansioon
2. Kopioi repositorion osoite ja syötä se komentoriville komennolla `git clone <osoite>`
3. Siirry repositorion juureen komennolla `cd pathfinding`
4. Asenna ohjelman riippuvuudet komennolla `poetry install`

## Ohjelman käynnistäminen

Ohjelman voi käynnistää komennolla `poetry run invoke start`

## Ohjelman testaaminen

Ohjelman testit voi suorittaa komennolla `poetry run invoke test`
Ohjelman testikattavuuden voi tarkistaa komennolla `poetry run invoke coverage`, jos haluat nähdä testikattavuuden selaimessa, suorita komento `firefox htmlcov/index.html`
