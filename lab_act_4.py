class Plant:
    def __init__(self, name, species, height, age, soil_type, growth_rate):
        self.name = name
        self.species = species
        self.height = height
        self.age = age
        self.soil_type = soil_type
        self.growth_rate = growth_rate
    
    def watering(self):
        print(f"{self.name} has been watered. The soil remains suitable for {self.soil_type} soil plants.")
    
    def photosynthesize(self):
        print(f"{self.name} is converting sunlight into energy through photosynthesis.")
    
    def grow(self):
        self.height += self.growth_rate
        print(f"{self.name} has grown by {self.growth_rate} cm. New height is {self.height} cm.")

    def lifespan(self):
        pass

class Tree(Plant):
    def __init__(self, name, height, age, soil_type, growth_rate, wood_type, is_fruitbearing=True, shed_leaves=True):
        super().__init__(name, height, age, soil_type, growth_rate)
        self.wood_type = wood_type
        self.is_fruitbearing = is_fruitbearing
        self.shed_leaves = shed_leaves

    def is_fruitbearing(self):
        if self.is_fruitbearing == False:
            print(f"{self.name} is not fruitbearing.")
        else:
            print(f"{self.name} is fruitbearing.")

    def shed_leaves(self):
        if self.shed_leaves == False:
            print(f"{self.name} is not ready to shed leaves.")
        else:
            print(f"{self.name} is ready to shed leaves.")

class Shrub(Plant):
    def __init__(self, name, species, age, soil_type, growth_rate, has_thorns=True, shed_leaves=True, is_healthy=True ):
        super().__init__(name, species, age, soil_type, growth_rate)
        self.has_thorns = has_thorns
        self.shed_leaves = shed_leaves
        self.is_healthy = is_healthy

    def shed_leaves(self):
        if self.shed_leaves == False:
            print(f"{self.name} is not ready to shed leaves.")
        else:
            print(f"{self.name} is ready to shed leaves.")

    def prune(self):
        if shed.leaves == False and is_healthy == True:
            return f"{self.name} is currently prunable."
        elif shed.leaves == True and is_healthy == False:
            return f"{self.name} is not currently prunable."
        elif shed.leaves == True and is_healthy == True:
            return f"{self.name} can be pruned now."
        else:
            return f"{self.name} cannot be pruned for now."

class Flower(Plant):
    def __init__(self, name, species, height, age, soil_type, growth_rate, petal_color, petal_type, scent, has_nectar=True):
        super().__init__(name, species, age, soil_type, growth_rate)
        self.petal_color = petal_color
        self.petal_type = petal_type
        self.scent = scent
        self.has_nectar = has_nectar
        #wadodoo: dictionary of pollinators
    def bloomed(self):
        if self.age >= 2: #years
            print(f"{self.name} is currently blooming.")

    def fragrance(self):
        print(f"{self.name} has a {self.scent} fragrance.")
        

    def attracted_pollinators(self):
        pass

class Herb(Plant):
    def __init__(name, species, height, age, soil_type, growth_rate, use_type, is_toxic):
        super().__init__(name)
        self.use = use_type
        self.is_toxic = True

    def harvest():
        print(f"Harvesting {self.name} for {self.use}")

    def check_safety():
        if is_toxic:
            print(f"{self.name} is not safe to consume")
        else: 
            print(f"{self.name} is safe to consume")

class Succulent(Plant):
        def __init__(name, species, height, age, soil_type, growth_rate, water_storage_type, is_water_stored):
        super().__init__(name, soil_type)
        self.water_storage = water_storage_type
        self.is_water_stored = is_water_stored
        

        def store_water():
            print(f"The {self.name} is now storing water...")
            return is_water_stored = True

        def drought_protection():
            if is_water_stored:
                print(f"The {self.name} can survive the drought.")
            else:
                print(f"{self.name} won't survive the drought.")

class Vine(Plant):
        def __init__(name, species, height, age, soil_type, growth_rate, thickness, spread_direction):
        super().__init__(name, growth_rate)
        self.thickness = thickness
        self.spread_direction = spread_direction

        def crawl():
            print(f"The vine {self.name} is now growing horizontally")
            spread_direction = "Horizontally"
        def climb():
            print(f"The vine {self.name} is now growing vertically")
            spread_direction = "Vertically"
        def spread():
            if spread_direction == "Vertically" or spread_direction == "Horizontally":
                print(f"{self.name} is now spreading {self.spread_direction} at the rate {self.growth_rate} per day and is currently {self.thick} in diameter.")
            else:
                print(f"{self.name} is now spreading at the rate {self.growth_rate} per day and is currently {self.thick} in diameter.")
        