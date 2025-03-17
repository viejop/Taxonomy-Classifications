class Kingdom:
    def __init__(self, kingdom):
        super().__init__()
        self.kingdom = kingdom
        self.kingdominfo = self.kingdomDescription()
        
    def kingdomDescription(self):
        if self.kingdom == "Animalia":
            return "The Animalia kingdom includes multicellular, eukaryotic organisms that eat other organisms, can move, and usually reproduce sexually."
        else:
            return "Unknown kingdom"

class Phylum(Kingdom):
    def __init__(self, phylum, kingdom):
        super().__init__(kingdom)
        self.phylum = phylum
        self.phyluminfo = self.phylumDescription()
        
    def phylumDescription(self):
        if self.phylum == "Chordata":
            return "The Chordata phylum consists of animals that have, at some stage of their life, a notochord, a dorsal nerve cord, pharyngeal slits, and a post-anal tail."
        else:
            return "Unknown phylum"
        
class Class(Phylum):
    def __init__(self, class_, phylum, kingdom):
        super().__init__(phylum, kingdom)
        self.class_ = class_
        self.classinfo = self.classDescription()
        
    def classDescription(self):
        if self.class_ == "Mammalia":
            return "The Mammalia class includes warm-blooded animals that have hair or fur, give live birth (except for monotremes), and nurse their young with milk."
        else:
            return "Unknown class"
        
class Order(Class):
    def __init__(self, order, class_, phylum, kingdom):
        super().__init__(class_, phylum, kingdom)
        self.order = order
        self.orderinfo = self.orderDescription()
        
    def orderDescription(self):
        if self.order == "Carnivora":
            return "The Carnivora order includes animals that primarily eat meat, have sharp teeth and claws for hunting, and include species like cats, dogs, and bears."
        else:
            return "Unknown order"

class Family(Order):
    def __init__(self, family, order, class_, phylum, kingdom):
        super().__init__(order, class_, phylum, kingdom)
        self.family = family
        self.familyinfo = self.familyDescription()
        
    def familyDescription(self):
        if self.family == "Canidae":
            return "The Canidae family includes carnivorous or omnivorous mammals commonly referred to as the dog family. This family includes a variety of species such as domestic dogs (Canis lupus familiaris), wolves, foxes, jackals, and coyotes."
        else:
            return "Unknown family"

class Genus(Family):
    def __init__(self, genus, family, order, class_, phylum, kingdom):
        super().__init__(family, order, class_, phylum, kingdom)
        self.genus = genus
        self.genusinfo = self.genusDescription()
        
    def genusDescription(self):
        if self.genus == "Canis":
            return "The Canis genus has carnivorous mammals that includes species such as domestic dogs, wolves, coyotes, and jackals, characterized by their sharp teeth, keen sense of smell, and often social behavior."
        else:
            return "Unknown genus"

class Species(Genus):
    def __init__(self, species, genus, family, order, class_, phylum, kingdom):
        super().__init__(genus, family, order, class_, phylum, kingdom)
        self.species = species
        self.speciesinfo = self.speciesDescription()
        
    def speciesDescription(self):
        if self.species == "Canis lupus familiaris":
            return "The Canis lupus familiaris species refers to the domesticated dog, a subspecies of the gray wolf, characterized by its wide variety of breeds, behaviors, and roles in human society."
        else:
            return "Unknown species"

def beagle():
    print("ENTRY 001 - BEAGLE\n")
    
    Beagle = Species("Canis lupus familiaris", "Canis", "Canidae", "Carnivora", "Mammalia", "Chordata", "Animalia")
    
    print("\nTAXONOMY:")
    print(f"Kingdom: {Beagle.kingdom} - {Beagle.kingdominfo} \n")
    print(f"Phylum: {Beagle.phylum} - {Beagle.phyluminfo} \n")
    print(f"Class: {Beagle.class_} - {Beagle.classinfo} \n")
    print(f"Order: {Beagle.order} - {Beagle.orderinfo} \n")
    print(f"Family: {Beagle.family} - {Beagle.familyinfo} \n")
    print(f"Genus: {Beagle.genus} - {Beagle.genusinfo} \n")
    print(f"Species: {Beagle.species} - {Beagle.speciesinfo} \n")
    
    print("\nIMAGE:")

