<h1 align="center">🌿 Plant Simulator 🍃</h1>
<p align="center"> Computer Science 121: Advanced Computer Programming | Abstract Base Class </p>

<p align="center">
    <img src="https://64.media.tumblr.com/5d2d839cd70bc3db2fa9acddb9cedd92/tumblr_nbpotrjgO11qi4ibzo1_500.gifv" alt="oogie boogie woogie~" width="500">
</p>

‎ 
# **🔖 Project Overview**
Our team was assigned the abstract base class **`Plant`** as part of our exploration of inheritance and abstraction in Python.

‎ 
# **👥 Team:**

👨‍💻 [Abrigo, John Nathaniel](https://github.com/Invxty)  
👨‍💻 [Angsioco, Edrian](https://github.com/edangsioco)  
👨‍💻 [Atienza, Dhanreigh](https://github.com/Dadanchiii)  
👩‍💻 [Calabia, Geanne Margaret](https://github.com/Ennage)

‎ 

<p align="center">
  <img src="https://64.media.tumblr.com/b24bb7086049debe86ccb94762a7d264/5784a6cb587e4fe8-ac/s1280x1920/18284d55366b80010515a2eaf76209a3f93eb845.gifv" alt="oogie boogie woogie~" width="1000">
</p>

<h1 align="center">The System</h1>

‎ 
## **📊 Class Diagram**
This diagram illustrates the relationship between the abstract base class `Plant` and its various subclasses. 
Each subclass represents a type of plant with its own unique attributes and behaviors.

![Class Diagram for our project](diagram.png)


‎ 
## 🧬 **Properties**

| **Type** |  **Class**  | **Properties**                                                 |
| :------: | :---------: | :------------------------------------------------------------- |
|  Parent  |   `Plant`   | `name`, `age`, `species`, `soil_type`, `growth_rate`, `height`, `is_healthy`, `is_watered`, `has_photosynthesized` |
|   Child  |    `Tree`   | `can_drop_leaves`, `has_fruit` |
|   Child  |   `Shrub`   | `can_shed_leaves`, `has_thorns` |
|   Child  |   `Flower`  | `petal_color`, `scent`, `has_nectar`, `is_blooming`, `pollinator` |
|   Child  |    `Herb`   | `herb_use`, `is_toxic` |
|   Child  | `Succulent` | `has_thorns`, `water_storage_type` |
|   Child  |    `Vine`   | `thickness`, `spread_direction_vertical`, `spread_direction_horizontal` |

‎ 
## ⚙️ **Methods**

Below are the functions defined per class. 
These methods reflect typical behaviors or actions of each plant type.

### **🌾 `Plant` (Abstract Base Class)**
* __init__()
* water()
* photosynthesize()
* grow()
* exit()

### **🌲 `Tree`**
* check_for_fruits()
* drop_leaves()

### **🌳 `Shrub`**
* prune()
* shed_leaves()

### **🌷 `Flower`**
* check_blooming()
* check_fragrance()
* attracted_pollinators()

### **🌿 `Herb`**
* check_consumption()
* check_use
* harvest()

### **🌱 `Succulent`**
* check_water_storage()
* drought_protection()

### **🎋 `Vine`**
* crawl()
* climb()
* check_vine_spread()

‎ 
<p align="center">
  <img src="https://64.media.tumblr.com/b24bb7086049debe86ccb94762a7d264/5784a6cb587e4fe8-ac/s1280x1920/18284d55366b80010515a2eaf76209a3f93eb845.gifv" alt="oogie boogie woogie~" width="1000">
</p>
‎ 
<h1 align="center"> Running the Program </h1>

<p align="justify"> ‎‎ ‎ ‎ ‎ To run the program, ensure your Python environment is set up, then execute the main script. Each plant type can be instantiated and interacted with using the provided methods. </p>


‎ 
<h1 align="center"> Acknowledgment </h1>

‎ ‎ ‎ ‎ We would like to thank our instructor, [Ms. Fatima Marie](https://github.com/marieemoiselle), for the collaborative learning environment that helped make this project possible. For the GIFs in this markdown we credit [@fulifuli on Tumblr](https://fulifuli.tumblr.com/) (dancing plants) and [@animatedglittergraphics-n-more on Tumblr](https://animatedglittergraphics-n-more.tumblr.com/) (plant divider).

‎ 
<p align="center">
  <img src="https://64.media.tumblr.com/b24bb7086049debe86ccb94762a7d264/5784a6cb587e4fe8-ac/s1280x1920/18284d55366b80010515a2eaf76209a3f93eb845.gifv" alt="oogie boogie woogie~" width="1000">
</p>

#  Code Sample

To display output in the console, use:

```python
print("hello world")
```

Sample method (abstract format):

```python
def watering(self):
    pass

def photosynthesize(self):
    pass

def grow(self):
    pass

def lifespan(self):
    pass
```

