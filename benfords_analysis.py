import re
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from scipy.stats import chisquare

print(matplotlib.get_backend())

def extract_decimal(text):
    return re.findall(r'\b\d+\.\d+\b', text)

def get_leading_digits(decimal_output, digit_count):
    for i in range(0, len(decimal_output)):
        c = decimal_output[i][0]
        if c == '0':
            continue
        else:
            digit_count[c] = digit_count.get(c, 0) + 1

def compute_chi_square(actual, expected):
    digits = sorted(actual.keys())
    actual_vals = [actual[d] for d in digits]
    expected_vals = [expected[d] for d in digits]
    chi_stat, p_val = chisquare(f_obs = actual_vals, f_exp = expected_vals)
    print("chi_stat(How much the actual data differs from the expected data) : ", chi_stat)
    print("p_val(The probability that this deviation is dues to chance) : ", p_val)

def plot_distribution(actual, expected):
    digits = sorted(actual.keys())
    actual_vals = [actual[d] for d in digits]
    expected_vals = [expected[d] for d in digits]

    plt.figure(figsize=(10, 6))
    plt.plot(digits, actual_vals, color='blue', marker='o', label='Company Distribution')
    plt.plot(digits, expected_vals, color='red', marker='o', label='Benfords Expected')
    plt.xlabel("Leading Digit")
    plt.ylabel("Percentage")
    plt.title("Benford's Law Comparison")
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    digit_count = {}
    with open('data.txt', 'r') as f:
        raw_text = f.read()

    decimal_output = extract_decimal(raw_text)
    get_leading_digits(decimal_output, digit_count)

    total= sum(digit_count.values())

    percentage_of_digits = {}

    for key, value in digit_count.items():
        percentage = (value/total)*100
        percentage_of_digits[key] = round(percentage, 2)

    print("Count of each digit : ", digit_count)
    print("Percentage of each digit : ", percentage_of_digits)
    
    benford_expected = {
        '1': 30.1,
        '2': 17.6,
        '3': 12.5,
        '4': 9.7,
        '5': 7.9,
        '6': 6.7,
        '7': 5.8,
        '8': 5.1,
        '9': 4.6
    }
    
    compute_chi_square(percentage_of_digits, benford_expected)
    plot_distribution(percentage_of_digits, benford_expected)

if __name__ == "__main__":
    main()
