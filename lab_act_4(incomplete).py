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

    def drop_leaves(self):
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
                print(f"{self.name} is dropping leaves.")
            self.can_drop_leaves = False
            print(f"Entering month {self.age + 1}...")
            time.sleep(4)
            print(f"{self.name} has grown by {self.growth_rate} cm. New height is {self.height} cm.")
        else:
            print(f"Please water the {self.name} first and let it photosynthesize...")

    def exit(self):
        print("\nPlant Information:")
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        print(f"Age: {self.age}")
        print(f"Height: {self.height:.3f} cm")
        print(f"Health: {'Healthy' if self.is_healthy else 'Unhealthy'}")
        print(f"Has Fruits: {'Yes' if self.has_fruit else 'No'}\n")
        print(f"Thank you for playing! ^ _ ^")
 

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
            choice2 = input(f"{self.name} is currently prunable. Proceed(y/n)?")
            if choice2 == "y":
                print("Currently pruning...")
                time.sleep(1)
                print("removing the branch...")
                time.sleep(2)
                print(f"Pruning complete, the {self.name} is now healthy.")
                self._has_thorns()
                if self.is_wounded:
                    print(f"You have been wounded by the thorns, please be careful next time!")
                self.is_wounded = False
                self.is_healthy = True
                self.last_prune = self.age

        elif (not self.can_shed_leaves
              and self.is_healthy
              and self.age - self.last_prune >= 1
              ):
            if self.has_thorns:
                print("Please be careful, the shrub has thorns.")
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
                self._has_thorns()
                if self.is_wounded:
                    print(f"You have been wounded by the thorns. Please be careful next time!")
                self.is_wounded = False
                self.last_prune = self.age
        else:
            print(f"{self.name} cannot be pruned for now.")

    def grow(self):
        if self.is_watered == True and self.has_photosynthesized == True and self.is_healthy == True:
            self.age += 1
            self.height += self.growth_rate
            self.has_photosynthesized = False
            self.is_watered = False
            if self.can_shed_leaves == True:
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
            
    def exit(self):
        print("\nPlant Information:")
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        print(f"Age: {self.age}")
        print(f"Height: {self.height:.3f} cm")
        print(f"Health: {'Healthy' if self.is_healthy else 'Unhealthy'}")
        print(f"Has thorns: {self.has_thorns}\n")
        print(f"Thank you for playing! ^ _ ^")    
            
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
            
    def exit(self):
        print("\nPlant Information:")
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        print(f"Age: {self.age}")
        print(f"Height: {self.height:.3f} cm")
        print(f"Health: {'Healthy' if self.is_healthy else 'Unhealthy'}")
        print(f"Has Bloomed: {'Yes' if self.is_blooming else 'No'}")
        print(f"Has Attracted pollinators: {'Yes' if self.attracted_pollinators else 'No'}\n")
        print(f"Thank you for playing! ^ _ ^")

# class: child (4/6)
class Herb(Plant):
    def __init__(self, name, species, soil_type, age, height, is_watered, has_photosynthesized, is_healthy, use_type=0):
        super().__init__(name, species, soil_type, age, height, is_watered, has_photosynthesized, is_healthy)
        self.use_type = use_type
        self.is_toxic = random.randint(1,5)
        if self.age <= 2:
            self.growth_rate = 15
        elif 3 < self.age <= 5:
            self.growth_rate = 10
        else:
            self.growth_rate = 5
        
    def check_consumption(self):
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
            
        # additional input
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

        return f"Selected uses: {use_type}"
        
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
            self.height += self.growth_rate
            self.age += 1
            self.has_photosynthesized = False
            self.is_watered = False
            print(f"Entering month {self.age}...")
            time.sleep(4)
            print(f"{self.name} has grown by {self.growth_rate} cm. New height is {self.height} cm.")
        else:
            print(f"Please water the {self.name} first and let it photosynthesize...")
            
    def exit(self):
                print("\nPlant Information:")
                print(f"Name: {self.name}")
                print(f"Species: {self.species}")
                print(f"Age: {self.age}")
                print(f"Height: {self.height:.3f} cm")
                print(f"Health: {'Healthy' if self.is_healthy else 'Unhealthy'}")
                print(f"Is safe for consumption: {'Yes' if self.check_consumption else 'No'}")
                print(f"Used for: {self.use_type}\n")
                print(f"Thank you for playing! ^ _ ^")


