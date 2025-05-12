from abc import ABC, abstractmethod
import time
import random

# class: PARENT
class Plant(ABC):
    def __init__(self, name, soil_type, age, height, growth_rate, is_watered, has_photosynthesized=False, is_healthy=True):
        self.name = name
        self.species = species
        self.soil_type = soil_type
        self.age = age
        self.height = height
        self.growth_rate = growth_rate
        self.is_healthy = is_healthy
        self._is_watered = is_watered
        self._has_photosynthesized = has_photosynthesized
    
    def water(self):
        if self.is_watered:
            print(f"{self.name} has been watered. Please try again next time")
        else:
            print(f"{self.name} has been watered.")
            self.is_watered = True

    def photosynthesize(self):
        if self.has_photosynthesized:
            print(f"{self.name} is currently photosynthesizing. Please do not disturb.")
        else:
            print(f"{self.name} is converting sunlight into energy through photosynthesis.")
            self.has_photosynthesized = True
            
    @property
    def is_watered(self):
        return self._is_watered
    
    @is_watered.setter
    def is_watered(self, value):
        self._is_watered = value
    
    @property
    def has_photosynthesized(self):
        return self._has_photosynthesized
    
    @has_photosynthesized.setter
    def has_photosynthesized(self, value):
        self._has_photosynthesized = value

    def grow(self):
        pass

# class: CHILD (1)
class Tree(Plant):
    def __init__(self, name, harvest, height, age, soil_type, growth_rate, can_drop_leaves=True, has_fruit = False):
        super().__init__(name, age, soil_type, growth_rate, height, has_photosynthesized, is_watered, is_healthy=True)
        self.can_drop_leaves = can_drop_leaves
        if self.age <= 12:
            self.growth_rate = 100
        elif self.age > 12 and self.age <= 36:
            self.growth_rate = 60
        else:
            self.growth_rate = 30
        self.harvest = harvest
        self.has_fruit = has_fruit
        self.last_fruit_month = 0

    def check_for_fruits(self):
        if (
        self.age >= 15
        and self.is_watered
        and self.has_photosynthesized
        and not self.has_fruit
        and self.age - self.last_fruit_month >= 3
         ):
            self.has_fruit = True
            self.last_fruit_month = self.age

        if self.has_fruit:
            harvest =  input(f"{self.name} is now bearing fruit. Harvest(y/n)? ").lower()
            if harvest == "y":
                    print("Harvesting fruit...")
                    time.sleep(3)
                    print("Fruit has been harvested!")
                    self.has_fruit = False
            else:
                 print(f"{self.name}'s fruits stay.")
        else:
            print(f"{self.name} is not ready to produce fruits.")

    def shed_leaves(self):
        if self.age > 15 and self.age % 6 == 0:
            self.can_drop_leaves = True
        else:
            self.can_drop_leaves = False
            
    def grow(self):
        if self.is_watered == True and self.has_photosynthesized == True:
            self.age += 1
            self.height += self.growth_rate
            self.has_photosynthesized = False
            self.is_watered = False
            if self.can_drop_leaves == True:
                print(f"{self.name} is sheding leaves.")
            self.can_drop_leaves = False
            print(f"Entering month {self.age + 1}...")
            time.sleep(4)
            print(f"{self.name} has grown by {self.growth_rate} cm. New height is {self.height} cm.")
        else:
            print(f"Please water the {self.name} first and let it photosynthesize...")

# class: CHILD (2)
class Shrub(Plant):
    def __init__(self, name, soil_type, height, age, choice2, choice3, can_shed_leaves=False, is_healthy=True):
        super().__init__(name, age, soil_type, height, has_photosynthesized, is_watered)
        self.can_shed_leaves = can_shed_leaves
        if self.age <= 6:
            self.growth_rate = 30
        elif self.age > 7 and self.age <= 18:
            self.growth_rate = 10
        else:
            self.growth_rate = 30
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
            choice2 = input(f"{self.name} is currently prunable. Proceed(y/n)?")
            if choice2 == "y":
                print("Currently pruning...")
                time.sleep(1)
                print("removing the branch...")
                time.sleep(2)
                print(f"Pruning complete, the {self.name} is now healthy.")
                self.is_healthy = True
                self.last_prune = self.age

        elif (self.can_shed_leaves == False
              and self.is_healthy == True
              and self.age - self.last_prune >= 1
              ):
            choice3 = input("Plant is currently healthy. Pruning would only cause harm. Continue(y/n)?")
            if choice3 == "y":
                print("Currently pruning...")
                time.sleep(1)
                print("removing the branch...")
                time.sleep(2)
                if self.num == 1:
                    print(f"Pruning complete. A minor issue was found and fixed. The pruning has made {self.name} even healthier!")
                    self.is_healthy = True
                else:
                    print(f"Pruning complete. The pruning has made the {self.name} unhealthy")
                    self.is_healthy = False
                self.last_prune = self.age
        else:
            print(f"{self.name} cannot be pruned for now.")

    def shed_leaves(self):
        if self.age >= 12 and self.age % 6 == 0:
            self.can_shed_leaves = True
        else:
            self.can_shed_leaves = False

    def grow(self):
        if self.is_watered == True and self.has_photosynthesized == True and self.is_healthy == True:
            self.age += 1
            self.height += self.growth_rate
            self.has_photosynthesized = False
            self.is_watered = False
            if self.can_drop_leaves == True:
                print(f"{self.name} is sheding leaves.")
            self.can_drop_leaves = False
            print(f"Entering month {self.age + 1}...")
            time.sleep(4)
            print(f"{self.name} has grown by {self.growth_rate} cm. New height is {self.height} cm.")
            if self.age > 6 and self.age % 3 == 0:
                print(f"The {self.name} needs pruning.")
                self.is_healthy = False
        else:
            print(f"Please water and prune the {self.name} plant first and let it photosynthesize...")       
            
