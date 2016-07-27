class AdoptionCenter :
    def __init__(self, name, species_types, location):
        self.name = name
        self.species_types = species_types
        self.location = (float(location[0]),float(location[1]))

    def get_name(self):
        # Returns name of the adoption center
        return self.name[:]

    def get_location(self):
        # Returns location of the adoption center
        return self.location[:]

    def get_species_count(self):
        # Returns a copy of the full list and count of the available species at the adoption center.
        import copy
        return copy.deepcopy(self.species_types)

    def get_number_of_species(self,species_name):
        # Returns number of a given species that the adoption center has.
        try:
            return self.species_types[species_name]
        except:
            return 0

    def adopt_pet(self, species_name):
        if self.species_types[species_name] > 0:
            self.species_types[species_name] -= 1
        if self.species_types[species_name] ==0 :
            del self.species_types[species_name]



name = "ac"
species_types = {'Dog': 20, 'Cat': 5, 'Lizard': 65}
location = (1, 1)
ac = AdoptionCenter(name, species_types, location)
print ac.get_name()
print ac.get_location()
print ac.get_species_count()
ac.adopt_pet('Cat')
print ac.get_species_count()
ac.adopt_pet('Cat')
print ac.get_species_count()
ac.adopt_pet('Cat')
print ac.get_species_count()
ac.adopt_pet('Cat')
print ac.get_species_count()
print ac.get_number_of_species('Cat')
print "-------------------------------"

class Adopter(AdoptionCenter):
    def __init__(self, name, desired_species):
        """
        :param name: A string that represents the name of the adopter
        :param desired_species:  A string that represents the desired species to adopt
        """
        self.name = name
        self.desired_species = desired_species

    def get_name(self):
        """Returns the name of the adopter"""
        return self.name[:]

    def get_desired_species(self):
        """Returns the desired species of the adopter"""
        return self.desired_species[:]

    def get_score(self, adoption_center):
        """ Returns the score of adoption_center """
        return 1.0 * adoption_center.get_number_of_species(self.desired_species)


name = "ad"
desired_species = 'Dog'
adopter = Adopter(name, desired_species)
print adopter.get_name()
print adopter.get_desired_species()
print adopter.get_score(ac)
print "-------------------------------"

class FlexibleAdopter(Adopter):
    def __init__(self, name, desired_species, considered_species):
        """
        :param name: A string that represents the name of the adopter
        :param desired_species:  A string that represents the desired species to adopt
        """
        Adopter.__init__(self, name, desired_species)
        self.considered_species = considered_species

    def get_score(self, adoption_center):
        """ Returns the score of adoption_center """
        tot = sum ([adoption_center.get_number_of_species(self.considered_species[i])
                    for i in xrange(len(self.considered_species))])
        return Adopter.get_score(self,adoption_center) + 0.3 * tot



name = "ad_flex"
desired_species = 'Dog'
considered_species= ['Cat', 'Lizard']
adopter_flex = FlexibleAdopter(name, desired_species,considered_species)
print adopter_flex.get_name()
print adopter_flex.get_desired_species()
print adopter_flex.get_score(ac)
print "-------------------------------"



class FearfulAdopter(Adopter):
    def __init__(self, name, desired_species, feared_species):
        """
        :param name: A string that represents the name of the adopter
        :param feared_species:  A string that is the name of the feared species.
        """
        Adopter.__init__(self, name, desired_species)
        self.feared_species = feared_species

    def get_score(self, adoption_center):
        """ Returns the score of adoption_center """
        tot = adoption_center.get_number_of_species(self.feared_species)
        return max(0.0, Adopter.get_score(self,adoption_center)  - 0.3 * tot)

name = "ad_fear"
desired_species = 'Dog'
feared_species= 'Lizard'
adopter_fear = FearfulAdopter(name, desired_species,feared_species)
print adopter_fear.get_name()
print adopter_fear.get_desired_species()
print adopter_fear.get_score(ac)
print "-------------------------------"

