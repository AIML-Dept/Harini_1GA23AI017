from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import random
import matplotlib.pyplot as plt


# ==========================================================
# GENERATE RANDOM BALANCED FUNCTION
# ==========================================================

def generate_random_balanced_function(n):

    total_inputs = 2 ** n

    half = total_inputs // 2

    # Create equal number of 0s and 1s

    outputs = (
        [0] * half +
        [1] * half
    )

    # Randomly shuffle

    random.shuffle(outputs)

    return outputs


# ==========================================================
# CREATE RANDOM BALANCED ORACLE
# ==========================================================

def create_random_balanced_oracle(n, truth_table):

    oracle = QuantumCircuit(n + 1)

    # ------------------------------------------------------
    # For every input combination
    # ------------------------------------------------------

    for input_number in range(2 ** n):

        output = truth_table[input_number]

        # If function output is 1,
        # construct the corresponding multi-controlled X.

        if output == 1:

            binary = format(
                input_number,
                f"0{n}b"
            )

            # --------------------------------------------------
            # Convert controls according to binary value
            # --------------------------------------------------

            for qubit in range(n):

                if binary[n - 1 - qubit] == "0":

                    oracle.x(qubit)

            # --------------------------------------------------
            # Multi-controlled X
            # --------------------------------------------------

            oracle.mcx(
                list(range(n)),
                n
            )

            # --------------------------------------------------
            # Undo X gates
            # --------------------------------------------------

            for qubit in range(n):

                if binary[n - 1 - qubit] == "0":

                    oracle.x(qubit)

    return oracle


# ==========================================================
# DEUTSCH-JOZSA CIRCUIT
# ==========================================================

def deutsch_jozsa(n, truth_table):

    qc = QuantumCircuit(
        n + 1,
        n
    )

    # ------------------------------------------------------
    # Prepare output qubit |1>
    # ------------------------------------------------------

    qc.x(n)

    # ------------------------------------------------------
    # Hadamard gates
    # ------------------------------------------------------

    for i in range(n + 1):

        qc.h(i)

    # ------------------------------------------------------
    # Random balanced oracle
    # ------------------------------------------------------

    oracle = create_random_balanced_oracle(
        n,
        truth_table
    )

    qc.compose(
        oracle,
        inplace=True
    )

    # ------------------------------------------------------
    # Final Hadamard
    # ------------------------------------------------------

    for i in range(n):

        qc.h(i)

    # ------------------------------------------------------
    # Measurement
    # ------------------------------------------------------

    for i in range(n):

        qc.measure(
            i,
            i
        )

    return qc


# ==========================================================
# RUN ONE TEST
# ==========================================================

def run_one_test(n):

    # Generate random balanced function

    truth_table = (
        generate_random_balanced_function(n)
    )

    # Create circuit

    qc = deutsch_jozsa(
        n,
        truth_table
    )

    # Simulator

    simulator = AerSimulator()

    # Run

    result = simulator.run(
        qc,
        shots=256
    ).result()

    counts = result.get_counts()

    # ------------------------------------------------------
    # For a balanced function, 000...0 should NOT occur
    # ideally.
    # ------------------------------------------------------

    zero_string = "0" * n

    if counts.get(zero_string, 0) == 0:

        correct = True

    else:

        correct = False

    return truth_table, counts, correct


# ==========================================================
# MAIN PROGRAM
# ==========================================================

n = 3

number_of_tests = 10

successful_tests = 0

failed_tests = 0

print("=" * 70)

print(
    "CHALLENGE: RANDOM BALANCED ORACLE GENERATOR"
)

print("=" * 70)

print(
    f"\nNumber of input qubits: {n}"
)

print(
    f"Number of random tests: {number_of_tests}"
)


# ==========================================================
# RUN MULTIPLE RANDOM TESTS
# ==========================================================

for test in range(
    1,
    number_of_tests + 1
):

    truth_table, counts, correct = (
        run_one_test(n)
    )

    print(
        f"\nTest {test}"
    )

    print(
        "Random truth table:"
    )

    print(
        truth_table
    )

    print(
        "Measurement:"
    )

    print(
        counts
    )

    if correct:

        print(
            "Classification: BALANCED ✓"
        )

        successful_tests += 1

    else:

        print(
            "Classification: INCORRECT ✗"
        )

        failed_tests += 1


# ==========================================================
# ACCURACY
# ==========================================================

accuracy = (
    successful_tests /
    number_of_tests
) * 100


print("\n" + "=" * 70)

print(
    "FINAL RESULTS"
)

print("=" * 70)

print(
    "Successful tests:",
    successful_tests
)

print(
    "Failed tests:",
    failed_tests
)

print(
    f"Accuracy: {accuracy:.2f}%"
)


# ==========================================================
# GRAPH
# ==========================================================

labels = [
    "Successful",
    "Failed"
]

values = [
    successful_tests,
    failed_tests
]


plt.figure(figsize=(7, 5))

plt.bar(
    labels,
    values
)

plt.xlabel(
    "Test Result"
)

plt.ylabel(
    "Number of Tests"
)

plt.title(
    "Random Balanced Oracle Verification"
)

plt.show()