import matplotlib.pyplot as plt
import pypsa

plt.rc("figure", figsize=(8,8))

network = pypsa.examples.ac_dc_meshed(from_master=True)

# Current type (AC or DC) of the lines from the buses
lines_current_type = network.lines.bus0.map(network.buses.carrier)

network.plot(
    line_colors=lines_current_type.map(lambda ct: "r" if ct == "DC" else "b"),
    title="Mixed AC (blue) - DC (red) network - DC (cyan)",
    color_geomap=True,
    jitter=0.3,
)
plt.tight_layout()