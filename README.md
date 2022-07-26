# pelea-de-personajes

## Contexto
Implementación de una aplicación de consola que permite simular peleas entre heroes provistos por la [SuperHero API](https://www.superheroapi.com/index.html). Detalles sobre la simulación se encuentran en el archivo [Pelea_de_personajes.pdf](Pelea_de_personajes.pdf).

## Mecanismo de peleas
Cada ronda de pelea ocurre entre el primer heroe de cada equipo.
El heroe vencedor se queda para la siguiente ronda y el perdedor se elimina del equipo dando paso al siguiente en la lista.

## Cómo correr la simulación
1. Instalar dependencias.
```
pip install -r requirements.txt
```
1. Crear archvo `.env` con una llave de [Sendgrid](sendgrid.com) (API para mandar correos) y de [SuperHero API](https://www.superheroapi.com/index.html).
```.env
SENDGRID_API_KEY='SG.XXXXXXXXXX.XXXXXXXXXX'
HERO_API_KEY='XXXXXXXXXXXXXXXX'
```
3. Correr programa.
```
python main.py <youremail@email.com>
```

## Supuestos
1. En la primera mensión de AS (Actual Stamina) se establece que para cada stat de cada personaje se debe crear una variable AS.
   > A cada uno de los personajes, por cada uno de sus stats (intelligence, strength, speed, durability, power, combat) deberas asignarles una nueva variable de forma aleatoria llamada AS (Actual Stamina).

    Luego de esto se presenta la fórmula:
    
    $$ stats = \lfloor \frac{2 * Base + AS}{1.1} * FB \rfloor$$
    
    Para la simulación supondré que con esta fórmula expresa algo equivalente a esto:
    
    $$ RealStat(stat_i, AS_i) = \lfloor \frac{2 * stat_i + AS_i}{1.1} * FB \rfloor$$
    
    con $stat_i$ el valor de cada una de las stats del heroe y $AS_i$ su respectiva AS.

2. En la formula de HP:

   $$ HP = \lfloor \frac{strength * 0.8 + durability * 0.7 + power}{2} * (1 + \frac{AS}{10}) \rfloor + 100$$
   
   Se hace referencia a AS más no se especifíca cuál de todas las AS del heroe utilizar (por la suposición 1 tenemos que hay varias AS para cada heroe). Es por eso que se supondrá que esta AS es la de $power$ ya que es la stat que más impacto tiene sobre el HP.
   
   $$ HP = \lfloor \frac{strength * 0.8 + durability * 0.7 + power}{2} * (1 + \frac{AS_{power}}{10}) \rfloor + 100$$
