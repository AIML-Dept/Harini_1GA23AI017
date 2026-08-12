from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

# Create a 2-qubit circuit
qc = QuantumCircuit(2)

# Create Bell state
qc.h(0)
qc.cx(0, 1)

# Get state
state = Statevector.from_instruction(qc)

# Display circuit
print("Bell State Circuit:")
print(qc.draw())

# Display state
print("\nStatevector:")
print(state)

# Run 1024 shots
counts = state.sample_counts(1024)

print("\nMeasurement Results:")
print(counts)