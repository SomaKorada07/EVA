# TD3 Implementation on Custom Environment

## Goal

To make a car learn to drive on the roads of a map (custom environment) using **TD3** architecture.

###  Video - https://youtu.be/NN52iN3ZEhU

## Approach taken

### Following were done even before implementing Assignment 10

1. Understood the TD3 architecture and the way to implement it for the environments - AntBulletEnv-v0, Walker2DBulletEnv-v0 and HalfCheetahBulletEnv-v0.

2. Printed the different environment variables like Action Space, Observation Space - their low, high and sample values.

   print(env.observation_space.high) - [inf inf inf inf inf inf inf inf inf inf inf inf inf inf inf inf inf inf inf inf inf inf]

   print(env.observation_space.low) - [-inf -inf -inf -inf -inf -inf -inf -inf -inf -inf -inf -inf -inf -inf -inf -inf -inf -inf -inf -inf -inf -inf]

   print(env.action_space.high) - [1. 1. 1. 1. 1. 1.]

   print(env.action_space.low) - [-1. -1. -1. -1. -1. -1.]

   env.env.action_space.sample() - array([-0.58517057, -0.5024034 , -0.6100568 , -0.88058037, -0.14023775,       -0.7811404 ], dtype=float32)

   env.observation_space.sample() - array([ 0.2560038 ,  1.2759786 ,  0.5100617 ,  0.6512928 ,  1.6200854 ,       -0.28926647,  0.06890053, -1.6094683 , -0.9811666 ,  0.12742993,        1.3960222 , -0.04613981, -0.8242046 , -1.4867542 ,  0.11702857,       -0.76355684,  0.7695135 ,  0.3610245 ,  1.0636773 , -1.0533894 ,        0.5983344 , -0.1122881 ], dtype=float32)

3. Explored the available Github of pybullet to understand these variables - https://github.com/bulletphysics/bullet3/blob/ec2b6dd920135a5df804d521727cc06446a6a3bd/examples/pybullet/gym/pybullet_envs/robot_locomotors.py#L103

4. Went through Github of CarRacing-v0 and Atari environments to understand how to implement TD3 when image screenshots of the environment are required.

5. Understood the "step" function of the environment.

### Steps done for Assignment 10

1. ***Keeping the sensors as-is***, changed the DQN architecture to TD3 architecture (without CNN. Similar to "walker" environment) to make it work.
2. After Step 1 was completed, implemented TD3 with a ***cropped image*** as input to Actor network. This cropped image **did not have car image** embedded into it. I made this work first. Parameters in this approach were as below:
   1. Input to Actor - Cropped Image
   2. State - Cropped image of size 80x80 but reduced to 32x32 for the CNN.
   3. Replay Buffer
      1. State (cropped image without car)
      2. Next State (cropped image from sand image with the car's new position based on the action taken)
      3. Reward for the action taken based on the "Distance"
      4. Action taken
      5. Done (defined it to True when the car hit the walls or when it reached target or when the episode was completed)
3. After Step 2 was completed, improvised the image by ***embedding the car*** into it taking its angle into consideration, but the image of the car was surrounded by a rectangle around it! Still went ahead with the same Replay Buffer and same parameters. Modified parameters were as below:
   1.  Input to Actor - Cropped Image along with car considering its angle
   2. State - Cropped image of size 160x160 map along with car considering its angle but reduced to 32x32 for the CNN.
   3. Replay Buffer
      1. State (cropped image without car)
      2. Next State (cropped image from sand image with the car's new position based on the action taken)
      3. Reward for the action taken based on the "Distance"
      4. Action taken
      5. Done (defined it to True when the car hit the walls or when it reached target or when the episode was completed)
4. ***Added* "*Distance*"** parameter as an additional attribute to Actor network. Modified parameters were as below:
   1. Input to Actor - Distance and Cropped Image along with car considering its angle
   2. State - Cropped image of size 160x160 map along with car considering its angle but reduced to 32x32 for the CNN.
   3. Replay Buffer
      1. State (cropped image without car)
      2. Next State (cropped image from sand image with the car's new position based on the action taken)
      3. Distance
      4. Next Distance (based on the car's new position based on the action taken)
      5. Reward for the action taken based on the "Distance"
      6. Action taken
      7. Done (defined it to True when the car hit the walls or when it reached target or when the episode was completed)
5. **Removed car image** from the cropped image of sand as I was not satisfied with the way it was done. ***Added "Orientation"*** parameter as an additional attribute to Actor network. Modified parameters are as below:
   1. Input to Actor - Distance, Orientation and Cropped Image **without** car image embedded
   2. State - Cropped image of size 160x160 map but reduced to 32x32 for the CNN.
   3. Replay Buffer
      1. State (cropped image without car)
      2. Next State (cropped image from sand image with the car's new position based on the action taken)
      3. Distance
      4. Next Distance (based on the car's new position based on the action taken)
      5. Orientation
      6. Next Orientation (based on the car's new position based on the action taken)
      7. Reward for the action taken based on the "Distance"
      8. Action taken
      9. Done (defined it to True when the car hit the walls or when it reached target or when the episode was completed)
6. Improvised the ***Rewards strategy***. As I observed that when car gets stuck at the walls, it was not able to come out of that state, I am using high negative rewards in this case. As car mostly goes on sand and less on roads, I have made positive reward for going on road to be higher than the negative reward for going on sand. Also, ending the episode and giving penalty when the car stays on sand for certain number of timesteps continuously.
7. Also, to avoid the car from going to boundary, I am resetting the car position in such a case and giving high negative rewards (same as boundary case rewards). I did not implement any padding to sand image.
8. Every time Done becomes true, I am ***resetting the car's position randomly***.
9. Saving the models when it is Done (=True) and when Episode reward is positive.
10. Implemented the inferencing using best positive episode reward models.

### Things tried

1. Tried using 3 states - Cropped Image rotated with car's angle, [+Orientation, -Orientation] and Distance. But using all the 3 states only resulted in my car going all over the map. It was not traversing between the targets too.
2. Tried using only 2 states - Cropped Image rotated with car's angle and [+Orientation, -Orientation]. This resulted in car learning to traverse between the 2 targets. It could not learn to stay on road.
3. Tuned Learning Rate hyperparameter to get out of rotation issue.