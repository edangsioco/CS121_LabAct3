from abc import ABC, abstractmethod
import time
import random

# class: PARENT
class Plant(ABC):
    def __init__(self, name, soil_type, species, age, height, is_healthy=True, is_watered=False, has_photosynthesized=False):
        self.name = name
        self.soil_type = soil_type
        self.species = species
        self.age = age
        self.height = height
        self.is_healthy = is_healthy
        self.is_watered = is_watered
        self.has_photosynthesized = has_photosynthesized
    
    def water(self):
        if self.is_watered:
            print(f"{self.name} has been watered. Please try again next time.")
        else:
            self.is_watered = True
            print(f"{self.name} has been watered.")

    def photosynthesize(self):
        if self.is_photosynthesized:
            print(f"{self.name} is currently photosynthesizing. Please do not disturb.")
        else:
            self.is_photosynthesized = True
            print(f"{self.name} is converting sunlight into energy through photosynthesis.")
    
    @property
    def watered(self):
        return self._watered
    
    @watered.setter
    def watered(self, value):
        self._is_watered = value
    
    @property
    def photosynthesized(self):
        return self._photosynthesized
    
    @photosynthesized.setter
    def photosynthesized(self, value):
        self._is_photosynthesized = value

    @abstractmethod
    def grow(self):
        pass

    # @abstractmethod
    def check_lifespan(self):
        pass

# class: CHILD (1)
class Tree(Plant):
    def __init__(self, name, harvest, height, age, soil_type, growth_rate=2, can_drop_leaves=True, has_fruit=False):
        super().__init__(name=name, soil_type=soil_type, species="Tree", age=age, height=height, is_healthy=True, is_watered=False, has_photosynthesized=False)
        self.can_drop_leaves = can_drop_leaves
        self.growth_rate = growth_rate
        self.harvest = harvest
        self.has_fruit = has_fruit
        self.last_fruit_month = 0

    def check_for_fruits(self):
        # if Tree has no fruit:
        if (
        self.age >= 15 # months
        and self.is_watered
        and self.has_photosynthesized
        and not self.has_fruit
        and self.age - self.last_fruit_month >= 3
        ):
            self.has_fruit = True
            self.last_fruit_month = self.age

        # if Tree has fruit:
        if self.has_fruit:
            harvest =  input(f"{self.name} is now bearing fruit. Harvest? (y/n): ").lower()
            if harvest == "y":
                    print("Harvesting fruit... ")
                    time.sleep(3)
                    print("Fruit has been harvested!")
                    self.has_fruit = False
            else:
                print(f"{self.name}'s fruits stay.")
        else:
            print(f"{self.name} is not ready to produce fruits.")

    def drop_leaves(self):
        if self.age > 15 and self.age % 6 == 0:
            self.can_drop_leaves = True
        else:
            self.can_drop_leaves = False
            
    def grow(self):
        if self.is_watered == True and self.has_photosynthesized == True:
            self.height += self.growth_rate
            self.age += 1
            self.photosynthesized = False
            self.watered = False
            self.can_drop_leaves = False
            
            # optional logic?
            if self.can_drop_leaves:
                print(f"{self.name} is dropping leaves.")
            
            print(f"Entering month {self.age}... ")
            time.sleep(4)
            print(f"{self.name} has grown by {self.growth_rate} cm. New height is {self.height} cm.")
            
        else:
            print(f"Please water {self.name} first and let it photosynthesize...")

