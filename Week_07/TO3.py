from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt


# ===================================================
# GENERIC ORACLE FUNCTION
# ===================================================

def create_oracle(function_type):

    oracle = QuantumCircuit(2)

    # -----------------------------------------------
    # CONSTANT FUNCTION f(x) = 0
    # -----------------------------------------------

    if function_type == "constant_0":

        # Output is always 0
        pass


    # -----------------------------------------------
    # CONSTANT FUNCTION f(x) = 1
    # -----------------------------------------------

    elif function_type == "constant_1":

        # Output is always 1
        oracle.x(1)


    # -----------------------------------------------
    # BALANCED FUNCTION f(x) = x
    # -----------------------------------------------

    elif function_type == "balanced_identity":

        oracle.cx(0, 1)


    # -----------------------------------------------
    # BALANCED FUNCTION f(x) = NOT x
    # -----------------------------------------------

    elif function_type == "balanced_not":

        oracle.x(1)
        oracle.cx(0, 1)


    else:

        raise ValueError(
            "Invalid function type!"
        )

    return oracle


# ===================================================
# DEUTSCH ALGORITHM
# ===================================================

def deutsch_algorithm(function_type):

    qc = QuantumCircuit(2, 1)

    # Prepare auxiliary qubit |1>
    qc.x(1)

    # Create superposition
    qc.h(0)
    qc.h(1)

    # Select oracle dynamically
    oracle = create_oracle(function_type)

    qc.compose(
        oracle,
        inplace=True
    )

    # Final Hadamard
    qc.h(0)

    # Measurement
    qc.measure(0, 0)

    return qc


# ===================================================
# FUNCTION TYPES
# ===================================================

function_types = [
    "constant_0",
    "constant_1",
    "balanced_identity",
    "balanced_not"
]


# ===================================================
# RUN ALL FUNCTIONS
# ===================================================

results = []

print("GENERIC ORACLE SELECTION")
print("=" * 50)


for function_type in function_types:

    print("\nFunction:", function_type)

    # Create circuit
    qc = deutsch_algorithm(function_type)

    # Display circuit
    print(qc.draw())

    # Simulator
    simulator = AerSimulator()

    # Run
    result = simulator.run(
        qc,
        shots=1024
    ).result()

    counts = result.get_counts()

    print("Measurement:", counts)

    # Determine output
    zero_count = counts.get("0", 0)
    one_count = counts.get("1", 0)

    if zero_count > one_count:

        output = 0
        classification = "CONSTANT"

    else:

        output = 1
        classification = "BALANCED"

    print("Output:", output)
    print("Classification:", classification)

    results.append(output)


# ===================================================
# GRAPH
# ===================================================

plt.figure(figsize=(10, 6))

plt.bar(
    function_types,
    results
)

plt.xlabel("Function Type")
plt.ylabel("Deutsch Algorithm Output")

plt.title(
    "Generic Oracle Selection Using Deutsch Algorithm"
)

plt.yticks(
    [0, 1],
    ["Constant", "Balanced"]
)

plt.xticks(rotation=20)

plt.show()