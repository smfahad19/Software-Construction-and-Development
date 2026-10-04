def calculate_total(marks):
	return sum(marks)


def calculate_average(marks):
	return calculate_total(marks) / len(marks)


def calculate_grade(average):
	if average >= 80:
		return "A"
	if average >= 70:
		return "B"
	if average >= 60:
		return "C"
	if average >= 50:
		return "D"
	return "F"
