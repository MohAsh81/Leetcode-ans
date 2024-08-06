from collections import Counter
import math

class Solution:
    def minimumPushes(self, word: str) -> int:
        """
        Calculate the minimum number of pushes required to input a word on a device
        where each button can store up to 8 distinct characters.

        Parameters:
        word (str): The word to be input on the device.

        Returns:
        int: The minimum number of pushes required.
        """
        cost = 0
        # Calculate the frequency of each character and sort the frequencies in descending order
        values_dict = sorted((Counter(word).values()), reverse=True)
        count = len(values_dict)
        
        # If there are 8 or fewer distinct characters, each character can be mapped to a button directly
        if count <= 8:
            return len(word)
        else:
            # Process the frequencies until all characters are accounted for
            while len(values_dict) != 0:
                # Calculate the number of full button presses needed (8 characters per button)
                quotient = math.ceil(count / 8)
                # Add the cost of the current lowest frequency character in the list
                cost += quotient * values_dict[-1]
                # Remove the character with the lowest frequency from the list
                values_dict.pop()
                # Decrease the count of remaining characters
                count -= 1

        return cost
