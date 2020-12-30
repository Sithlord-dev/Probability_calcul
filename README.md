### Probability calculator

Suppose there is a hat containing 5 blue balls, 4 red balls, and 2 green balls. What is the probability that a random draw of 4 balls will contain at least 1 red ball and 2 green balls?  Here is a program that would perform a large number of experiments to determine the approximate probability of drawing certain balls randomly from a hat. 

It uses a `Hat` class in which takes a variable number of arguments that specify the number of balls of each color that are in the hat. For example:
```
hat1 = Hat(yellow=3, blue=2, green=6)
hat2 = Hat(red=5, orange=4)
hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
```

A hat will always be created with at least one ball, it has a `draw` method that accepts an argument indicating the number of balls to draw from the hat. 

There is also that takes for arguments:
    * `hat`: A hat object containing balls.
    * `expected_balls`: An object indicating the exact group of balls to attempt to draw from the hat for the experiment. For example, to determine the probability of drawing 2 blue balls and 1 red ball from the hat, set `expected_balls` to `{"blue":2, "red":1}`.
    * `num_balls_drawn`: The number of balls to draw out of the hat in each experiment.
    * `num_experiments`: The number of experiments to perform. (The higher it is, the better the approximation is.)

and returns a probability. 

Here is an example of an experiment:

```
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat, 
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)
```
