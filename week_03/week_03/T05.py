from qiskit import QuantumCircuit
from qiskit.quantum_info import Operator

# HZH Circuit
qc_hzh = QuantumCircuit(1)
qc_hzh.h(0)
qc_hzh.z(0)
qc_hzh.h(0)

# X Gate Circuit
qc_x = QuantumCircuit(1)
qc_x.x(0)

op_hzh = Operator(qc_hzh)

op_x = Operator(qc_x)

print("HZH Matrix:\n")
print(op_hzh.data)

print("\nX Matrix:\n")
print(op_x.data)

if op_hzh.equiv(op_x):
    print("\nResult")
    print("HZH is equivalent to X Gate")
else:
    print("Not Equivalent")

print("\nHZH Circuit")
print(qc_hzh.draw())

print("\nX Circuit")
print(qc_x.draw())