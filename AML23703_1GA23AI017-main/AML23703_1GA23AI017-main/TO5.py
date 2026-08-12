from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit_aer.noise import NoiseModel, depolarizing_error


# Create 1-qubit circuit
qc = QuantumCircuit(1, 1)

qc.h(0)
qc.measure(0, 0)

print("Circuit:")
print(qc)


# ----------------------------
# Ideal Simulator
# ----------------------------

ideal_backend = Aer.get_backend("aer_simulator")

ideal_job = ideal_backend.run(
    transpile(qc, ideal_backend),
    shots=1024
)

ideal_result = ideal_job.result()

ideal_counts = ideal_result.get_counts()


print("\nIdeal Simulator Result:")
print(ideal_counts)



# ----------------------------
# Noisy Simulator
# ----------------------------

noise_model = NoiseModel()

error = depolarizing_error(
    0.05,
    1
)

noise_model.add_all_qubit_quantum_error(
    error,
    ["h"]
)


noisy_backend = Aer.get_backend("aer_simulator")


noisy_job = noisy_backend.run(
    transpile(qc, noisy_backend),
    shots=1024,
    noise_model=noise_model
)


noisy_result = noisy_job.result()

noisy_counts = noisy_result.get_counts()


print("\nNoise Simulator Result:")
print(noisy_counts)
