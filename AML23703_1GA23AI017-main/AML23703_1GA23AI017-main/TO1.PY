from qiskit import __version__
from qiskit_aer import Aer

print("Qiskit Version:", __version__)

print("\nAvailable Aer Backends:")

for backend in Aer.backends():
    print("-", backend.name)
