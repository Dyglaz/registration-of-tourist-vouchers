import customtkinter
import customtkinter as ctk
import tkinter
from tkinter import ttk
from database.db import Database


class FunctionsWindow(ctk.CTk):
    def __init__(self, parent, title):
        super().__init__()
        self.title = title
        self.db_obj = Database()
        self.root = ctk.CTkToplevel(parent)
        self.root.geometry("1300x250")
        self.root.title(title)
        self.root.resizable(False, False)
        customtkinter.set_appearance_mode("light")
        customtkinter.set_default_color_theme("green")
        self.draw_widgets()
        self.grab_focus()

    def set_styles(self):
        # Styles tables
        self.style = ttk.Style()
        self.style.theme_use("default")
        self.style.configure(
            "Treeview.Heading",
            background="palegreen1",
            foreground="black",
            font=('Arial', 13, 'bold')
        )
        self.style.configure(
            "Treeview",
            foreground="black",
            background="white",
            font=('Arial', 10, 'bold')
        )
        # Tab style
        self.style2 = ttk.Style()
        self.style2.theme_use("default")
        self.style2.configure(
            "TNotebook",
            background="white",
            tabposition="sw"
        )
        self.style2.configure(
            "TNotebook.Tab",
            background="cadetblue1",
            foreground="black",
            font=('Arial', 10, 'bold')
        )
        self.style2.map(
            "TNotebook.Tab",
            background=[("selected", "palegreen1")],
        )

    def get_tourist_vouchers_by_tour_name(self) -> None:
        tour_name = self.tour_name.get()
        count_sold_vouchers = self.db_obj.call_func_get_tourist_vouchers_by_tour_name(tour_name)
        count = list(count_sold_vouchers[0].values())[0]
        self.tour_name_var.set(f"Количество проданных путёвок по туру: {count}")

    def creating_a_tabular_part_of_employees_by_position(self):
        positions = self.entry_staff.get()
        active_count_data = self.db_obj.call_proc_get_employees_by_position(positions)
        if hasattr(self, 'tree') and isinstance(self.tree, ttk.Treeview):
            self.tree.destroy()
        try:
            active_count_data_keys = list(active_count_data[0].keys())
            self.tree = ttk.Treeview(master=self.tab_employees_by_position, columns=active_count_data_keys,
                                     show="headings")
            for col in active_count_data_keys:
                self.tree.heading(col, text=col)
            for line in active_count_data:
                self.tree.insert("", tkinter.END, values=list(line.values()), tags=("odd",))
            self.tree.pack(fill=tkinter.BOTH, expand=1)
        except IndexError:
            print("Specialists by position or not, or the name of the position is entered incorrectly")

    def draw_widgets(self) -> None:
        # Styles exec
        self.set_styles()
        # Tabs
        tab_control = ttk.Notebook(self.root)
        self.tab_employees_by_position = ctk.CTkFrame(tab_control, fg_color="white")
        tab_customer_service_information = ctk.CTkFrame(tab_control, fg_color="white")
        tab_min_max_tour_prices = ctk.CTkFrame(tab_control, fg_color="white")
        tab_average_cost_of_the_tour = ctk.CTkFrame(tab_control, fg_color="white")
        tab_tourist_vouchers_by_tour_name = ctk.CTkFrame(tab_control, fg_color="white")
        tab_control.add(self.tab_employees_by_position, text="Получить сотрудников по должности")
        tab_control.add(tab_customer_service_information, text="Информация об обслуживании клиентов")
        tab_control.add(tab_min_max_tour_prices, text="Самый дешёвый и дорогой тур")
        tab_control.add(tab_average_cost_of_the_tour, text="Средняя цена по всем турам")
        tab_control.add(tab_tourist_vouchers_by_tour_name, text="Получить количество проданных путёвок по туру")
        tab_control.pack(expand=1, fill="both")

        # Employees by position
        employee_by_position_frame = ctk.CTkFrame(self.tab_employees_by_position, fg_color="white")
        # Row
        row_employee_by_position = ctk.CTkFrame(employee_by_position_frame, fg_color="white")
        label_employee_by_position = ctk.CTkLabel(row_employee_by_position, text="Должность", fg_color="white")
        self.entry_staff = ctk.CTkEntry(row_employee_by_position, width=200)
        label_employee_by_position.grid(row=0, column=0, padx=15)
        self.entry_staff.grid(row=0, column=1, padx=15)
        row_employee_by_position.pack(pady=5)
        # Button
        price_btn = ctk.CTkButton(employee_by_position_frame, text="Accept",
                                  command=self.creating_a_tabular_part_of_employees_by_position)
        price_btn.pack(pady=5)
        employee_by_position_frame.pack(side="bottom")

        # Customer service information
        active_count_data = self.db_obj.call_proc_get_customer_service_information()
        active_count_data_keys = list(active_count_data[0].keys())
        tree = ttk.Treeview(master=tab_customer_service_information, columns=active_count_data_keys, show="headings")
        for col in active_count_data_keys:
            tree.heading(col, text=col)
        for line in active_count_data:
            tree.insert("", tkinter.END, values=list(line.values()), tags=("odd",))
        tree.pack(fill=tkinter.BOTH, expand=1)

        # Min and max tour prices
        active_count_data = self.db_obj.call_proc_get_min_max_tour_prices()
        active_count_data_keys = list(active_count_data[0].keys())
        tree = ttk.Treeview(master=tab_min_max_tour_prices, columns=active_count_data_keys, show="headings")
        for col in active_count_data_keys:
            tree.heading(col, text=col)
        for line in active_count_data:
            tree.insert("", tkinter.END, values=list(line.values()), tags=("odd",))
        tree.pack(fill=tkinter.BOTH, expand=1)

        # Average cost of the tour
        active_count_data = self.db_obj.call_func_get_the_average_cost_of_the_tour()
        active_count_data_keys = list(active_count_data[0].keys())
        tree = ttk.Treeview(master=tab_average_cost_of_the_tour, columns=active_count_data_keys, show="headings")
        tree.heading(active_count_data_keys[0], text=active_count_data_keys[0])
        tree.insert("", tkinter.END, values=list(active_count_data[0].values()), tags=("odd",))
        tree.pack(fill=tkinter.BOTH, expand=1)

        # number of tickets sold by tour name
        tickets_count_frame = ctk.CTkFrame(tab_tourist_vouchers_by_tour_name, fg_color="white")
        # Result label
        self.tour_name_var = tkinter.StringVar()
        tour_lbl = ctk.CTkLabel(tickets_count_frame, textvariable=self.tour_name_var, fg_color="white")
        tour_lbl.pack(pady=10)
        # Row
        row_tour = ctk.CTkFrame(tickets_count_frame, fg_color="white")
        label_tour = ctk.CTkLabel(row_tour, text="Название тура", fg_color="white")
        self.tour_name = ctk.CTkEntry(row_tour, width=300)
        label_tour.grid(row=0, column=0, padx=15)
        self.tour_name.grid(row=0, column=1, padx=15)
        row_tour.pack(pady=5)
        # Button
        tour_btn = ctk.CTkButton(tickets_count_frame, text="Accept", command=self.get_tourist_vouchers_by_tour_name)
        tour_btn.pack(pady=5)
        tickets_count_frame.pack()

    def grab_focus(self) -> None:
        self.root.grab_set()
        self.root.focus_set()
        self.root.wait_window()

