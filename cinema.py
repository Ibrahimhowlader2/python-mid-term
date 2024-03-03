class Star_Cinema:
    hall_list = []

    def entry_hall(self, hall):
        self.hall_list.append(hall)


class Hall:
    def __init__(self, rows, cols, hall_no):
        self._seats = {}
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        self.entry_show(id="default", movie_name="Default Movie", time="00:00 AM")

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self._show_list.append(show_info)
        self._seats[id] = [[0] * self._cols for _ in range(self._rows)]

    def book_tickets(self, id, num_tickets):
        for _ in range(num_tickets):
            row = int(input(f"Enter the row for ticket {_ + 1}: "))
            col = int(input(f"Enter the column for ticket {_ + 1}: "))
            self.book_seat(id, row, col)
        self.show_options()

    def book_seat(self, id, row, col):
        if 1 <= row <= self._rows and 1 <= col <= self._cols:
            if self._seats[id][row - 1][col - 1] == 0:
                self._seats[id][row - 1][col - 1] = 1
                print(f"\n\t---> Seat ({row}, {col}) booked successfully!")
            else:
                print(f"\n\t---> !!! Seat ({row}, {col}) is already booked")
        else:
            print(f"\n\t---> !!! Invalid seat ({row}, {col})")

    def view_show_list(self):
        print("\n\tShows Today:")
        for show in self._show_list:
            print(f"\tID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")

    # def view_available_seats(self, id):
    #     if id in self._seats:
    #         print(f"\n\tAvailable Seats for Show ID {id}:")
    #         for i in range(self._rows):
    #             for j in range(self._cols):
    #                 if self._seats[id][i][j] == 0:
    #                     print(f"\t({i + 1}, {j + 1})")
    #     else:
    #         print(f"\n\t---> !!! Invalid show ID: {id}")

    def view_available_seats(self, show_id):
        if show_id in self._seats:
            print(f"\n\tSeats Matrix for Show ID {show_id}:\n")
            print("\t    " + " ".join(f"{i + 1}" for i in range(self._cols)))
            for i in range(self._rows):
                print(f"\t{i + 1}   " + " ".join("X" if seat == 1 else "O" for seat in self._seats[show_id][i]))
        else:
            print(f"\n\t---> !!! Invalid show ID: {show_id}")

    def show_options(self):
        print("\nOptions:")
        print("1: View All Shows Today")
        print("2: View Available Seats")
        print("3: Book Tickets")
        print("4: Exit (Stop the program)")


class Counter:
    def __init__(self, cinema):
        self._cinema = cinema

    def run_counter(self):
        while True:
            print("Counter Options:")
            print("1: View All Shows Today")
            print("2: View Available Seats")
            print("3: Book Tickets")
            print("4: Exit (Stop the program)")

            ch = int(input("\nEnter Option:"))

            if ch == 1:
                for hall in self._cinema.hall_list:
                    hall.view_show_list()

            elif ch == 2:
                show_id = input("Enter the ID of the show: ")
                for hall in self._cinema.hall_list:
                    hall.view_available_seats(show_id)

            elif ch == 3:
                show_id = input("Enter the ID of the show: ")
                num_tickets = int(input("Enter the number of tickets to book: "))
                for hall in self._cinema.hall_list:
                    hall.book_tickets(show_id, num_tickets)

            elif ch == 4:
                break

            else:
                print("\n\t---> !!! Choose a valid option\n")


if __name__ == "__main__":
    cinema = Star_Cinema()
    hall1 = Hall(rows=3, cols=4, hall_no=1)
    hall2 = Hall(rows=2, cols=3, hall_no=2)

    hall1.entry_show(id="A1", movie_name="Movie 1", time="12:00 PM")
    hall1.entry_show(id="A2", movie_name="Movie 2", time="3:00 PM")

    hall2.entry_show(id="B1", movie_name="Movie 3", time="5:00 PM")
    hall2.entry_show(id="B2", movie_name="Movie 4", time="8:00 PM")

    cinema.entry_hall(hall1)
    cinema.entry_hall(hall2)

    counter = Counter(cinema)
    counter.run_counter()
