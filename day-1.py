def number_to_words(num):
    # Define word representations for numbers up to 20
    words_up_to_20 = [
        'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
        'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'
    ]
    
    # Define word representations for tens
    tens_words = [
        '', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'
    ]
    
    if num < 20:
        return words_up_to_20[num]
    
    if num < 100:
        tens = num // 10
        ones = num % 10
        if ones == 0:
            return tens_words[tens]
        else:
            return tens_words[tens] + '-' + words_up_to_20[ones]
    
    return "Number out of range"

def add_numbers(num1, num2):
    result = num1 + num2
    return result

# Get the input numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Add the numbers
sum_result = add_numbers(num1, num2)

# Convert the sum to words
sum_in_words = number_to_words(sum_result)

# Print the result
print("The sum of", num1, "and", num2, "is:", sum_in_words)