from bayes_opt import BayesianOptimization
from bayes_opt.logger import JSONLogger
from bayes_opt.event import Events


# min = -39.16599*dimensions at x = (-2.903..., ..., -2.903...)
# in our example dimensions = 2  =>  min = -78.33
def styblinski_tang(x, y):
    """Function with unknown internals we wish to maximize.

    This is just serving as an example, for all intents and
    purposes think of the inte  rnals of this function, i.e.: the process
    which generates its output values, as unknown.
    """

    return -0.5*((x**4 - 16*x**2 + 5*x) + (y**4 - 16*y**2 + 5*y))


# Bounded region of parameter space
pbounds = {'x': (-5, 5), 'y': (-5, 5)}

optimizer = BayesianOptimization(
    f=styblinski_tang,
    pbounds=pbounds,
    random_state=1,
)

# logger = JSONLogger(path="./logs300.json")
# optimizer.subscribe(Events.OPTIMIZATION_STEP, logger)

optimizer.maximize(
    init_points=2,
    n_iter=300,
)
print(styblinski_tang(-2.903, -2.903))