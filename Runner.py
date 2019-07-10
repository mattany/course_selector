from AllCourses import AllCourses

all_courses = AllCourses().get_list_of_courses()
num_of_students = 100
num_of_strategies = 4

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

def cakes():
    return cake_factory(0, [0 for i in range(num_of_strategies)],[])


print(len(cakes()))
# f= open("combinations.txt","w+")
# f.write(str(cakes()))