# class: child (5/6)
class Succulent(Plant):
        def __init__(self, name, species, soil_type, age, height, is_watered, has_photosynthesized, is_healthy, is_storing_water=False):
            super().__init__(name, species, soil_type, age, height, is_watered, has_photosynthesized, is_healthy)
            if self.age <= 3:
                self.growth_rate = 1
            elif self.age > 3 and self.age <= 12:
                self.growth_rate = 2
            else:
                self.growth_rate = 3
                self.is_storing_water = is_storing_water

        def water(self):
            if self.is_watered:
                print(f"{self.name} has already been water this month.")
            else:
                print(f"{self.name} has been watered and is storing water.")
                self.is_watered = True
                self.is_storing_water = True


        def grow(self):
            if self.has_photosynthesized and self.is_watered:
                if self.is_watered:
                    self.age+=1
                    self.height += self.growth_rate
                    self.is_watered = False
                    self.has_photosynthesized = False
                    print(f"Entering month {self.age}...")
                    time.sleep(4)
                    print(f"{self.name} has grown by {self.growth_rate}cm using fresh water. ")
                    print(f"New height is {self.height:.3f} cm.")
                elif self.is_storing_water:
                    self.age +=1
                    self.height += self.growth_rate
                    self.is_storing_water = False
                    self.has_photosynthesized = False
                    print(f"Entering month {self.age}...")
                    time.sleep(4)
                    print(f"{self.name} has grown by {self.growth_rate} cm using stored water.")
                    print(f"New height is {self.height:.3f} cm.")
                else:
                    print(f"{self.name} needs water to grow.")
            else:
                print(f"{self.name} needs to photosynthesize to grow.")

        def check_water_storage(self):
            if self.is_storing_water == True:
                print(f"The {self.name} has water stored.")
            else:
                print(f"The {self.name} could use a drink.")

        def drought_protection(self):
            if self.is_storing_water == True:
                print(f"The {self.name} can survive the drought because it has water stored.")
            else:
                print(f"{self.name} won't survive the drought.")
                
        def exit(self):
            print("\nPlant Information:")
            print(f"Name: {self.name}")
            print(f"Species: {self.species}")
            print(f"Age: {self.age}")
            print(f"Height: {self.height:.3f} cm")
            print(f"Health: {'Healthy' if self.is_healthy else 'Unhealthy'}")
            print(f"Has stored water: {'Yes' if self.is_storing_water else 'No'}\n")
            print(f"Thank you for playing! ^ _ ^")


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
                print(f"The vine {self.name} is now growing horizontally")
            elif self.spread_direction_vertical and self.spread_direction_horizontal:
                print(f"The vine {self.name} is now growing horizontally and vertically")
            
        def climb(self):
            self.spread_direction_vertical = True
            if self.spread_direction_vertical and not self.spread_direction_horizontal:
                print(f"The vine {self.name} is now growing vertically")
            elif self.spread_direction_vertical and self.spread_direction_horizontal:
                print(f"The vine {self.name} is now growing vertically and horizontally")
            
        def check_vine_spread(self):
            if self.spread_direction == "Vertically" or self.spread_direction == "Horizontally":
                print(f"{self.name} is now spreading {self.spread_direction} at the rate {self.growth_rate} per day and is currently {self.thickness} in diameter.")
            else:
                print(f"{self.name} is now spreading at the rate {self.growth_rate} per day and is currently {self.thickness} in diameter.")

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
                print(f"Entering month {self.age}...")
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
                print(f"Please water the {self.name} first and let it photosynthesize...")
                
        def exit(self):
            print("\nPlant Information:")
            print(f"Name: {self.name}")
            print(f"Species: {self.species}")
            print(f"Age: {self.age}")
            print(f"Vertical height: {self.height_vertical:.3f} cm")
            print(f"Horizontal height: {self.height_horizontal:.3f} cm")
            print(f"Thickness: {self.thickness:.3f} cm")
            print(f"Health: {'Healthy' if self.is_healthy else 'Unhealthy'}\n")
            print(f"Thank you for playing! ^ _ ^")

