# Define class MyFirstClass

class MyFirstClass():
    print('Who wrote this')
    index= "Author-Book"

    def hand_list(self, philosopher, book):
        print(MyFirstClass.index)
        print(philosopher + "Wrote the book: " + book)
        

# Call function handlist()

whodunnit = MyFirstClass()
whodunnit.hand_list("Plato ","Republic")