class AllergicAdopter(Adopter):
    def __init__(self, name, desired_species, allergic_species):
        """
        :param name: A string that represents the name of the adopter
        :param allergic_species:  A list of strings of one or more species that the adopter is allergic to.
        """
        Adopter.__init__(self, name, desired_species)
        self.allergic_species = allergic_species

    def get_score(self, adoption_center):
        """ Returns the score of adoption_center """
        for animal in adoption_center.get_species_count().keys():
            if animal in self.allergic_species:
                return 0.0
        return Adopter.get_score(self,adoption_center)

name = "ad_Allergic"
desired_species = 'Dog'
allergic_species = ['Dino', 'Cat']
adopter_Allergic = AllergicAdopter(name, desired_species, allergic_species)
print adopter_Allergic.get_name()
print adopter_Allergic.get_desired_species()
print adopter_Allergic.get_score(ac)
print "-------------------------------"


class MedicatedAllergicAdopter(AllergicAdopter):
    def __init__(self, name, desired_species, allergic_species, medicine_effectiveness):
        """
        :param name: A string that represents the name of the adopter
        :param allergic_species:  A list of strings of one or more species that the adopter is allergic to.
        :param medicine_effectiveness: A dictionary of {string: float} of the medicines effectiveness to certain species.
        """
        AllergicAdopter.__init__(self, name, desired_species, allergic_species)
        self.medicine_effectiveness = medicine_effectiveness

    def get_score(self, adoption_center):
        """ Returns the score of adoption_center """
        min_w = 1.0
        for animal in adoption_center.get_species_count().keys():
            if animal in self.allergic_species:
                min_w = min(min_w, self.medicine_effectiveness[animal])
        return min_w*Adopter.get_score(self,adoption_center)

name = "ad_MAllergic"
desired_species = 'Dog'
m_allergic_species = ['Dino', 'Cat']
medicine_effectiveness = {"Dog": 1.0, "Cat": 0.8, "Horse": 0.4}
adopter_m_Allergic = MedicatedAllergicAdopter(name, desired_species, allergic_species, medicine_effectiveness)
print adopter_m_Allergic.get_name()
print adopter_m_Allergic.get_desired_species()
print adopter_m_Allergic.get_score(ac)
print "-------------------------------"


class SluggishAdopter(Adopter):
    def __init__(self, name, desired_species, location):
        Adopter.__init__(self, name, desired_species)
        self.location = (float(location[0]),float(location[1]))

    def get_linear_distance(self, to_location):
        from math import sqrt
        return sqrt(     (self.location[0]-to_location[0])**2 + (self.location[1]-to_location[1])**2   )

    def get_score(self, adoption_center):
        """ Returns the score of adoption_center """
        import random
        distance = self.get_linear_distance(adoption_center.get_location())
        if distance < 1:
            return Adopter.get_score(self, adoption_center)
        elif distance < 3:
            return random.uniform(0.7,0.9) * Adopter.get_score(self, adoption_center)
        elif distance < 5:
            return random.uniform(0.5,0.7) * Adopter.get_score(self, adoption_center)
        else:
            return random.uniform(0.1,0.5) * Adopter.get_score(self, adoption_center)


name = "ad_slug"
desired_species = 'Dog'
location = (1,4)
adopter_slug =  SluggishAdopter(name, desired_species, location)
print adopter_slug.get_name()
print adopter_slug.get_desired_species()
print adopter_slug.get_score(ac)
print "-------------------------------"


def get_ordered_adoption_center_list(adopter, list_of_adoption_centers) :
    """
    :param adopter:  A single Adopter or Adopter Subclass instance
    :param list_of_adoption_centers: A list of AdoptionCenter instances.
    :return: A list of an organized adoption_center such that the scores
    for each AdoptionCenter to the Adopter will be ordered from highest score to lowest score.
    """
    ranking = [(ac, adopter.get_score(ac)) for ac in list_of_adoption_centers]
    # Sort by score first, in case of duplicates - sort by center's name
    ranking = sorted(ranking, key=lambda x: x[0].get_name())      #sort by name
    ranking = sorted(ranking, key=lambda x: x[1], reverse=True)   #sort by score
    return [ac[0] for ac in ranking]

