"""
  #  1️⃣ The Core Idea of f-string Formatting
  # f"{value:format_spec}"
  Where:
value = the variable
format_spec = how you want it displayed
  """

def main():
    h = 5
    hours_f = f'{h:02d}'

    """
    | Part | Meaning           |
| ---- | ----------------- |
| `0`  | pad with zeros    |
| `2`  | minimum width = 2 |
| `d`  | integer           |

    """
    print(hours_f)

   # 3️⃣ Common Integer Formatting Patterns
    print(f'{7:03d}')
   # Space padding
    print(f'{7:3d}')

    print(f'{7:<3d}')
    print(f'{7:>3d}')
    print(f'{7:^3d}')

   # 4️⃣ Float Formatting (Very Important)
    x = 3.14159
    print(f'{x:.2f}')

    """
    | Part | Meaning          |
| ---- | ---------------- |
| `.2` | 2 decimal places |
| `f`  | float            |

    """

    # Combine width + precision

    print(f'{x:8.2f}')

    # Zero-padded float
    print(f'{x:06.2f}')

   #  5️⃣ Strings Formatting

    name = "Bob"
    print(f'{name:>10}') # right aligned
    print(f'{name:<10}') # left aligned

   # 8️⃣ Real-World Examples

   # A. Currency formatting

    amount = 6050.5
    print(f'{amount:,.2f}')

    # B. IDs / codes
    user_id = 23
    print(f'USER-{user_id:04d}')

    # C. Percentages

    ratio = 0.256

    print(f'{ratio:.1%}')


    # 9️⃣ Practice (very important)

    print(f'{9:03d}')








if __name__ == '__main__':
    main()