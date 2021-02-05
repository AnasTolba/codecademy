class Pokemon:
    def __init__(self, name, level, type):
        self.name = name
        self.level = level
        self.type = type
        self.current_health = 10 * level
        self.max_health = 10 * level
        self.is_knocked_out = False

    def __repr__(self):
        return '{} is a {} type pokemon at level {} with a health pool of {}'.format(self.name, self.type, self.level, self.max_health)

    def knock_out(self):
        self.is_knocked_out = True
        print('{} has taken too much damage and is now knocked out'.format(self.name))
    
    def revive(self):
        self.is_knocked_out = False
        print('{} has been revived yay!'.format(self.name))

    def lose_health(self, damage):
        self.current_health -= damage
        if self.current_health <= 0:
            self.current_health = 0
            print('{} has taken {} damage and is now sitting at {} health'.format(self.name, damage, self.current_health))
            self.knock_out()
        
        print('{} has taken {} damage and is now sitting at {} health'.format(self.name, damage, self.current_health))

    def gain_health(self, health):
        if self.current_health == 0:
            self.revive()
        
        self.current_health += health
        if self.current_health >= self.max_health:
            self.current_health = self.max_health
            print('yay {} has gained {} health and is now sitting at {} health'.format(self.name, health, self.current_health))
        else:
            print('yay {} has gained {} health and is now sitting at {} health'.format(self.name, health, self.current_health))
    
    def attack(self, pokemon):
        if self.is_knocked_out:
            print('{} can\'t attack because they are knocked out'.format(self.name))

        if (self.type == 'Grass' and pokemon.type =='Grass') or (self.type == 'Water' and pokemon.type == 'Water') or (self.type == 'Fire' and pokemon.type == 'Fire'):
            print('{} attacked {}, they are both {} type\ndamage is regular'.format(self.name, pokemon.name, self.type))
            pokemon.lose_health(self.level)

        elif (self.type == 'Grass' and pokemon.type == 'Water') or (self.type == 'Fire' and pokemon.type == 'Grass') or (self.type == 'Water' and pokemon.type == 'Fire'):
            print('{} attacked {}, {} has type advantage\ndamage is doubled'.format(self.name, pokemon.name, self.name, self.type))
            pokemon.lose_health(self.level * 2)

        elif (self.type == 'Grass' and pokemon.type == 'Fire') or (self.type == 'Water' and pokemon.type == 'Grass') or (self.type == 'Fire' and pokemon.type == 'Water'):
            print('{} attacked {}, {} has type advantage\ndamage is halved'.format(self.name, pokemon.name, pokemon.name, self.type))
            pokemon.lose_health(self.level / 2)

class Trainer:
    def __init__(self, pokemons, name, potions):
        self.pokemons = pokemons
        self.name = name
        self.potions = potions
        self.currently_active_pokemon = 0
    
    def __repr__(self):
        print('{} has the following pokemon'.format(self.name))
        
        for pokemon in self.pokemons:
            print(pokemon.name)
        return '{}\'s current active pokemon is: {}'.format(self.name, self.pokemons[self.currently_active_pokemon].name)
    
    def use_potion(self, pokemon):
        index_of_choice = 0
        if pokemon in self.pokemons:
            for i in range(len(self.pokemons)):
                if self.pokemons[i] == pokemon:
                    index_of_choice = i
        else:
            print('{} does not own {}'.format(self.name, pokemon))

        if self.potions > 0:
            print('{} used a potion on {}'.format(self.name, self.pokemons[index_of_choice].name))
            self.pokemons[index_of_choice].gain_health(20)
            self.potions -= 1
        else:
            print('{} does not have enough potions to use them'.format(self.name))

    def attack_trainer(self, trainer):
        print('{} has chosen to attack {}'.format(self.name, trainer.name))
        self.pokemons[self.currently_active_pokemon].attack(trainer.pokemons[trainer.currently_active_pokemon])
    
    def switch_active_pokemon(self, new_active_pokemon):
        index_of_choice = 0
        if new_active_pokemon in self.pokemons:
            for i in range(len(self.pokemons)):
                if self.pokemons[i] == new_active_pokemon:
                    index_of_choice = i
        else:
            print('{} does not own {}'.format(self.name, new_active_pokemon))    
        
        if self.pokemons[index_of_choice].is_knocked_out:
            print('{} is knocked out. You can\'t make it {}\'s active pokemon'.format(self.pokemons[index_of_choice].name, self.name))
        elif index_of_choice == self.currently_active_pokemon:
            print('{} is already {}\'s active pokemon'.format(self.pokemons[index_of_choice].name, self.name))
        else:
            self.currently_active_pokemon = index_of_choice
            print('{} I choose you!'.format(self.pokemons[self.currently_active_pokemon].name))
    
# testing

a = Pokemon('Charmander', 7, 'Fire')
b = Pokemon('Squirtle', 10, 'Water')
c = Pokemon('Bulbasaur', 10, 'Grass')
d = Pokemon('Bulbasaur', 8, 'Grass')
e = Pokemon('Charmander', 12, 'Fire')
f = Pokemon('Squirtle', 4, 'Water')



trainer_one = Trainer([a,b,c], 'Alex', 3)
trainer_two = Trainer([d,e,f], 'Sara', 5)

print(trainer_one)
print(trainer_two)

trainer_one.attack_trainer(trainer_two)
trainer_two.attack_trainer(trainer_one)
trainer_two.use_potion(d)
trainer_one.attack_trainer(trainer_two)
trainer_two.switch_active_pokemon(d)
trainer_two.switch_active_pokemon(e)