class Movie:

    def __init__(self,Movie_name,Artist_name,Year,Rating):
        self.Movie_name=Movie_name
        self.Artist_name=Artist_name
        self.Year=Year
        self.Rating=Rating

    def DisplayDetails(self):
        print("----------MOVIE DETAILS--------------")
        print("")
        print("Name : ",self.Movie_name)
        print("Artist : ",self.Artist_name)
        print("Year of Release : ",self.Year)
        print("Rating : ",self.Rating)
        print("")
        print("-------------------------------------")

    def menu(self):
        print("1.Change Movie Name ")
        print("2.Change Release Date ")
        print("3.Change Artist Name ")
        print("4.Change Rating")
        print()

    def UpdateDetails(self):
        self.menu()
        choice=int(input("Enter your choice : "))

        if choice==1:
            name=input("Enter Movie Name : ")
            self.Movie_name=name
            self.menu()

        if choice==2:
            name=input("Enter Release Date : ")
            self.Year=name
            self.menu()

        if choice==3:
            name=input("Enter Artist Name : ")
            self.Artist_name=name
            self.menu()

        if choice==4:
            name=input("Enter Rating : ")
            self.Rating=name
            self.menu()

        if choice!=1 and choice!=2 and choice!=3 and choice!=4:
            print("Invalid Choice.")


movie=Movie("Rampage","Tony Stark","2018","*****")
movie.DisplayDetails()
