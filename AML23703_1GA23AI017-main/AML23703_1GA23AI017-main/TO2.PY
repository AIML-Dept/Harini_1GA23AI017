from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Create 1 qubit circuit with 1 classical bit
qc = QuantumCircuit(1, 1)

# Apply Hadamard gate
qc.h(0)

# Measure qubit
qc.measure(0, 0)

print("Quantum Circuit:")
print(qc)

# Select simulator
backend = Aer.get_backend("aer_simulator")

# Compile circuit
compiled_circuit = transpile(qc, backend)

# Execute 1024 shots
job = backend.run(compiled_circuit, shots=1024)

# Get result
result = job.result()

# Get measurement counts
counts = result.get_counts()

print("\nMeasurement Results:")
print(counts)

# Plot histogram
plot_histogram(counts)

plt.show()
