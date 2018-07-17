import os, csv
from pokemon import pokedex

Pokedex = pokedex("pokemon.csv")
output = open("output.txt", "w")

Pokedex.image_search("Charizard")

query1 = Pokedex.type_search("Poison")
output.write("Pokemon with the poison type:\n")
output.write(str(query1) + "\n\n")

Pokedex.reset()
query2 = Pokedex.stat_search("Total", 650)
output.write("Pokemon with total stats over 650:\n")
output.write(str(query2) + "\n\n")

Pokedex.reset()
query3 = Pokedex.legend_search()
output.write("Legendary Pokemon:\n")
output.write(str(query3) + "\n\n")

Pokedex.reset()
query4 = Pokedex.stronger_type_search("Charizard")
output.write("Types that are super effective against Charizard:\n")
output.write(str(query4) + "\n\n")

Pokedex.reset()
query5 = Pokedex.stronger_stat_search("Pikachu")
output.write("Pokemon with higher stats than Pikachu:\n")
output.write(str(query5) + "\n\n")

Pokedex.reset()
query6 = Pokedex.weaker_stat_search("Pidgey")
output.write("Pokemon with weaker stats than Pidgey:\n")
output.write(str(query6) + "\n\n")

Pokedex.reset()
query7 = Pokedex.stronger_pokemon_search("Dragonite")
output.write("Pokemon that are stronger than Dragonite:\n")
output.write(str(query7) + "\n\n")


