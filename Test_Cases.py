import subprocess
import pytest

def run_test(input_data, expected_output):
    result = subprocess.run(
        ['python3', 'mergesort.py'] + input_data.split(), stdout=subprocess.PIPE
    )
    assert result.stdout.decode('utf-8').strip() == expected_output

# ---------- VALID TEST CASES ----------

# Random Data: Test with typical, arbitrary values (e.g. [5, 2, 2, 10, 6])
@pytest.mark.Valid
@pytest.mark.Harir
def test_mergesort_random_data():
    input_data = "3 1 5 8 2 5 1 3"
    expected_output = "Sorted list: [1, 1, 2, 3, 3, 5, 5, 8]"
    run_test(input_data, expected_output)

# Sorted Data: Test with elements that are already sorted (e.g. [1, 2, 6, 7, 9])
@pytest.mark.Valid
@pytest.mark.Harir
def test_mergesort_sorted_data():
    input_data = "1 2 6 7 9"
    expected_output = "Sorted list: [1, 2, 6, 7, 9]"
    run_test(input_data, expected_output)

# Reverse Sorted Data: Test with elements sorted in descending order (e.g. [10, 9, 6, 4,1])
@pytest.mark.Valid
@pytest.mark.Harir
def test_mergesort_reverse_sorted_data():
    input_data = "5 3 2 1 0"
    expected_output = "Sorted list: [0, 1, 2, 3, 5]"
    run_test(input_data, expected_output)

# Even Number of Elements: Test with (relatively large) lists containing an
# even number of elements (e.g.: [1, 5, 2, 3, 6, 4])
@pytest.mark.Valid
@pytest.mark.Harir
def test_mergesort_even_num_elements():
    input_data = "1 5 2 3 6 4"
    expected_output = "Sorted list: [1, 2, 3, 4, 5, 6]"
    run_test(input_data, expected_output)

# Odd Number of Elements: Test with (relatively large) lists containing an
# odd number of elements (e.g.: [1, 5, 2, 3, 6, 4, 7])
@pytest.mark.Valid
@pytest.mark.Harir
def test_mergesort_odd_num_elements():
    input_data = "1 5 2 3 6 4 7"
    expected_output = "Sorted list: [1, 2, 3, 4, 5, 6, 7]"
    run_test(input_data, expected_output)

# Duplicate Data: Test with lists containing duplicate values (e.g. [6, 7, 2, 7, 6])
@pytest.mark.Valid
@pytest.mark.Harir
def test_mergesort_duplicate_data():
    input_data = "6 7 2 7 6"
    expected_output = "Sorted list: [2, 6, 6, 7, 7]"
    run_test(input_data, expected_output)

# Zero Values: Test with lists containing zeros (e.g. [2, 0, 3, 5, 1])
@pytest.mark.Valid
@pytest.mark.Ivan
def test_mergesort_zero_values():
    input_data = "2 0 3 5 1"
    expected_output = "Sorted list: [0, 1, 2, 3, 5]"
    run_test(input_data, expected_output)
    
# Negative Values: Test with lists containing negatives (e.g. [-2, -6, -3, -1, -10])
@pytest.mark.Valid
@pytest.mark.Ivan
def test_mergesort_negative_values():
    input_data = "-2 -6 -3 -1 -10"
    expected_output = "Sorted list: [-10, -6, -3, -2, -1]"
    run_test(input_data, expected_output)

# Negative, Positive, and Zero Values: Test with a list containing negative, positive,
# and zero values (e.g. [-4, -5, 2, 6, 0])
@pytest.mark.Valid
@pytest.mark.Ivan
def test_mergesort_negative_positive_zero_values():
    input_data = "-4 -5 2 6 0"
    expected_output = "Sorted list: [-5, -4, 0, 2, 6]"
    run_test(input_data, expected_output)

# ---------- BOUNDARY TEST CASES ----------

# Large Positive Input Values: Test with lists containing very large positive values
# (e.g. [999999997, 999999998, 999999999]
@pytest.mark.Boundary
@pytest.mark.Ivan
def test_mergesort_large_positive_values():
    input_data = "999999999999999997 999999999999999998 999999999999999999"
    expected_output = "Sorted list: [999999999999999997, 999999999999999998, 999999999999999999]"
    run_test(input_data, expected_output)