def labradorRetriever():
    print("ENTRY 002 - LABRADOR RETRIEVER\n")
    
    LabradorRetriever = Species("Canis lupus familiaris horribilis", "Canis", "Canidae", "Carnivora", "Mammalia", "Chordata", "Animalia")
    
    print("\nTAXONOMY:")
    print(f"Kingdom: {LabradorRetriever.kingdom} - {LabradorRetriever.kingdominfo} \n")
    print(f"Phylum: {LabradorRetriever.phylum} - {LabradorRetriever.phyluminfo} \n")
    print(f"Class: {LabradorRetriever.class_} - {LabradorRetriever.classinfo} \n")
    print(f"Order: {LabradorRetriever.order} - {LabradorRetriever.orderinfo} \n")
    print(f"Family: {LabradorRetriever.family} - {LabradorRetriever.familyinfo} \n")
    print(f"Genus: {LabradorRetriever.genus} - {LabradorRetriever.genusinfo} \n")
    print(f"Species: {LabradorRetriever.species} - {LabradorRetriever.speciesinfo} \n")
    
    print("\nIMAGE:")
    
def germanShepherd():
    
    print("ENTRY 003 - GERMAN SHEPHERD\n")
  
    GermanShepherd = Species("Canis lupus familiaris", "Canis", "Canidae", "Carnivora", "Mammalia", "Chordata", "Animalia")
  
    print("\nTAXONOMY:")
    print(f"Kingdom: {GermanShepherd.kingdom} - {GermanShepherd.kingdominfo} \n")
    print(f"Phylum: {GermanShepherd.phylum} - {GermanShepherd.phyluminfo} \n")
    print(f"Class: {GermanShepherd.class_} - {GermanShepherd.classinfo} \n")
    print(f"Order: {GermanShepherd.order} - {GermanShepherd.orderinfo} \n")
    print(f"Family: {GermanShepherd.family} - {GermanShepherd.familyinfo} \n")
    print(f"Genus: {GermanShepherd.genus} - {GermanShepherd.genusinfo} \n")
    print(f"Species: {GermanShepherd.species} - {GermanShepherd.speciesinfo} \n")
  
  
def poodle():
    
    print("ENTRY 004 - POODLE")
    
    Poodle = Species("Canis lupus familiaris", "Canis", "Canidae", "Carnivora", "Mammalia", "Chordata", "Animalia")
    
    print("\nTAXONOMY:")
    print(f": {Poodle.kingdom} - {Poodle.kingdominfo} \n")
    print(f"Phylum: {Poodle.phylum} - {Poodle.phyluminfo} \n")
    print(f"Class: {Poodle.class_} - {Poodle.classinfo} \n")
    print(f"Order: {Poodle.order} - {Poodle.orderinfo} \n")
    print(f"Family: {Poodle.family} - {Poodle.familyinfo} \n")
    print(f"Genus: {Poodle.genus} - {Poodle.genusinfo} \n")
    print(f"Species: {Poodle.species} - {Poodle.speciesinfo} \n")
    
    
def dachshund():
    
    print("ENTRY 005 - DACHSHUND")
    
    Dachshund = Species("Canis lupus familiaris", "Canis", "Canidae", "Carnivora", "Mammalia", "Chordata", "Animalia")
    
    print("\nTAXONOMY:")
    print(f": {Dachshund.kingdom} - {Dachshund.kingdominfo} \n")
    print(f"Phylum: {Dachshund.phylum} - {Dachshund.phyluminfo} \n")
    print(f"Class: {Dachshund.class_} - {Dachshund.classinfo} \n")
    print(f"Order: {Dachshund.order} - {Dachshund.orderinfo} \n")
    print(f"Family: {Dachshund.family} - {Dachshund.familyinfo} \n")
    print(f"Genus: {Dachshund.genus} - {Dachshund.genusinfo} \n")
    print(f"Species: {Dachshund.species} - {Dachshund.speciesinfo} \n")
    
