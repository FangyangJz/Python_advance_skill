Using MAP to improve convergence
If you ran the above example yourself, you may have noticed that our results were not consistent: perhaps your cluster division was more scattered, or perhaps less scattered. The problem is that our traces are a function of the starting values of the MCMC algorithm.

It can be mathematically shown that letting the MCMC run long enough, by performing many steps, the algorithm should forget its initial position. In fact, this is what it means to say the MCMC converged (in practice though we can never achieve total convergence). Hence if we observe different posterior analysis, it is likely because our MCMC has not fully converged yet, and we should not use samples from it yet (we should use a larger burn-in period ).

In fact, poor starting values can prevent any convergence, or significantly slow it down. Ideally, we would like to have the chain start at the peak of our landscape, as this is exactly where the posterior distributions exist. Hence, if we started at the "peak", we could avoid a lengthy burn-in period and incorrect inference. Generally, we call this "peak" the maximum a posterior or, more simply, the MAP.

Of course, we do not know where the MAP is. PyMC3 provides a function that will approximate, if not find, the MAP location. In the PyMC3 main namespace is the find_MAP function. If you call this function within the context of Model(), it will calculate the MAP which you can then pass to pm.sample() as a start parameter.

start = pm.find_MAP()
trace = pm.sample(2000, step=pm.Metropolis, start=start)
The find_MAP() function has the flexibility of allowing the user to choose which optimization algorithm to use (after all, this is a optimization problem: we are looking for the values that maximize our landscape), as not all optimization algorithms are created equal. The default optimization algorithm in function call is the Broyden-Fletcher-Goldfarb-Shanno (BFGS) algorithm to find the maximum of the log-posterior. As an alternative, you can use other optimization algorithms from the scipy.optimize module. For example, you can use Powell's Method, a favourite of PyMC blogger Abraham Flaxman 1, by calling find_MAP(fmin=scipy.optimize.fmin_powell). The default works well enough, but if convergence is slow or not guaranteed, feel free to experiment with Powell's method or the other algorithms available.

The MAP can also be used as a solution to the inference problem, as mathematically it is the most likely value for the unknowns. But as mentioned earlier in this chapter, this location ignores the uncertainty and doesn't return a distribution.

Speaking of the burn-in period
It is still a good idea to decide on a burn-in period, even if we are using find_MAP() prior to sampling, just to be safe. We can no longer automatically discard sample with a burn parameter in the sample() function as we could in PyMC2, but it is easy enough to simply discard the beginning section of the trace just through array slicing. As one does not know when the chain has fully converged, a good rule of thumb is to discard the first half of your samples, sometimes up to 90% of the samples for longer runs. To continue the clustering example from above, the new code would look something like:

with pm.Model() as model:
    start = pm.find_MAP()
    
    step = pm.Metropolis()
    trace = pm.sample(100000, step=step, start=start)

burned_trace = trace[50000:]