# Large Negative Input Values: Test with lists containing very large negative values
# (e.g. [-999999997, -999999998, -999999999]
@pytest.mark.Boundary
@pytest.mark.Ivan
def test_mergesort_large_negative_values():
    input_data = "-999999999999999997 -999999999999999998 -999999999999999999"
    expected_output = "Sorted list: [-999999999999999999, -999999999999999998, -999999999999999997]"
    run_test(input_data, expected_output)

# Single Element: Test with lists containing single element (e.g. [6])
@pytest.mark.Boundary
@pytest.mark.Aasim
def test_mergesort_single_element():
    input_data = "6"
    expected_output = "Sorted list: [6]"
    run_test(input_data, expected_output)

# Two Elements (Smallest Even): Test with lists containing two elements (smallest even) (e.g. [4, 2])
@pytest.mark.Boundary
@pytest.mark.Aasim
def test_mergesort_two_even_elements():
    input_data = "4 2"
    expected_output = "Sorted list: [2, 4]"
    run_test(input_data, expected_output)

# Three Elements (Smallest Odd): Test with lists containing three elements (smallest odd) (e.g. [54, 8, 4])
@pytest.mark.Boundary
@pytest.mark.Aasim
def test_mergesort_three_odd_elements():
    input_data = "54 8 4"
    expected_output = "Sorted list: [4, 8, 54]"
    run_test(input_data, expected_output)

# Homogeneous Data: Test with lists containing homogeneous elements (e.g. [6, 6, 6, 6, 6])
@pytest.mark.Boundary
@pytest.mark.Aasim
def test_mergesort_homogeneous_elements():
    input_data = "6 6 6 6 6"
    expected_output = "Sorted list: [6, 6, 6, 6, 6]"
    run_test(input_data, expected_output)

# Large Input Size: Test with lists containing a large number of elements (e.g. [6, 6 … 1000000])
@pytest.mark.Boundary
@pytest.mark.Aasim
def test_mergesort_large_input_size():
    input_data = "6 6 6 6 6 5 5 2 0 0 5 7 3 0 10500 10350 9 9 9 8 9 8 8 7 8"
    expected_output = "Sorted list: [0, 0, 0, 2, 3, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10350, 10500]"
    run_test(input_data, expected_output)

# ---------- INVALID TEST CASES ----------

# No Arguments: Test by passing in no arguments
@pytest.mark.Invalid
@pytest.mark.Rehan
def test_mergesort_no_arguments():
    input_data = ""
    expected_output = "Usage: python merge_sort.py <space-separated list of numbers>"
    run_test(input_data, expected_output)

# String Values: Test with lists containing strings (e.g. [test, zesty, cat])
@pytest.mark.Invalid
@pytest.mark.Rehan
def test_mergesort_string_values():
    input_data = "boii wha da heeeee"
    expected_output = "Usage: python merge_sort.py <space-separated list of numbers>"
    run_test(input_data, expected_output)

# Decimal Values: Test with lists containing decimals (e.g. [2.21, 6.61, 10.01])
@pytest.mark.Invalid
@pytest.mark.Rehan
def test_mergesort_decimal_values():
    input_data = "3.142 0.55 1.12 0.69"
    expected_output = "Usage: python merge_sort.py <space-separated list of numbers>"
    run_test(input_data, expected_output)

# Some Invalid Values: Test with a list containing some valid inputs and some different
# types of invalid values (e.g. 5, 43fg3rgf, 3.1422354, 5)
@pytest.mark.Invalid
@pytest.mark.Rehan
def test_mergesort_some_invalid_values():
    input_data = "boii 5 da 3.74 34"
    expected_output = "Usage: python merge_sort.py <space-separated list of numbers>"
    run_test(input_data, expected_output)

# Values with Whitespace: Test with different types of whitespace
# (e.g. [2  , 3, 2\t, 1, 5\n, 2])
@pytest.mark.Invalid
@pytest.mark.Rehan
def test_mergesort_whitespace():
    input_data = "3 12   6\n 1\t5"
    expected_output = "Sorted list: [1, 3, 5, 6, 12]"
    run_test(input_data, expected_output)

# Values Containing Separators: Test using a value containing comma separators (e.g: [2,3,67,87])
@pytest.mark.Invalid
@pytest.mark.Rehan
def test_mergesort_seperators():
    input_data = "6,23,7,1"
    expected_output = "Usage: python merge_sort.py <space-separated list of numbers>"
    run_test(input_data, expected_output)
