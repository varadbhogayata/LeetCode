class Solution:
    def romanToInt(self, s: str) -> int:
        roman_value_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        subtraction_dict = {'IV': 4, 'IX': 9,
                            'XL': 40, 'XC': 90,
                            'CD': 400, 'CM': 900}
        int_value = 0
        for k, v in subtraction_dict.items():
            while k in s:
                s_index = s.find(k)
                s = s[:s_index] + s[s_index+2:]
                int_value = int_value + v
                # print(s)

        for char in s:
            int_value = int_value + roman_value_dict[char]

        return int_value