# class: CHILD (3)
class Flower(Plant):
    def __init__(self, name, petal_color, soil_type, choice4, height, age, has_nectar=True, is_blooming = True):
        super().__init__(name, soil_type, age,height, has_photosynthesized, is_watered, is_healthy=True)
        all_scents = ["Sweet", "Mild", "Fresh", "Strong", "Fruity", "Spicy"]
        self.scent = random.choice(all_scents)
        self.petal_color = petal_color
        self.pollinator = {
                "bee": {
                    "colors": ["Blue", "Purple", "Violet", "White", "Yellow"],
                    "scents": ["Sweet", "Mild", "Fresh"]
                },
                "butterfly": {
                    "colors": ["Red", "Pink", "Orange", "Purple"],
                    "scents": ["Light", "Sweet"]
                },
                "moth": {
                    "colors": ["White", "Pink", "Yellow"],
                    "scents": ["Strong", "Sweet", "Night-Scented"]
                },
                "beetle": {
                    "colors": ["White", "Green", "Dull Red"],
                    "scents": ["Fruity", "Spicy"]
                }
            }

        self.has_nectar = has_nectar
        self.is_blooming = is_blooming
        if self.age <= 2:
            self.growth_rate = 13
        elif self.age > 3 and self.age <= 5:
            self.growth_rate = 8
        else:
            self.growth_rate = 3
        self.choice4 = choice4
    def check_blooming(self):
        if self.age >= 10:
            self.is_blooming = True
            

    def check_fragrance(self):
        print(f"{self.name} has a {self.scent} fragrance.")
        choice4 = input("Do you want to change the scent (y/n)? ")
        if choice4 == "y":
            all_scents = ["Sweet", "Mild", "Fresh", "Strong", "Fruity", "Spicy"]

            if hasattr(self, 'scent'):
                possible_scents = [s for s in all_scents if s != self.scent]
            else:
                possible_scents = all_scents

            self.scent = random.choice(possible_scents)
            print(f"New scent is {self.scent}")
        
    def attracted_pollinators(self):
        attracted_pollinators = []
        for pollinator, preferences in self.pollinator.items():
            if self.petal_color in preferences["colors"] and self.scent in preferences["scents"]:
                attracted_pollinators.append(pollinator)

        if attracted_pollinators:
            for pollinator in attracted_pollinators:
                print(f"{pollinator.capitalize()} is attracted to the {self.petal_color} flower with a {self.scent} scent!")
                return True
        else:
            print(f"No pollinator is attracted to the {self.petal_color} flower with a {self.scent} scent!")
            return False
    def grow(self):
        if self.is_watered == True and self.has_photosynthesized == True:
            self.height += self.growth_rate
            self.age += 1
            self.has_photosynthesized = False
            self.is_watered = False
            self.can_drop_leaves = False
            if self.is_blooming == True:
                print(f"{self.name} is currently blooming.")
            print(f"Entering month {self.age + 1}...")
            time.sleep(4)
            print(f"{self.name} has grown by {self.growth_rate} cm. New height is {self.height} cm.")
        else:
            print(f"Please water the {self.name} first and let it photosynthesize...")

