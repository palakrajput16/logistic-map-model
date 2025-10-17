# logistic-map-model
Population dynamics simulation using the logistic map model in Python

Overview
The Logistic Map Model provides a revealing insight into the dynamics of populations over time in environments that are limited by resources. The logistic model is different from the exponential models of growth that refer to an assumption of growth using unlimited resources, by incorporating the key notion of carrying capacity-the maximum population density to which the environment can support economically. 
Modeling Workflow
1. Problem Definition
The logistic map model addresses the fundamental ecological question: What do populations do when resources are not sufficient for their survival? Although exponential growth might describe population dynamics in a resource-rich environment on short timescales, actual populations are never in such environments. The logistic equation reflects this fact by adding a self-limiting term.
This model is especially useful for:
Looking at how various growth rates affect population paths
The recognition of transition points between stable, oscillatory, and chaotic population behaviors
The prediction of long-term population equilibrium states in resource-limited systems
The examination of the interaction between reproduction rates and environmental carrying capacity
2. Model Formulation
The discrete logistic map equation is given as:
Pt+1 = rPt [1- (Pt / K)]
where
Pt: Population size at time t
Pt+1: Population size during the next time step (t+1)
r: Intrinsic rate of growth—maximum rate of per-capita reproduction under optimal conditions
K: Carrying capacity—the highest sustainable population size in the presence of environmental limits
P0: Starting population size that initiates the growth process
For this particular exercise in modeling, the following parameter values were chosen:
Carrying capacity (K) = 1000 individuals
Initial population (P0) = 30 individuals
Duration of time (T) = 10 time units
Growth rates studied (r) = 1.5, 2.5, 3.2, and 3.51
The factor [1- (Pt / K)] in the formula serves as a density-dependent regulator. As the population reaches the carrying capacity, this measure diminishes, thereby lessening the growth rate of the population. This mathematical expression conveys the biological fact that resources grow scarcer with rising population density.
3. Implementation
The numerical computation of the model was done using Python in a systematic sequence:
Parameter initialization: Initializing the model with given parameters for K, P0, and T.


Iterative computation: Computing the next value of the population for each time step based on the discrete logistic equation.


Comparative analysis: Parallel simulations are conducted with various growth rates (r=1.5, 2.5, 3.2, 3.51) to see how the populations respond differently.


Visualization: Creating time-series plots of population size against time for each growth rate scenario.


Reference visualization: Adding a horizontal line indicating the carrying capacity (K=1000) to give context for how populations behave in relation to this ecological limit.


Sensitivity analysis: Further tests were run with different initial population sizes to explore how initial conditions affect long-term dynamics.


4. Simulation
The simulation output indicated characteristic population growth patterns in response to various growth rate parameters:
Moderate Growth Rate (r=1.5):
The population showed steady monotonic growth but remained well below carrying capacity within the timeframe
By t=10, the population only reached about 300 individuals (30% of K)
Growth followed a gradual curve with no signs of oscillation
Moderate-High Growth Rate (r=2.5):
The population grew more rapidly than at r=1.5
It stabilized at approximately 600 individuals (60% of carrying capacity) rather than reaching K
No oscillations were observed within the timeframe
High Growth Rate (r=3.2):
The population exhibited oscillatory behavior
Population showed fluctuations between approximately 550 and 790 individuals
The oscillations appeared to be gradually increasing in amplitude over time
The population never stabilized at carrying capacity
Very High Growth Rate (r=3.51):
The population demonstrated chaotic dynamics
Unpredictable fluctuations occurred with no discernible pattern
Population sizes varied dramatically between time steps (from around 380 to 880)
The system never reached a stable equilibrium or regular periodic behavior
Note on Initial Population:
All simulations began with the same initial population of P0=30
Additional theoretical analysis suggests that higher initial populations (P0 > 600) would show different dynamics, but this was not included in the current graph
5. Analysis
Evidence from simulation provides insight into some important aspects of population dynamics in limiting environments:
Bifurcation Phenomenon: Stable to chaotic dynamics transition with increasing growth rate is a sequence of bifurcations. For low values of r, the system has one stable equilibrium point. On increasing r above some critical value, bifurcation occurs with the doubling of the period, whereby the system oscillates between two values. On further increase of r, more bifurcations occur until at values like r = 3.51.
Sensitivity to Initial Conditions: The logistic model depicts the characteristic of chaotic systems, sensitivity to initial conditions. It displays marked differences in final conditions, even with slight variations in starting populations, particularly when the growth is high. This characteristic has important consequences for ecological prediction and management.
Ecological Implications: These mathematical behaviors translate to phenomena in nature:
Low-reproduction species (low r) have stable populations that may approach carrying capacity over longer timeframes
Moderately high reproductive species might undergo population cycles, like the populations of some rodents or insects
Extremely high reproductive species might have the appearance of their populations fluctuating at random, like some insect pest populations
Resource Utilization Efficiency: The model demonstrates that populations do not always maximize the use of resources. At high rates of growth, competitive impacts and overshooting dynamics can keep populations below carrying capacity, rather than stabilize at the theoretical maximum. This result has broader implications for interpreting ecological efficiency and resource management.
Conclusion
The logistics map  model has become a significant tool for modeling population dynamics under conditions of resource limitation. The present analysis has demonstrated that a growth rate alone may give a parameter such as r the ability to influence population dynamics and cause transformations from stable equilibrium to attractor chaotic behavior.
last point about the logistic is that, in its simplicity, it qualifies the complex dynamic situation into a fairly perilous mathematical structure so that it has become a firm foundation in population ecology for generations.
