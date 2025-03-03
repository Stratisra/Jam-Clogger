# Jam-Clogger
***Jam Clogger*** is an machine learning-based system designed to efficiently control traffic to reduce traffic congestion.

It operates in a simulated environment, utilizing Q-Learning to navigate various states (tuples that record the number of vehicles waiting at each lane). This environment consists of 2,499,561 distinct states, each corresponding to a unique combination of vehicles waiting at the traffic lights. The agent can choose from 4 base actions, representing different configurations in which traffic lights can turn green for varied durations (2, 4, 6, 8, 10 seconds), thus totaling 20 actions.

![Actions](https://github.com/Stratisra/Jam-Clogger/blob/aa9f5b48e6c8fff455cbc2be519070fa11ec3299/Road/3%20Lanes/All%20Actions.png)

# Training
During training, the agent goes through 400,000,000 episodes structured as follows: a random state is generated, and then, the agent selects the next action based on the Q-values associated with that state. This selection uses the epsilon-greedy algorithm, which controls the probability of exploring new states or exploiting actions that have previously yielded the best results. After performing an action, the agent receives a reward, which is used to update its Q-value via Bellman's Equation. This process continues until no vehicles remain.

The data from the Q-table is then used in the web simulation where the action with the highest Q-value is implemented for each encountered state.

![Simulation](https://github.com/Stratisra/Jam-Clogger/blob/ac99966e8fe5d410a714979a06933d4808dd059c/Final%20Version%20(5.4)/Simulation/Version%202/Static%20simulation/Simulation.png)

### [Video Presentation](https://www.youtube.com/watch?v=Xc8GmtV-Xro) 

# Awards
***Jam Clogger*** was submitted to the World Artificial Intelligence Competition for Youth ([WAICY](https://www.waicy.org/)) in 2022 and received the **Impact Excellence Award** (highest score in problem statement, AI ethics, and presentation & communication).