# class: CHILD (2)
class Shrub(Plant):
    def __init__(self, name, choice2, choice3, soil_type, height, age, can_shed_leaves=False, is_healthy=True):
        super().__init__(name, age, soil_type, height, is_watered=False, has_photosynthesized=False)
        self.can_shed_leaves = can_shed_leaves
        self.growth_rate = 1
        self.choice2 = choice2
        self.choice3 = choice3
        self.is_healthy = is_healthy
        self.num = random.randint(1,2)
        self.last_prune = 0

    def prune(self):
        if (not self.can_shed_leaves
            and not self.is_healthy
            and self.age - self.last_prune >= 3
            ):
            choice2 = input(f"{self.name} is currently prunable. Proceed? (y/n): ").lower()
            
            if choice2 == "y":
                print("Currently pruning... ")
                time.sleep(2)
                print("removing the branch...")
                time.sleep(4)
                print(f"Pruning complete, the {self.name} is now healthy.")
                self.is_healthy = True
                self.last_prune = self.age

        elif (self.can_shed_leaves == False
            and self.is_healthy == True
            and self.age - self.last_prune >= 1
            ):
            
            choice3 = input("Plant is currently healthy, but pruning right now could cause harm. Take the risk? (y/n): ").lower()
            
            if choice3 == "y":
                print("Currently pruning... ")
                time.sleep(2)
                print("Removing the branch...")
                time.sleep(4)
                
                if self.num == 1:
                    self.is_healthy = True
                    print(f"Pruning complete. A minor issue was found and fixed. The pruning has made {self.name} even healthier!")
                    
                else:
                    self.is_healthy = False
                    print(f"Pruning complete. The pruning has made the {self.name} unhealthy :(")
                
                self.last_prune = self.age
        else:
            print(f"{self.name} cannot be pruned right now.")

    def shed_leaves(self):
        if self.age >= 12 and self.age % 6 == 0:
            self.can_shed_leaves = True
        else:
            self.can_shed_leaves = False

    def grow(self):
        if self.is_watered == True and self.has_photosynthesized == True and self.is_healthy == True:
            self.height += self.growth_rate
            self.age += 1
            self.has_photosynthesized = False
            self.is_watered = False
            self.can_drop_leaves = False
            
            # optional logic? (2)
            if self.can_drop_leaves:
                print(f"{self.name} is shedding leaves.")
            
            print(f"Entering month {self.age}... ")
            time.sleep(4)
            print(f"{self.name} has grown by {self.growth_rate} cm. New height is {self.height} cm.")
            
            if self.age >= 12 and (self.age % 3 == 0 or self.age % 4 == 0):
                self.is_healthy = False
                print(f"The {self.name} could use some pruning.")

        else:
            print(f"Please water and prune {self.name} plant first, and let it photosynthesize...")       
            
# class: CHILD (3)
class Flower(Plant):
    def __init__(self, name, species, height, age, soil_type, growth_rate, petal_color, petal_type, scent, has_nectar=True):
        super().__init__(name, age, soil_type, growth_rate, height, has_photosynthesized=False, is_watered=False, is_healthy=True)
        self.petal_color = petal_color
        self.petal_type = petal_type
        self.scent = scent
        self.has_nectar = has_nectar
    
    def is_blooming(self):
        if self.age >= 2: # years
            print(f"{self.name} is currently blooming.")

    def check_fragrance(self):
        print(f"{self.name} has a {self.scent} fragrance.")
        
    def attracted_pollinators(self):
        pass

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


# SHELF OF KNOWLEDGE

# guide: Soil
soil_types = ["chalky", "clay", "loamy", "peaty", "sandy", "silty"]

# guide: Pollinators (placeholder, can be edited later)
pollinators = {
    "Bee": {
        "petal_color": ["Yellow", "Purple", "Blue"],
        "scent": ["Sweet", "Floral"],
    },
    "Butterfly": {
        "petal_color": ["Red", "Purple", "Orange"],
        "scent": ["Sweet", "Fruity"],
    },
    "Hummingbird": {
        "petal_color": ["Red", "Orange", "Pink"],
        "scent": ["Mild", "Sweet"],
    },
    "Moth": {
        "petal_color": ["White", "Pale Yellow", "Light Purple"],
        "scent": ["Strong", "Night-blooming"],
    },
    "Bat": {
        "petal_color": ["White", "Pale Green", "Purple"],
        "scent": ["Strong", "Musky"],
    },
}


