from classes import *
from game_functions import *

'''P'''
'''O'''
'''K'''
'''E'''
'''M'''
'''O'''
'''N'''
'''S'''

# Normal
Pidgey      = Normal('Pidgey', 16)
Pidgeotto   = Normal('Pidgeotto', 17)
Pidgeot     = Normal('Pidgeot', 18)
Rattata     = Normal('Rattata', 19)
Raticate    = Normal('Raticate', 20)
Spearow     = Normal('Spearow', 21)
Fearow      = Normal('Fearow', 22)
Jigglypuff  = Normal('Jigglypuff', 39)
Wigglytuff  = Normal('Wigglytuff', 40)
Meowth      = Normal('Meowth', 52)
Persian     = Normal('Persian', 53)
Farfetchd   = Normal('Farfetchd', 83)
Doduo       = Normal('Doduo', 84)
Dodrio      = Normal('Dodrio', 85)
Lickitung   = Normal('Lickitung', 108)
Chansey     = Normal('Chansey', 113)
Kangaskhan  = Normal('Kangaskhan', 115)
Tauros      = Normal('Tauros', 128)
Ditto       = Normal('Ditto', 132)
Eevee       = Normal('Eevee', 133)
Porygon     = Normal('Porygon', 137)
Snorlax     = Normal('Snorlax', 143)

# Grass
Bulbasaur   = Grass('Bulbasaur', 1)
Ivysaur     = Grass('Ivysaur', 2)
Venusaur    = Grass('Venusaur', 3)
Oddish      = Grass('Oddish', 43)
Gloom       = Grass('Gloom', 44)
Vileplume   = Grass('Vileplume', 45)
Bellsprout  = Grass('Bellsprout', 69)
Weepinbell  = Grass('Weepinbell', 70)
Victreebel  = Grass('Victreebel', 71)
Exeggcute   = Grass('Exeggcute', 102)
Exeggutor   = Grass('Exeggutor', 103)
Tangela     = Grass('Tangela', 114)

# Fire
Charmander  = Fire('Charmander', 4)
Charmeleon  = Fire('Charmeleon', 5)
Charizard   = Fire('Charizard', 6)
Vulpix      = Fire('Vulpix', 37)
Ninetales   = Fire('Ninetales', 38)
Growlithe   = Fire('Growlithe', 58)
Arcanine    = Fire('Arcanine', 59)
Ponyta      = Fire('Ponyta', 77)
Rapidash    = Fire('Rapidash', 78)
Magmar      = Fire('Magmar', 126)
Flareon     = Fire('Flareon', 136)
Moltres     = Fire('Moltres', 146)

# Water
Squirtle    = Water('Squirtle', 7)
Wartortle   = Water('Wartortle', 8)
Blastoise   = Water('Blastoise', 9)
Psyduck     = Water('Psyduck', 54)
Golduck     = Water('Golduck', 55)
Poliwag     = Water('Poliwag', 60)
Poliwhirl   = Water('Poliwhirl', 61)
Poliwrath   = Water('Poliwrath', 62)
Tentacool   = Water('Tentacool', 72)
Tentacruel  = Water('Tentacruel', 73)
Slowpoke    = Water('Slowpoke', 79)
Slowbro     = Water('Slowbro', 80)
Seel        = Water('Seel', 86)
Dewgong     = Water('Dewgong', 87)
Shellder    = Water('Shellder', 90)
Cloyster    = Water('Cloyster', 91)
Krabby      = Water('Krabby', 98)
Kingler     = Water('Kingler', 99)
Horsea      = Water('Horsea', 116)
Seadra      = Water('Seadra', 117)
Goldeen     = Water('Goldeen', 118)
Seaking     = Water('Seaking', 119)
Staryu      = Water('Staryu', 120)
Starmie     = Water('Starmie', 121)
Magikarp    = Water('Magikarp', 129)
Gyarados    = Water('Gyarados', 130)
Lapras      = Water('Lapras', 131)
Vaporeon    = Water('Vaporeon', 134)

# Electric
Pikachu     = Electric('Pikachu', 25)
Raichu      = Electric('Raichu', 26)
Magnemite   = Electric('Magnemite', 81)
Magneton    = Electric('Magneton', 82)
Voltorb     = Electric('Voltorb', 100)
Electrode   = Electric('Electrode', 101)
Electabuzz  = Electric('Electabuzz', 125)
Jolteon     = Electric('Jolteon', 135)
Zapdos      = Electric('Zapdos', 145)

# Ice
Jynx        = Ice('Jynx', 124)
Articuno    = Ice('Articuno', 144)

# Fighting
Mankey      = Fighting('Mankey', 56)
Primeape    = Fighting('Primeape', 57)
Machop      = Fighting('Machop', 66)
Machoke     = Fighting('Machoke', 67)
Machamp     = Fighting('Machamp', 68)
Hitmonlee   = Fighting('Hitmonlee', 106)
Hitmonchamp = Fighting('Hitmonchamp', 107)

# Poison
Ekans       = Poison('Ekans', 23)
Arbok       = Poison('Arbok', 24)
Nidoran     = Poison('Nidoran', 29)
Nidorina    = Poison('Nidorina', 30)
Nidoqueen   = Poison('Nidoqueen', 31)
Nidorano    = Poison('Nidorano', 32)
Nidorino    = Poison('Nidorino', 33)
Nidoking    = Poison('Nidoking', 34)
Zubat       = Poison('Zubat', 41)
Golbat      = Poison('Golbat', 42)
Grimer      = Poison('Grimer', 88)
Muk         = Poison('Muk', 89)
Koffing     = Poison('Koffing', 109)
Weezing     = Poison('Weezing', 110)

