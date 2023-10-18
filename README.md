# Boarding simulator
This boarding simulator allows you to respond de question: what is the most efficient boarding strategy? By comparing 4 different methods:
- Back to Front (BTF)
- Random 
- Window Middle Aisle (WILMA)
- Alternated Window Middle Aisle 

![Boarding Strategies](/media/BoardingStrategies.jpg)


Also creates a GIF using python's library Matplotlib.

# How to use
Clone the repository and execute the main.py file, then write the boarding method you want to check and the number of executions you want to perform.
Note: animation will only be created if you execute 1 time.

# Files 
### Aeronave.py 
Collects aircraft characteristics such as the number of rows and columns, and the number of passengers contains the data structures required for the simulation.
### AsignaAsiento.py
This file contains the method that generates the seat distribution according to the strategy.
### Embarque.py
In this file the simulation is developed, it represents the boarding time and the handling of the entities and resources.
### Main.py
is the master file, orchestrates the execution of the simulation and interacts with the user.


# More info
project developed for the subject Design of Simulation Models studied at the University of Jaén as part of the degree in computer engineering.


# Contact 
If you have questions about any of the solution presented or wish to discuss, please do not hesitate to contact me through the following means:
- Email: fjmv28012000@gmail.com
- LindkedIn: linkedin.com/in/javier-merelo-vacas
