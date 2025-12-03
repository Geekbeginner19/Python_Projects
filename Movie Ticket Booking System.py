# 🔥 Daily OOP Python Project: Movie Ticket Booking System 🎬

# Concept

# Build a simple system where users can book movie tickets, check available seats, and cancel bookings.
# Everything is stored using classes and objects.

# Classes & Responsibilities

# Movie
# Attributes: title, total_seats, booked_seats (default 0)

# Methods:
# display_info() → Show movie title and available seats
# book_seats(n) → Book n seats if available
# cancel_seats(n) → Cancel n booked seats

# TicketManager
# Attributes: list of movies

# Methods:
# add_movie(movie) → Add new movie to list
# view_movies() → Display all movies
# book_ticket(title, n) → Find movie by title and book seats
# cancel_ticket(title, n) → Find movie by title and cancel seats

class Movie:
    def __init__(self, title:str, total_seats = 100, booked_seats = 0):
        self.title = title
        self.total_seats = total_seats
        self.booked_seats = booked_seats
    
    def display_info(self):
        print(f"Movie Title: {self.title} | Available seats: {self.total_seats - self.booked_seats} | Booked Seats: {self.booked_seats}")

    def book_seats(self, seats:int):
        self.seats = seats
        if seats > (self.total_seats - self.booked_seats):
            print("Cannot book more than available seats")
        else:
            self.booked_seats += seats
            print("Seats booked successfully!")
    
    def cancel_seats(self, seats:int):
        if self.booked_seats == 0:
            print("No booked seats to cancel")
        elif seats > (self.total_seats - self.booked_seats):
            print("Cannot cancel more than available seats")
        elif seats > self.booked_seats:
            print("Cannot cancel more than booked seats")
        else:
            self.booked_seats -= seats
            print("Seats cancelled successfully!")


class TicketManager:
    def __init__(self):
        self.movies = []#List to store movie objects 

    def add_movie(self, movie):
        self.movies.append(movie)#Remember that the 'movie' here is an object of the Movie class
    
    def view_movies(self):
        if len(self.movies) == 0:
            print("Sorry, no movies to display")
        else:                
            for mov in self.movies:
                mov.display_info()#Accessing the methods of the Movie class through it objects

    def book_ticket(self, title = str, seats = int):
        for mov in self.movies:
            if title.lower() == mov.title.lower():
                mov.book_seats(seats)
            else:
                continue

    def cancel_ticket(self, title = str, seats = int):
        for mov in self.movies:
            if title.lower() == mov.title.lower():
                mov.cancel_seats(seats)
            else:
                continue


def movie_add():
    movie = input("Enter movie title: ")
    return Movie(movie)

tikmanager = TicketManager() #Creating a TicketManager class in the main scope to handle inputs 

while True:
    print("\n=== Movie Ticket Booking System ===")
    print("1. Add Movie")
    print("2. View Movies")
    print("3. Book Tickets")
    print("4. Cancel Tickets")
    print("5. Quit\n")
    option = input("Select option >> ")

    try :
        option = int(option)
        if option < 1 or option > 5:
            print("Enter a valid option")
        else:
            if option == 1:
                addmov = movie_add()
                tikmanager.add_movie(addmov)
            elif option == 2:
                tikmanager.view_movies()
            elif option == 3:
                title = input("Enter movie title: ")
                seats = int(input("Enter number of seats: "))
                tikmanager.book_ticket(title, seats)
            elif option == 4:
                title = input("Enter movie title: ")
                seats = int(input("Enter number of seats: "))
                tikmanager.cancel_ticket(title, seats)
            elif option == 5:
                print("Goodbye!")
                break
    except ValueError as V:
        print(f"Invalid option {V}")
    

            
