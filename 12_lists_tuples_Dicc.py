########
#LIST### are dynamic need more memory
########

## obj = [1,"False", 2]
## obj.append(3) => [1,"False", 2, 3]
## obj.pop(1) => [1, 2, 3]   To delete elements from a list
## for elemnt in obj:
##      print(element)
## obj[::-1] => [3, 2, 1]
## using slice obj[1:3]
## obj_2 = [5, 6] --> f = obj + obj_2 = [3,2,1,5,6]
## obj * 2 --> 2x the elements [3,2,1,3,2,1]


##########
#TUPLES### Static element cannot change (imutable) same as strings
#########  for with tuples are faster

#my_tuple = (1,2,3,4,5)


################ Data structure of keys(index) and values(values)
#Dictionaries### 
################ 

def run():
    my_dic = {
        "key1" : 1,
        "key2" : 2,
        "key3" : 3,
    }
    #print(my_dic) ##this print all the strcuture {'key1' : 1 .....}
    # print(my_dic["key1"]) #To just retrieve the contents
    # print(my_dic["key2"])
    # print(my_dic["key3"])
    population_countries = {
        'Argentina' : 44938712,
        'Brazil' : 210147125,
        'Colombia' : 507372424,

    }
    
    # print(population_countries["USA"])

    ##################
    #Using for loop##
    ##################

    # for country in population_countries.keys():   ##To print keys
    # for country in population_countries.values():     #To print values
    #     print(country)


    ####Displaying keys and values
    for country, population in population_countries.items(): #country(key), pupulation(value), items() returns key and value
        print(country + " has " + str(population) + " habitants.")


if __name__== "__main__":
    run()