class Podcast:
    def __init__(self, podcast_id, name):
        self.id = podcast_id
        self.name = name

    def setID(self, podcast_id):
        self.id = podcast_id

    def getID(self):
        return self.id

    def getName(self):
        return self.name

    def ratePodcast(self, rating):
        print(f"Rating the podcast '{self.getName()}' with rating: {rating}")

# Example Usage:
podcast1 = Podcast("P001", "Tech Talks")
podcast2 = Podcast("P002", "Science Explained")


class Book:
    def __init__(self,title, author):
        self.title=title
        self.author=author

    def setTitle(self,title):
        self.title=title

    def getTitle(self):
        return self.title

    def setAuthor(self, author):
        self.author=author

# An instance of the class book
book1 = Book("To Kill a Mockingbird", "Harper Lee")

class Podcast:

    def __init__(self, id, name):
        self.podcast_id = id
        self.podcast_name = name

    def getpodcast_id(self):
        return self.podcast_id

    def getpodcast_name(self):
        return self.podcast_id

    def setpodcast_name(self, name):
        self.podcast_name = name

    def rate_the_podcast(self):
        return self.rate_the_podcast

class Item:
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setPrice(self, price):
        self.price = price

    def getPrice(self):
        return self.price
# instances of the class
sale_item1=Item("iphone",3599)
sale_item2=Item("samsung phone",2500)



class Auction:
    def __init__(self, description, highest_bid):
        self.description = description
        self.highest_bid = highest_bid

    def setDescription(self, description):
        self.description = description

    def getDescription(self):
        return self.description

    def setHighestBid(self, highest_bid):
        self.highest_bid = highest_bid

    def getHighestBid(self):
        return self.highest_bid

class Student:
    def __init__(self, gpa, name, student_id):
        self.gpa = gpa
        self.name = name
        self.id = student_id

    def setGPA(self, gpa):
        self.gpa = gpa

    def getGPA(self):
        return self.gpa

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setID(self, student_id):
        self.id = student_id

    def getID(self):
        return self.id

# Example Usage:
student1 = Student(3.8, "John Doe", "123456")






