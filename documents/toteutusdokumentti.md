# Toteutusdokumentti

## Yleistä

Toteutusdokumentti on osa kurssin [tiralabra](https://tiralabra.github.io/2023_p4/) harjoitustyötä. Toteutusdokumentti on tarkoitettu ohjaajille ja muille tarkastajille, jotka haluavat tutustua sovelluksen toteutukseen. Dokumentti on kirjoitettu suomeksi.

## Sovelluksen tarkoitus

Sovelluksen tarkoitus on vertailla eri polkujen etsintä algoritmeja. Sovellus on toteutettu Python-ohjelmointikielellä ja se on tarkoitettu käytettäväksi komentoriviltä. Sovelluksen käyttöliittymä on tekstipohjainen.

## Sovelluksen käyttö

Sovelluksen käynnistämiseksi suoritetaan komento `python3 main.py`. Sovelluksen käynnistyksen jälkeen käyttäjä näkee ohjeet sovelluksen käyttöön. Käyttäjä syöttää haluamansa algoritmin ja syötteen. Sovellus tulostaa polun ja sen pituuden. Sovelluksen voi lopettaa syöttämällä komennon `q`. Sovelluksen syötteenä kelpaa myös tiedoston nimi, joka sisältää kartan. Tällöin sovellus tulostaa polun ja sen pituuden. Tiedoston tulee olla samassa kansiossa kuin sovellus.

## Sovelluksen toteutus

Sovellus on toteutettu Python-ohjelmointikielellä. Sovelluksen toteutus on jaettu kahteen osaan: algoritmien toteutus ja käyttöliittymä. 

### Algoritmien toteutus

Dijkstran lyhimmänpolun algoritmi:

```python
def dijkstra(self, start, end):
        self.distances[start[0]][start[1]] = 0
        self.previous[start[0]][start[1]] = start

        while True:
            self.operations += 1
            current = self.get_closest_node()
            if current is None:
                break
            self.visited[current[0]][current[1]] = True
            for direction in self.directions:
                neighbor = (current[0] + direction[0], current[1] + direction[1])
                if self.is_valid(neighbor):
                    if direction in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
                        new_distance = self.distances[current[0]][current[1]] + math.sqrt(2)
                    else:
                        new_distance = self.distances[current[0]][current[1]] + 1
                    if new_distance < self.distances[neighbor[0]][neighbor[1]]:
                        self.distances[neighbor[0]][neighbor[1]] = new_distance
                        self.previous[neighbor[0]][neighbor[1]] = current
                        self.operations += 1


        return self.get_path(start, end)
```

A*-algoritmi:

```python
def a_star(self, start, end):
        self.distances[start[0]][start[1]] = 0
        self.previous[start[0]][start[1]] = start

        heap = [(self.heuristic(start, end), start)]
        while heap:
            self.operations += 1
            current = heapq.heappop(heap)[1]
            if current == end:
                break
            if self.visited[current[0]][current[1]]:
                continue
            self.visited[current[0]][current[1]] = True

            for direction in self.directions:
                neighbor = (current[0] + direction[0], current[1] + direction[1])
                if self.is_valid(neighbor):
                    if direction in [(1,1), (1,-1), (-1,1), (-1,-1)]:
                        # Diagonal movement, distance is sqrt(2)
                        new_distance = self.distances[current[0]][current[1]] + math.sqrt(2)
                    else:
                        # Horizontal/Vertical movement, distance is 1
                        new_distance = self.distances[current[0]][current[1]] + 1
    
                    if new_distance < self.distances[neighbor[0]][neighbor[1]]:
                        self.distances[neighbor[0]][neighbor[1]] = new_distance
                        self.previous[neighbor[0]][neighbor[1]] = current
                        heapq.heappush(heap, (self.heuristic(neighbor, end) + new_distance, neighbor))

        return self.get_path(start, end)
```

### Käyttöliittymä

Käyttöliittymää ei ole vielä toteutettu.

## Lähteet

[1] [Dijkstran algoritmi](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)

[2] [A* algoritmi](https://en.wikipedia.org/wiki/A*_search_algorithm)