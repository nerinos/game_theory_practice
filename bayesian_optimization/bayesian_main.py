from bayes_opt import BayesianOptimization


def styblinski_tang(x,y):
    return -0.5*((x**4 - 16*x**2 + 5*x) + (y**4 - 16*y**2 + 5*y))

pbounds = {'x': (-5, 5), 'y': (-5, 5)}


optimizer = BayesianOptimization(
    f=styblinski_tang,
    pbounds=pbounds,
    random_state=1,
)

optimizer.maximize(
    init_points=2,
    n_iter=100,
)

print(styblinski_tang(-2.903, -2.903))