# Ground
Sandshrew   = Ground('Sandshrew', 27)
Sandslash   = Ground('Sandslash', 28)
Diglett     = Ground('Diglett', 50)
Dugtrio     = Ground('Dugtrio', 51)
Cubone      = Ground('Cubone', 104)
Marowak     = Ground('Marowak', 105)
Rhyhorn     = Ground('Rhyhorn', 111)
Rhydon      = Ground('Rhydon', 112)

# Psychic
Abra        = Psychic('Abra', 63)
Kadabra     = Psychic('Kadabra', 64)  
Alakazam    = Psychic('Alakazam', 65)
Drowzee     = Psychic('Drowzee', 96)
Hypno       = Psychic('Hypno', 97)
Mime        = Psychic('Mime', 122)
Mewtwo      = Psychic('Mewtwo', 150)
Mew         = Psychic('Mew', 151)

# Bug
Caterpie    = Bug('Caterpie', 10)
Metapod     = Bug('Metapod', 11)
Butterfree  = Bug('Butterfree', 12)
Weedle      = Bug('Weedle', 13)
Kakuna      = Bug('Kakuna', 14)  
Beedrill    = Bug('Beedrill', 15)
Paras       = Bug('Paras', 46)
Parasect    = Bug('Parasect', 47)     
Venonat     = Bug('Venonat', 48)   
Venomoth    = Bug('Venomoth', 49)
Scyther     = Bug('Scyther', 123)
Pinsir      = Bug('Pinsir', 127)

# Rock
Geodude     = Rock('Geodude', 74)
Graveler    = Rock('Graveler', 75)
Golem       = Rock('Golem', 76)
Onix        = Rock('Onix', 95)
Omanyte     = Rock('Omanyte', 138)
Omastar     = Rock('Omastar', 139)
Kabuto      = Rock('Kabuto', 140)    
Kabutops    = Rock('Kabutops', 141)        
Aerodactyl  = Rock('Aerodactyl', 142)

# Ghost
Gastly      = Ghost('Gastly', 92)
Haunter     = Ghost('Haunter', 93)
Gengar      = Ghost('Gengar', 94)

# Dragon
Dratini     = Dragon('Dratini', 147)
Dragonair   = Dragon('Dragonair', 148)
Dragonite   = Dragon('Dragonite', 149)

# Fairy
Clefairy    = Fairy('Clefairy', 35)
Clefable    = Fairy('Clefairy', 36)

'''A'''
'''R'''
'''E'''
'''A'''
'''S'''

# P65%, G90%, U100%
object_forest = [
    Pikachu, Caterpie, Butterfree, Bellsprout, Exeggcute, 
    Pidgey, Oddish, Gloom, Weedle, Kakuna, Zubat, 
    Weepinbell, Abra, Rattata
    ]

# P60%, G80%, U95%
object_mount = [
    Paras, Clefairy, Mankey, Beedrill, Raticate,
    Spearow, Doduo, Jigglypuff, Wigglytuff, Farfetchd, 
    Pidgeotto, Primeape, Metapod, Clefable
    ]

# P55%, G75%, U90%
object_cave = [
    Arbok, Golbat, Parasect, Venomoth, Kadabra, Drowzee,
    Magneton, Dodrio, Ditto, Voltorb, Koffing, Kabuto, 
    Grimer, Magnemite
    ]

# P50%, G70%, U90%
object_tunnel = [
    Machop, Diglett, Dugtrio, Machoke, Golem,
    Electrode, Omanyte, Omastar, Sandshrew, Sandslash, Muk
    ]

# P35%, G50%, U75%
object_safari = [
    Nidorano, Nidorina, Nidoran, Nidorino, Venonat,	Chansey,
    Tangela, Pinsir, Magikarp, Kingler, Slowpoke,
    Dratini, Cubone, Kangaskhan, Ekans    
    ]

# P25%, G40%, U70%
object_islands = [
    Psyduck, Golduck, Slowbro, Seel, Goldeen,
    Shellder, Horsea, Staryu, Krabby, Tentacool, Tentacruel,
    Poliwag, Dewgong, Poliwhirl, Seadra, Lickitung
    ]

# P15%, G35%, U65%
object_road = [
    Geodude, Graveler, Onix, Bulbasaur, Poliwrath,
    Marowak, Tauros, Meowth, Persian, Haunter, Squirtle,
    Vileplume, Cloyster, Seaking, Mime, Charmander, Nidoking
    ]

# G15%, U65%, M90%
object_trees = [
    Charmeleon, Charizard, Ivysaur, Venusaur, Wartortle, Blastoise,
    Vulpix, Growlithe, Ponyta, Magmar, Flareon, Gyarados, Exeggutor,
    Vaporeon, Flareon, Jolteon, Weezing, Kabutops, Rhyhorn, Nidoqueen
    ]

# G10%, U50%, M90%
object_valley = [
    Eevee, Jynx, Gastly, Scyther, Dragonite, Pidgeot, Fearow,
    Ninetales, Arcanine, Machamp, Victreebel, Starmie, Electabuzz,
    Lapras, Aerodactyl, Rapidash, Raichu, Hitmonlee, Hitmonchamp,
    Snorlax, Porygon, Alakazam, Hypno, Gengar, Rhydon
    ]

# U35%, M75%
object_center = [
    Articuno, Zapdos, Moltres, Mew, Mewtwo
    ]


Bulbasaur.initial_level()
Charmander.initial_level()
Squirtle.initial_level()