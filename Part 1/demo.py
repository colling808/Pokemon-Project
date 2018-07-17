import os, csv
from pokemon import pokedex

Pokedex = pokedex("pokemon.csv")
output = open("output_demo.txt", "w")

Pokedex.image_search("")

type = ""
query1 = Pokedex.type_search(type)
output.write("Pokemon with the " + type + " type:\n")
output.write(str(query1) + "\n\n")

Pokedex.reset()
stat = "";
value = 0;
query2 = Pokedex.stat_search(stat, value)
output.write("Pokemon with " + " stat over " + value + ":\n")
output.write(str(query2) + "\n\n")

Pokedex.reset()
query3 = Pokedex.legend_search()
output.write("Legendary Pokemon:\n")
output.write(str(query3) + "\n\n")

Pokedex.reset()
pokemon = ""
query4 = Pokedex.stronger_type_search(pokemon)
output.write("Types that are super effective against " + pokemon + ":\n")
output.write(str(query4) + "\n\n")

Pokedex.reset()
query5 = Pokedex.stronger_stat_search(pokemon)
output.write("Pokemon with higher stats than " + pokemon + ":\n")
output.write(str(query5) + "\n\n")

Pokedex.reset()
query6 = Pokedex.weaker_stat_search(pokemon)
output.write("Pokemon with weaker stats than " + pokemon + ":\n")
output.write(str(query6) + "\n\n")

Pokedex.reset()
query7 = Pokedex.stronger_pokemon_search(pokemon)
output.write("Pokemon that are stronger than " + pokemon + ":\n")
output.write(str(query7) + "\n\n")


