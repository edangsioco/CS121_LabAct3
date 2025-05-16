from abc import ABC, abstractmethod
import time
import random


# class: parent
class Plant(ABC):
    def __init__(self, name, species, soil_type, age, height, is_watered, has_photosynthesized, is_healthy):
        self.name = name
        self.species = species
        self.soil_type = soil_type
        self.age = age
        self.height = height
        self.is_healthy = is_healthy
        self._is_watered = is_watered
        self._has_photosynthesized = has_photosynthesized
    
    def water(self):
        if self.is_watered:
            print(f"\n| {self.name} has been nourished. Return when it thirsts once more.")
        else:
            print(f"\n| Moisture graces the soil of {self.name}.")
            self.is_watered = True

    def photosynthesize(self):
        if self.has_photosynthesized:
            print(f"\n| {self.name} is basking in sunlight and weaving energy—kindly let it be.")
        else:
            print(f"\n| {self.name} is performing the ancient art of photosynthesis.")
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

    @abstractmethod
    def grow(self):
        pass

    @abstractmethod
    def exit(self):
        pass


# class: child (1/6)
class Tree(Plant):
    def __init__(self, name, species, soil_type, age, height, has_photosynthesized, is_watered, is_healthy, can_drop_leaves=True, has_fruit=False):
        super().__init__(name, species, soil_type, age, height, has_photosynthesized, is_watered, is_healthy)
        self.can_drop_leaves = can_drop_leaves
        if self.age <= 12:
            self.growth_rate = 100
        elif self.age > 12 and self.age <= 36:
            self.growth_rate = 60
        else:
            self.growth_rate = 30
        self.has_fruit = has_fruit
        self.last_fruit_month = 0
        self.species = species
        
    def drop_leaves(self):
        if self.age > 15 and self.age % 6 == 0:
            self.can_drop_leaves = True
        else:
            self.can_drop_leaves = False

    def check_for_fruits(self):
        self.drop_leaves()
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
            harvest =  input(f"{self.name} is now bearing fruit. Harvest?\n(y/n): ").lower()
            if harvest == "y":
                print("\nHarvesting fruit...")
                time.sleep(3)
                print("Fruit has been harvested!")
                self.has_fruit = False
            else:
                print(f"{self.name}'s fruits stay.")
        else:
            print(f"\n| In due time, {self.name} will fruit—but not today.")

    def drop_leaves(self):
        if self.age > 15 and self.age % 6 == 0:
            self.can_drop_leaves = True
        else:
            self.can_drop_leaves = False
            
    def grow(self):
        if self.is_watered == True and self.has_photosynthesized == True:
            # age
            self.age += 1
            self.height += self.growth_rate
            self.has_photosynthesized = False
            self.is_watered = False
            if self.can_drop_leaves == True:
                print(f"\n{self.name} is dropping leaves.")
            self.can_drop_leaves = False
            
            # time passes
            print(f"\n| Entering month {self.age}...")
            time.sleep(4)
            print(f"|\n| {self.name} has grown by {self.growth_rate} cm. New height is {self.height} cm.")
        else:
            print(f"\n| Bestow water upon {self.name} first, and let photosynthesis work its quiet magic...")

    def exit(self):
        print("\nTree Information:")
        print(f"| Name       : {self.name}")
        print(f"| Species    : {self.species}")
        print(f"| Age        : {self.age}")
        print(f"| Height     : {self.height:.3f} cm")
        print(f"| Health     : {'Healthy' if self.is_healthy else 'Unhealthy'}")
        print(f"| Has Fruits : {'Yes' if self.has_fruit else 'No'}\n|")
        
        print(f"Together we've grown—thank you! 🌳🤗🌿\n")



