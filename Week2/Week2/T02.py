from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
import matplotlib.pyplot as plt

qc = QuantumCircuit(1)

# Hadamard gate
qc.h(0)

# Phase (S) gate
qc.s(0)

print(qc)

state = Statevector.from_instruction(qc)

print("Statevector:")
print(state)

plot_bloch_multivector(state)
plt.show()