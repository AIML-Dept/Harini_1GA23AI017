import matplotlib.pyplot as plt


# ==========================================================
# INPUT VALUES
# ==========================================================

n_values = list(range(2, 11))


# ==========================================================
# CLASSICAL WORST-CASE QUERY COUNT
# ==========================================================

classical_queries = []

for n in n_values:

    queries = (2 ** (n - 1)) + 1

    classical_queries.append(
        queries
    )


# ==========================================================
# QUANTUM QUERY COUNT
# ==========================================================

quantum_queries = [
    1 for n in n_values
]


# ==========================================================
# PRINT TABLE
# ==========================================================

print("=" * 60)
print("CLASSICAL VS QUANTUM QUERY COMPLEXITY")
print("=" * 60)

print(
    f"{'n':<10}"
    f"{'Classical':<15}"
    f"{'Quantum':<10}"
)

print("-" * 35)


for n, classical, quantum in zip(
    n_values,
    classical_queries,
    quantum_queries
):

    print(
        f"{n:<10}"
        f"{classical:<15}"
        f"{quantum:<10}"
    )


# ==========================================================
# GRAPH 1 — LINEAR SCALE
# ==========================================================

plt.figure(figsize=(9, 6))

plt.plot(
    n_values,
    classical_queries,
    marker="o",
    label="Classical worst case"
)

plt.plot(
    n_values,
    quantum_queries,
    marker="o",
    label="Quantum"
)

plt.xlabel(
    "Number of Input Bits (n)"
)

plt.ylabel(
    "Number of Oracle Queries"
)

plt.title(
    "Classical vs Quantum Query Count"
)

plt.xticks(n_values)

plt.legend()

plt.grid(
    True,
    alpha=0.3
)

plt.show()


# ==========================================================
# GRAPH 2 — LOG SCALE
# ==========================================================

plt.figure(figsize=(9, 6))

plt.plot(
    n_values,
    classical_queries,
    marker="o",
    label="Classical worst case"
)

plt.plot(
    n_values,
    quantum_queries,
    marker="o",
    label="Quantum"
)

plt.xlabel(
    "Number of Input Bits (n)"
)

plt.ylabel(
    "Number of Oracle Queries"
)

plt.title(
    "Exponential Query Gap: Log Scale"
)

plt.xticks(n_values)

plt.yscale("log")

plt.legend()

plt.grid(
    True,
    alpha=0.3
)

plt.show()