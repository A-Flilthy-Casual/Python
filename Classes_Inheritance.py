#created by Roman Sanchez October 19th 2022
from turtle import distance
from typing import Tuple

"""
    vvvv      YOUR SOLUTION      vvvv
"""
# A function for storyline progression
def pause()->None:
    j=input("Press Enter key to continue the epic story...")
    print(j)


class Entity:

    def __init__(self, name: str, coords: Tuple[int, int], hit_points: int) -> None:
        # "constructor", more precisely "initializer"
        # initialize Entity here
        # name is string such as "Rob"
        # coords is tuple to represent x and y coordinates in the field: (1, 2) menas x = 1 and y = 2; expect also negative values
        # hitpoints represents count of remaining hitpoints as int, 0 or less hitpoints means death
        self.name=name
        self.coords=coords
        self.hit_points=hit_points

    

    def take_damage(self, damage_amount: int) -> None:
        # m# method to apply damage on this entity, it takes damage_amount and applies it by own rules to the entity
        # this is abstract method, just keep it as it is
        raise NotImplementedError("This method is abstract. Please implement it")  # in the child, not here :-)

    def is_alive(self) -> bool:
        # method to check if entity is alive
        # return True if it has hit points above 0
        # return False if it has hit points equal to 0 or less
        if self.hit_points>0:
            return True
        return False
        

    def get_distance(self, other_coords: Tuple[int, int]) -> int:
        # method to count distance to other object
        # for calculation of distance use Taxicab/Manhattan metric: https://en.wikipedia.org/wiki/Taxicab_geometry
        # returns the distance
        distance=abs(self.coords[0]-other_coords[0])+abs(self.coords[1]-other_coords[1])
        return distance


class Rock(Entity):

    def take_damage(self, damage_amount: int) -> None:
        # method to apply damage on this entity
        # rock takes damage only when it is hit with damage_amount of at least 10,
        # each such hit takes him 1 hitpoint, smaller hits don't cause any damage to him
        if damage_amount>=10:
            self.hit_points-=1
        


class Furniture(Entity):

    # add take_damage method as for the Rock
    # Furniture takes as damage the whole amount of damage_amount incoming
    def take_damage(self, damage_amount: int) -> None:
        self.hit_points-=damage_amount


class LivingEntity(Entity):

    def __init__(self, name: str, coords: Tuple[int, int], hit_points: int, level: int, damage: int, attack_range: int) -> None:
        # "constructor", more precisely "initializer"
        # use parent constructor
        # initialize level, damage and attack_range after both are ints
        super().__init__(name,coords,hit_points)
        self.level=level
        self.damage=damage
        self.attack_range=attack_range

    def level_up(self) -> None:
        # this method should increase the level of this entity by 1
        self.level+=1
        

    def take_damage(self, damage_amount: int) -> None:
        # method to apply damage on this entity
        # the whole damage_amount is applied to hitpoints
        self.hit_points-=damage_amount


    def hit(self, other_entity: Entity) -> None:
        # method to hit other entity to cause them to take damage
        # this is abstract method, just keep it as it is
        raise NotImplementedError("This method is abstract. Please implement it")  # in the child, not here :-)

    def move(self, vector: Tuple[int, int]) -> None:
        # method to make entity move on the board
        # it expects vector of steps in x and y directions, the vector is represented as tuple (x, y)
        # the move is executed by editing coordinates by the vector elements
        # x is editing x axis and y is editing y axis
        # +x, -x, +y, -y define also direction of move
        alist2=list(vector)
        alist=list(self.coords)
        alist[0]+=alist2[0]
        alist[1]+=alist2[1]
        self.coords=tuple(alist)
        vector=tuple(alist2)
        

    def in_range(self, other_entity: Entity) -> bool:
        # method to check if other entity is in range
        # return True if get_distance to other entity <= self.range
        # return False if get_distance to other entity > self.range
        if self.get_distance(other_entity.coords)<=self.attack_range:
            return True

        else:
            return False


class Warrior(LivingEntity):

    def hit(self, other_entity: Entity) -> None:
        # implement hit to another entity
        #   if other entity is in range make it to take damage with it's own method take_damage
        #       damage_amount applied to other entity is equal to damage of attacking entity
        if self.in_range(other_entity)==True:
            other_entity.take_damage(self.damage)

    def take_damage(self, damage_amount: int) -> None:
        # method to apply damage on this entity
        # Warrior is taking damage only when the damage_amount is bigger then his level
        #   If damage is bigger than level Warrior takes the difference as a damage_amount
        #   Else Warrior takes no damage
        if damage_amount>self.level:
            self.hit_points=self.hit_points-(damage_amount-self.level)

    def level_up(self) -> None:
        # this method should increase the level according to parent; use call to parent's method
        # also increase damage by 1 and hit_points by 2
        super().level_up()
        self.damage+=1
        self.hit_points+=2
        


class Archer(LivingEntity):

    def hit(self, other_entity: Entity) -> None:
        # implement hit to another entity
        #   if other entity is in range make it to take damage with it's own method take_damage
        #       damage_amount applied to other entity is equal to damage of attacking entity
        if self.in_range(other_entity)==True:
            other_entity.take_damage(self.damage)


    def level_up(self) -> None:
        # this method should increase the level according to parent; use call to parent's method
        # also increase damage by 2 and hit_points by 1
        super().level_up()
        self.damage+=2
        self.hit_points+=1


"""
    ^^^^      YOUR SOLUTION      ^^^^
#################################################################
    vvvv TESTS FOR YOUR SOLUTION vvvv
"""


