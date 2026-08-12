from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
import matplotlib.pyplot as plt

# Create one-qubit circuit
qc = QuantumCircuit(1)

# Apply X gate
qc.x(0)

print(qc)

# Get statevector
state = Statevector.from_instruction(qc)

print("Statevector:")
print(state)

# Plot Bloch Sphere
plot_bloch_multivector(state)
plt.show()