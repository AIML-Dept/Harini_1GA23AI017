from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt


# ==========================================================
# CONSTANT ORACLE
# ==========================================================

def constant_oracle(n):

    oracle = QuantumCircuit(n + 1)

    # f(x) = 0
    # No gates required.

    return oracle


# ==========================================================
# BALANCED PARITY ORACLE
# ==========================================================

def balanced_oracle(n):

    oracle = QuantumCircuit(n + 1)

    # f(x1,x2,...,xn) = x1 XOR x2 XOR ... XOR xn

    for i in range(n):
        oracle.cx(i, n)

    return oracle


# ==========================================================
# DEUTSCH-JOZSA ALGORITHM
# ==========================================================

def deutsch_jozsa(n, function_type):

    qc = QuantumCircuit(n + 1, n)

    # ------------------------------------------------------
    # Output qubit |1>
    # ------------------------------------------------------

    qc.x(n)

    # ------------------------------------------------------
    # Hadamard on all qubits
    # ------------------------------------------------------

    for i in range(n + 1):
        qc.h(i)

    # ------------------------------------------------------
    # Select oracle
    # ------------------------------------------------------

    if function_type == "constant":

        oracle = constant_oracle(n)

    elif function_type == "balanced":

        oracle = balanced_oracle(n)

    else:

        raise ValueError(
            "Invalid function type"
        )

    qc.compose(
        oracle,
        inplace=True
    )

    # ------------------------------------------------------
    # Final Hadamard on input qubits
    # ------------------------------------------------------

    for i in range(n):
        qc.h(i)

    # ------------------------------------------------------
    # Measurement
    # ------------------------------------------------------

    for i in range(n):
        qc.measure(i, i)

    return qc


# ==========================================================
# RUN SIMULATION
# ==========================================================

def run_test(n, function_type):

    qc = deutsch_jozsa(
        n,
        function_type
    )

    simulator = AerSimulator()

    result = simulator.run(
        qc,
        shots=1024
    ).result()

    counts = result.get_counts()

    # ------------------------------------------------------
    # Deutsch-Jozsa decision
    # ------------------------------------------------------

    if counts.get("0" * n, 0) == 1024:

        classification = "CONSTANT"

    else:

        classification = "BALANCED"

    return counts, classification


# ==========================================================
# MAIN PROGRAM
# ==========================================================

print("=" * 70)
print("HARD: GENERAL DEUTSCH–JOZSA ALGORITHM")
print("=" * 70)


n_values = [2, 3, 4, 5]

constant_results = []
balanced_results = []


for n in n_values:

    print("\n" + "-" * 60)

    print(f"Number of input qubits: n = {n}")

    # ------------------------------------------------------
    # Constant function
    # ------------------------------------------------------

    constant_counts, constant_class = run_test(
        n,
        "constant"
    )

    print("\nConstant Oracle:")
    print(constant_counts)

    print(
        "Classification:",
        constant_class
    )

    # ------------------------------------------------------
    # Balanced function
    # ------------------------------------------------------

    balanced_counts, balanced_class = run_test(
        n,
        "balanced"
    )

    print("\nBalanced Oracle:")
    print(balanced_counts)

    print(
        "Classification:",
        balanced_class
    )

    # ------------------------------------------------------
    # Store result
    # ------------------------------------------------------

    constant_results.append(
        0 if constant_class == "CONSTANT" else 1
    )

    balanced_results.append(
        0 if balanced_class == "CONSTANT" else 1
    )


# ==========================================================
# GRAPH
# ==========================================================

x_labels = [
    "n=2",
    "n=3",
    "n=4",
    "n=5"
]

plt.figure(figsize=(9, 6))

x = range(len(x_labels))

width = 0.35

plt.bar(
    [i - width / 2 for i in x],
    constant_results,
    width=width,
    label="Constant"
)

plt.bar(
    [i + width / 2 for i in x],
    balanced_results,
    width=width,
    label="Balanced"
)

plt.xlabel("Number of Input Qubits")

plt.ylabel(
    "Deutsch–Jozsa Output"
)

plt.title(
    "Generalised Deutsch–Jozsa Algorithm"
)

plt.xticks(
    x,
    x_labels
)

plt.yticks(
    [0, 1],
    ["Constant", "Balanced"]
)

plt.legend()

plt.show()