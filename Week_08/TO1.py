from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt


# ==========================================================
# CONSTANT ORACLE
# f(x) = 0
# ==========================================================

def constant_oracle(n):

    oracle = QuantumCircuit(n + 1)

    # Constant function f(x) = 0
    # No X or CNOT gates are required.

    return oracle


# ==========================================================
# DEUTSCH-JOZSA ALGORITHM
# ==========================================================

def deutsch_jozsa(n):

    # n input qubits + 1 output qubit
    qc = QuantumCircuit(n + 1, n)

    # ------------------------------------------------------
    # Step 1: Prepare output qubit in |1>
    # ------------------------------------------------------

    qc.x(n)

    # ------------------------------------------------------
    # Step 2: Apply Hadamard to all qubits
    # ------------------------------------------------------

    for i in range(n + 1):
        qc.h(i)

    # ------------------------------------------------------
    # Step 3: Apply constant oracle
    # ------------------------------------------------------

    oracle = constant_oracle(n)

    qc.compose(
        oracle,
        inplace=True
    )

    # ------------------------------------------------------
    # Step 4: Apply Hadamard to input qubits
    # ------------------------------------------------------

    for i in range(n):
        qc.h(i)

    # ------------------------------------------------------
    # Step 5: Measure input qubits
    # ------------------------------------------------------

    for i in range(n):
        qc.measure(i, i)

    return qc


# ==========================================================
# MAIN PROGRAM
# ==========================================================

n = 3

qc = deutsch_jozsa(n)

print("=" * 60)
print("EASY: CONSTANT FUNCTION FOR 3 INPUT QUBITS")
print("=" * 60)

print("\nQuantum Circuit:\n")
print(qc.draw())


# ==========================================================
# SIMULATION
# ==========================================================

simulator = AerSimulator()

result = simulator.run(
    qc,
    shots=1024
).result()

counts = result.get_counts()

print("\nMeasurement Results:")
print(counts)


# ==========================================================
# VERIFY RESULT
# ==========================================================

if len(counts) == 1 and counts.get("000", 0) == 1024:

    print("\nResult: 000")
    print("The function is CONSTANT.")

else:

    print("\nUnexpected result.")


# ==========================================================
# GRAPH
# ==========================================================

labels = ["000"]
values = [counts.get("000", 0)]

plt.figure(figsize=(6, 5))

plt.bar(labels, values)

plt.xlabel("Measurement Result")
plt.ylabel("Number of Shots")

plt.title(
    "Deutsch–Jozsa: Constant Function f(x)=0"
)

plt.show()