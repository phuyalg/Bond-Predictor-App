import unittest
from phuyalg_determine_bond import BondType

class TestBondType(unittest.TestCase):

    def setUp(self):
        self.bond_type = BondType()
    def test_ionic_character(self):
        # Test case 1: Sodium Chloride
        self.bond_type.element_1 = 'Na'
        self.bond_type.element_2 = 'Cl'
        self.bond_type.calculate_ionic_character()
        self.assertAlmostEqual(self.bond_type.ionic_character, 2.23, places=2)

        # Test case 2: Magnesium Fluoride
        self.bond_type.element_1 = 'Mg'
        self.bond_type.element_2 = 'F'
        self.bond_type.calculate_ionic_character()
        self.assertAlmostEqual(self.bond_type.ionic_character, 2.68, places=1)

        # Test case 3: Lithium Sulfur
        self.bond_type.element_1 = 'Li'
        self.bond_type.element_2 = 'S'
        self.bond_type.calculate_ionic_character()
        self.assertAlmostEqual(self.bond_type.ionic_character, 1.56, places=1)

    def test_determine_bond_type(self):
        # Test case 1: Ionic bond
        self.bond_type.ionic_character = 1.9
        self.bond_type.determine_bond_type()
        self.assertEqual(self.bond_type.bond_type, 'Ionic')

        # Test case 2: Invalid bond type (should be Polar Covalent)
        self.bond_type.ionic_character = 1.5
        self.bond_type.determine_bond_type()
        self.assertIsNot(self.bond_type.bond_type, 'Ionic')

        # Test case 3: Non-polar covalent bond
        self.bond_type.ionic_character = 0.2
        self.bond_type.determine_bond_type()
        self.assertEqual(self.bond_type.bond_type, 'Covalent')

    def test_get_user_inputs(self):

        # Test case 1: Valid input for element 1
        self.bond_type.element_1 = 'NA'
        self.bond_type.get_user_input_1()
        self.assertEqual(self.bond_type.element_1, 'Na')

        # Test case 2: Valid input for element 2
        self.bond_type.element_2 = 'o'
        self.bond_type.get_user_input_2()
        self.assertEqual(self.bond_type.element_2, 'O')


if __name__ == '__main__':
    unittest.main()
