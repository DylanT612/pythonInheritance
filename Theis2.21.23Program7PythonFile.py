
# Description: Grandchild Inheritance

import random


# Creating the Grandchild or the "parent" class
class Grandchild:
    # Initialize objects attributes
    def __init__(self, name, age, favorite_color):
        self.name = name
        self.age = age
        self.favorite_color = favorite_color
        global total_objects_created
        total_objects_created += 1

    # setting the name
    def setname(self):
        return self.name

    # setting the age
    def setage(self):
        return [self.age]

    # setting favorite_color
    def setfavorite_color(self):
        return {self.favorite_color}

    # returns class attributes
    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}, ' \
               f'Favorite Color: {self.favorite_color}'

    # Compares age attributes between compared grandchildren
    def isOlder(self, otherGrandchild):
        if otherGrandchild.setage() > [self.age]:
            print("The other grandchild is younger")
        elif otherGrandchild.setage() < [self.age]:
            print("The other grandchild is older")
        elif otherGrandchild.setage() == [self.age]:
            print("The grandchildren are the same age")
        else:
            print("Could not compute ages.")

    # getting the objects created
    def getCounter(self):
        return total_objects_created

    # setting the object counter
    def setCounter(self):
        return {total_objects_created}


# Global Variables
total_objects_created = 0
SportyCounter = 0
BookwormCounter = 0


# Making the sporty or "child" class
class Sporty(Grandchild):
    # Initializing the class
    def __init__(self, name, age, favorite_color, sport, season):
        super().__init__(name, age, favorite_color)
        self.sport = sport
        self.season = season
        global SportyCounter
        SportyCounter += 1

    # returning attribute values
    def __str__(self):
        return (f'Name: {self.name}, Age: {self.age}, Favorite Color: '
                f'{self.favorite_color}, Sport: {self.sport}, '
                f'Season: {self.season}')

    # setting the object counter
    def setCounter(self):
        return SportyCounter

    # getting the object counter
    def getCounter(self):
        return SportyCounter

    # setting sport
    def setsport(self):
        return self.sport

    # getting sport
    def getsport(self):
        return self.sport

    # setting season
    def setseason(self):
        return self.season

    # getting season
    def getseason(self):
        return self.season


# Making the bookworm which is another "child" class
class Bookworm(Grandchild):
    # Initializing class
    def __init__(self, name, age, favorite_color, favAuthor, numBooksRead):
        super().__init__(name, age, favorite_color)
        self.favAuthor = favAuthor
        self.numBooksRead = numBooksRead
        global BookwormCounter
        BookwormCounter += 1

    # returning attribute values
    def __str__(self):
        return (f'Name: {self.name}, Age: {self.age}, Favorite Color: '
                f'{self.favorite_color}, Favorite Author: {self.favAuthor}, '
                f'Number of Books Read: {self.numBooksRead}')

    # setting the counter
    def setCounter(self):
        return BookwormCounter

    # getting the counter
    def getCounter(self):
        return BookwormCounter

    # setting favAuthor
    def setfavAuthor(self):
        return self.favAuthor

    # getting favAuthor
    def getfavAuthor(self):
        return self.favAuthor

    # setting numBooksRead
    def setnumBooksRead(self):
        return self.numBooksRead

    # Getting numBooksRead
    def getnumBooksRead(self):
        return self.numBooksRead


# main function
def main():
    # Creating 3 Sporty Grandchild objects
    Grandchild1 = Sporty("Kyle", '11', "Green", "Football", "Fall")
    Grandchild2 = Sporty('Molly', '14', 'Purple', "Hockey", "Winter")
    Grandchild3 = Sporty('Ted', '6', "Red", "Baseball", "Spring")

    # Creating 3 Bookworm Grandchild objects
    Grandchild4 = Bookworm("Brittany", "13", "Blue", "Hemingway", "11")
    Grandchild5 = Bookworm("Hailey", "14", "Pink", "Austen", "7")
    Grandchild6 = Bookworm('Mary', '15', "Blue", "R.L. Stine", "15")

    # Calling the getCounter method
    total = Grandchild3.getCounter() + Grandchild6.getCounter()
    print("The getCounter() of Sporty and Bookworm: ", total, "\n")

    # Attributes of each object
    Original_6_Grandchildren_list = [Grandchild1, Grandchild2, Grandchild3,
                                     Grandchild4, Grandchild5, Grandchild6]
    for ele in Original_6_Grandchildren_list:
        print(f'Characteristics of each grandchild: {ele.__str__()}')
    print()

    # Changing data attributes of a Sporty Grandchild
    Grandchild1 = Sporty("Thomas", "15", "Red", "Lacrosse", "Spring")
    # Or you can do
    Grandchild1.name = "Josh"
    Grandchild1.age = "17"
    Grandchild1.favorite_color = "Orange"
    Grandchild1.sport = "Motocross"
    Grandchild1.season = "Summer"
    print(f'The attributes of the changed grandchild: '
          f'{Grandchild1.__str__()}', "\n")

    # Printing only the data attribute values
    print(Grandchild2.name, Grandchild2.age, Grandchild2.favorite_color,
          Grandchild2.sport, Grandchild2.season)
    print()

    # Creating a loop for the 10 new grandchildren
    # sporty_grandkids = []
    # for kid in range(5):
    #     kid = Sporty(input("Name: "), input("Age: "), input("Color: "),
    #                  input("Sport: "), input("Season: "))
    #     sporty_grandkids.append(kid)
    # bookworm_grandkids = []
    # for kid in range(5):
    #     kid = Bookworm(input("Name: "), input("Age: "), input("Color: "),
    #                    input("Favorite Author: "),
    #                    input("Number of Books Read: "))
    #     bookworm_grandkids.append(kid)

    # Creating 10 more grandchildren to show it works
    Grandchild7 = Sporty("Bob", '16', "Green", "Darts", "Summer")
    Grandchild8 = Sporty("Lee", "13", "Orange", "Tennis", "Summer")
    Grandchild9 = Sporty("Aidan", "11", "Yellow", "Soccer", "Spring")
    Grandchild10 = Sporty("Dylan", "18", "Red", "Soccer", "Fall")
    Grandchild11 = Sporty("Rachel", "17", "Blue", "Bowling", "Summer")
    Grandchild12 = Bookworm("Tyler", "15", "Red", "Rowling", "1")
    Grandchild13 = Bookworm("Amanda", "16", "Pink", "Hemingway", "4")
    Grandchild14 = Bookworm("Amy", "13", "Blue", "Dickens", "14")
    Grandchild15 = Bookworm("Sarah", "12", "Blue", "Jones", "6")
    Grandchild16 = Bookworm("Ali", "6", "Green", "Seuss", "2")
    _10_grandchildren_list = [Grandchild7, Grandchild8, Grandchild9,
                              Grandchild10, Grandchild11, Grandchild12,
                              Grandchild13, Grandchild14, Grandchild15,
                              Grandchild16]

    # If we want the updated grandchild to show we can do
    Original_6_Grandchildren_list[0] = Grandchild1
    all_my_grandkids = Original_6_Grandchildren_list + _10_grandchildren_list

    # Printing all the grandchildren
    kid_rank = 1
    for i in all_my_grandkids:
        print(kid_rank, i.__str__())
        kid_rank += 1


if __name__ == "__main__":
    main()
