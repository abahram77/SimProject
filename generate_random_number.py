# this class is responsible for generating random variables of different distributions
import random
import math


class ExponentialGenerator:
    def __init__(self, lambdaa):
        self.lambdaa = lambdaa
        self.random_generator = random.Random()

    def next_random(self):
        return -math.log(self.random_generator.random()) / self.lambdaa


class BernoulliGenerator:
    def __init__(self, p, true_val, false_val):
        self.p = p
        self.true_val = true_val
        self.false_val = false_val
        self.random_generator = random.Random()

    def next_random(self):
        if self.random_generator.random() <= self.p:
            return self.true_val
        else:
            return self.false_val


# generates number of exponential distribution with lambda mean
def get_exponential_generator(lambdaa):
    generator = ExponentialGenerator(lambdaa)
    return generator


# generates #number of bernoulli distribution with probability p and true value = true_val and false value = false_val
def get_bernoulli_generator(p, true_val, false_val):
    return BernoulliGenerator(p, true_val, false_val)