def get_adopters_for_advertisement(adoption_center, list_of_adopters, n):
    """

    :param adoption_center: A single AdoptionCenter instance
    :param list_of_adopters: A list of Adopter (or a subclass of Adopter) instances.
    :param n: The number of adopters, up to a maximum of n, who will be sent advertisements.
    :return: a list of length up to n that represents the highest scoring Adopters/Adopter Subclasses
    for the specific AdoptionCenter (You want to find the top n best Adopter matches).
    """
    ranking = [(ad, ad.get_score(adoption_center)) for ad in list_of_adopters]
    # Sort by score first, in case of duplicates - sort by adopters's name
    ranking = sorted(ranking, key=lambda x: x[0].get_name())      # sort by name
    ranking = sorted(ranking, key=lambda x: x[1], reverse=True)   #sort by score
    return [x[0] for x in ranking[0:n]]




adopter = MedicatedAllergicAdopter("One", "Cat", ['Dog', 'Horse'], {"Dog": .5, "Horse": 0.2})
adopter2 = Adopter("Two", "Cat")
adopter3 = FlexibleAdopter("Three", "Horse", ["Lizard", "Cat"])
adopter4 = FearfulAdopter("Four","Cat","Dog")
adopter5 = SluggishAdopter("Five","Cat", (1,2))
adopter6 = AllergicAdopter("Six", "Cat", "Dog")

ac = AdoptionCenter("Place1", {"Mouse": 12, "Dog": 2}, (1,1))
ac2 = AdoptionCenter("Place2", {"Cat": 12, "Lizard": 2}, (3,5))
ac3 = AdoptionCenter("Place3", {"Horse": 25, "Dog": 9}, (-2,10))

# how to test get_adopters_for_advertisement
print get_adopters_for_advertisement(ac2, [adopter, adopter2, adopter3, adopter4, adopter5, adopter6], 10)
print "----------------------------"
# you can print the name and score of each item in the list returned




adopter4 = FearfulAdopter("Four","Cat","Dog")
adopter5 = SluggishAdopter("Five","Cat", (1,2))
adopter6 = AllergicAdopter("Six", "Lizard", "Cat")

ac  = AdoptionCenter("Place1", {"Cat": 12, "Dog": 2}, (1,1))
ac2 = AdoptionCenter("Place2", {"Cat": 12, "Lizard": 2}, (3,5))
ac3 = AdoptionCenter("Place3", {"Cat": 40, "Dog": 4}, (-2,10))
ac4 = AdoptionCenter("Place4", {"Cat": 33, "Horse": 5}, (-3,0))
ac5 = AdoptionCenter("Place5", {"Cat": 45, "Lizard": 2}, (8,-2))
ac6 = AdoptionCenter("Place6", {"Cat": 23, "Dog": 7, "Horse": 5}, (-10,10))

# how to test get_ordered_adoption_center_list
print get_ordered_adoption_center_list(adopter4, [ac,ac2,ac3,ac4,ac5,ac6])
# you can print the name and score of each item in the list returned



'''
Wrong sol

def get_ordered_adoption_center_list(adopter, list_of_adoption_centers) :
    """
    :param adopter:  A single Adopter or Adopter Subclass instance
    :param list_of_adoption_centers: A list of AdoptionCenter instances.
    :return: A list of an organized adoption_center such that the scores
    for each AdoptionCenter to the Adopter will be ordered from highest score to lowest score.
    """
    scores = {}
    for ac in list_of_adoption_centers:
        scores[ac.get_name()] = adopter.get_score(ac)
    list_value = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    list_keys = [k for k, v in list_value]
    return list_keys

def get_adopters_for_advertisement(adoption_center, list_of_adopters, n):
    """

    :param adoption_center: A single AdoptionCenter instance
    :param list_of_adopters: A list of Adopter (or a subclass of Adopter) instances.
    :param n: The number of adopters, up to a maximum of n, who will be sent advertisements.
    :return: a list of length up to n that represents the highest scoring Adopters/Adopter Subclasses
    for the specific AdoptionCenter (You want to find the top n best Adopter matches).
    """
    from operator import itemgetter
    scores = {}
    for adopters in list_of_adopters:
        scores[adopters.get_name()] = adopters.get_score(adoption_center)
    list_value = sorted(scores.items(), key=itemgetter(1), reverse=True)
    list_keys = [k for k, v in list_value]
    #print list_value
    return  list_keys[:n]

'''