# class: CHILD (4)
class Herb(Plant):
    def __init__(self, name, soil_type, age, height, growth_rate, use_type, choice_safety, is_watered=False, has_photosynthesized=False, is_healthy=True,  is_toxic=False):
        super().__init__(name, soil_type, age, height, growth_rate, is_watered, has_photosynthesized, is_healthy)
        self.growth_rate = growth_rate
        self.use_type = use_type
        self.choice_safety = choice_safety
        self.is_toxic = random.randint(1,5)
        
        
    def check_consumption_safety(self):
        if self.is_toxic == 1:
            self.is_toxic = True
            print(f"{self.name} is not safe to consume.")
            
            # safety change
            choice_safety = input(f"Would you like to make {self.name} safe for consumption? \n(y/n): ")
            if choice_safety == "y":
                print("Fairies are finalizing the magic… give them just 10 seconds!")
                time.sleep(10)
                self.is_toxic = False 
                print("By eliminating its toxic elements through precise processing, the once-dangerous plant is reborn as a safe and healing herb!")
                
            else: 
                print(f"Really..?", end=" ")
                time.sleep(3)
                print("Alright then, moving on...")
        
        else:
            self.is_toxic = False
            print(f"{self.name} is safe to consume.")
    
    def check_use(self):
        herb_uses = ["Aromatherapy", "Culinary Uses", "Crafts and Decor", "Household & Personal Care", "Medicinal Uses", "Pest Control"]
        use_type = []
        
        if self.is_toxic == False:
            use_type.append(herb_uses[1])
        
        if not use_type:
            print("Nothing on the list...\n")
        else:
            print(f"Uses so far: {use_type}\n.")
            
        # Prompt the user for additional input
        print("Here are the available uses:")
        for index, use in enumerate(herb_uses, 1):
            print(f"{index}. {use}")

        # select a use / add their own4
        user_input = input("Select a number for a use from the list, or type your own use: ")

        # check input is a valid number from the list
        if user_input.isdigit() and 1 <= int(user_input) <= len(herb_uses):
            # picked from the list
            use_type.append(herb_uses[int(user_input) - 1])
        else:
            # custom input
            use_type.append(user_input)

        print(f"Selected uses: {use_type}")
            

    def harvest(self):
        if (age > 2
        and self.is_healthy
        and self.is_watered
        and self.has_photosynthesized
        ):
            print(f"{self.name} is ready for a harvest!", end=" ")
            time.sleep(3)
            print("Harvest complete!")
        else:
            print(f"The {self.name} is too young to be harvested.")
        
    def grow(self):
        if self.is_watered == True and self.has_photosynthesized == True:
            # age herb
            self.age += 1
            
            if self.age <= 1:
                self.growth_rate = random.randint(1, 5)
            elif self.age <= 2:
                self.growth_rate = random.randint(1, 10)
            elif self.age <= 3:
                self.growth_rate = random.randint(1, 15)
            else:
                self.growth_rate = random.randint(1, 30)
            
            self.height += self.growth_rate
            self.has_photosynthesized = False
            self.is_watered = False
            
            print(f"Entering month {self.age}...")
            time.sleep(4)
            print(f"{self.name} has grown by {self.growth_rate} cm. New height is {self.height} cm.")
        else:
            print(f"Please water the {self.name} first and let it photosynthesize...")

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

