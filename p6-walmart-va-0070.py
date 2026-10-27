import matplotlib.pyplot as plt
import numpy as np
# Axel Guzman NC 0070

cant_productos=[100,150,200,300,500]
precio = [4000, 7000, 9000, 12000, 18000]

plt.plot(cant_productos,precio)
plt.show()
# personalizar graficas
plt.figure()
plt.plot(cant_productos,precio,color="green",marker="o",linestyle="dashed",linewidth=2,markersize=12)
plt.title("ventas de walmart")
plt.xlabel("cant prod")
plt.ylabel("precio")
plt.show()
