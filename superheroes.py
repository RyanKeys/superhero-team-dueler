import random


class Ability:
    def __init__(self, name, max_dmg):
        '''Create Instance Variables:
        name: str
        max_damage: int'''
        self.name = name
        self.max_dmg = max_dmg

    def attack(self):
        ''' Return a value between 0 and the value set by self.max_damage.'''
        dmg = random.randint(0, self.max_dmg)
        return dmg


class Armor:
    def __init__(self, name, max_block):
        '''Instantiate instance properties.
            name: String
            max_block: Integer
        '''
        self.name = name
        self.max_block = max_block

    def block(self):
        block = random.randint(0, self.max_block)
        return block


class Hero:
    def __init__(self, name, starting_health=100):
        '''Instance properties:
          abilities: List
          armors: List
          name: String
          starting_health: Integer
          current_health: Integer'''
        self.abilities = []
        self.armors = []
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def add_ability(self, ability):
        '''add ability to list'''
        self.abilities.append(ability)
        return self.abilities

    def attack(self):
        '''Calculate the total damage from all ability attacks.
          return: total:Int'''

        for hit in self.abilities:
            return Ability.attack(hit)

    def add_armor(self, armor):
        '''Add armor to self.armors Armor: Armor Object'''
        for armor in self.armors:
            return armor + self.current_health

    def defend(self, dmg_amt):
        for armor in self.armors:
            return dmg_amt - armor

    def take_dmg(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.'''
        return self.current_health - damage


if __name__ == "__main__":
    hero = Hero("Grace Hopper", 200)
    shield = Armor("Shield", 50)
    hero.add_armor(shield)
    hero.take_dmg(50)
    print(hero.current_health)
