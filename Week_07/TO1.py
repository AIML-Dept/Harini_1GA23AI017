from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt


# ---------------------------------------------------
# CONSTANT ORACLE: f(x) = 0
# ---------------------------------------------------

def constant_oracle():
    oracle = QuantumCircuit(2)

    # f(x) = 0
    # No gate is required because output is always 0.

    return oracle


# ---------------------------------------------------
# DEUTSCH ALGORITHM
# ---------------------------------------------------

qc = QuantumCircuit(2, 1)

# Step 1: Put second qubit into |1>
qc.x(1)

# Step 2: Apply Hadamard gates
qc.h(0)
qc.h(1)

# Step 3: Apply constant oracle
qc.compose(constant_oracle(), inplace=True)

# Step 4: Apply Hadamard to first qubit
qc.h(0)

# Step 5: Measure first qubit
qc.measure(0, 0)


# ---------------------------------------------------
# DISPLAY CIRCUIT
# ---------------------------------------------------

print("Deutsch Algorithm - Constant Function f(x)=0")
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

if zero_count > one_count:
    print("\nResult: 0")
    print("Function is CONSTANT")
else:
    print("\nResult: 1")
    print("Function is BALANCED")


# ---------------------------------------------------
# GRAPH
# ---------------------------------------------------

labels = ["0", "1"]
values = [zero_count, one_count]

plt.figure(figsize=(7, 5))

plt.bar(labels, values)

plt.xlabel("Measurement Result")
plt.ylabel("Number of Shots")
plt.title("Deutsch Algorithm - Constant Function f(x)=0")

plt.show()