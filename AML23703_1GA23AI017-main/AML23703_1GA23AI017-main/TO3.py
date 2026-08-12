from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Create 3 qubit circuit with 3 classical bits
qc = QuantumCircuit(3, 3)

# Apply Hadamard gates to create superposition
qc.h(0)
qc.h(1)
qc.h(2)

# Measure all qubits
qc.measure([0, 1, 2], [0, 1, 2])

print("Quantum Circuit:")
print(qc)

# Use simulator
backend = Aer.get_backend("aer_simulator")

# Compile circuit
compiled_circuit = transpile(qc, backend)

# Run 8192 shots
job = backend.run(compiled_circuit, shots=8192)

# Get results
result = job.result()

counts = result.get_counts()

print("\nMeasurement Counts:")
print(counts)

print("\nProbability Distribution:")

for state in sorted(counts):
    probability = counts[state] / 8192
    print(state, ":", round(probability, 3))

# Plot histogram
plot_histogram(counts)

plt.show()
