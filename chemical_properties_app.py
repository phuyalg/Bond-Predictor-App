import tkinter as tk
from tkinter import ttk

class ChemicalPropertiesApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Chemical Properties App")
        self.geometry("500x500")
        self.homepage_label = ttk.Label(justify="center", padding=5, text="Welcome to the Chemical Properties App!",
                                        font=("Arial",16,"bold"))
        self.homepage_label.pack(pady=50)
        self.bond_calculator_button = ttk.Button(self, text="Bond Type Calculator", command=self.open_bond_calculator,width=20)
        self.bond_calculator_button.pack(pady=20)
    def open_bond_calculator(self):
        self.destroy()
        bond_calculator = BondCalculator()


class BondType:
    def __init__(self):
        self.element_1 = None
        self.element_2 = None
        self.electronegativity_dict = {
            'H': 2.2, 'He': None, 'Li': 0.98, 'Be': 1.57, 'B': 2.04,
            'C': 2.55, 'N': 3.04, 'O': 3.44, 'F': 3.98, 'Ne': None,
            'Na': 0.93, 'Mg': 1.31, 'Al': 1.61, 'Si': 1.9, 'P': 2.19,
            'S': 2.58, 'Cl': 3.16, 'K': 0.82, 'Ar': None, 'Ca': 1.0,
            'Sc': 1.36, 'Ti': 1.54, 'V': 1.63, 'Cr': 1.66, 'Mn': 1.55,
            'Fe': 1.83, 'Ni': 1.91, 'Co': 1.88, 'Cu': 1.9, 'Zn': 1.65,
            'Ga': 1.81, 'Ge': 2.01, 'As': 2.18, 'Se': 2.55, 'Br': 2.96,
            'Kr': 3.0, 'Rb': 0.82, 'Sr': 0.95, 'Y': 1.22, 'Zr': 1.33,
            'Nb': 1.6, 'Mo': 2.16, 'Tc': None, 'Ru': 2.2, 'Rh': 2.28,
            'Pd': 2.2, 'Ag': 1.93, 'Cd': 1.69, 'In': 1.78, 'Sn': 1.96,
            'Sb': 2.05, 'I': 2.66, 'Te': 2.1, 'Xe': 2.6, 'Cs': 0.79,
            'Ba': 0.89, 'La': 1.1, 'Ce': 1.12, 'Pr': 1.13, 'Nd': 1.14,
            'Pm': None, 'Sm': 1.17, 'Eu': 1.2, 'Gd': 1.2, 'Tb': 1.2,
            'Dy': 1.22, 'Ho': 1.23, 'Er': 1.24, 'Tm': 1.25, 'Yb': 1.1,
            'Lu': 1.27, 'Hf': 1.3, 'Ta': 1.5, 'W': 2.36, 'Re': 1.9,
            'Os': 2.2, 'Ir': 2.2, 'Pt': 2.28, 'Au': 2.54, 'Hg': 2.0,
            'Tl': 1.62, 'Pb': 2.33, 'Bi': 2.02, 'Th': 1.3, 'Pa': None,
            'U': None, 'Np': None, 'Pu': None, 'Am': None, 'Cm': None,
            'Bk': None, 'Cf': None, 'Es': None, 'Fm': None, 'Md': None,
            'No': None, 'Lr': None, 'Rf': None, 'Db': None, 'Sg': None,
            'Bh': None, 'Hs': None, 'Mt': None, 'Ds': None, 'Rg': None,
            'Cn': None, 'Nh': None, 'Fl': None, 'Mc': None, 'Lv': None,
            'Ts': None, 'Og': None
        }
        self.metals = ['Li', 'Be', 'B', 'Na', 'Mg', 'Al', 'Si', 'K',
                       'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co',
                       'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Rb', 'Sr',
                       'Yb', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd',
                       'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'Cs', 'Ba',
                       'La', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt',
                       'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'Fr', 'Ra',
                       'Ac', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds',
                       'Rg', 'Cn', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu',
                       'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu',
                       'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk',
                       'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr']

    def get_electronegativity(self, element):
        return self.electronegativity_dict.get(element)

    def calculate_bond_type(self, element_1, element_2):
        self.element_1 = element_1
        self.element_2 = element_2

        electronegativity_1 = self.get_electronegativity(element_1)
        electronegativity_2 = self.get_electronegativity(element_2)

        if electronegativity_1 is None or electronegativity_2 is None:
            return "Unknown"

        if element_1 in self.metals and element_2 in self.metals:
            return "Metallic"
        else:
            difference = abs(electronegativity_1 - electronegativity_2)
            if difference > 1.7:
                return "Ionic"
            elif 1.7 >= difference >= 0.3:
                if element_1 in self.metals or element_2 in self.metals:
                    return "Ionic"
                else:
                    return "Polar Covalent"
            else:
                return "Covalent"


class BondCalculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Bond Type Calculator")
        self.geometry("500x500")

        self.element_1_label = ttk.Label(self, text="Element 1:")
        self.element_1_label.pack()
        self.element_1_entry = ttk.Entry(self)
        self.element_1_entry.pack()

        self.element_2_label = ttk.Label(self, text="Element 2:")
        self.element_2_label.pack()
        self.element_2_entry = ttk.Entry(self)
        self.element_2_entry.pack()
        self.calculate_button = ttk.Button(self, text="Calculate", command=self.initiate_bond_type)
        self.calculate_button.pack()
        self.return_button = ttk.Button(self, text="return to homepage", command=self.return_homepage)
        self.return_button.pack(pady=20)




        self.result_label = ttk.Label(self, text="")
        self.result_label.pack()

        self.bond_calculator = BondType()

    def return_homepage(self):
        self.destroy()
        homepage = ChemicalPropertiesApp()
    def initiate_bond_type(self):
        if len(self.element_1_entry.get()) > 2:
            element_1 = None
        else:
            if len(self.element_1_entry.get()) == 2:
                element_1 = self.element_1_entry.get()[0].upper() + self.element_1_entry.get()[1].lower()
            else:
                element_1 = self.element_1_entry.get()[0].upper()
        if len(self.element_2_entry.get()) > 2:
            element_2 = None
        else:
            if len(self.element_2_entry.get()) == 2:
                element_2 = self.element_2_entry.get()[0].upper() + self.element_2_entry.get()[1].lower()
            else:
                element_2 = self.element_2_entry.get()[0].upper()
        bond_type = self.bond_calculator.calculate_bond_type(element_1,element_2)

        if element_1 is None or element_2 is None:
            self.result_label.config(text="Invalid Entry. Please Try again")
        else:
            self.result_label.config(text="Bond Type: " + bond_type)


if __name__ == "__main__":
    gui = ChemicalPropertiesApp()
    gui.mainloop()
