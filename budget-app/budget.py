class Category:

	def __init__(self, name):
		self.name = name
		self.ledger = []

	def __str__(self):
		num_stars = int(15 - (len(self.name)/2))
		name_line = "*" * num_stars + self.name
		end_stars = 30 - len(name_line)
		name_line = name_line + ("*" * end_stars) + "\n"
		
		ledger_lines = ""
		for line in self.ledger:
			description_length = len(line["description"])
			if description_length > 23:
				description = line["description"][:23]
			else:
				spaces = 23 - description_length
				description = line["description"] + (" " * spaces)

			amount = "{:.2f}".format(line["amount"])
			amount_length = len(amount)
			if amount_length < 7:
				spaces = 7 - amount_length
				amount = (" " * spaces) + amount
			ledger_line = description + amount + "\n"
			ledger_lines += ledger_line

		total = str(round(self.get_balance(), 2))
		total_line = f"Total: {total}"

		return name_line + ledger_lines + total_line

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
	total_spend = 0
	category_spend_values = []
	category_percentages = []

	for category in categories:
		category_spend = 0
		for line_item in category.ledger:
			if line_item["amount"] < 0:
				category_spend -= line_item["amount"]
		category_spend_values.append(category_spend)
		total_spend += category_spend

	for category_amount in category_spend_values:
		category_percentage = round((int(category_amount * 100) // total_spend) // 10) * 10
		category_percentages.append(category_percentage)

	spend_chart = "Percentage spent by category\n"

	for x in range (100, -1, -10):
		if len(str(x)) < 3:
			percentage_string = (" " * (3 - len(str(x))) + str(x))
		else:
			percentage_string = str(x)
		spend_chart += (percentage_string + "|")
		for percentage in category_percentages:
			if percentage >= x:
				spend_chart += " o "
			else:
				spend_chart += "   "
		if x == 0:
			spend_chart += " \n    "
		else:
			spend_chart += " \n"

	for x in range(len(categories)):
		spend_chart += "---"
		if x == (len(categories) - 1):
			spend_chart += "-\n"

	category_name_lengths = [len(category.name) for category in categories]
	max_category_name_length = max(category_name_lengths)

	for x in range(max_category_name_length):
		spend_chart += "    "
		for category in categories:
			if x < len(category.name):
				spend_chart += f" {category.name[x]} "
			else:
				spend_chart += "   "
		if x < (max_category_name_length - 1):
			spend_chart += " \n"
		else:
			spend_chart += " "

	return spend_chart