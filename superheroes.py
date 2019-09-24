import random


class Ability:
    def __init__(self, name, attack_power):
        '''Create Instance Variables:
        name: str
        max_damage: int'''
        self.name = name
        self.max_dmg = attack_power

    def attack(self):
        ''' Return a value between 0 and the value set by self.max_damage.'''
        return random.randint(0, self.max_dmg)


class Armor:
    def __init__(self, name, max_block):
        '''Instantiate instance properties.
            name: String
            max_block: Integer
        '''
        self.name = name
        self.max_block = max_block

    def block(self):
        return random.randint(0, self.max_block)


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

    def attack(self):
        '''Calculate the total damage from all ability attacks.
          return: total:Int'''
        count = 0
        for ability in self.abilities:
            count += ability.attack()
            return count

    def add_armor(self, armor):
        '''Add armor to self.armors Armor: Armor Object'''
        self.armors.append(armor)

    def defend(self, dmg_amt):
        count = 0
        for armor in self.armors:
            block_int = int(armor.block())
            count += block_int
        return count + dmg_amt

    def take_dmg(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.'''
        hp = self.current_health
        defense = self.defend(damage)
        self.current_health = hp - defense

    def is_alive(self):
        if self.current_health < 0:
            print(f"{self.name} is dead!")
            return False
        else:
            return True
        pass

    def fight(self, opponent):
        '''Current Hero will take turns fighting the opponent hero passed in.'''
        attacking = True
        while attacking:
            if self.is_alive():
                dmg = self.attack()
                opponent.take_dmg(dmg)
                print(f"{self.name} has {self.current_health} health left.")

            else:
                print(f"{self} lost")
                break

            if opponent.is_alive():
                enemy_dmg = opponent.attack()
                self.take_dmg(enemy_dmg)
                print(f"{opponent.name} has {opponent.current_health} health left.")

            else:
                break


if __name__ == "__main__":
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)
