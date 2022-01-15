class Category:

	def __init__(self, name):
		self.name = name
		self.ledger = []

	def get_balance(self):
		balance = 0
		for line_item in self.ledger:
			balance += line_item["amount"]
		return balance

	def check_funds(self, amount):
		balance = self.get_balance()
		if amount <= balance:
			return True
		else:
			return False

	def deposit(self, amount, description=""):
		line_item = {"amount": amount, "description": description}
		self.ledger.append(line_item)

	def withdraw(self, amount, description=""):
		withdraw_complete = False
		if self.check_funds(amount):
			negative_amount = amount * -1
			line_item = {"amount": negative_amount, "description": description}
			self.ledger.append(line_item)
			withdraw_complete = True
		return withdraw_complete

	def transfer(self, amount, category):
		transfer_complete = False
		if self.check_funds(amount):
			category_name = category.name
			withdraw_description = f"Transfer to {category_name}"
			deposit_description = f"Transfer from {self.name}"
			self.withdraw(amount, withdraw_description)
			category.deposit(amount, deposit_description)
			transfer_complete = True
		return transfer_complete


def create_spend_chart(categories):
	return ""