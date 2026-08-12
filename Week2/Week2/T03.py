from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

qc = QuantumCircuit(2)

# Apply Hadamard to both qubits
qc.h(0)
qc.h(1)

print(qc)

state = Statevector.from_instruction(qc)

print("Statevector:")
print(state)

# Probability check
probabilities = state.probabilities()

print("\nProbabilities:")
for i, p in enumerate(probabilities):
    print(f"|{i:02b}> : {p:.3f}")

print("\nSum =", sum(probabilities))