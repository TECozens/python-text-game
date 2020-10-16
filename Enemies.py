#Works the same as Item Class
class Enemy:
    def __init__(self, name, health, description, attack_dmg):
        self.name = name 
        self.description = description 
        self.health = health
        self.attack_dmg = attack_dmg

    def get_name(self):
        return self.name
    
    def get_attack_dmg(self):
        return self.attack_dmg

    def get_health(self):
        return self.health

    def set_health(self, dmg_dealt):
        self.health = self.health - dmg_dealt

    def get_description(self):
        return self.description

    

class Warmonger(Enemy):
    def __init__(self, name, health, description, attack_dmg):
        super().__init__(name="Warmonger", health=100, description="A Warmonger wielding a strong Axe be careful of his Swings!", attack_dmg=25)

    def warning(self):
        print(self.get_name(), 'Attacks with his Axe!\n  <<Deals', self.get_attack_dmg(),'>>')