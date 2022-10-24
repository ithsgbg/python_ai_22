data = [
    {
        'name': 'A',
        'version': '1.0.5'
    },
    {
        'name': 'B',
        'version': '1.0.7'
    },
    {
        'name': 'C',
        'version': '1.0b.0'
    },
    {
        'name': 'D',
        'version': '1.0a.0'
    }
]
"""
Output:
data = [
    {
        'name': 'D',
        'version': '1.0a.0'
    },
    {
        'name': 'C',
        'version': '1.0b.0'
    },
    {
        'name': 'A',
        'version': '1.0.5'
    },
    {
        'name': 'B',
        'version': '1.0.7'
    }
]

"""
values = [5, 3, 1, 7, 2]

values.sort()
print(values)