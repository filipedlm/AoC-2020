import Helpers


def import_input_1():
    return [int(x) for x in Helpers.import_input(r'Inputs\Input_day1.txt')]


@Helpers.timeit
def solve_day1_1(to_found=2020, report=import_input_1()):
    sum_to_2020 = set([to_found - x for x in report])

    for expense in report:
        # given one expense, find another one in the same report: expense2 such as expense2 = 2020 - expense
        if expense in sum_to_2020:
            return expense, expense * (to_found - expense)


@Helpers.timeit
def solve_day1_2():
    expense_report = import_input_1()
    results = [(exp,) + solve_day1_1(2020 - exp, expense_report) for exp in expense_report]
    return [(a, b, c, a * c) for a, b, c in results if b != 0]
