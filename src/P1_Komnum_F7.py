import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def bolzano_method(f, a, b, tol):
    if f(a) * f(b) >= 0:
        raise ValueError("Fungsi harus memiliki tanda yang berbeda pada a dan b.")
    
    iterasi = []
    c = a
    iter_count = 0
    while (b - a) / 2.0 > tol:
        c = (a + b) / 2.0
        iterasi.append([iter_count + 1, a, b, c, f(a), f(b), f(c)])
        iter_count += 1
        if f(c) == 0:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    
    # Create a DataFrame to display the iterations in a table
    df_iterasi = pd.DataFrame(iterasi, columns=["Iterasi", "a", "b", "c", "f(a)", "f(b)", "f(c)"])
    return c, df_iterasi

def plot_bolzano(f, a, b, tol, df_iterasi):
    x = np.linspace(a - 1, b + 1, 400)
    y = f(x)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label='f(x)')
    plt.axhline(0, color='black', linewidth=0.5)
    
    for _, row in df_iterasi.iterrows():
        a_i, b_i, c_i, f_a, f_b, f_c = row[1], row[2], row[3], row[4], row[5], row[6]
        plt.plot([a_i, b_i], [f_a, f_b], 'ro-')
        plt.plot(c_i, f_c, 'bo')
    
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Proses Iteratif Metode Bolzano')
    plt.legend()
    plt.grid(True)
    plt.show()

# Fungsi contoh: f(x) = x^2 - 4
def f(x):
    return x**3 + x**2 - 3*x - 3

# Parameter
a = 1
b = 2
tol = 1e-3
# Menjalankan metode Bolzano
try:
    akar, df_iterasi = bolzano_method(f, a, b, tol)
    print(f"Akar ditemukan: {akar}")
    print(df_iterasi)
    # Plotting the iterative process
    plot_bolzano(f, a, b, tol, df_iterasi)
except ValueError as e:
    print(e)

# save table to csv
df_iterasi.to_csv("output_iterasi.csv", index=False)