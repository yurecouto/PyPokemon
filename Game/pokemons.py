from classes import *

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

normal_type = [
    Pidgey, Pidgeotto, Pidgeot, Rattata, Raticate, Spearow, Fearow, Jigglypuff, Wigglytuff,
    Meowth, Persian, Farfetchd, Doduo, Dodrio, Lickitung, Chansey, Kangaskhan, Tauros, Ditto, 
    Eevee, Porygon, Snorlax
    ]

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

grass_type = [
    Bulbasaur, Ivysaur, Venusaur, Oddish, Gloom, Vileplume, Bellsprout, Weepinbell, Victreebel, 
    Exeggcute, Exeggutor, Tangela
    ]

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

fire_type = [
    Charmander, Charmeleon, Charizard, Vulpix, Ninetales, Growlithe, Arcanine, Ponyta, Rapidash,
    Magmar, Flareon, Moltres
    ]

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

water_type = [
    Squirtle, Wartortle, Blastoise, Psyduck, Golduck, Poliwag, Poliwhirl, Poliwrath, Tentacool, 
    Tentacruel, Slowpoke, Slowbro, Seel, Dewgong, Shellder, Cloyster, Krabby, Kingler, Horsea,
    Seadra, Goldeen, Seaking, Staryu, Starmie, Magikarp, Gyarados, Lapras, Vaporeon
    ]

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

electric_type = [
    Pikachu, Raichu, Magnemite, Magneton, Voltorb, Electrode, Electabuzz, Jolteon, Zapdos
    ]

# Ice
Jynx        = Ice('Jynx')
Articuno    = Ice('Articuno')

ice_type = [
    Jynx, Articuno
    ]

# Fighting
Mankey      = Fighting('Mankey')
Primeape    = Fighting('Primeape')
Machop      = Fighting('Machop')
Machoke     = Fighting('Machoke')
Machamp     = Fighting('Machamp')
Hitmonlee   = Fighting('Hitmonlee')
Hitmonchamp = Fighting('Hitmonchamp')

fighting_type = [
    Mankey, Primeape, Machop, Machoke, Machamp, Hitmonlee, Hitmonchamp
    ]

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

poison_type = [
    Ekans, Arbok, Nidoran, Nidorina, Nidoqueen, Nidorano, Nidorino, Nidoking, Zubat, Golbat, 
    Grimer, Muk, Koffing, Weezing
    ]

# Ground
Sandshrew   = Ground('Sandshrew')
Sandslash   = Ground('Sandslash')
Diglett     = Ground('Diglett')
Dugtrio     = Ground('Dugtrio')
Cubone      = Ground('Cubone')
Marowak     = Ground('Marowak')
Rhyhorn     = Ground('Rhyhorn')
Rhydon      = Ground('Rhydon')

ground_type = [
    Sandshrew, Sandslash, Diglett, Dugtrio, Cubone, Marowak, Rhyhorn, Rhydon
    ]

# Flying

# Psychic
Abra        = Psychic('Abra')
Kadabra     = Psychic('Kadabra')  
Alakazam    = Psychic('Alakazam')
Drowzee     = Psychic('Drowzee')
Hypno       = Psychic('Hypno')
Mime        = Psychic('Mime')
Mewtwo      = Psychic('Mewtwo')
Mew         = Psychic('Mew')

psychic_type = [
    Abra, Kadabra, Alakazam, Drowzee, Hypno, Mime, Mewtwo, Mew
    ]

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

bug_type = [
    Caterpie, Metapod, Butterfree, Weedle, Kakuna, Beedrill, Paras, Parasect, Venonat, Venomoth, Scyther
    ]

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

rock_type = [
    Geodude, Graveler, Golem, Onix, Omanyte, Omastar, Kabuto, Kabutops, Aerodactyl
    ]

# Ghost
Gastly      = Ghost('Gastly')
Haunter     = Ghost('Haunter')
Gengar      = Ghost('Gengar')

ghost_type = [
    Gastly, Haunter, Gengar
    ]

# Dragon
Dratini     = Dragon('Dratini')
Dragonair   = Dragon('Dragonair')
Dragonite   = Dragon('Dragonite')

dragon_type = [
    Dratini, Dragonair, Dragonite
    ]

# Dark

# Steel

# Fairy