import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("final.csv")

mass = df["Mass"].to_list()
radius = df["Radius"].to_list()
gravity = df["Gravity"].to_list()

mass.sort()
radius.sort()
gravity.sort()

plt.plot(mass,radius)
plt.title("Mass vs Radius")
plt.ylabel("Radius")
plt.xlabel("Mass")
plt.show()

plt.plot(mass,gravity)
plt.title("Mass vs Gravity")
plt.ylabel("Gravity")
plt.xlabel("Mass")
plt.show()


