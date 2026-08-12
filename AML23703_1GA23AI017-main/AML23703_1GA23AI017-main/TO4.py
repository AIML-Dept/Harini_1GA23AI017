import random

from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer


backend = Aer.get_backend("aer_simulator")


# Create quantum circuit once
qc = QuantumCircuit(1, 1)

qc.h(0)
qc.measure(0, 0)

compiled = transpile(qc, backend)


# Run 1000 quantum shots together
job = backend.run(compiled, shots=1000)

result = job.result()

quantum_counts = result.get_counts()


# Python random generator
python_counts = {
    "0": 0,
    "1": 0
}

for i in range(1000):
    bit = random.randint(0, 1)
    python_counts[str(bit)] += 1


print("Quantum Random Generator")
print("------------------------")
print(quantum_counts)


print("\nPython Random Generator")
print("------------------------")
print(python_counts)


print("\nQuantum probability of 1:")
print(quantum_counts.get("1",0)/1000)


print("\nPython probability of 1:")
print(python_counts.get("1",0)/1000)
