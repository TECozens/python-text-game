class Item:
    def __init__(self,name,weight,description):
        self.name = name # item's name
        self.weight = weight # item's weight
        self.description = description # item's description

    def get_name(self):
        return self.name
    
    def get_weight(self):
        return self.weight

    def get_description(self):
        return self.description


#Note 1- 
# Incorporating Subclasses using their own attributes for increased item variation and gameplay additions
#End

# Offensive Items:
class Offensive(Item):
    def __init__(self, name, weight, description, damage):
        self.damage = damage
        #Here I start to use Supers to overwrite names and create subclasses which can be instantiated as they are, instances then contain what is set in class
        super().__init__(name, weight, description) 

    def get_damage(self):
        return self.damage

class Lost_Blade(Offensive):
    def __init__(self):
        super().__init__(name="Lost Blade", weight=20, description="A  suitable tempered blade imbued with a strange essence, it could be enhanced", damage=10)


    # Function to upgrade weapon:
    # def Enhance(self, parameter_list):
    #     pass

# Protection Items:
class Protection(Item):
    def __init__(self, name, weight, description, durability, defense):
        self.durability = durability
        self.defense = defense

    def get_durability(self):
        return self.durability

    def get_defense(self):
        return self.defense

class Warrior_Helmet(Protection):
    def __init__(self):
        super().__init__(name="Warrior Helmet", weight=5, description="Helmet of a Warrior", durability=100, defense=25)

class Warrior_Chestplate(Protection):
    def __init__(self):
        super().__init__(name="Warrior Chestplate", weight=10, description="Chestplate of a Warrior", durability=100, defense=25)

class Warrior_Leggings(Protection):
    def __init__(self):
        super().__init__(name="Warrior Leggings", weight=10, description="Leggings of a Warrior", durability=100, defense=15)

class Warrior_Greaves(Protection):
    def __init__(self):
        super().__init__(name="Warrior Greaves", weight=5, description="Greaves of a Warrior", durability=100, defense=25)

# Consumables:
class Consumables(Item):
    def __init__(self, name, weight, description, quantity):
        self.quantity = quantity

    def get_quantity(self):
        return self.quantity

class Meteora(Consumables):
    def __init__(self):
        super().__init__(name="Meteora", weight=5, description="An ominuous Material which looks like it can be used to enhance offensive attributes", quantity=self.quantity)
