from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

# Create a 5-qubit circuit
qc = QuantumCircuit(5)

# Input:
# A = 1
# B = 1
# Cin = 0

qc.x(0)
qc.x(1)

# -------------------------
# SUM = A XOR B XOR Cin
# -------------------------

qc.cx(0, 3)
qc.cx(1, 3)
qc.cx(2, 3)

# -------------------------
# CARRY = AB XOR ACin XOR BCin
# -------------------------

qc.ccx(0, 1, 4)
qc.ccx(0, 2, 4)
qc.ccx(1, 2, 4)

# Get final state
state = Statevector.from_instruction(qc)

# Display circuit
print("Full Adder Circuit:")
print(qc.draw())

# Display final state
print("\nFinal State:")
print(state)

# Display probabilities
print("\nProbabilities:")
print(state.probabilities_dict())