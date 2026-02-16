class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_details(self):
        print(f"Title : {self.title}")
        print(f"Author: {self.author}")


# Creating 3 different book objects
book1 = Book("The Alchemist", "Paulo Coelho")
book2 = Book("1984", "George Orwell")
book3 = Book("Harry Potter", "J.K. Rowling")

# Printing details

book1.display_details()
book2.display_details()
book3.display_details()


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width


        self.area = length * width
        self.perimeter = 2 * (length + width)


rect = Rectangle(10, 5)


print(f"Length   : {rect.length}")
print(f"Width    : {rect.width}")

print(f"Area     : {rect.area}")
print(f"Perimeter: {rect.perimeter}")