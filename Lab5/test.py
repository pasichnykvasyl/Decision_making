from simplex import Simplex
objective = '1y_1 + 1y_2 + 1y_3'
constraints = ['11y_1 + 14y_2 + 17y_3 <= 1', '10y_1 + 16y_2 + 13y_3 <= 1', '12y_1 + 11y_2 + 9y_3 <= 1']
Lp_system = Simplex(num_vars=3, constraints=constraints, objective_function=objective)
print(Lp_system.solution)
print(Lp_system.optimize_val)
