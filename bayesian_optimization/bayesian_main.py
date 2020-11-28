from bayes_opt import BayesianOptimization
from bayes_opt.logger import JSONLogger
from bayes_opt.event import Events
import json

def styblinski_tang(x,y):
    return -0.5*((x**4 - 16*x**2 + 5*x) + (y**4 - 16*y**2 + 5*y))

pbounds = {'x': (-5, 5), 'y': (-5, 5)}


optimizer = BayesianOptimization(
    f=styblinski_tang,
    pbounds=pbounds,
    random_state=1,
)
logger = JSONLogger(path="./logs.json")
optimizer.subscribe(Events.OPTIMIZATION_STEP, logger)

optimizer.maximize(
    init_points=2,
    n_iter=30,
)

print(styblinski_tang(-2.903, -2.903))

def parse():
    x_points = []
    y_points = []
    target = []
    with open("./logs.json", "r") as read_file:
        for line in read_file.readlines():
            data = json.loads(line)
            points = data['params']
            target.append(data['target'])
            x_points.append(points['x'])
            y_points.append(points['y'])
    print(len(x_points), len(y_points), len(target))
    print(x_points)
    print(y_points)
    print(target)
