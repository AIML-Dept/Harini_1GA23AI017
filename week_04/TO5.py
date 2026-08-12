from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
import numpy as np

# Create a 2-qubit circuit
qc = QuantumCircuit(2)

# Create arbitrary entangled state
qc.ry(np.pi / 3, 0)
qc.cx(0, 1)

# Get statevector
state = Statevector.from_instruction(qc)

# Display circuit
print("Arbitrary Entangled State Circuit:")
print(qc.draw())

# Display statevector
print("\nStatevector:")
print(state)

# Display probabilities
print("\nProbabilities:")
print(state.probabilities_dict())

# Run 1024 shots
counts = state.sample_counts(1024)

print("\nMeasurement Results:")
print(counts)