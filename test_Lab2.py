import Lab2

# Test 1: Calculate Average
def test_calc_average():
    input_list = [10.0, 20.0, 30.0, 40.0, 50.0]
    expected_result = 30.0

    # Adjust function name if your Lab2.py uses calc_average_temperature
    result = Lab2.calc_average(input_list)
    assert result == expected_result


# Test 2: Find Min and Max
def test_find_min_max():
    input_list = [5.0, 67.0, 32.0, 2.0, 99.0]
    expected_result = [2.0, 99.0]

    # Adjust function name if your Lab2.py uses calc_min_max_temperature
    result = Lab2.find_min_max(input_list)
    assert result == expected_result


# Test 3: Calculate Median Temperature
def test_calc_median_temperature():
    # Odd number of elements
    odd_list = [5.0, 67.0, 32.0]
    assert Lab2.calc_median_temperature(odd_list) == 32.0

    # Even number of elements
    even_list = [10.0, 20.0, 30.0, 40.0]
    assert Lab2.calc_median_temperature(even_list) == 25.0