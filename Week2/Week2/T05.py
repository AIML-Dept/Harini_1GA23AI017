from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
import matplotlib.pyplot as plt
import numpy as np

def create_state(theta, phi):
    qc = QuantumCircuit(1)

    # Rotation around Y-axis
    qc.ry(theta, 0)

    # Rotation around Z-axis
    qc.rz(phi, 0)

    state = Statevector.from_instruction(qc)

    print(qc)
    print("\nStatevector:")
    print(state)

    # Manual calculation
    alpha = np.cos(theta/2) * np.exp(-1j * phi / 2)
    beta = np.sin(theta/2) * np.exp(1j * phi / 2)

    print("\nManual calculation:")
    print(f"|ψ> = ({alpha})|0> + ({beta})|1>")

    plot_bloch_multivector(state)
    plt.show()

# Example
theta = np.pi / 3
phi = np.pi / 4

create_state(theta, phi)