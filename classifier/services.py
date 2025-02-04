import math
import requests
from typing import List
from functools import lru_cache

class NumberClassifier:
    @staticmethod
    def is_armstrong(num: int) -> bool:
        """Check if number is an Armstrong number."""
        num = abs(num)  # Convert to absolute value
        str_num = str(num)
        power = len(str_num)
        return num == sum(int(digit) ** power for digit in str_num)
    
    @staticmethod
    def is_prime(num: int) -> bool:
        """Check if number is prime."""
        if num < 2:  # Negative numbers and 0,1 are not prime
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True
    
    @staticmethod
    def is_perfect(num: int) -> bool:
        """Check if number is perfect."""
        if num < 1:  # Negative numbers and 0 are not perfect numbers
            return False
        return sum(i for i in range(1, num) if num % i == 0) == num
    
    @staticmethod
    def digit_sum(num: int) -> int:
        """Calculate sum of digits for a number, including negative numbers."""
        num = abs(num)  # Convert to absolute value
        return sum(int(digit) for digit in str(num))
    
    @staticmethod
    def get_properties(num: int) -> List[str]:
        """Get list of number properties."""
        properties = []
        
        # Check if Armstrong
        if NumberClassifier.is_armstrong(num):
            properties.append("armstrong")
        
        # Check odd/even
        properties.append("odd" if num % 2 else "even")
        
        return properties

    @staticmethod
    @lru_cache(maxsize=1000)  # Cache results to improve performance
    def get_fun_fact(num: int) -> str:
        """Get fun fact from Numbers API."""
        try:
            response = requests.get(f'http://numbersapi.com/{num}/math')
            return response.text
        except requests.RequestException:
            # Fallback fun fact if API fails
            num = abs(num)  # Convert to absolute value for meaningful facts
            if NumberClassifier.is_armstrong(num):
                digits = str(num)
                power = len(digits)
                calculation = ' + '.join(f'{d}^{power}' for d in digits)
                return f"{num} is an Armstrong number because {calculation} = {num}"
            return f"The number {num} is {'even' if num % 2 == 0 else 'odd'}"