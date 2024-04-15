phone = input("Phone:")
digits_mapping = {
    "1": "ONE",
    "2": "TWO",
    "3": "THREE",
    "4": "FOUR"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)