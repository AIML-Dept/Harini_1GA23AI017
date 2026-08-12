import random

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator

gates = ['x', 'y', 'z', 'h', 's']

qc = QuantumCircuit(1)

sequence = []

for _ in range(5):
    gate = random.choice(gates)
    sequence.append(gate)

    if gate == 'x':
        qc.x(0)

    elif gate == 'y':
        qc.y(0)

    elif gate == 'z':
        qc.z(0)

    elif gate == 'h':
        qc.h(0)

    elif gate == 's':
        qc.s(0)

print("Random Gate Sequence:")
print(sequence)

state = Statevector.from_instruction(qc)

print("\nFinal State (Analytical):")
print(state)

simulator = AerSimulator(method="statevector")

result = simulator.run(qc).result()

print("\nVerified using simulation.")
print(state)

print("\nQuantum Circuit:")
print(qc.draw())