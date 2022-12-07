
#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    r_nums = {
        'MMM': 3000,
        'MM': 2000,
        'M': 1000,
        'DCCC': 800,
        'DCC': 700,
        'DC': 600,
        'CCC': 300,
        'CC': 200,
        'CD': 400,
        'D': 500,
        'CM': 900,
        'LXXX': 80,
        'LXX': 70,
        'LX': 60,
        'XXX': 30,
        'XX': 20,
        'XL': 40,
        'L': 50,
        'XC': 90,
        'C': 100,
        'VIII': 8,
        'VII': 7,
        'III': 3,
        'II': 2,
        'VI': 6,
        'IV': 4,
        'V': 5,
        'IX': 9,
        'X': 10,
        'I': 1,

    }
    result = 0
    for key in r_nums.keys():
        if key in roman_string:
            result += r_nums[key]
            roman_string = roman_string.replace(key, '')

    return result