def chihuahua():
    print("ENTRY 006 - CHIHUAHUA")
    
    Chihuahua = Species("Canis lupus familiaris", "Canis", "Canidae", "Carnivora", "Mammalia", "Chordata", "Animalia")
    
    print("\nTAXONOMY:")
    print(f": {Chihuahua.kingdom} - {Chihuahua.kingdominfo} \n")
    print(f"Phylum: {Chihuahua.phylum} - {Chihuahua.phyluminfo} \n")
    print(f"Class: {Chihuahua.class_} - {Chihuahua.classinfo} \n")
    print(f"Order: {Chihuahua.order} - {Chihuahua.orderinfo} \n")
    print(f"Family: {Chihuahua.family} - {Chihuahua.familyinfo} \n")
    print(f"Genus: {Chihuahua.genus} - {Chihuahua.genusinfo} \n")
    print(f"Species: {Chihuahua.species} - {Chihuahua.speciesinfo} \n") 
    
def goldenRetriever():
    print("ENTRY 007 - GOLDEN RETRIEVER")
    
    GoldenRetriever = Species("Canis lupus familiaris", "Canis", "Canidae", "Carnivora", "Mammalia", "Chordata", "Animalia")
    
    print("\nTAXONOMY:")
    print(f": {GoldenRetriever.kingdom} - {GoldenRetriever.kingdominfo} \n")
    print(f"Phylum: {GoldenRetriever.phylum} - {GoldenRetriever.phyluminfo} \n")
    print(f"Class: {GoldenRetriever.class_} - {GoldenRetriever.classinfo} \n")
    print(f"Order: {GoldenRetriever.order} - {GoldenRetriever.orderinfo} \n")
    print(f"Family: {GoldenRetriever.family} - {GoldenRetriever.familyinfo} \n")
    print(f"Genus: {GoldenRetriever.genus} - {GoldenRetriever.genusinfo} \n")
    print(f"Species: {GoldenRetriever.species} - {GoldenRetriever.speciesinfo} \n")
    
def boxer():
    print("ENTRY 008 - BOXER")
    
    Boxer = Species("Canis lupus familiaris", "Canis", "Canidae", "Carnivora", "Mammalia", "Chordata", "Animalia")
    
    print("\nTAXONOMY:")
    print(f": {Boxer.kingdom} - {Boxer.kingdominfo} \n")
    print(f"Phylum: {Boxer.phylum} - {Boxer.phyluminfo} \n")
    print(f"Class: {Boxer.class_} - {Boxer.classinfo} \n")
    print(f"Order: {Boxer.order} - {Boxer.orderinfo} \n")
    print(f"Family: {Boxer.family} - {Boxer.familyinfo} \n")
    print(f"Genus: {Boxer.genus} - {Boxer.genusinfo} \n")
    print(f"Species: {Boxer.species} - {Boxer.speciesinfo} \n")
    
def rottweiler():
    print("ENTRY 009 - ROTTWEILER")
    
    Rottweiler = Species("Canis lupus familiaris", "Canis", "Canidae", "Carnivora", "Mammalia", "Chordata", "Animalia")
    
    print("\nTAXONOMY:")
    print(f": {Rottweiler.kingdom} - {Rottweiler.kingdominfo} \n")
    print(f"Phylum: {Rottweiler.phylum} - {Rottweiler.phyluminfo} \n")
    print(f"Class: {Rottweiler.class_} - {Rottweiler.classinfo} \n")
    print(f"Order: {Rottweiler.order} - {Rottweiler.orderinfo} \n")
    print(f"Family: {Rottweiler.family} - {Rottweiler.familyinfo} \n")
    print(f"Genus: {Rottweiler.genus} - {Rottweiler.genusinfo} \n")
    print(f"Species: {Rottweiler.species} - {Rottweiler.speciesinfo} \n")
    
def siberianHusky():
    print("ENTRY 010 - SIBERIAN HUSKY")
    
    SiberianHusky = Species("Canis lupus familiaris", "Canis", "Canidae", "Carnivora", "Mammalia", "Chordata", "Animalia")
    
    print("\nTAXONOMY:")
    print(f": {SiberianHusky.kingdom} - {SiberianHusky.kingdominfo} \n")
    print(f"Phylum: {SiberianHusky.phylum} - {SiberianHusky.phyluminfo} \n")
    print(f"Class: {SiberianHusky.class_} - {SiberianHusky.classinfo} \n")
    print(f"Order: {SiberianHusky.order} - {SiberianHusky.orderinfo} \n")
    print(f"Family: {SiberianHusky.family} - {SiberianHusky.familyinfo} \n")
    print(f"Genus: {SiberianHusky.genus} - {SiberianHusky.genusinfo} \n")
    print(f"Species: {SiberianHusky.species} - {SiberianHusky.speciesinfo} \n")

