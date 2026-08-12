from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

# Create a 3-qubit circuit
qc = QuantumCircuit(3)

# Create GHZ state
qc.h(0)
qc.cx(0, 1)
qc.cx(0, 2)

# Get state
state = Statevector.from_instruction(qc)

# Display circuit
print("3-Qubit GHZ Circuit:")
print(qc.draw())

# Display statevector
print("\nStatevector:")
print(state)

# Run 1024 shots
counts = state.sample_counts(1024)

print("\nMeasurement Results:")
print(counts)