"""
area_code, prefix, line_num =input("Paste phone nro: ").split() #split between spaces
area_code, prefix, line_num = int(area_code), int(prefix), int(line_num)
print(type(area_code))
"""
#input = 555  457  2345
#input = 555  929  6453

area_code, prefix, line_num =input("").split() #split between spaces
area_code, prefix, line_num = int(area_code), int(prefix), int(line_num)

print("Country  Phone Number")
print("-------  ------------")
print(f"U.S.     +1 ({area_code}){prefix}-{line_num}") #can include str or int in {}
print(f"Brazil   +55 ({area_code}){prefix + 100}-{line_num}")
print(f"Croatia  +385 ({area_code}){prefix}-{line_num + 50}")
print(f"Egypt    +20 ({area_code + 30}){prefix}-{line_num}")
print(f"France   +33 ({prefix}){area_code}-{line_num}")

# Another option to output = print("U.S. +1 " + str(area_code) + "-")

