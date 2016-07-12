 # Paste your code into this box
# string = raw_input("Please enter sting: ");
string = 'azcbobobegghakl'
vowels = "aeiou"
print(sum([1 for letter in string.lower() if letter in vowels]))

print(sum([1 for i in range(len(string.lower())) if string[i:i+3]=='bob']))



from collections import Counter
def item_order_test(order):
    return Counter(order.split());

def item_order(order):
   list = {}
   for element in order.split() :
      if element in list :
         list[element] += 1
      else:
         list[element] = 1
   return list;


# Paste your code into this box
def item_order(order):
   string =  'salad:'     + str(order.split().count("salad"))     + " "
   string += 'hamburger:' + str(order.split().count("hamburger")) + " "
   string += 'water:'     + str(order.split().count("water"))
   return string;
# print item_order( "salad water hamburger salad hamburger" )