# MENU
soil_types = ["sandy", "clay", "silty", "loamy", "peaty", "chalky"]
while(True):
    print("| Choose a plant:")
    print("| 1. Tree    3. Flower   5. Succulent   7. Exit")
    print("| 2. Shrub   4. Herb     6. Vine")
    choice = input("Enter the number of your choice (1-7):  ")

    # Plant: Tree
    if choice == "1":
        name = input("Enter name of the plant: ").capitalize() + " Tree"
        height = 0
        age = 0
        is_healthy = True
        while(True):
            
            soil_type = input("Enter soil type: (Sandy, Clay, Silty, Loamy, Peaty, Chalky): ").lower()

            if soil_type == "sandy" or soil_type == "chalky":
                print("Trees are not compatible with that soil, please select again.")
            elif soil_type not in soil_types:
                print("Invalid choice, please select again")
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

    # Plant: Shrub
    elif choice == "2":
        name = input("Enter name of the plant: ").capitalize()
        height = 0
        age = 0
        
        while(True):
            soil_type = input("Enter soil type: (Sandy, Clay, Silty, Loamy, Peaty, Chalky): ").lower()
            if soil_type == "sandy" or soil_type == "chalky":
                print("Shrubs are not compatible with that soil, please select again.")
            elif soil_type not in soil_types:
                print("Invalid choice, please select again")
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

    # Plant: Flower
    elif choice == "3":
        petal_colors = ["Red", "Orange", 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet', 'White', 'Pink']
        name = input("Enter name of the plant: ")
        while(True):
            print("For the colors please choose here:" )
            print("Red, Orange, Yellow, Green, Blue, Indigo, Violet, White, Pink")
            petal_color = input("Enter preferred color: ").capitalize()
            if petal_color not in petal_colors:
                print("Invalid choice, please select again")
            else:
                break

        height = 0
        age = 0
        
        while(True):
            soil_type = input("Enter soil type: (Sandy, Clay, Silty, Loamy, Peaty, Chalky): ").lower()
            if soil_type == "clay" or soil_type == "chalky":
                print("Flowers are not compatible with that soil, please select again.")
            elif soil_type not in soil_types:
                print("Invalid choice, please select again")
            else:
                break
        is_healthy = True
        is_watered = False
        has_photosynthesized = False
        plant = Flower(name, petal_color, soil_type, height, age, is_watered, has_photosynthesized)
        while True:
            print(f"MONTH {plant.age}")
            print("| What do you want to do?")
            print("| 1. Water the plant   3. Go to the next day")
            print("| 2. Photosynthesize   4. Check scent")
            print("| 5. Attract pollinators")

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
                plant.check_fragrance()
                input("Press enter to continue...")
            if choice1 == "5":
                plant.attracted_pollinators()
                input("Press enter to continue...")
        
    # Plant: Herb
    elif choice == "4":
        name = input("Enter name of the plant: ")
        age = 0
        height = 0
        growth_rate = 1
        is_healthy = True
        is_watered = False
        has_photosynthesized = False
        use_type = 0
        choice_safety= 0
        
        # pick soil
        soil_type = input("Enter soil type: (Sandy, Clay, Silty, Loamy, Peaty, Chalky): ").lower()
        while(True):
            if soil_type == "sandy" or soil_type == "chalky" or soil_type == "peaty":
                print("Herbs are not compatible with that soil, please select again.")
            elif soil_type not in soil_types:
                print("Invalid choice, please select again")
            else:
                break
        
        # existence of herb
        plant = Herb(name, soil_type, age, height, growth_rate, choice_safety, is_watered, has_photosynthesized)
        
        # care for herb
        while True:
            print(f"MONTH {plant.age}")
            print("| What do you want to do?")
            print("| 1. Water the plant     5. Check use")
            print("| 2. Photosynthesize     4. Check consumption safety")
            print("| 3. Go to the next day  6. Harvest")
            
            choice_herb = input("Enter number of your choice: ")
            if choice_herb == "1":
                plant.water()
                input("Press enter to continue...")
            if choice_herb == "2":
                plant.photosynthesize()
                input("Press enter to continue...")
            if choice_herb == "3":
                plant.grow()
                input("Press enter to continue...")
            if choice_herb == "4":
                plant.check_consumption_safety()
                input("Press enter to continue...")
            if choice_herb == "5":
                plant.check_use()
                input("Press enter to continue...")
            if choice_herb == "6":
                plant.harvest()
                input("Press enter to continue...")


    elif choice == "5":
        name = input("Enter name of the plant: ")
        species = "Succulent"
        height = 0
        age = 0
        soil_type = input("Enter soil type: (Sandy, Clay, Silty, Loamy, Peaty, Chalky): ").lower()
        while(True):
            if soil_type == "clay" or soil_type == "peaty" or soil_type == "silty":
                print("Trees are not compatible with that soil, please select again.")
            elif soil_type not in soil_types:
                print("Invalid choice, please select again")
            else:
                break
        is_healthy = True
        growth_rate = 0.3
        plant = Succulent(name, soil_type)


    elif choice == "6":
        name = input("Enter name of the plant: ")
        species = "Vine"
        height = 0
        age = 0
        soil_type = input("Enter soil type: (Sandy, Clay, Silty, Loamy, Peaty, Chalky): ").lower()
        while(True):
            if soil_type == "chalky":
                print("Trees are not compatible with that soil, please select again.")
            elif soil_type not in soil_types:
                print("Invalid choice, please select again")
            else:
                break
        is_healthy = True
        growth_rate = 4
        plant = Vine(name, species, height, age, soil_type)
        print(f"MONTH {plant.age}")
        print("| What do you want to do?")
        print("| 1. Water the plant          4. Check vine spread")
        print("| 2. Photosynthesize          5. Climb")
        print("| 3. Go to the next day       6. Crawl")

        choice1 = input("Enter number of your choice: ")
        if choice1 == "1":
            plant.water()
            input("Press enter to continue...")
        elif choice1 == "2":
            plant.photosynthesize()
            input("Press enter to continue...")
        elif choice1 == "3":
            plant.grow()
            input("Press enter to continue...")
        elif choice1 == "4":
            plant.check_vine_spread()
            input("Press enter to continue...")
        elif choice1 == "5":
            plant.climb()
            input("Press enter to continue...")
        elif choice1 == "6":
            plant.crawl()
            input("Press enter to continue...")

    elif choice == "7":
        print("Thank you for using the Plant Simulator!")
        break
    else:
        print("Invalid choice.")

    