# Simple Entity tests
entity = Entity("E", (0, 0), 10)
print("A new Era dawns as the entity'",entity.name,"'materializes at the origin of all")
pause()
# constructor
assert entity.name == "E"
assert entity.coords == (0, 0)
assert entity.hit_points == 10
# is alive check
assert entity.is_alive()
# get distance check
assert entity.get_distance((0, 0)) == 0

# Rock tests
rocky = Rock("Rocky", (0, 1), 5)

print("The previous era now known as the 'short lived era' is now over as a new type of entity spawns near the origin of all. '",rocky.name,"'is born")
# constructor
assert rocky.name == "Rocky"
assert rocky.coords == (0, 1)
assert rocky.hit_points == 5
# is alive check
assert rocky.is_alive()
# get distance check
assert rocky.get_distance((0, 0)) == 1
# damage taking
rocky.take_damage(7)
print("""Rock decides to focus his inner aura to sense nerby entitys as he has no senses.
Embassingly, he focuses too hard and his mental psyche takes a hit of 7. 
This is nothing for the entity known as Rock who pushes to find new limits.
He then refocuses.... only to take psyche damage of 100 resulting in a hit of one to his life force""")
pause()
assert rocky.hit_points == 5
rocky.take_damage(100)
assert rocky.hit_points == 4

# Table tests
table = Furniture("Table", (1, 0), 3)
# constructor
assert table.name == "Table"
assert table.coords == (1, 0)
assert table.hit_points == 3
# is alive check
assert table.is_alive()
# get distance check
assert table.get_distance((0, 0)) == 1
# damage taking
table.take_damage(2)
assert table.hit_points == 1
print("""Not to be outdone... 'E' decides to hit the nearest table that has always been there at (1,0)"
the entity impressivly does 2 damage""")
table.take_damage(2)
print("Not knowing its own power 'E' hits the table for another two damage killing it")
pause()
assert table.hit_points == -1
assert not table.is_alive()

# LivingEntity tests
tim = LivingEntity("Tim", (-1, 0), 3, 1, 1, 1)
print("Tim is willed into existence, perhaps by the efforts of Rock or 'E'")
# constructor
assert tim.name == "Tim"
assert tim.coords == (-1, 0)
assert tim.hit_points == 3
assert tim.level == 1
assert tim.damage == 1
assert tim.attack_range == 1
# is alive check
assert tim.is_alive()
# get distance check
assert tim.get_distance((0, 0)) == 1
# level up check
print("""After exisiting for a short period the LivingEntity Tim has aquired enough energy to ...
level up""")
pause()
tim.level_up()
assert tim.level == 2
# damage taking
tim.take_damage(1)
assert tim.hit_points == 2
assert tim.is_alive()
# move check
assert tim.in_range(entity)
tim.move((0, -1))
assert not tim.in_range(entity)

# Warrior tests
willy = Warrior("William Wallace", (1, 1), 3, 5, 8, 2)
print("""Not to be outdone the entity known as "e" decides to spawn his own LivingEntity named William Wallace""")
# constructor
assert willy.name == "William Wallace"
assert willy.coords == (1, 1)
assert willy.hit_points == 3
assert willy.level == 5
assert willy.damage == 8
assert willy.attack_range == 2
# is alive check
assert willy.is_alive()
# get distance check
assert willy.get_distance((0, 0)) == 2
# level up check
willy.level_up()
assert willy.hit_points == 5
assert willy.level == 6
assert willy.damage == 9
# damage taking
willy.take_damage(1)
assert willy.hit_points == 5
willy.take_damage(7)
assert willy.hit_points == 4
print(willy.name,"Takes some damage and what not leveling up and training...")
pause()
# fight checks
rocky = Rock("Rocky", (0, 1), 5)
willy.hit(rocky)
assert rocky.hit_points == 5
print(willy.name,"""Attempts to injure rocky, the son of rock...
He fails, miserably...""")
pause()
table = Furniture("Table", (1, 0), 3)
willy.hit(table)
assert table.hit_points == -6
tim = LivingEntity("Tim", (-1, 0), 3, 1, 1, 1)
willy.hit(tim)
assert tim.hit_points == 3
willy.move((-1, -1))
assert willy.get_distance((0, 0)) == 0
willy.hit(tim)
assert tim.hit_points == -6
print("William then fights a table, not intersting enough to narrate..")
# Archer tests
rob = Archer("Robin Hood", (5, 8), 3, 1, 7, 10)
# constructor
assert rob.name == "Robin Hood"
assert rob.coords == (5, 8)
assert rob.hit_points == 3
assert rob.level == 1
assert rob.damage == 7
assert rob.attack_range == 10
# is alive check
assert rob.is_alive()
# get distance check
assert rob.get_distance((0, 0)) == 13
# level up check
rob.level_up()
assert rob.hit_points == 4
assert rob.level == 2
assert rob.damage == 9
# damage taking
rob.take_damage(1)
assert rob.hit_points == 3
# fight checks
willy = Warrior("William Wallace", (1, 1), 3, 5, 8, 2)
print(rob.name,"Spawns in origins unknown, he quickly starts to harras William for his treatment of furniture")
rob.hit(willy)
print("this psychological blow leaves willy with only three hit points")
assert willy.hit_points == 3
rob.move((0, -1))
print("Of course Robinhood scurries about like the scoundrel he is")
rob.hit(willy)
print("He then hits William Wallace again...")
pause()
print("William Wallace is alive is now a",willy.is_alive(),"statement ;)")
assert willy.hit_points == -1
assert not willy.is_alive()