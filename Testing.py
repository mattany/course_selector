from AllCourses import AllCourses
from Student import Student
from Strategy import Strategy

all_courses = AllCourses().get_list_of_courses()

st1 = Student(Strategy.Linear, all_courses)
st1.fit_courses_and_scores()

print("The points distribution: ")
print(st1.get_courses_and_scores())

ass1 = ["Algorithms", "Infi"]
print("Satisfaction after assignment to " + str(ass1))
print(st1.evaluate_satisfaction(ass1))

ass2 = ["Intro to NN", "Probability"]
print("Satisfaction after assignment to " + str(ass2))
print(st1.evaluate_satisfaction(ass2))

ass3 = ["Intro to AI", "Crypto"]
print("Satisfaction after assignment to " + str(ass3))
print(st1.evaluate_satisfaction(ass3))
