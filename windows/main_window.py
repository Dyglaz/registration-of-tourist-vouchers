import customtkinter
import customtkinter as ctk
from .table_window import TableWindow
from .functions_window import FunctionsWindow
from PIL import Image


class MainWindow(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()
        self.geometry("1040x1050")
        self.resizable(False, False)
        self.title("Registration of tourist vouchers")
        customtkinter.set_appearance_mode("light")
        customtkinter.set_default_color_theme("green")
        self.scrollable_frame = ctk.CTkScrollableFrame(self, orientation="vertical", width=1017, fg_color="white",
                                                       label_text="Результаты запросов", label_fg_color="white")
        self.scrollable_frame.pack()
        self.scrollable_frame.place(x=0, y=800)
        self.text_label = ctk.CTkLabel(self.scrollable_frame, text="")
        self.text_label.pack()
        self.draw_widgets()

    def open_arrival_cities(self) -> None:
        window: TableWindow = TableWindow(self, "arrival_cities", self.text_label)

    def open_customers(self) -> None:
        window: TableWindow = TableWindow(self, "customers", self.text_label)

    def open_flights(self) -> None:
        window: TableWindow = TableWindow(self, "flights", self.text_label)

    def open_positions(self) -> None:
        window: TableWindow = TableWindow(self, "positions", self.text_label)

    def open_staff(self) -> None:
        window: TableWindow = TableWindow(self, "staff", self.text_label)

    def open_tours(self) -> None:
        window: TableWindow = TableWindow(self, "tours", self.text_label)

    def open_travel_packages(self) -> None:
        window: TableWindow = TableWindow(self, "travel_packages", self.text_label)

    def open_types_of_tours(self) -> None:
        window: TableWindow = TableWindow(self, "types_of_tours", self.text_label)

    def open_functions(self) -> None:
        window: FunctionsWindow = FunctionsWindow(self, "Functions and procedures", self.text_label)

    def draw_widgets(self) -> None:
        # Main scheme
        # scheme_img = tkinter.PhotoImage(file="./assets/main.png")
        scheme_img = customtkinter.CTkImage(Image.open("./assets/main.png"), size=(1040, 800))
        scheme_label = ctk.CTkLabel(self, image=scheme_img, text="")
        scheme_label.pack(expand=1)
        scheme_label.place(x=0, y=0)

        # Arrival cities button
        arrival_cities_button = ctk.CTkButton(
            self,
            text="",
            command=self.open_arrival_cities,
            width=20,
            height=20,
            bg_color="white"
        )
        arrival_cities_button.place(x=806, y=523)
        # Customers button
        customers_button = ctk.CTkButton(
            self,
            text="",
            command=self.open_customers,
            width=20,
            height=20,
            bg_color="white"
        )
        customers_button.place(x=118, y=49)
        # Flights button
        flights_button = ctk.CTkButton(
            self,
            text="",
            command=self.open_flights,
            width=20,
            height=20,
            bg_color="white"
        )
        flights_button.place(x=544, y=523)
        # Positions button
        positions_button = ctk.CTkButton(
            self,
            text="",
            command=self.open_positions,
            width=20,
            height=20,
            bg_color="white"
        )
        positions_button.place(x=709, y=11)
        # Staff button
        staff_button = ctk.CTkButton(
            self,
            text="",
            command=self.open_staff,
            width=20,
            height=20,
            bg_color="white"
        )
        staff_button.place(x=448, y=11)
        # Tours button
        tours_button = ctk.CTkButton(
            self,
            text="",
            command=self.open_tours,
            width=20,
            height=20,
            bg_color="white"
        )
        tours_button.place(x=283, y=523)
        # Travel packages button
        travel_packages_button = ctk.CTkButton(
            self,
            text="",
            command=self.open_travel_packages,
            width=20,
            height=20,
            bg_color="white"
        )
        travel_packages_button.place(x=282, y=265)
        # Types of tours button
        types_of_tours_button = ctk.CTkButton(
            self,
            text="",
            command=self.open_types_of_tours,
            width=20,
            height=20,
            bg_color="white"
        )
        types_of_tours_button.place(x=21, y=523)
        # Functions button
        functions_and_procedures_button = ctk.CTkButton(
            self,
            text="Functions and procedures",
            command=self.open_functions,
            text_color="black",
            bg_color="white"
        )
        functions_and_procedures_button.place(x=0, y=0)

    def run_app(self) -> None:
        self.mainloop()