def shihTzu():
    print("ENTRY 011 - AMERICAN BROWN BEAR")
    
    ShihTzu = Species("Canis lupus familiaris", "Canis", "Canidae", "Carnivora", "Mammalia", "Chordata", "Animalia")
    
    print("\nTAXONOMY:")
    print(f": {ShihTzu.kingdom} - {ShihTzu.kingdominfo} \n")
    print(f"Phylum: {ShihTzu.phylum} - {ShihTzu.phyluminfo} \n")
    print(f"Class: {ShihTzu.class_} - {ShihTzu.classinfo} \n")
    print(f"Order: {ShihTzu.order} - {ShihTzu.orderinfo} \n")
    print(f"Family: {ShihTzu.family} - {ShihTzu.familyinfo} \n")
    print(f"Genus: {ShihTzu.genus} - {ShihTzu.genusinfo} \n")
    print(f"Species: {ShihTzu.species} - {ShihTzu.speciesinfo} \n")

def bulldog():
    print("ENTRY 012 - BULLDOG")
    
    Bulldog = Species("Canis lupus familiaris", "Canis", "Canidae", "Carnivora", "Mammalia", "Chordata", "Animalia")
    
    print("\nTAXONOMY:")
    print(f": {Bulldog.kingdom} - {Bulldog.kingdominfo} \n")
    print(f"Phylum: {Bulldog.phylum} - {Bulldog.phyluminfo} \n")
    print(f"Class: {Bulldog.class_} - {Bulldog.classinfo} \n")
    print(f"Order: {Bulldog.order} - {Bulldog.orderinfo} \n")
    print(f"Family: {Bulldog.family} - {Bulldog.familyinfo} \n")
    print(f"Genus: {Bulldog.genus} - {Bulldog.genusinfo} \n")
    print(f"Species: {Bulldog.species} - {Bulldog.speciesinfo} \n")
    
def titleScreen():
    print("············································································")
    print(":████████▄...▄██████▄.....▄██████▄..████████▄.....▄████████.▀████....▐████▀:")
    print(":███...▀███.███....███...███....███.███...▀███...███....███...███▌...████▀.:")
    print(":███....███.███....███...███....█▀..███....███...███....█▀.....███..▐███...:")
    print(":███....███.███....███..▄███........███....███..▄███▄▄▄........▀███▄███▀...:")
    print(":███....███.███....███.▀▀███.████▄..███....███.▀▀███▀▀▀........████▀██▄....:")
    print(":███....███.███....███...███....███.███....███...███....█▄....▐███..▀███...:")
    print(":███...▄███.███....███...███....███.███...▄███...███....███..▄███.....███▄.:")
    print(":████████▀...▀██████▀....████████▀..████████▀....██████████.████.......███▄:")
    print("············································································")

    while True:
        print("1. Beagle\n2. Labrador Retriever\n3. German Shepherd\n4. Poodle\n5. Dachshund\n6. Chihuahua\n7. Golden Retriever\n8. Boxer\n9. Rottweiler\n10. Siberian Husky\n11. Shih Tzu\n12. Bulldog\n13. How to use\n14. Quit")
        titleInput = input("")

        if titleInput.isdigit():
            titleInput = int(titleInput)
            if titleInput == 1:
                beagle()
                break
            elif titleInput == 2:
                labradorRetriever()
                break
            elif titleInput == 3:
                germanShepherd()
                break
            elif titleInput == 4:
                poodle()
                break
            elif titleInput == 5:
                dachshund()
                break
            elif titleInput == 6:
                chihuahua()
                break
            elif titleInput == 7:
                goldenRetriever()
                break
            elif titleInput == 8:
                boxer()
                break
            elif titleInput == 9:
                rottweiler()
                break
            elif titleInput == 10:
                siberianHusky()
                break
            elif titleInput == 11:
                shihTzu()
                break
            elif titleInput == 12:
                bulldog()
                break
            elif titleInput == 13:
                
                break
            elif titleInput == 14:
            
                break
            else:
                print("Input must be between 1 and 14.")
        elif not titleInput.isdigit():
            print("Invalid input")
            break
titleScreen()
