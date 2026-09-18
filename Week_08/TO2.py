from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt


# ==========================================================
# BALANCED PARITY ORACLE
# f(x1,x2,x3) = x1 XOR x2 XOR x3
# ==========================================================

def parity_oracle(n):

    oracle = QuantumCircuit(n + 1)

    # Apply CNOT from every input qubit
    # to the output qubit.

    for i in range(n):
        oracle.cx(i, n)

    return oracle


# ==========================================================
# DEUTSCH-JOZSA ALGORITHM
# ==========================================================

def deutsch_jozsa(n):

    qc = QuantumCircuit(n + 1, n)

    # Prepare output qubit |1>
    qc.x(n)

    # Hadamard on all qubits
    for i in range(n + 1):
        qc.h(i)

    # Apply parity oracle
    oracle = parity_oracle(n)

    qc.compose(
        oracle,
        inplace=True
    )

    # Hadamard on input qubits
    for i in range(n):
        qc.h(i)

    # Measure input qubits
    for i in range(n):
        qc.measure(i, i)

    return qc


# ==========================================================
# MAIN
# ==========================================================

n = 3

qc = deutsch_jozsa(n)

print("=" * 60)
print("MEDIUM: BALANCED PARITY FUNCTION")
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
# VERIFY
# ==========================================================

if "000" in counts:

    print("\nOutput contains 000.")

    if counts["000"] == 1024:
        print("This would indicate a constant function.")

    else:
        print("Other non-zero results are present.")

else:

    print("\n000 was not measured.")
    print("Result is NON-ZERO.")
    print("The function is BALANCED.")


# ==========================================================
# GRAPH
# ==========================================================

labels = list(counts.keys())
values = list(counts.values())

plt.figure(figsize=(8, 5))

plt.bar(labels, values)

plt.xlabel("Measurement Result")
plt.ylabel("Number of Shots")

plt.title(
    "Deutsch–Jozsa: Balanced Parity Function"
)

plt.show()