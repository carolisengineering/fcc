import copy
import random
# Consider using the modules imported above.

class Hat:

	def __init__(self, red=0, orange=0, yellow=0, green=0, blue=0, test=0):
		self.contents = []
		for x in range(red):
			self.contents.append("red")
		for x in range(orange):
			self.contents.append("orange")
		for x in range(yellow): 
			self.contents.append("yellow")
		for x in range(green):
			self.contents.append("green")
		for x in range(blue):
			self.contents.append("blue")
		for x in range(test):
			self.contents.append("test") 

	def draw(self, number_of_balls):
		balls_removed = []
		for x in range(number_of_balls):
			index_of_ball_to_remove = random.randint(1,number_of_balls)
			ball_to_remove = self.contents[index_of_ball_to_remove]
			del self.contents[index_of_ball_to_remove]
			balls_removed.append(ball_to_remove)
			number_of_balls -= number_of_balls
		return balls_removed




def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
	print('this is an expriment.')
	probability = 0
	original_hat = hat
	for experiment in range(0,num_experiments):
		actual_balls = hat.draw(num_balls_drawn)
		print(actual_balls)
		print(expected_balls)