# class: child (2/6)
class Shrub(Plant):
    def __init__(self, name, species, soil_type, height, age, has_photosynthesized, is_watered, is_healthy, has_thorns, is_wounded=False, can_shed_leaves=False):
        super().__init__(name, species, soil_type, height, age, is_watered, has_photosynthesized, is_healthy)
        self.can_shed_leaves = can_shed_leaves
        if self.age <= 6:
            self.growth_rate = 30
        elif 7 <= self.age <= 18:
            self.growth_rate = 10
        else:
            self.growth_rate = 30
        self.is_healthy = is_healthy
        self.num = random.randint(1,2)
        self.last_prune = 0
        self.is_wounded = is_wounded
        
    def _has_thorns(self):
        if self.has_thorns:
            wounded = random.randint(1,2)
            if wounded == 2:
                self.is_wounded = True
            else:
                self.is_wounded = False
                
    def shed_leaves(self):
        if self.age >= 12 and self.age % 6 == 0:
            self.can_shed_leaves = True
        else:
            self.can_shed_leaves = False
                
    def prune(self):
        self.shed_leaves()
        if (self.can_shed_leaves
            and not self.is_healthy
            and self.age - self.last_prune >= 0
            ):
            if self.has_thorns:
                print("Please be careful, the shrub has thorns.")
            choice2 = input(f"{self.name} is currently prunable. Proceed?\n(y/n): ")
            if choice2 == "y":
                print("\nCurrently pruning...")
                time.sleep(1)
                print("Removing the branch...")
                time.sleep(2)
                print(f"Pruning complete, the {self.name} is now healthy.")
                self._has_thorns()
                if self.is_wounded:
                    print(f"Ouch! The thorns have left their mark—tread carefully ahead.")
                self.is_wounded = False
                self.is_healthy = True
                self.last_prune = self.age

        elif (not self.can_shed_leaves
            and self.is_healthy
            and self.age - self.last_prune >= 1
            ):
            if self._has_thorns:
                print("\n| Please be careful, the shrub has thorns.")
            choice3 = input("\n| Plant is currently healthy. Pruning would only cause harm. Continue?\n(y/n): ")
            if choice3 == "y":
                print("Currently pruning...")
                time.sleep(1)
                print("Removing the branch...")
                time.sleep(2)
                if self.num == 1:
                    print(f"\n| Pruning complete. A small imperfection was gently healed. {self.name} now thrives even more!")
                    self.is_healthy = True
                else:
                    print(f"\n| The pruning is done, though {self.name} has suffered some distress...")
                    self.is_healthy = False
                    self._has_thorns()
                if self.is_wounded:
                    print(f"Ouch! The thorns have left their mark—tread carefully ahead.")
                self.is_wounded = False
                self.last_prune = self.age
        else:
            print(f"\n| {self.name} is currently too delicate for pruning.")

    def grow(self):
        if self.is_watered == True and self.has_photosynthesized == True and self.is_healthy == True:
            self.age += 1
            self.height += self.growth_rate
            self.has_photosynthesized = False
            self.is_watered = False
            if self.can_shed_leaves == True:
                print(f"{self.name} is shedding leaves.")
            self.can_drop_leaves = False
            print(f"\n| Entering month {self.age}...")
            time.sleep(4)
            print(f"{self.name} has grown by {self.growth_rate} cm. New height is {self.height} cm.")
            if self.age > 6 and self.age % 3 == 0:
                print(f"The {self.name} needs pruning.")
                self.is_healthy = False
        else:
            print(f"\n| Bestow water upon {self.name} first, and let photosynthesis work its quiet magic...") 
            
    def exit(self):
        print("\nShrub Information:")
        print(f"| Name       : {self.name}")
        print(f"| Species    : {self.species}")
        print(f"| Age        : {self.age}")
        print(f"| Height     : {self.height:.3f} cm")
        print(f"| Health     : {'Healthy' if self.is_healthy else 'Unhealthy'}")
        print(f"| Has Thorns : {'Yes' if self._has_thorns else 'No'}\n|")

        print("Your care has shaped a mighty shrub—farewell for now! 🌳🌟\n")



