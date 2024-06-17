import pypsa
import numpy as np

network = pypsa.Network()

# Building buses
n_buses = 3

for i in range(n_buses):
    network.add("Bus", "My bus {}".format(i), v_nom=20.)

## Buidling lines, generators and loads
# Add 3 lines in a ring
for i in range(n_buses):
    network.add("Line", "My line {}".format(i),
                bus0 = "My bus {}".format(i),
                bus1 = "My bus {}".format((i+1)%3),
                x=0.1,
                r=0.01)

# Add a generator at bus 0
network.add("Generator", "My gen",
            bus="My bus 0",
            p_set=100,
            control="PQ")

# Add a load at bus 1
network.add("Load", "My load",
            bus="My bus 1",
            p_set=100,
            q_set=100)

# Newton Raphson Power Flow
network.pf()

# Active power flow on the lines
network.lines_t.p0

# Voltage angle on buses
network.buses_t.v_ang * 180/ np.pi

# Voltage magnitudes
network.buses_t.v_mag_pu