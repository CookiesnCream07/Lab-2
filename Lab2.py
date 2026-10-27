def display_main_menu():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    user_str = input()
    # Split string into list elements by comma
    str_list = user_str.split(",")
    # Convert each string element into float and strip extra whitespace
    float_list = [float(item.strip()) for item in str_list]
    return float_list

def calc_average(num_list):
    avg = sum(num_list) / len(num_list)
    return float(avg)

def find_min_max(num_list):
    min_val = min(num_list)
    max_val = max(num_list)
    return [min_val, max_val]

def sort_temperature(num_list):
    sorted_list = sorted(num_list)
    return sorted_list

def calc_median_temperature(num_list):
    sorted_list = sort_temperature(num_list)
    n = len(sorted_list)
    
    # If odd number of elements
    if n % 2 == 1:
        median = sorted_list[n // 2]
    # If even number of elements, average middle two
    else:
        median = (sorted_list[(n // 2) - 1] + sorted_list[n // 2]) / 2.0
        
    return float(median)

def main():
    display_main_menu()
    num_list = get_user_input()
    
    print("\n--- Results ---")
    print("Average Temperature:", calc_average(num_list))
    print("Min and Max Temperature:", find_min_max(num_list))
    print("Sorted Temperatures:", sort_temperature(num_list))
    print("Median Temperature:", calc_median_temperature(num_list))

if __name__ == "__main__":
    main()