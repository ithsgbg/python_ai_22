from packaging.version import Version
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

sorted_values = sorted(data, key=lambda item: Version(item['version']))
for item in sorted_values:
    print(item)