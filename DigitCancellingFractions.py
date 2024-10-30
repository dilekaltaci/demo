from fractions import Fraction

def find_curious_fractions():
    curious_fractions = []
    
    for numerator in range(10, 100):
        for denominator in range(numerator + 1, 100):
            num_str, den_str = str(numerator), str(denominator)
            common_digits = set(num_str) & set(den_str)
            
            if len(common_digits) == 1 and '0' not in common_digits:
                common_digit = common_digits.pop()
                new_num_str = num_str.replace(common_digit, "", 1)
                new_den_str = den_str.replace(common_digit, "", 1)
             
                if new_num_str.isdigit() and new_den_str.isdigit():
                    new_numerator = int(new_num_str)
                    new_denominator = int(new_den_str)
                    
                    if new_denominator != 0 and numerator * new_denominator == denominator * new_numerator:
                        curious_fractions.append(Fraction(numerator, denominator))
    
    product_of_fractions = Fraction(1, 1)
    for fraction in curious_fractions:
        product_of_fractions *= fraction
    
    return product_of_fractions.denominator

find_curious_fractions()