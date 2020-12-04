from bayes_opt import BayesianOptimization
from bayes_opt.logger import JSONLogger
from bayes_opt.event import Events
import json

def styblinski_tang(**args):
    f = 0
    for i in args:
        x = args[i]
        f += x ** 4 - 16 * x ** 2 + 5 * x
    return -0.5 * f

pbounds = {}
for i in range(20):
    pbounds['x' + str(i)] = (-5, 5)


optimizer = BayesianOptimization(
    f=styblinski_tang,
    pbounds=pbounds,
    random_state=1,
)
logger = JSONLogger(path="./logs20.json")
optimizer.subscribe(Events.OPTIMIZATION_STEP, logger)

optimizer.maximize(
    init_points=2,
    n_iter=150,
)

print(styblinski_tang(-2.903, -2.903))

def parse():
    X = []
    target = []
    with open("./logs20.json", "r") as read_file:
        for line in read_file.readlines():
            data = json.loads(line)
            points = data['params']
            # print(points)
            temp = []
            for i in range(len(points)):
                temp.append(points['x' + str(i)])
            X.append(temp)
            target.append(data['target'])
    print(len(X), len(target))
    print(X)
    print(target)
