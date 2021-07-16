from classes import *
from random import randint
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
Pidgey      = Normal('Pidgey')
Pidgeotto   = Normal('Pidgeotto')
Pidgeot     = Normal('Pidgeot')
Rattata     = Normal('Rattata')
Raticate    = Normal('Raticate')
Spearow     = Normal('Spearow')
Fearow      = Normal('Fearow')
Jigglypuff  = Normal('Jigglypuff')
Wigglytuff  = Normal('Wigglytuff')
Meowth      = Normal('Meowth')
Persian     = Normal('Persian')
Farfetchd   = Normal('Farfetchd')
Doduo       = Normal('Doduo')
Dodrio      = Normal('Dodrio')
Lickitung   = Normal('Lickitung')
Chansey     = Normal('Chansey')
Kangaskhan  = Normal('Kangaskhan')
Tauros      = Normal('Tauros')
Ditto       = Normal('Ditto')
Eevee       = Normal('Eevee')
Porygon     = Normal('Porygon')
Snorlax     = Normal('Snorlax')

# Grass
Bulbasaur   = Grass('Bulbasaur')
Ivysaur     = Grass('Ivysaur')
Venusaur    = Grass('Venusaur')
Oddish      = Grass('Oddish')
Gloom       = Grass('Gloom')
Vileplume   = Grass('Vileplume')
Bellsprout  = Grass('Bellsprout')
Weepinbell  = Grass('Weepinbell')
Victreebel  = Grass('Victreebel')
Exeggcute   = Grass('Exeggcute')
Exeggutor   = Grass('Exeggutor')
Tangela     = Grass('Tangela')

# Fire
Charmander  = Fire('Charmander')
Charmeleon  = Fire('Charmeleon')
Charizard   = Fire('Charizard')
Vulpix      = Fire('Vulpix')
Ninetales   = Fire('Ninetales')
Growlithe   = Fire('Growlithe')
Arcanine    = Fire('Arcanine')
Ponyta      = Fire('Ponyta')
Rapidash    = Fire('Rapidash')
Magmar      = Fire('Magmar')
Flareon     = Fire('Flareon')
Moltres     = Fire('Moltres')

# Water
Squirtle    = Water('Squirtle')
Wartortle   = Water('Wartortle')
Blastoise   = Water('Blastoise')
Psyduck     = Water('Psyduck')
Golduck     = Water('Golduck')
Poliwag     = Water('Poliwag')
Poliwhirl   = Water('Poliwhirl')
Poliwrath   = Water('Poliwrath')
Tentacool   = Water('Tentacool')
Tentacruel  = Water('Tentacruel')
Slowpoke    = Water('Slowpoke')
Slowbro     = Water('Slowbro')
Seel        = Water('Seel')
Dewgong     = Water('Dewgong')
Shellder    = Water('Shellder')
Cloyster    = Water('Cloyster')
Krabby      = Water('Krabby')
Kingler     = Water('Kingler')
Horsea      = Water('Horsea')
Seadra      = Water('Seadra')
Goldeen     = Water('Goldeen')
Seaking     = Water('Seaking')
Staryu      = Water('Staryu')
Starmie     = Water('Starmie')
Magikarp    = Water('Magikarp')
Gyarados    = Water('Gyarados')
Lapras      = Water('Lapras')
Vaporeon    = Water('Vaporeon')

# Electric
Pikachu     = Electric('Pikachu')
Raichu      = Electric('Raichu')
Magnemite   = Electric('Magnemite')
Magneton    = Electric('Magneton')
Voltorb     = Electric('Voltorb')
Electrode   = Electric('Electrode')
Electabuzz  = Electric('Electabuzz')
Jolteon     = Electric('Jolteon')
Zapdos      = Electric('Zapdos')

# Ice
Jynx        = Ice('Jynx')
Articuno    = Ice('Articuno')

# Fighting
Mankey      = Fighting('Mankey')
Primeape    = Fighting('Primeape')
Machop      = Fighting('Machop')
Machoke     = Fighting('Machoke')
Machamp     = Fighting('Machamp')
Hitmonlee   = Fighting('Hitmonlee')
Hitmonchamp = Fighting('Hitmonchamp')

# Poison
Ekans       = Poison('Ekans')
Arbok       = Poison('Arbok')
Nidoran     = Poison('Nidoran')
Nidorina    = Poison('Nidorina')
Nidoqueen   = Poison('Nidoqueen')
Nidorano    = Poison('Nidorano')
Nidorino    = Poison('Nidorino')
Nidoking    = Poison('Nidoking')
Zubat       = Poison('Zubat')
Golbat      = Poison('Golbat')
Grimer      = Poison('Grimer')
Muk         = Poison('Muk')
Koffing     = Poison('Koffing')
Weezing     = Poison('Weezing')