# MENU
soil_types = ["sandy", "clay", "silty", "loamy", "peaty", "chalky"]
while(True):
    print("| Welcome to the Plant Simulator |\n")
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
        species = "Tree"
        plant = Tree(name, species, soil_type, height, age, is_watered, has_photosynthesized, is_healthy)
        while True:
            print(f"MONTH {age + 1}")
            print("Note: In order to bear fruit, must be at least 15 months old,")
            print("and it must have been watered and undergone photosynthesis.")
            print("\n| What do you want to do?")
            print("| 1. Water the plant         4. Check for fruits")
            print("| 2. Photosynthesize         5.  ")
            print("| 3. Go to the next month    6. Exit")

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
                plant.check_for_fruits()
                input("Press enter to continue...")
            elif choice1 == "5":
                plant.exit()
                break

    # Plant: Shrub
    elif choice == "2":
        name = input("Enter name of the plant: ").capitalize() + " Shrub"
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
        while(True):
            choice_thorns = input("Would you like the shrub to have thorns(y/n)? ").lower()
            if choice_thorns == 'y':
                has_thorns = True
                print(f"The {name} is going to contain thorns.")
                break
            elif choice_thorns == 'n':
                has_thorns = False
                print(f"The {name} is not going to contain thorns.")
                break
            else:
                print("Invalid choice, please select again")
                
        is_healthy = True
        is_watered = False
        has_photosynthesized = False
        species = "Shrub"
        plant = Shrub(name, species, soil_type, height, age, is_watered, has_photosynthesized, is_healthy, has thorns)
        while True:
            print(f"\nMONTH {plant.age}")
            print("| What do you want to do?")
            print("| 1. Water the plant   3. Go to the next month")
            print("| 2. Photosynthesize   4. Prune")
            print("| 5. Exit")

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
                plant.prune()
                input("Press enter to continue...")
            elif choice1 == "5":
                plant.exit()
                break

    # Plant: Flower
    elif choice == "3":
        petal_colors = ["Red", "Orange", 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet', 'White', 'Pink']
        name = input("Enter name of the plant: ").capitalize()
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
        species = "Flower"
        plant = Flower(name, species, petal_color, soil_type, height, age, is_watered, has_photosynthesized, is_healthy)
        while True:
            print(f"\nMONTH {plant.age}")
            print("| What do you want to do?")
            print("| 1. Water the plant   3. Go to the next month")
            print("| 2. Photosynthesize   4. Check scent")
            print("| 5. Attract pollinators 6. Exit")

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
                plant.check_fragrance()
                input("Press enter to continue...")
            elif choice1 == "5":
                plant.attracted_pollinators()
                input("Press enter to continue...")
            elif choice1 == "6":
                plant.exit()
                break
        
    # Plant: Herb
    elif choice == "4":
        name = input("Enter name of the plant: ").capitalize()
        age = 0
        height = 0
        is_healthy = True
        is_watered = False
        has_photosynthesized = False
        use_type = 0
        species = "Herb"
        
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
        plant = Herb(name, species, soil_type, age, height, is_watered, has_photosynthesized, is_healthy)
        
        # care for herb
        while True:
            print(f"MONTH {plant.age}")
            print("| What do you want to do?")
            print("| 1. Water the plant     5. Check use")
            print("| 2. Photosynthesize     4. Check consumption safety")
            print("| 3. Go to the next month  6. Harvest")
            print("| 7. Exit")
            
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
            elif choice_herb == "4":
                plant.check_consumption()
                input("Press enter to continue...")
            elif choice_herb == "5":
                plant.check_use()
                input("Press enter to continue...")
            elif choice_herb == "6":
                plant.harvest()
                input("Press enter to continue...")
            elif choice_herb == "7":
                plant.exit()
                break

    elif choice == "5":
        soil_types = ["sandy", "clay", "silty", "loamy", "peaty", "chalky"]
        name = input("Enter name of the plant: ").capitalize()
        species = "Succulent"
        height = 0
        age = 0
        is_watered = False
        has_photosynthesized = False
        is_healthy = True
        while(True):
            soil_type = input("Enter soil type: (Sandy, Clay, Silty, Loamy, Peaty, Chalky): ").lower()
            if soil_type in ["clay", "peaty", "silty"]:
                print("Trees are not compatible with that soil, please select again.")
            elif soil_type not in soil_types:
                print("Invalid choice, please select again")
            else:
                break

        plant = Succulent(name, species, soil_type, age, height, is_watered, has_photosynthesized, is_healthy)
        while True:
            print(f"\nMONTH {plant.age}")
            print("| What do you want to do?")
            print("| 1. Water the plant   3. Go to the next month")
            print("| 2. Photosynthesize   4. Check water storage")
            print("| 5. Check drought protection   6. Exit")
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
                plant.check_water_storage()
                input("Press enter to continue...")
            elif choice1 == "5":
                plant.drought_protection()
                input("Press enter to continue...")
            elif choice1 == "6":
                plant.exit()
                break

    elif choice == "6":
        name = input("Enter name of the plant: ").capitalize()
        species = "Vine"
        height = 0
        height_vertical = 0
        height_horizontal = 0
        thickness = 0
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
        is_watered = False
        has_photosynthesized = False
        plant = Vine(name, species, soil_type, age, height, is_watered, has_photosynthesized, is_healthy, height_vertical, height_horizontal, thickness)
        while(True):
            print(f"MONTH {plant.age}")
            print("| What do you want to do?")
            print("| 1. Water the plant          4. Climb")
            print("| 2. Photosynthesize          5. Crawl")
            print("| 3. Go to the next month     6. Exit")      

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
                plant.climb()
                input("Press enter to continue...")
            elif choice1 == "5":
                plant.crawl()
                input("Press enter to continue...")
            elif choice1 == "6":
                plant.exit()
                break

    elif choice == "7":
        print("Thank you for using the Plant Simulator!")
        break
    else:
        print("Invalid choice.")

    
