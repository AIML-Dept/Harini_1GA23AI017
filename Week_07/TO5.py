from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt
import numpy as np


# ===================================================
# IMPERFECT HADAMARD
# ===================================================

def imperfect_hadamard(qc, qubit, error):

    # Ideal Hadamard-like rotation
    # Error is added to the rotation angle

    angle = (np.pi / 2) + error

    qc.ry(
        angle,
        qubit
    )


# ===================================================
# BALANCED ORACLE
# ===================================================

def balanced_oracle():

    oracle = QuantumCircuit(2)

    # f(x) = x
    oracle.cx(0, 1)

    return oracle


# ===================================================
# RUN EXPERIMENT
# ===================================================

def run_experiment(error, shots=1000):

    qc = QuantumCircuit(2, 1)

    # ------------------------------------------------
    # Prepare output qubit |1>
    # ------------------------------------------------

    qc.x(1)


    # ------------------------------------------------
    # Imperfect Hadamard
    # ------------------------------------------------

    imperfect_hadamard(
        qc,
        0,
        error
    )

    imperfect_hadamard(
        qc,
        1,
        error
    )


    # ------------------------------------------------
    # Oracle
    # ------------------------------------------------

    qc.compose(
        balanced_oracle(),
        inplace=True
    )


    # ------------------------------------------------
    # Final imperfect Hadamard
    # ------------------------------------------------

    imperfect_hadamard(
        qc,
        0,
        error
    )


    # ------------------------------------------------
    # Measurement
    # ------------------------------------------------

    qc.measure(0, 0)


    # ------------------------------------------------
    # Simulator
    # ------------------------------------------------

    simulator = AerSimulator()

    result = simulator.run(
        qc,
        shots=shots
    ).result()

    counts = result.get_counts()


    # ------------------------------------------------
    # Correct answer is 1
    # ------------------------------------------------

    correct_count = counts.get(
        "1",
        0
    )


    reliability = (
        correct_count / shots
    ) * 100


    return reliability, counts


# ===================================================
# ERROR VALUES
# ===================================================

errors = [
    0.00,
    0.02,
    0.05,
    0.10,
    0.20,
    0.30,
    0.40
]


# ===================================================
# STORE RESULTS
# ===================================================

reliability_values = []


print("IMPERFECT HADAMARD EXPERIMENT")
print("=" * 60)


for error in errors:

    reliability, counts = run_experiment(
        error,
        shots=1000
    )

    reliability_values.append(
        reliability
    )

    print(
        f"Error = {error:.2f} radians"
    )

    print(
        f"Measurement = {counts}"
    )

    print(
        f"Reliability = {reliability:.2f}%"
    )

    print("-" * 60)


# ===================================================
# BAR CHART
# ===================================================

labels = [
    f"{error:.2f}"
    for error in errors
]


plt.figure(figsize=(10, 6))

plt.bar(
    labels,
    reliability_values
)

plt.xlabel(
    "Hadamard Gate Error (radians)"
)

plt.ylabel(
    "Correct Measurement Reliability (%)"
)

plt.title(
    "Effect of Imperfect Hadamard Gate on Reliability"
)

plt.ylim(
    0,
    105
)

plt.grid(
    axis="y",
    alpha=0.3
)

plt.show()


# ===================================================
# CONCLUSION
# ===================================================

print("\nCONCLUSION")
print("=" * 60)

print(
    "The experiment shows the effect of gate imperfections "
    "on the Deutsch algorithm."
)

print(
    "As the Hadamard gate error increases, the quantum "
    "interference is disturbed and measurement reliability "
    "can decrease."
)