# class: child (3/6)
class Flower(Plant):
    def __init__(self, name, species, petal_color, soil_type, age, height, is_watered, has_photosynthesized, is_healthy, has_nectar=True, is_blooming=True):
        super().__init__(name, species, soil_type, age, height,  is_watered, has_photosynthesized, is_healthy)
        all_scents = ["Sweet", "Mild", "Fresh", "Strong", "Fruity", "Spicy"]
        self.scent = random.choice(all_scents)
        self.petal_color = petal_color
        self.is_healthy = is_healthy
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
        
    def check_blooming(self):
        if self.age >= 10:
            self.is_blooming = True
            
    def check_fragrance(self):
        print(f"\n| {self.name} has a {self.scent} fragrance.")
        choice4 = input("| Do you want to change the scent?\n(y/n): ")
        if choice4 == "y":
            all_scents = ["Sweet", "Mild", "Fresh", "Strong", "Fruity", "Spicy"]

            if hasattr(self, 'scent'):
                possible_scents = [s for s in all_scents if s != self.scent]
            else:
                possible_scents = all_scents

            self.scent = random.choice(possible_scents)
            print(f"\n| New scent is {self.scent}.")
        
    def attracted_pollinators(self):
        attracted_pollinators = []
        for pollinator, preferences in self.pollinator.items():
            if self.petal_color in preferences["colors"] and self.scent in preferences["scents"]:
                attracted_pollinators.append(pollinator)

        if attracted_pollinators:
            for pollinator in attracted_pollinators:
                print(f"\n| {pollinator.capitalize()} is attracted to the {self.petal_color} flower with a {self.scent} scent!")
                return True
        else:
            print(f"\n| No pollinator is attracted to the {self.petal_color} flower with a {self.scent} scent!")
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
            print(f"\n| Entering month {self.age}...")
            time.sleep(4)
            print(f"{self.name} has grown by {self.growth_rate} cm. New height is {self.height} cm.")
        else:
            print(f"\n| Bestow water upon {self.name} first, and let photosynthesis work its quiet magic...")
            
    def exit(self):
        print("\nFlower Information:")
        print(f"| Name                  : {self.name}")
        print(f"| Species               : {self.species}")
        print(f"| Age                   : {self.age}")
        print(f"| Height                : {self.height:.3f} cm")
        print(f"| Health                : {'Healthy' if self.is_healthy else 'Unhealthy'}")
        print(f"| Has Bloomed           : {'Yes' if self.is_blooming else 'No'}")
        print(f"| Attracted Pollinators : {'Yes' if self.attracted_pollinators else 'No'}\n|")

        print("The petals whisper their thanks. 🌺✨\n")



