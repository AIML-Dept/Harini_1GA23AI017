from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator

qc = QuantumCircuit(1)

# |-> = Z(H|0>)
qc.h(0)
qc.z(0)

state = Statevector.from_instruction(qc)

print("Statevector:")
print(state)

simulator = AerSimulator(method="statevector")

result = simulator.run(qc).result()

print("\nVerified using simulation.")
print(state)