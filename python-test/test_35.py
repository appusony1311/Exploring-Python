#Question:
#Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).
list_square = []

def define_list():
	for i in range(1,21):
		list_square.append(i)

define_list()
print(list_square)
