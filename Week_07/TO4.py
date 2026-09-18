from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt


# ===================================================
# CLASSIFICATION ORACLE
# ===================================================

def classification_oracle():

    oracle = QuantumCircuit(2)

    # CNOT represents a binary classification rule
    oracle.cx(0, 1)

    return oracle


# ===================================================
# QUANTUM CLASSIFICATION CIRCUIT
# ===================================================

qc = QuantumCircuit(2, 1)


# ---------------------------------------------------
# STEP 1: Prepare input qubit
# ---------------------------------------------------

qc.h(0)


# ---------------------------------------------------
# STEP 2: Prepare auxiliary qubit in |1>
# ---------------------------------------------------

qc.x(1)
qc.h(1)


# ---------------------------------------------------
# STEP 3: Apply classification oracle
# ---------------------------------------------------

qc.compose(
    classification_oracle(),
    inplace=True
)


# ---------------------------------------------------
# STEP 4: Apply Hadamard
# ---------------------------------------------------

qc.h(0)


# ---------------------------------------------------
# STEP 5: Measure
# ---------------------------------------------------

qc.measure(0, 0)


# ===================================================
# DISPLAY CIRCUIT
# ===================================================

print("Phase Kickback - Binary Classification")

print("\nQuantum Circuit:")
print(qc.draw())


# ===================================================
# SIMULATION
# ===================================================

simulator = AerSimulator()

result = simulator.run(
    qc,
    shots=1024
).result()

counts = result.get_counts()

print("\nMeasurement Results:")
print(counts)


# ===================================================
# CLASSIFICATION
# ===================================================

zero_count = counts.get("0", 0)
one_count = counts.get("1", 0)

if zero_count > one_count:

    print("\nClassification: CLASS 0")

else:

    print("\nClassification: CLASS 1")


# ===================================================
# MEASUREMENT GRAPH
# ===================================================

labels = ["Class 0", "Class 1"]

values = [
    zero_count,
    one_count
]

plt.figure(figsize=(7, 5))

plt.bar(
    labels,
    values
)

plt.xlabel("Classification")
plt.ylabel("Number of Measurements")

plt.title(
    "Quantum Binary Classification Using Phase Kickback"
)

plt.show()


# ===================================================
# CONCEPTUAL DIAGRAM
# ===================================================

print("\n")
print("CONCEPTUAL PHASE-KICKBACK CLASSIFICATION")
print("=" * 50)

print("""
                INPUT
                  |
                  v
        +-------------------+
        | Quantum Classifier |
        +-------------------+
                  |
          +-------+-------+
          |               |
          v               v
       Class 0          Class 1
          |               |
          v               v
      + Phase          - Phase
          \\               /
           \\             /
            v           v
              INTERFERENCE
                   |
                   v
              MEASUREMENT
                   |
                   v
             FINAL DECISION
""")