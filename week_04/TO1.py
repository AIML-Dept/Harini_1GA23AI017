from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

# Create a 2-qubit circuit
qc = QuantumCircuit(2)

# Set control qubit to |1>
qc.x(0)

# Apply CNOT gate
qc.cx(0, 1)

# Get final state
state = Statevector.from_instruction(qc)

# Display circuit
print("CNOT Circuit:")
print(qc.draw())

# Display final state
print("\nFinal State:")
print(state)

# Display probabilities
print("\nProbabilities:")
print(state.probabilities_dict())