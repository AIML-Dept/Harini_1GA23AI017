from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

print("----- X Gate -----")
qc_x = QuantumCircuit(1)
qc_x.x(0)
state_x = Statevector.from_instruction(qc_x)
print(state_x)

print("\n----- Y Gate -----")
qc_y = QuantumCircuit(1)
qc_y.y(0)
state_y = Statevector.from_instruction(qc_y)
print(state_y)

print("\n----- Z Gate -----")
qc_z = QuantumCircuit(1)
qc_z.z(0)
state_z = Statevector.from_instruction(qc_z)
print(state_z)