import math
import numpy as np
import matplotlib.pyplot as plt


def taylor_ln(x, n):
    """Polinomio de Taylor de grado n de ln(x) alrededor de x0 = 1."""
    suma = 0
    for k in range(1, n + 1):
        suma = suma + (-1)**(k + 1) * (x - 1)**k / k
    return suma


print("P3(1.5):", f"{taylor_ln(1.5, 3):.6f}")
print("P10(1.5):", f"{taylor_ln(1.5, 10):.6f}")
print("P10(2.5):", f"{taylor_ln(2.5, 10):.6f}")

for n in range(1, 31):
    error = abs(math.log(1.5) - taylor_ln(1.5, n))
    if error < 1e-6:
        print("Menor grado con error < 1e-6:", n)
        break

# Grafica 1
x = np.linspace(0.1, 3, 400)
plt.figure(figsize=(10, 6))
plt.plot(x, np.log(x), label="ln(x)", linewidth=2.5)
for n in [1, 2, 3, 6]:
    plt.plot(x, taylor_ln(x, n), label=f"P{n}(x)")
plt.scatter([1], [0], color="black", zorder=5, label="(1, 0)")
plt.ylim(-3, 2)
plt.xlabel("x")
plt.ylabel("Valor de la funcion")
plt.title("Grafica 1: ln(x) y polinomios de Taylor alrededor de x0 = 1")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig("grafica_1.png", dpi=180)
plt.close()

# Grafica 2
n_values = np.arange(1, 31)
error_15 = [abs(math.log(1.5) - taylor_ln(1.5, int(n))) for n in n_values]
error_25 = [abs(math.log(2.5) - taylor_ln(2.5, int(n))) for n in n_values]
cota_15 = [0.5**(int(n) + 1) / (int(n) + 1) for n in n_values]
plt.figure(figsize=(10, 6))
plt.semilogy(n_values, error_15, marker="o", markersize=3, label="Error en x = 1.5")
plt.semilogy(n_values, error_25, marker="s", markersize=3, label="Error en x = 2.5")
plt.semilogy(n_values, cota_15, linestyle="--", label="Cota del error en x = 1.5")
plt.xlabel("Grado n")
plt.ylabel("Error absoluto (escala logaritmica)")
plt.title("Grafica 2: Error de Taylor de ln(x), grados 1 a 30")
plt.grid(True, which="both", alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig("grafica_2.png", dpi=180)
plt.close()