# class: child (4/6)
class Herb(Plant):
    def __init__(self, name, species, soil_type, age, height, is_watered, has_photosynthesized, is_healthy, herb_use=""):
        super().__init__(name, species, soil_type, age, height, is_watered, has_photosynthesized, is_healthy)
        self.herb_use = herb_use
        self.is_toxic = random.randint(1,5)
        if self.age <= 2:
            self.growth_rate = 15
        elif 3 < self.age <= 5:
            self.growth_rate = 10
        else:
            self.growth_rate = 5
        
    def check_consumption(self):
        if self.is_toxic >= 1:
            self.is_toxic = True
            print(f"\n| {self.name} is not safe to consume.")
            
            # safety change
            choice_safety = input(f"| Would you like to make {self.name} safe for consumption? \n(y/n): ")
            if choice_safety == "y":
                print("\n| Fairies are finalizing the magic… give them just 10 seconds!")
                time.sleep(10)
                self.is_toxic = False 
                print("|\n| By eliminating its toxic elements through precise processing, the once-dangerous plant is reborn as a safe and healing herb!")
                
            else: 
                print(f"\n| Really..?", end=" ")
                time.sleep(5)
                print("Alright then, moving on...")
        
        else:
            self.is_toxic = False
            print(f"\n| {self.name} is safe to consume.")
    
    def check_use(self):
        herb_uses = ["Aromatherapy", "Culinary Uses", "Crafts and Decor", "Household & Personal Care", "Medicinal Uses", "Pest Control"]
        use_type = []
        
        if self.is_toxic == False:
            use_type.append(herb_uses[1])
        
        if not use_type:
            print("\n| Nothing on the list...\n")
        else:
            print(f"\n| Uses so far: {use_type}.\n")
            
        # additional input
        print("Here are the available uses:")
        for index, use in enumerate(herb_uses, 1):
            print(f"{index}. {use}")

        # select a use / add their own4
        user_input = input("\n| Select a number for a use from the list, \nor type your own use: ")

        # check input is a valid number from the list
        if user_input.isdigit() and 1 <= int(user_input) <= len(herb_uses):
            # picked from the list
            use_type.append(herb_uses[int(user_input) - 1])
        else:
            # custom input
            use_type.append(user_input)
        self.herb_use = "".join(use_type)
        print(f"\n| Selected uses: {use_type}")
        
    def harvest(self):
        if self.age > 2 and self.is_healthy and self.is_watered and self.has_photosynthesized:
            print(f"\n| {self.name} is ready for a harvest!...")
            time.sleep(5)
            print("| Harvest complete!")
        else:
            print(f"\n| The {self.name} is too young to be harvested.")
        
    def grow(self):
        if self.is_watered == True and self.has_photosynthesized == True:
            # age herb
            self.height += self.growth_rate
            self.age += 1
            self.has_photosynthesized = False
            self.is_watered = False
            print(f"\n| Entering month {self.age}...")
            time.sleep(4)
            print(f"{self.name} has grown by {self.growth_rate} cm. New height is {self.height} cm.")
        else:
            print(f"\n| Bestow water upon {self.name} first, and let photosynthesis work its quiet magic...")
            
    def exit(self):
            print("\nHerb Information:")
            print(f"| Name                 : {self.name}")
            print(f"| Species              : {self.species}")
            print(f"| Age                  : {self.age}")
            print(f"| Height               : {self.height:.3f} cm")
            print(f"| Health               : {'Healthy' if self.is_healthy else 'Unhealthy'}")
            print(f"| Safe for Consumption : {'Yes' if self.check_consumption else 'No'}")
            print(f"| Used for             : {self.herb_use}\n|")

            print("The herb thanks you with a fragrant breeze. 🌾💨\n")



# class: child (5/6)
class Succulent(Plant):
        def __init__(self, name, species, soil_type, age, height, is_watered, has_photosynthesized, is_healthy, water_storage_type, is_storing_water=False):
            super().__init__(name, species, soil_type, age, height, is_watered, has_photosynthesized, is_healthy)
            valid_storage_types = ["leaves", "stems", "roots"]
            if water_storage_type not in valid_storage_types:
                print(f"\n| Invalid water storage type: {water_storage_type}. It must be one of {valid_storage_types}")
            self.water_storage_type = water_storage_type
            self.is_storing_water = is_storing_water
            if self.age <= 3:
                self.growth_rate = 1
            elif self.age > 3 and self.age <= 12:
                self.growth_rate = 2
            else:
                self.growth_rate = 3
                

        def water(self):
            if self.is_watered:
                print(f"\n| {self.name} has already been watered this month.")
            else:
                print(f"\n| {self.name} has been watered and is storing water in {self.water_storage_type}.")
                self.is_watered = True
                self.is_storing_water = True

        def grow(self):
            if not self.has_photosynthesized:
                print(f"\n| {self.name} needs to photosynthesize to grow.")
                
            elif self.is_watered:
                self.age+=1
                self.height += self.growth_rate
                self.is_watered = False
                self.has_photosynthesized = False
                print(f"\n| Entering month {self.age}...")
                time.sleep(4)
                print(f"{self.name} has grown by {self.growth_rate}cm using fresh water. ")
                print(f"New height is {self.height:.3f} cm.")
                
            elif self.is_storing_water:
                self.age +=1
                self.height += self.growth_rate
                self.is_storing_water = False
                self.has_photosynthesized = False
                print(f"\n| Entering month {self.age}...")
                time.sleep(4)
                print(f"{self.name} has grown by {self.growth_rate} cm using stored water from its {self.water_storage_type}.")
                print(f"New height is {self.height:.3f} cm.")
            else:
                print(f"{self.name} needs water to grow.")

        def check_water_storage(self):
            if self.is_storing_water == True:
                print(f"\n| The {self.name} has water stored in its {self.water_storage_type}.")
            else:
                print(f"\n| The {self.name} could use a drink.")

        def drought_protection(self):
            if self.is_storing_water == True:
                print(f"\n| The {self.name} can survive the drought because it has water stored in its {self.water_storage_type}.")
            else:
                print(f"\n| {self.name} won't survive the drought.")
                
        def exit(self):
            print("\nSucculent Information:")
            print(f"| Name               : {self.name}")
            print(f"| Species            : {self.species}")
            print(f"| Age                : {self.age}")
            print(f"| Height             : {self.height:.3f} cm")
            print(f"| Water Storage Type : {self.water_storage_type}")
            print(f"| Health             : {'Healthy' if self.is_healthy else 'Unhealthy'}")
            print(f"| Stored Water       : {'Yes' if self.is_storing_water else 'No'}\n|")

            print("Thanks for hydrating hope in the driest of places. 🌵✨")



