import math
import turtle
import tkinter as tk
from tkinter import ttk
from time import sleep
class BondType:
    """
     A class which predicts the type of bond two elements will make.

     Attributes:

     element_1:
        a string representing the symbol of the first element.

     element_2:
        a string representing the symbol of the second element.
     electronegativity_dict:
        a dictionary that stores the electronegativity values of all elements on the Pauling scale.

     metals:
        a list that stores the symbols of all metals in the periodic table of elements.

     electronegativity_1:
        an int that represents the electronegativity value of the first element.

     electronegativity_1:
        an int that represents the electronegativity value of the second element.

     ionic_character:
        an int that represents the ionic character of the compound.

     bond_type:
        a string that represents the type of bond formed by the two elements.

     image:
        an img file that is set in display_image based off of the bond type.

     Methods:

     init(self):
        Constructor method that initializes the BondPredictor object.

      get_user_input_1(self):
        Takes user inputs for the first element.

     get_user_input_1(self):
        Takes user inputs for the second element.

      calculate_ionic_character(self):
        Calculates the ionic character of the bond based on the electronegativity values of the two elements.

      determine_bond_type(self):
        Determines the type of bond (ionic, polar covalent, or covalent) based on the calculated ionic character.

      display_bond_type(self):
        Displays the bond type prediction and an option to show more information.

      display_image(self):
        Displays an image corresponding to the bond type prediction made in the display_bond_type() method.

      bond_type_wn(self):
        Draws the interface for the bond type prediction program.

    """
    """
     Initializes attributes for the BondType class

     :returns - none
     """
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

        self.ionic_character = None
        self.percent_ionic_character = None
        self.bond_type = None
        self.electronegativity_1 = None
        self.electronegativity_2 = None
        self.image = None

    """
     Takes user input for first element, checks if it is valid length, 
     capitalizes first & lower cases second letter of user input.

     :returns - self.element_1 (cleaned up first element input)
     """
    def get_user_input_1(self):
        self.element_1 = (input("Please enter the symbol of the first element (Copper = Cu): "))
        while len(self.element_1) > 2:
            self.element_1 = input("Invalid Symbol. Please reenter the symbol of the first element (Copper = Cu): ")
        if len(self.element_1) == 2:
            self.element_1 = self.element_1[0].upper() + self.element_1[1].lower()
            return self.element_1
        else:
            self.element_1 = self.element_1[0].upper()
            return self.element_1

    """
     Takes user input for second element, checks if it is valid length, 
     capitalizes first & lower cases second letter of user input.

     :returns - self.element_2 (cleaned up second element input)
     """
    def get_user_input_2(self):
        self.element_2 =(input("Please enter the symbol of the second element (Oxygen = O): "))
        while len(self.element_2) > 2:
            self.element_2 = input("Invalid Symbol. Please reenter the symbol of the second element (Oxygen = O): ")
        if len(self.element_2) == 2:
            self.element_2 = self.element_2[0].upper() + self.element_2[1].lower()
            return self.element_2
        else:
            self.element_2 = self.element_2[0].upper()
            return self.element_2

    """
     Prompts user to re enter first element if element is not in electronegativity_dict 
     or if its value is none.

     :returns - self.element_1
     """
    def check_element_1(self):
        while self.element_1 not in self.electronegativity_dict.keys() or self.electronegativity_dict[self.element_1] == None:
            print("\n")
            sleep(1)
            print("Invalid element or no data available.")
            sleep(1)
            print("Try again!")
            self.get_user_input_1()

    """
     Prompts user to re enter first element if element is not in self.electronegativity_dict.
     or if its value is none.

     :returns - self.element_1
     """
    def check_element_2(self):
        while self.element_2 not in self.electronegativity_dict.keys() or self.electronegativity_dict[self.element_2] == None:
            print("\n")
            sleep(1)
            print("Invalid element or no data available.")
            sleep(1)
            print("Try again!")
            self.get_user_input_2()

    """
     Sets electronegativity value of the first element based on key's (symbol's) corresponding value in self.electronegativity_dict.

     :returns - self.electronegativity_1: an float value of electronegativity 
     """
    def set_electronegativity_1(self):
        self.electronegativity_1 = self.electronegativity_dict[self.element_1]
        return self.electronegativity_1

    """
     Sets electronegativity value of the second element based on key's (symbol's) corresponding value in self.electronegativity_dict.

     :returns - self.electronegativity_2: an int value of electronegativity 
     """
    def set_electronegativity_2(self):
        self.electronegativity_2 = self.electronegativity_dict[self.element_2]
        return self.electronegativity_2

    """
     Calculates the ionic character of the bond by subtracting the lower electronegativity value from the greater value.

     :returns - self.ionic_character: a float value of ionic character 
     """

    """  
     Calculates the ionic character between two elements based on their electronegativity values. 
     If both elements are metals, it returns None. Otherwise, it returns the absolute value of the
     difference between the electronegativity values rounded to two decimal places.

     :returns - self.ionic_character: a float value of ionic character 
     """
    def calculate_ionic_character(self):
        if self.element_1 and self.element_2 in self.metals:
            self.ionic_character = None
            return self.ionic_character
        else:
            self.ionic_character = abs(round(self.set_electronegativity_1() - self.set_electronegativity_2(),2))
            return self.ionic_character
    """
     Calculates the percent ionic character of the bond
     
     :returns - self.percent_ionic_character: a float value of percent ionic character 
     """
    def calculate_percent_ionic_character(self):
        if self.ionic_character == None:
            electro_neg_diff = None
            return electro_neg_diff
        else:
            electro_neg_diff = self.ionic_character
            self.percent_ionic_character = round(((1 - math.exp(-(electro_neg_diff/2)**2))*100),1)



    """
     Determines bond tye (ionic, polar covalent, or covalent) by comparing calculated ionic character to the Pauling scale.

     :returns - A print statement that describes the type of bond the two elements will make.
     """
    def determine_bond_type(self):
        if self.ionic_character == None:
            self.bond_type = "Metallic"
            return self.bond_type
        if self.ionic_character > 1.7:
            if self.element_1 and self.element_2 not in self.metals:
                self.bond_type = "Polar Covalent"
            else:
                self.bond_type = "Ionic"
                return self.bond_type
        elif 1.7 >= self.ionic_character >= 0.3:
            self.bond_type = "Polar Covalent"
            return self.bond_type
        else:
            self.bond_type = "Covalent"
            return self.bond_type

    """
     Displays the bond type prediction and an option to show more information.
     Deletes the "predict_button" and adds a new button labeled "Show more info". When clicked, this new button calls the display_image() method.

    :return: None
    """
    def display_bond_type(self):
        canvas = turtle.Screen().getcanvas()
        canvas.delete("predict_button")
        bond_type = self.bond_type
        t = turtle.Turtle()
        t.speed(0)
        t.hideturtle()
        t.penup()
        t.goto(-300, 150)
        t.write("Bond type prediction:", font=("Arial", 18, "normal"))
        t.goto(-300, 100)
        if self.ionic_character == None:
            sleep(1)
            t.write(
                f"{self.element_1} and {self.element_2} do not have ionic character and will form a {bond_type} bond",
                font=("Arial", 16, "normal"))
        else:
            sleep(1)
            t.write(
                f"{self.element_1} and {self.element_2} have an ionic character of {self.ionic_character} and will form a(n) {bond_type} bond",
                font=("Arial", 16, "normal"))
        button = tk.Button(canvas.master, text="Show more info", command=self.display_image)
        sleep(1)
        canvas.create_window(0, 0, window=button, tags="new_button")
        turtle.mainloop()

    """
     Displays an image corresponding to the bond type prediction made in the display_bond_type() method.
     Deletes any previous image and creates a new image with the appropriate file name. 
     Deletes the "new_button" created by display_bond_type() method.
     
    :return: None
    """
    def display_image(self):
        canvas = turtle.Screen().getcanvas()
        canvas.delete("image")
        bond_type = self.bond_type
        if bond_type == "Ionic":
            self.image = tk.PhotoImage(file="image/ionic_bond.png").subsample(2)
            canvas.create_image(0, 100, image=self.image, tags=("ionic",))
        elif bond_type == "Polar Covalent":
            self.image = tk.PhotoImage(file="image/polar_covalent.png").subsample(2)
            canvas.create_image(0, 100, image=self.image, tags=("polar_covalent",))
        elif bond_type == "Metallic":
            self.image = tk.PhotoImage(file="image/metallic.png").subsample(2)
            canvas.create_image(0, 100, image=self.image, tags=("metallic",))
        else:
            self.image = tk.PhotoImage(file="image/covalent.png").subsample(2)
            canvas.create_image(0, 100, image=self.image, tags=("covalent",))
        canvas.delete("new_button")

    """
    Draws the interface for the bond type prediction program.

    :returns: None
    """
    def bond_type_wn(self):
        wn = turtle.Screen()
        wn.bgcolor("light blue")
        wn.title("Bond Predictor")
        canvas = wn.getcanvas()
        t_canvas = canvas.master
        button = tk.Button(t_canvas, text="Predict Bond Type", command=self.display_bond_type)
        canvas.create_window(0, 0, window=button,tags="predict_button")
        wn.exitonclick()
        turtle.mainloop()

    """
     Collects user input for two chemical elements,
     calculates the ionic character of their bond, determines the bond type, and draws a visual representation
     of the bond type using Turtle graphics.

     :return: None
    """

def main():
    bond_type = BondType()
    print("Hello!")
    sleep(1)
    print("This program predicts the type of bond two elements will form.")
    sleep(2)
    print("To begin")
    sleep(1)
    bond_type.get_user_input_1()
    bond_type.check_element_1()
    bond_type.get_user_input_2()
    bond_type.check_element_2()
    bond_type.calculate_ionic_character()
    bond_type.calculate_percent_ionic_character()
    bond_type.determine_bond_type()
    bond_type.bond_type_wn()



if __name__ == '__main__':
    main()