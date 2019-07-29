from Strategy import Strategy
from Matcher import Matcher
from Runner import ALL_COURSES
from Main import CLASS_SIZE
from Runner import get_satisfactions

STRATEGY_1 = 0
STRATEGY_2 = 0
STRATEGY_3 = 0
STRATEGY_4 = 0
STRATEGY_5 = 0


cakes_counter = 0  # just to check progress ...
cake = [STRATEGY_1, STRATEGY_2, STRATEGY_3, STRATEGY_4, STRATEGY_5]
strategy_dict = dict(zip([i for i in Strategy], cake))
matcher = Matcher(ALL_COURSES, strategy_dict, CLASS_SIZE).match()
cake += get_satisfactions(matcher)
print(cake)

