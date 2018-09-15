#flashcards.py
import random

def main():
	print("hello")
	list_of_questions = [
		['0','1'],
		['1','2'],
		['2','4'],
		['3','8'],
		['4','16'],
		['5','32'],
		['6','64'],
		['7','128'],
		['8','256'],
		['9','512'],
		['10','1024']]

	answer = ' '
	while answer.capitalize()[0] != "Q":
		set = random.choice(list_of_questions)
		q_or_a = random.randint(0,1)
		question = set[q_or_a]
		if q_or_a == 0: 
			answer = input("What is 2^{}? ".format(question))
		else:
			answer = input("What is log base 2 of {}? ".format(question))
		if answer == set[1 - q_or_a]:
			print("Correct!")
		else:
			print("False!")

main()
