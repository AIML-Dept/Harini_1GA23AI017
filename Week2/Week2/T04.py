from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
import matplotlib.pyplot as plt
import numpy as np

qc = QuantumCircuit(1)

# Create superposition
qc.h(0)

# Random phase error
phase = np.random.uniform(0, np.pi/4)

qc.p(phase, 0)

print(f"Random phase error = {phase:.4f} radians")

state = Statevector.from_instruction(qc)

print(state)

plot_bloch_multivector(state)
plt.show()