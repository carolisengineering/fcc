import copy
import random
from collections import Counter
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
		if number_of_balls > len(self.contents):
			return self.contents
		balls_to_draw = self.contents
		balls_removed = []
		for x in range(number_of_balls):
			index_of_ball_to_remove = random.randint(0,len(balls_to_draw)-1)
			ball_to_remove = balls_to_draw[index_of_ball_to_remove]
			balls_removed.append(ball_to_remove)
			del balls_to_draw[index_of_ball_to_remove]
		return balls_removed




def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
	probability = 0
	actual_matches_expected_count = 0
	experiment_success = False
	for experiment in range(num_experiments):
		actual_balls = hat.draw(num_balls_drawn)
		ball_counter = Counter(actual_balls)
		for item in expected_balls:
			if ball_counter[item] >= expected_balls[item]:
				experiment_success = True
			else:
				experiment_success = False
				break
		if experiment_success:
			actual_matches_expected_count += 1
		print(f"expected_balls: {expected_balls}")
		print(f"actual balls: {actual_balls}")
		print(f"ball counter: {ball_counter}")
		print(f"experiment_success: {experiment_success}")
		print(f"actual matches expected: {actual_matches_expected_count}")

	probability = actual_matches_expected_count / num_experiments

	return probability
