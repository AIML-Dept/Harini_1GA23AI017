from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt


# ---------------------------------------------------
# BALANCED ORACLE: f(x) = x
# ---------------------------------------------------

def balanced_oracle():

    oracle = QuantumCircuit(2)

    # CNOT implements f(x) = x
    oracle.cx(0, 1)

    return oracle


# ---------------------------------------------------
# DEUTSCH ALGORITHM
# ---------------------------------------------------

qc = QuantumCircuit(2, 1)

# Step 1: Prepare second qubit in |1>
qc.x(1)

# Step 2: Apply Hadamard gates
qc.h(0)
qc.h(1)

# Step 3: Apply balanced oracle
qc.compose(balanced_oracle(), inplace=True)

# Step 4: Apply Hadamard to first qubit
qc.h(0)

# Step 5: Measure first qubit
qc.measure(0, 0)


# ---------------------------------------------------
# DISPLAY CIRCUIT
# ---------------------------------------------------

print("Deutsch Algorithm - Balanced Function f(x)=x")

print("\nQuantum Circuit:")
print(qc.draw())


# ---------------------------------------------------
# SIMULATION
# ---------------------------------------------------

simulator = AerSimulator()

result = simulator.run(
    qc,
    shots=1024
).result()

counts = result.get_counts()

print("\nMeasurement Results:")
print(counts)


# ---------------------------------------------------
# DETERMINE FUNCTION TYPE
# ---------------------------------------------------

zero_count = counts.get("0", 0)
one_count = counts.get("1", 0)

if one_count > zero_count:

    print("\nResult: 1")
    print("Function is BALANCED")

else:

    print("\nResult: 0")
    print("Function is CONSTANT")


# ---------------------------------------------------
# GRAPH
# ---------------------------------------------------

labels = ["0", "1"]
values = [zero_count, one_count]

plt.figure(figsize=(7, 5))

plt.bar(labels, values)

plt.xlabel("Measurement Result")
plt.ylabel("Number of Shots")

plt.title("Deutsch Algorithm - Balanced Function f(x)=x")

plt.show()