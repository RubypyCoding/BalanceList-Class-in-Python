import unittest
from balance_list import *


class BalanceListTests(unittest.TestCase):

	def setUp(self):
		self.func = BalanceList("Manuel", [["Julio", 234], ["Enero", 456], ["Agosto", 123]])

	def test_name_is_evaluated_as_getter(self):
	    self.assertEqual(self.func.name, "Manuel")

	def test_name_is_evaluated_as_setter(self):
		with self.assertRaises(AttributeError):
		    self.func.name = "Javier"

	def test_number_of_balances_returns_a_total_balance_numbers_in_list(self):
		self.assertEqual(self.func.number_of_balances(), 3)

	def test_total_balance_returns_an_overall_total_balance(self):
		self.assertEqual(self.func.total_balance(), 813)

	def test_add_balance_push_a_new_list_with_month_and_balance(self):
		self.func.add_balance(["Marzo", 678])
		self.assertEqual(self.func.number_of_balances(), 4)

	def test_current_balance_per_month_returns_string_with_month_and_balance(self):
		self.assertEqual(self.func.current_balance_per_month(), "Mes: Julio, Saldo: 234")

	def test_next_balance_returns_the_next_balance_in_list(self):
		self.assertEqual(self.func.next_balance(), 456)

	def test_advanced_three_and_current_balance_is_index_0_of_list(self):
		self.func.add_balance(["Marzo", 678])
		for i in range(4):
		    self.func.next_balance()
		self.assertEqual(self.func.current_balance_per_month(), "Mes: Julio, Saldo: 234")

if __name__=="__main__":
    unittest.main()