# Määrittelydokumentti

## Gomoku-peli

Gomoku eli 20x20 ruudukolla pelattava ristinolla on peli, jonka voittaa kun saa vähintään 5 merkin pituisen suoran. Pelissä pelaaja ja tekoäly lisäävät vuorotellen merkin pelilaudalle tyhjään ruutun.
Pelaaja pystyy pelaamaan tekoälyä vastaan käyttöliittymän kautta. Minimax-algoritmiin perustuva tekoäly karsii tehokkaasti kokeiltavat siirrot ja laskee optimaalisen siirron. 

## Tietoa projektista
 
- Ohjelmointikielenä Python
- Opinto-ohjelma on tietojenkäsittelyn kandidaatti
- Vertaisarviointien kielenä myös Python
- Projektissa toteutettavat algoritmit
  - Seuraavan siirron laskeva minimax-algoritmi, jota on tehostettu alpha-beta-karsinnalla
  - Voiton tarkistus-algoritmi
  - Heuristinen funktio
- Ratkaistava ongelma on luoda tekoäly, joka pystyy tehokkaasti pelaamaan Gomoku-peliä käyttöliittymän kautta.
- Ohjelma saa pelaajan siirron syötteenä ja laskee optimaalisen siirron tehokkaasti.
- Aikavaatimus alpha-beta karsinnalla tehostetulle minimax-algoritmille on parhaassa tapauksessa $O(\sqrt{b^d})$ ja
 huonoimmassa tapauksessa $O(b^d)$ [1](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning),
 jossa b "branching factor" eli keskimääräinen mahdollisten siirtojen määrä ja d "depth" eli syvyys, joka kuvaa laskettavien siirtojen määrää (kuinka syvälle pelissä mennään).

- Viitteet:
 1. https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning

## Projektin Ydin

Projektin ydin on tekoäly. Tekoäly perustuu minimax-algoritmiin, jota on tehostettu alpha-beta-karsinnalla. Algoritmi tutkii vain vapaat ruudut, jotka ovat korkeintaan kahden ruudun päässä aiemmin tehdyistä siirroista. Algoritmi pitää yllä listaa sopivista ruuduista ja päivittää sitä tehtyjen tai minmaxissa kokeiltujen siirtojen myötä, sekä antaa sen parametrina eteenpäin minmaxissa.
 Algoritmi tutkii ensimmäisenä edellisen siirron lähinaapurit tehokkuuden lisäämiseksi.