# class: child (6/6)
class Vine(Plant):
        def __init__(self, name, species, soil_type, age, height, has_photosynthesized, is_watered, is_healthy, height_vertical, height_horizontal, thickness, spread_direction_vertical=False, spread_direction_horizontal=False):
            super().__init__(name, species, soil_type, age, height, is_watered, has_photosynthesized, is_healthy)
            self.thickness = thickness
            self.height_horizontal = height_horizontal
            self.height_vertical = height_vertical
            self.spread_direction_vertical = spread_direction_vertical
            self.spread_direction_horizontal = spread_direction_horizontal
            if self.age <= 3:
                self.growth_rate = 3
                self.thickness = 0.5
            elif self.age > 3 and self.age <= 12:
                self.growth_rate = 10
                self.thickness = 1
            else:
                self.growth_rate = 30
                self.thickness = 3
                
        def crawl(self):
            self.spread_direction_horizontal = True
            if not self.spread_direction_vertical and self.spread_direction_horizontal:
                print(f"\n| The vine {self.name} is now growing horizontally")
            elif self.spread_direction_vertical and self.spread_direction_horizontal:
                print(f"\n| The vine {self.name} is now growing horizontally and vertically")
            
        def climb(self):
            self.spread_direction_vertical = True
            if self.spread_direction_vertical and not self.spread_direction_horizontal:
                print(f"\n| The vine {self.name} is now growing vertically")
            elif self.spread_direction_vertical and self.spread_direction_horizontal:
                print(f"\n| The vine {self.name} is now growing vertically and horizontally")
            
        def check_vine_spread(self):
            if self.spread_direction == "Vertically" or self.spread_direction == "Horizontally":
                print(f"\n| {self.name} is now spreading {self.spread_direction} at the rate {self.growth_rate} per day and is currently {self.thickness} in diameter.")
            else:
                print(f"\n| {self.name} is now spreading at the rate {self.growth_rate} per day and is currently {self.thickness} in diameter.")

        def grow(self):
            if self.is_watered == True and self.has_photosynthesized == True:
                if self.spread_direction_vertical and not self.spread_direction_horizontal:
                    self.height_vertical += self.growth_rate 
                elif not self.spread_direction_vertical and self.spread_direction_horizontal:
                    self.height_horizontal += self.growth_rate 
                elif (self.spread_direction_vertical and self.spread_direction_horizontal) or (not self.spread_direction_vertical and not self.spread_direction_horizontal):
                    self.height_horizontal += self.growth_rate 
                    self.height_vertical += self.growth_rate 
                self.age += 1
                self.has_photosynthesized = False
                self.is_watered = False
                print(f"\n| Entering month {self.age}...")
                time.sleep(4)
                if not self.spread_direction_vertical and self.spread_direction_horizontal:
                    print(f"{self.name} has grown horizontally by {self.growth_rate} cm. New horizontal height is {self.height_horizontal} cm, New vertical height is {self.height_vertical} cm, and current thickness is {self.thickness} cm.")
                elif self.spread_direction_vertical and not self.spread_direction_horizontal:
                    print(f"{self.name} has grown vertically by {self.growth_rate} cm. New vertical height is {self.height_vertical} cm, new horizontal height is {self.height_horizontal} cm, and current thickness is {self.thickness} cm.")
                else:
                    print(f"{self.name} has grown by {self.growth_rate} cm. New vertical height is {self.height_vertical} cm, new horizontal height is {self.height_horizontal} cm, and current thickness is {self.thickness} cm.")
                self.spread_direction_vertical = False
                self.spread_direction_horizontal = False
            else:
                print(f"\n| Bestow water upon {self.name} first, and let photosynthesis work its quiet magic...")
                
        def exit(self):
            print("\nVine Information:")
            print(f"| Name              : {self.name}")
            print(f"| Species           : {self.species}")
            print(f"| Age               : {self.age}")
            print(f"| Vertical Height   : {self.height_vertical:.3f} cm")
            print(f"| Horizontal Spread : {self.height_horizontal:.3f} cm")
            print(f"| Thickness         : {self.thickness:.3f} cm")
            print(f"| Health            : {'Healthy' if self.is_healthy else 'Unhealthy'}\n|")

            print("Twisting, trailing, and truly grateful. 💚🌿\n")


