# PyPokemon

  This is my first serious and "original" project, the idea it's to practice my python sintaxe skills
and my OOP skills.

## The Code

  Here the fun starts, a OOP adventure doesn't have an incredible history or have an awesome gameplay
the main idea is to make a nostalgy about the oldschool text rpgs in the pokemon thematic, the history
makes some paralels to what was coded for that line of code.

there are 7 python files:

- classes.py
- game_functions.py
- structure_functions.py
- lists.py
- pokemons.py
- pokedex.py
- main.py

Even though the names are self explanatory bellow will be explanated the function of each file

### pokemon_class
  
  Here we have two main classes, Pokemon and Player, in pokemons, there are the pokemon atributes
like name, number, xp, max_xp, lvl, health, max_health, the explaination of these atributes are not going
to be done now, the methods of each pokemon are:

- level_up(self)                  =>         This method makes the pokemon up it's level. and
                                         sets the next level atributes for the pokemon object.

- atack(self, opponent)           =>         This methos makes the pokemon atack another pokemon 
                                         it uses an other function from game_functions (that
                                         uses the self.health as a paramether to atack, and the
                                         function get_damage will be explainated in the lists
                                         function.

- set_level(self, min_l, max_l)   =>         This one sets a randomic level, you can set the 
                                         minimum level and maximum level available, and sets each
                                         level atributes for the pokemon object, this function
                                         will will return in the explaination of the main.

- initial_level(self)             =>         It makes the same thing of the last one, but it's
                                         olny used for the initial pokemons.
                                         
- pokemon_out(self)               =>         This method returns a boolean valor based in the 
                                         pokemon.health.

### player_class
                                         
  And the Player's class represent's the player, and haves atributes referent to the bag of the
pokemon trainer, like Pokeballs, Potions and evolution stones, the only atribute are the capture atribute

capture(self, pokemon, area, methods)      =>      It receives the pokeballs to use as argument for the different 
                                                 chances to capture with the area, the way it works will be explained
                                                 in the list file explaination
                                                 
### Game Functions 
