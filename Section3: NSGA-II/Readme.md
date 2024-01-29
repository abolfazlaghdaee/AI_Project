## NSGA-II (Non-dominated Sorting Genetic Algorithm II)

![x2mate com-NSGAIIParetoFrontMulti-objectiveOptimization WDSystemRehabilitationPlanning -480p-ezgif com-video-to-gif-converter](https://github.com/abolfazlaghdaee/AI_Project/assets/69028985/cb160b28-fff3-4145-b66f-fcf6816dc5b5)


## How to Run: 
after inserting the whole files in your local machine type the following command in your terminal:

```bash
python3 NSGA-II.py
```

### overview of NSGA-II:
---

- **Fast Non-Dominated Sorting**
- **Crowding Distance**:

- **Selection**

- **Crossover and Mutation**

### this is my approach for NSGA-II:

1- initialize a population of candidate solutions.

2- valuate the population based on the objective functions.

3- perform non-dominated sorting to identify the Pareto fronts.

4- assign a crowding distance to individuals to maintain diversity.

5- generate new offspring through selection, crossover, and mutation.

6- combine the offspring with the parent population.

7- repeat steps 2-6 for multiple generations.

8- select the final set of solutions from the last Pareto front as the optimal solutions.


