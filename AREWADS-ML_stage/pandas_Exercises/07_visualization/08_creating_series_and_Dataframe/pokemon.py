#Step 1. Import the necessary libraries
import pandas as pd 
#Step 2. Create a data dictionary that looks like the DataFrame below
raw_data = {"name": ['Bulbasaur', 'Charmander','Squirtle','Caterpie'],
            "evolution": ['Ivysaur','Charmeleon','Wartortle','Metapod'],
            "type": ['grass', 'fire', 'water', 'bug'],
            "hp": [45, 39, 44, 45],
            "pokedex": ['yes', 'no','yes','no']                        
            } 
#Step 3. Assign it to a variable called pokemon
pokemon = pd.DataFrame(raw_data)
print(pokemon.head()) 
#evolution	hp	name	pokedex	type
#0	Ivysaur	45	Bulbasaur	yes	grass
#1	Charmeleon	39	Charmander	no	fire
#2	Wartortle	44	Squirtle	yes	water
#3	Metapod	45	Caterpie	no	bug
#Step 4. Ops...it seems the DataFrame columns are in alphabetical order. Place the order of the columns as name, type, hp, evolution, pokedex
pokemon = pokemon[['name', 'type', 'hp', 'evolution','pokedex']]
print(pokemon) 
#Step 5. Add another column called place, and insert what you have in mind.
pokemon['place'] = ['park','street','lake','forest']
print(pokemon) 
#Step 6. Present the type of each column
print(pokemon.dtypes) 
#BONUS: Create your own question and answer it.
 