# MENU
while(True):
    print("| Choose a plant:")
    print("| 1. Tree    3. Flower   5. Succulent   7. Exit")
    print("| 2. Shrub   4. Herb     6. Vine")
    choice = input("Enter the number of your choice (1-7):  ")

    # user choice Plant: Tree
    if choice == "1":
        name = input("Enter name of the plant: ").capitalize() + " Tree"
        species = "Tree"
        height = 0
        age = 0
        is_healthy = True
        
        while(True):            
            soil_type = input("Soil available: Chalky, Clay, Loamy, Peaty, Sandy, Silty \n Select one to use: ").lower()
            
            if soil_type == "sandy" or soil_type == "chalky":
                print("Trees are not compatible with that soil, please select again.")
            elif soil_type not in soil_types:
                print("We do not have that, please choose from the options available.")
            else:
                break
        
        is_watered = False
        has_photosynthesized = False
        
        plant = Tree(name, height, age, soil_type, is_watered, has_photosynthesized)
        
        while True:
            print(f"MONTH {age + 1}")
            print("Note: In order to bear fruit, must be at least 15 months old,")
            print("and it must have been watered and undergone photosynthesis.")
            print("\n| What do you want to do?")
            print("| 1. Water the plant   3. Go to the next day")
            print("| 2. Photosynthesize   4. Check for fruits")

            choice1 = input("Enter number of your choice: ")
            if choice1 == "1":
                plant.water()
                input("Press enter to continue...")
            if choice1 == "2":
                plant.photosynthesize()
                input("Press enter to continue...")
            if choice1 == "3":
                plant.grow()
                input("Press enter to continue...")
            if choice1 == "4":
                plant.check_for_fruits()
                input("Press enter to continue...")

    # user choice Plant: Shrub
    elif choice == "2":
        name = input("Enter name of the plant: ").capitalize()
        species = "Shrub"
        height = 0
        age = 0
        
        while(True):
            soil_type = input("Soil available: Chalky, Clay, Loamy, Peaty, Sandy, Silty \nSelect one to use: ").lower()
            
            if soil_type == "sandy" or soil_type == "chalky":
                print("Shrubs are not compatible with that soil, please select again.")
            elif soil_type not in soil_types:
                print("We do not have that, please choose from the options available.")
            else:
                break
        
        is_watered = False
        has_photosynthesized = False
        plant = Shrub(name, height, age, soil_type, is_watered, has_photosynthesized)
        
        while True:
            print(f"MONTH {plant.age}")
            print("| What do you want to do?")
            print("| 1. Water the plant   3. Go to the next day")
            print("| 2. Photosynthesize   4. Prune")

            choice1 = input("Enter number of your choice: ")
            if choice1 == "1":
                plant.water()
                input("Press enter to continue...")
            if choice1 == "2":
                plant.photosynthesize()
                input("Press enter to continue...")
            if choice1 == "3":
                plant.grow()
                input("Press enter to continue...")
            if choice1 == "4":
                plant.prune()
                input("Press enter to continue...")

    #3 user choice Plant: Flower
    elif choice == "3":
        name = input("Enter name of the plant: ")
        species = "Flower"
        height = 0
        age = 0
        
        while(True):
            soil_type = input("Soil available: Chalky, Clay, Loamy, Peaty, Sandy, Silty \n Select one to use: ").lower()
            
            if soil_type == "clay" or soil_type == "chalky":
                print("Flowers are not compatible with that soil, please select again.")
            elif soil_type not in soil_types:
                print("We do not have that, please choose from the options available.")
            else:
                break
        
        is_healthy = True
        growth_rate = 5
        plant = Flower(name, soil_type)
        
        sub_options(name, plant)
    
    # user choice Plant: Herb
    elif choice == "4":
        name = input("Enter name of the plant: ")
        species = "Herb"
        height = 0
        age = 0
        
        soil_type = input("Soil available: Chalky, Clay, Loamy, Peaty, Sandy, Silty \n Select one to use: ").lower()
        
        while(True):
            if soil_type == "sandy" or soil_type == "chalky" or soil_type == "peaty":
                print("Herbs are not compatible with that soil, please select again.")
            elif soil_type not in soil_types:
                print("Invalid choice, please select again")
            else:
                break
        
        is_healthy = True
        growth_rate = 7
        plant = Herb(name, soil_type)
        
        sub_options(name, plant)

    # user choice Plant: Succulent
    elif choice == "5":
        name = input("Enter name of the plant: ")
        species = "Succulent"
        height = 0
        age = 0
        
        soil_type = input("Soil available: Chalky, Clay, Loamy, Peaty, Sandy, Silty \n Select one to use: ").lower()
        
        while(True):
            if soil_type == "clay" or soil_type == "peaty" or soil_type == "silty":
                print("Trees are not compatible with that soil, please select again.")
            elif soil_type not in soil_types:
                print("We do not have that, please choose from the options available.")
            else:
                break
        
        is_healthy = True
        growth_rate = 0.3
        plant = Succulent(name, soil_type)
        
        sub_options(name, plant)

    # user choice Plant: vine
    elif choice == "6":
        name = input("Enter name of the plant: ")
        species = "Vine"
        height = 0
        age = 0
        
        soil_type = input("Soil available: Chalky, Clay, Loamy, Peaty, Sandy, Silty \n Select one to use: ").lower()
        
        while(True):
            if soil_type == "chalky":
                print("Trees are not compatible with that soil, please select again.")
            elif soil_type not in soil_types:
                print("We do not have that, please choose from the options available.")
            else:
                break
            
        is_healthy = True
        growth_rate = 4
        plant = Vine(name, soil_type)
        
        sub_options(name, plant)
        
    # EXIT
    elif choice == "7":
        print("Thank you for using the Plant Simulator!")
        break
    else:
        print("Invalid choice.")

    
