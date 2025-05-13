from abc import ABC, abstractmethod

# class: PARENT
class Plant:
    def __init__(self, name, species=None, age=0, soil_type=None, growth_rate=0, height=0, is_healthy=True):
        self.name = name
        self.species = species
        self.age = age
        self.soil_type = soil_type
        self.growth_rate = growth_rate
        self.height = height
        self.is_healthy = is_healthy
    
    def water(self):
        print(f"{self.name} has been watered. The soil remains suitable for {self.soil_type} soil plants.")
    
    def grow(self):
        self.height += self.growth_rate
        print(f"{self.name} has grown by {self.growth_rate} cm. New height is {self.height} cm.")

    def photosynthesize(self):
        print(f"{self.name} is converting sunlight into energy through photosynthesis.")

    def check_lifespan(self):
        pass
        # wadodo?

# class: CHILD (1)
class Tree(Plant):
    def __init__(self, name, height, age, soil_type, growth_rate, wood_type, is_fruit_bearing=True, can_drop_leaves=True):
        super().__init__(name, age, soil_type, growth_rate, height, is_healthy=True)
        self.wood_type = wood_type
        self.is_fruit_bearing = is_fruit_bearing
        self.can_drop_leaves = can_drop_leaves

    def check_for_fruits(self):
        if self.is_fruit_bearing == False:
            print(f"{self.name} is not fruit bearing.")
        else:
            print(f"{self.name} is fruit bearing.")

    def shed_leaves(self):
        if self.can_drop_leaves == False:
            print(f"{self.name} cannot shed leaves yet.")
        else:
            print(f"{self.name} is ready to shed leaves.")

# class: CHILD (2)
class Shrub(Plant):
    def __init__(self, name, species, age, soil_type, growth_rate, has_thorns=True, can_shed_leaves=True):
        super().__init__(name, species, age, soil_type, growth_rate, is_healthy=True)
        self.has_thorns = has_thorns
        self.can_shed_leaves = can_shed_leaves

    def prune(self):
        if self.can_shed_leaves == False and self.is_healthy == True:
            return f"{self.name} is currently prunable."
        elif self.shed_leaves == True and self.is_healthy == False:
            return f"{self.name} is not currently prunable."
        elif self.shed_leaves == True and self.is_healthy == True:
            return f"{self.name} can be pruned now."
        else:
            return f"{self.name} cannot be pruned for now."

    def shed_leaves(self):
        if not self.can_shed_leaves:
            print(f"{self.name} is not ready to shed leaves.")
        else:
            print(f"{self.name} is ready to shed leaves.")
            
# class: CHILD (3)
class Flower(Plant):
    def __init__(self, name, species, height, age, soil_type, growth_rate, petal_color, petal_type, scent, has_nectar=True):
        super().__init__(name, species, age, soil_type, growth_rate, is_healthy=True)
        self.petal_color = petal_color
        self.petal_type = petal_type
        self.scent = scent
        self.has_nectar = has_nectar
        
        #wadodoo: dictionary of pollinators
    
    def is_blooming(self):
        if self.age >= 2: # years
            print(f"{self.name} is currently blooming.")

    def check_fragrance(self):
        print(f"{self.name} has a {self.scent} fragrance.")
        
    def attracted_pollinators(self):
        pass
        # wadodo: another dictionary?

# class: CHILD (4)
class Herb(Plant):
    def __init__(self, name, species, height, age, soil_type, growth_rate, use_type, is_toxic=True):
        super().__init__(name, is_healthy=True)
        self.use_type = use_type
        self.is_toxic = is_toxic

    def check_safety(self):
        if self.is_toxic:
            print(f"{self.name} is not safe to consume.")
        else: 
            print(f"{self.name} is safe to consume.")

    def harvest(self):
        print(f"Harvesting {self.name} for {self.use}.")

# class: CHILD (5)
class Succulent(Plant):
        def __init__(self, name, species, height, age, soil_type, growth_rate, water_storage_type, is_storing_water=False):
            super().__init__(name, soil_type, is_healthy=True)
            self.water_storage = water_storage_type
            self.is_storing_water = is_storing_water

        def check_water_storage(self):
            if self.is_storing_water == True:
                print(f"The {self.name} has water stored.")
            else:
                print(f"The {self.name} could use a drink.")
    
        def store_water(self):
            print(f"The {self.name} is now storing water...")
            self.is_storing_water = True
            return self.is_storing_water

        def drought_protection(self):
            if self.is_storing_water == True:
                print(f"The {self.name} can survive the drought.")
            else:
                print(f"{self.name} won't survive the drought.")

# class: CHILD (6)
class Vine(Plant):
        def __init__(self, name, species, height, age, soil_type, growth_rate, thickness, spread_direction):
            super().__init__(name, species, age, soil_type, growth_rate, height, is_healthy=True)
            self.thickness = thickness
            self.spread_direction = spread_direction

        def crawl(self):
            print(f"The vine {self.name} is now growing horizontally")
            self.spread_direction = "Horizontally"
            
        def climb(self):
            print(f"The vine {self.name} is now growing vertically")
            self.spread_direction = "Vertically"
            
        def check_vine_spread(self):
            if self.spread_direction == "Vertically" or self.spread_direction == "Horizontally":
                print(f"{self.name} is now spreading {self.spread_direction} at the rate {self.growth_rate} per day and is currently {self.thickness} in diameter.")
            else:
                print(f"{self.name} is now spreading at the rate {self.growth_rate} per day and is currently {self.thickness} in diameter.")
        
