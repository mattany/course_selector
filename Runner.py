import math

from AllCourses import AllCourses
from Matcher import Matcher
from Strategy import Strategy

all_courses = AllCourses().get_list_of_courses()
num_of_students = 100
CLASS_SIZE = 30
num_of_strategies = len(Strategy)


def cake_factory(cur_index, cake, cakes):
    if cur_index == num_of_strategies - 1:
        cake[cur_index] = num_of_students - sum([cake[j] for j in range(cur_index)])
        cakes.append(cake.copy())
        return cakes

    for i in range(num_of_students + 1 - sum([cake[j] for j in range(
            cur_index)])):
        cake[cur_index] = i
        cakes = cake_factory(cur_index + 1, cake, cakes)

    return cakes


def get_cakes():
    return cake_factory(0, [0 for i in range(num_of_strategies)], [])


def get_strategy_dict(dist):

    return dict(zip([i for i in Strategy], dist))


def get_satisfactions(students):
    satisfactions = [[0, 0] for i in range(len(Strategy))]  # sum of satisfactions, count
    for student in students:
        satisfactions[student._strategy.value][0] += student.evaluate_satisfaction()
        satisfactions[student._strategy.value][1] += 1
    return [satisfactions[i][0] / satisfactions[i][1] if satisfactions[i][1] != 0 else 0 for i in range(len(satisfactions))]


def get_results():
    cakes = get_cakes()
    one_percent = math.floor(len(cakes)/100)                      #TODO delete - prints
    percents = [(one_percent * i, i) for i in range(100)]        #TODO delete - prints
    for cake in cakes:
        if len(percents) > 0 and cakes[percents[0][0]] == cake:                       #TODO delete - prints
            print(percents[0][1])                                  #TODO delete - prints
            percents.pop(0)                                   #TODO delete - prints
        strategy_dict = get_strategy_dict(cake)
        matcher = Matcher(all_courses, strategy_dict, CLASS_SIZE).match()
        cake += get_satisfactions(matcher)
    return cakes


if __name__ == "__main__":
    # print(str(get_strategy_dict([0, 1, 5, 1])))
    f = open("combinations.txt","w+")
    for item in get_results():
        f.write('%s\n' % item)
    f.close()