########################################################################################################################################

# soil for plants
soil_types = ["sandy", "clay", "silty", "loamy", "peaty", "chalky"]

# MENU
print()
print("| 🌼 Step into the Garden: Welcome to the Plant Simulator! 🌼\n|")


while(True):
    print("| Choose a plant:")
    print("| 1. Tree      4. Herb         7. Exit")
    print("| 2. Shrub     5. Succulent")
    print("| 3. Flower    6. Vine\n|")
    choice = input("Enter the number of your choice (1-7): ")

    
    # Plant: Tree
    if choice == "1":
        name = input("\n| Grant this plant its rightful name! \nName: ").capitalize() + " Tree"
        height = 0
        age = 0
        is_healthy = True
        
        # set soil type
        while(True):
            soil_type = input("\n| Enter soil type: (Chalky, Clay, Loamy, Peaty, Sandy, Silty)\n... I pick: ").lower()

            if soil_type == "sandy" or soil_type == "chalky":
                print("\nTrees are not compatible with that soil, please select again.")
            elif soil_type not in soil_types:
                print("\nOh dear, it seems that soil type isn't in our records. Let's try again!")
            else:
                break
        
        # set status
        is_watered = False
        has_photosynthesized = False
        species = "Tree"
        plant = Tree(name, species, soil_type, height, age, is_watered, has_photosynthesized, is_healthy)
        while True:
            print(f"\n| MONTH {plant.age}")
            print("| Note:    In order to bear fruit, must be at least 15 months old,")
            print("|         and it must have been watered and undergone photosynthesis.")
            print("|\n| What do you want to do?")
            print("| 1. Water the plant         5. Check for fruits")
            print("| 2. Photosynthesize ")
            print("| 3. Go to the next month")
            print("| 4. Exit")

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
            elif choice1 == "5":
                plant.check_for_fruits()
                input("Press enter to continue...")
            elif choice1 == "4":
                plant.exit()
                break

    
    # Plant: Shrub
    elif choice == "2":
        name = input("\n| Grant this plant its rightful name! \nName: ").capitalize() + " Shrub"
        height = 0
        age = 0

        # set soil type
        while(True):
            soil_type = input("\nEnter soil type: (Chalky, Clay, Loamy, Peaty, Sandy, Silty)\n... I pick: ").lower()
            
            if soil_type == "sandy" or soil_type == "chalky":
                print("\nShrubs are not compatible with that soil, please select again.")
            elif soil_type not in soil_types:
                print("\nOh dear, it seems that soil type isn't in our records. Let's try again!")
            else:
                break
        
        # thorny shrub?
        while(True):
            choice_thorns = input("\n| Would you like the shrub to have thorns? (y/n): ").lower()
            if choice_thorns == 'y':
                has_thorns = True
                print(f"The {name} shall contain thorns.")
                break
            elif choice_thorns == 'n':
                has_thorns = False
                print(f"No thorns for the {name}")
                break
            else:
                print("\nAlas, that isn't a valid choice. Pick again, wise one.\n")
        
        # set status
        is_healthy = True
        is_watered = False
        has_photosynthesized = False
        species = "Shrub"
        plant = Shrub(name, species, soil_type, height, age, is_watered, has_photosynthesized, is_healthy, has_thorns)
        while True:
            print(f"\n| MONTH {plant.age}\n|")
            print("| What do you want to do?")
            print("| 1. Water the plant         4. Exit")
            print("| 2. Photosynthesize         5. Prune")
            print("| 3. Go to the next month    ")

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
            elif choice1 == "5":
                plant.prune()
                input("Press enter to continue...")
            elif choice1 == "4":
                plant.exit()
                break


    
    # Plant: Flower
    elif choice == "3":
        name = input("\n| Grant this plant its rightful name! \nName: ").capitalize()
        height = 0
        age = 0
        petal_colors = ["Red", "Orange", 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet', 'White', 'Pink']
        
        # set colors
        while(True):
            print("\n| Kindly select your colors from the palette below: " )
            print("| Red, Orange, Yellow, Green, Blue, Indigo, Violet, White, Pink")
            petal_color = input("Chosen hue: ").capitalize()
            
            if petal_color not in petal_colors:
                print("\nAlas, that isn't a valid choice. Pick again, wise one.\n")
            else:
                break
        
        # set soil type
        while(True):
            soil_type = input("\nEnter soil type: (Chalky, Clay, Loamy, Peaty, Sandy, Silty)\n... I pick: ").lower()
            
            if soil_type == "clay" or soil_type == "chalky":
                print("Flowers are not compatible with that soil, please select again.")
            elif soil_type not in soil_types:
                print("\nOh dear, it seems that soil type isn't in our records. Let's try again!")
            else:
                break
        
        # set status
        is_healthy = True
        is_watered = False
        has_photosynthesized = False
        species = "Flower"
        plant = Flower(name, species, petal_color, soil_type, height, age, is_watered, has_photosynthesized, is_healthy)
        while True:
            print(f"\n| MONTH {plant.age}\n|")
            print("| What do you want to do?")
            print("| 1. Water the plant         5. Check scent")
            print("| 2. Photosynthesize         6. Attract Pollinators")
            print("| 3. Go to the next month")
            print("| 4. Exit")

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
            elif choice1 == "5":
                plant.check_fragrance()
                input("Press enter to continue...")
            elif choice1 == "6":
                plant.attracted_pollinators()
                input("Press enter to continue...")
            elif choice1 == "4":
                plant.exit()
                break

    
    # Plant: Herb
    elif choice == "4":
        name = input("\n| Grant this plant its rightful name! \nName: ").capitalize()
        age = 0
        height = 0
        is_healthy = True
        is_watered = False
        has_photosynthesized = False
        use_type = 0
        species = "Herb"
        
        # set soil type
        soil_type = input("\nEnter soil type: (Chalky, Clay, Loamy, Peaty, Sandy, Silty)\n... I pick: ").lower()
        
        while(True):
            if soil_type == "sandy" or soil_type == "chalky" or soil_type == "peaty":
                print("\nHerbs are not compatible with that soil, please select again.")
            elif soil_type not in soil_types:
                print("\nOh dear, it seems that soil type isn't in our records. Let's try again!")
            else:
                break
        
        # set status
        plant = Herb(name, species, soil_type, age, height, is_watered, has_photosynthesized, is_healthy)
        
        while True:
            print(f"\n| MONTH {plant.age}\n|")
            print("| What do you want to do?")
            print("| 1. Water the plant         5. Check use")
            print("| 2. Photosynthesize         6. Check consumption safety")
            print("| 3. Go to the next month    7. Harvest")
            print("| 4. Exit")
            
            choice_herb = input("Enter number of your choice: ")
            if choice_herb == "1":
                plant.water()
                input("Press enter to continue...")
            elif choice_herb == "2":
                plant.photosynthesize()
                input("Press enter to continue...")
            elif choice_herb == "3":
                plant.grow()
                input("Press enter to continue...")
            elif choice_herb == "6":
                plant.check_consumption()
                input("Press enter to continue...")
            elif choice_herb == "5":
                plant.check_use()
                input("Press enter to continue...")
            elif choice_herb == "7":
                plant.harvest()
                input("Press enter to continue...")
            elif choice_herb == "4":
                plant.exit()
                break

    # Plant: Succulent
    elif choice == "5":
        name = input("\n| Grant this plant its rightful name! \nName: ").capitalize()
        species = "Succulent"
        height = 0
        age = 0
        is_watered = False
        has_photosynthesized = False
        is_healthy = True
        
        # set soil type
        soil_types = ["sandy", "clay", "silty", "loamy", "peaty", "chalky"]
        while(True):
            soil_type = input("\nEnter soil type: (Chalky, Clay, Loamy, Peaty, Sandy, Silty)\n... I pick: ").lower()
            if soil_type in ["clay", "peaty", "silty"]:
                print("\nSucculents are not compatible with that soil, please select again.")
            elif soil_type not in soil_types:
                print("\nOh dear, it seems that soil type isn't in our records. Let's try again!")
            else:
                break

        storage_type = input("\n| Enter the storage type (leaves, stems, roots): \n... I pick: ").lower()
        while storage_type not in ["leaves", "stems", "roots"]:
            print(f"\n| Invalid storage type. Please choose leave, stems, or roots.")
            storage_type = input("Enter the storage type: ").lower()
        
        # set status
        plant = Succulent(name, species, soil_type, age, height, is_watered, has_photosynthesized, is_healthy, storage_type, is_storing_water=False)
        while True:
            print(f"\n| MONTH {plant.age}\n|")
            print("| What do you want to do?")
            print("| 1. Water the plant         5. Check water storage")
            print("| 2. Photosynthesize         6. Check drought protection")
            print("| 3. Go to the next month")
            print("| 4. Exit")
            
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
            elif choice1 == "5":
                plant.check_water_storage()
                input("Press enter to continue...")
            elif choice1 == "6":
                plant.drought_protection()
                input("Press enter to continue...")
            elif choice1 == "4":
                plant.exit()
                break

    
    # Plant: Vine
    elif choice == "6":
        name = input("\n| Grant this plant its rightful name! \nName: ").capitalize()
        species = "Vine"
        height = 0
        height_vertical = 0
        height_horizontal = 0
        thickness = 0
        age = 0
        
        # set soil type
        soil_type = input("\nEnter soil type: (Chalky, Clay, Loamy, Peaty, Sandy, Silty)\n... I pick: ").lower()
        while(True):
            if soil_type == "chalky":
                print("\nVines are not compatible with that soil, please select again.")
            elif soil_type not in soil_types:
                print("\nOh dear, it seems that soil type isn't in our records. Let's try again!")
            else:
                break
        
        # set status
        is_healthy = True
        is_watered = False
        has_photosynthesized = False
        plant = Vine(name, species, soil_type, age, height, is_watered, has_photosynthesized, is_healthy, height_vertical, height_horizontal, thickness)
        while(True):
            print(f"\n| MONTH {plant.age}\n|")
            print("| What do you want to do?")
            print("| 1. Water the plant         5. Climb")
            print("| 2. Photosynthesize         6. Crawl")
            print("| 3. Go to the next month")
            print("| 4. Exit")  

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
            elif choice1 == "5":
                plant.climb()
                input("Press enter to continue...")
            elif choice1 == "6":
                plant.crawl()
                input("Press enter to continue...")
            elif choice1 == "4":
                plant.exit()
                break

    
    # exit
    elif choice == "7":
        print("\n| With gratitude from the garden — thank you! 🌷\n")
        break
    else:
        print("Alas, that isn't a valid choice. Pick again, wise one.")

    
