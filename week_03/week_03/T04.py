from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

qc = QuantumCircuit(1)

# Quantum coin toss
qc.h(0)

state = Statevector.from_instruction(qc)

probabilities = state.probabilities_dict()

print("Quantum Coin Flip")

print("\nStatevector:")
print(state)

print("\nWinning Probabilities:")

for outcome, probability in probabilities.items():
    print(f"{outcome} : {probability:.2f}")

print("\nInterpretation")

print("0 = Heads")
print("1 = Tails")