# Ground
Sandshrew   = Ground('Sandshrew')
Sandslash   = Ground('Sandslash')
Diglett     = Ground('Diglett')
Dugtrio     = Ground('Dugtrio')
Cubone      = Ground('Cubone')
Marowak     = Ground('Marowak')
Rhyhorn     = Ground('Rhyhorn')
Rhydon      = Ground('Rhydon')

# Psychic
Abra        = Psychic('Abra')
Kadabra     = Psychic('Kadabra')  
Alakazam    = Psychic('Alakazam')
Drowzee     = Psychic('Drowzee')
Hypno       = Psychic('Hypno')
Mime        = Psychic('Mime')
Mewtwo      = Psychic('Mewtwo')
Mew         = Psychic('Mew')

# Bug
Caterpie    = Bug('Caterpie')
Metapod     = Bug('Metapod')
Butterfree  = Bug('Butterfree')
Weedle      = Bug('Weedle')
Kakuna      = Bug('Kakuna')  
Beedrill    = Bug('Beedrill')
Paras       = Bug('Paras')
Parasect    = Bug('Parasect')     
Venonat     = Bug('Venonat')   
Venomoth    = Bug('Venomoth')
Scyther     = Bug('Scyther')
Pinsir      = Bug('Pinsir')

# Rock
Geodude     = Rock('Geodude')
Graveler    = Rock('Graveler')
Golem       = Rock('Golem')
Onix        = Rock('Onix')
Omanyte     = Rock('Omanyte')
Omastar     = Rock('Omastar')
Kabuto      = Rock('Kabuto')    
Kabutops    = Rock('Kabutops')        
Aerodactyl  = Rock('Aerodactyl')

# Ghost
Gastly      = Ghost('Gastly')
Haunter     = Ghost('Haunter')
Gengar      = Ghost('Gengar')

# Dragon
Dratini     = Dragon('Dratini')
Dragonair   = Dragon('Dragonair')
Dragonite   = Dragon('Dragonite')

# Fairy
Clefairy    = Fairy('Clefairy')
Clefable    = Fairy('Clefairy')

'''A'''
'''R'''
'''E'''
'''A'''
'''S'''

object_forest = [
    Pikachu, Caterpie, Butterfree, Bellsprout, Exeggcute, 
    Pidgey, Oddish, Gloom, Beedrill, Weedle, Kakuna, 
    Weepinbell, Abra
    ]

object_mount = [
    Paras, Clefairy, Mankey, Rattata, Raticate,
    Spearow, Doduo, Jigglypuff, Wigglytuff, Farfetchd, 
    Pidgeotto, Primeape, Metapod, Clefable
    ]

object_cave = [
    Arbok, Golbat, Parasect, Venomoth, Kadabra, Drowzee,
    Magneton, Dodrio, Ditto, Voltorb, Koffing, Kabuto, 
    Grimer, Magnemite
    ]

object_tunnel = [
    Zubat, Machop, Diglett, Dugtrio, Machoke, Golem,
    Electrode, Omanyte, Omastar, Sandshrew, Sandslash, Muk
    ]

object_safari = [
    Nidorano, Nidorina, Nidoran, Nidorino, Venonat,	Chansey,
    Tangela, Pinsir, Magikarp, Kingler, Slowpoke,
    Dratini, Cubone, Kangaskhan, Ekans    
    ]

object_islands = [
    Psyduck, Golduck, Slowbro, Seel, Goldeen,
    Shellder, Horsea, Staryu, Krabby, Tentacool, Tentacruel,
    Poliwag, Dewgong, Poliwhirl, Seadra, Lickitung
    ]

object_road = [
    Geodude, Graveler, Onix, Bulbasaur, Poliwrath,
    Marowak, Tauros, Meowth, Persian, Haunter, Squirtle,
    Vileplume, Cloyster, Seaking, Mime, Charmander, Nidoking
    ]

object_trees = [
    Charmeleon, Charizard, Ivysaur, Venusaur, Wartortle, Blastoise,
    Vulpix, Growlithe, Ponyta, Magmar, Flareon, Gyarados, Exeggutor,
    Vaporeon, Flareon, Jolteon, Weezing, Kabutops, Rhyhorn, Nidoqueen
    ]

object_valley = [
    Eevee, Jynx, Gastly, Scyther, Dragonite, Pidgeot, Fearow,
    Ninetales, Arcanine, Machamp, Victreebel, Starmie, Electabuzz,
    Lapras, Aerodactyl, Rapidash, Raichu, Hitmonlee, Hitmonchamp,
    Snorlax, Porygon, Alakazam, Hypno, Gengar, Rhydon
    ]

object_center = [
    Articuno, Zapdos, Moltres, Mew, Mewtwo
    ]

ip_level(Bulbasaur, 5)
ip_level(Charmander, 5)
ip_level(Squirtle, 5)