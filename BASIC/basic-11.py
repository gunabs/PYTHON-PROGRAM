def pali(str):
    rev=str[ : : -1]
    return str.lower()==rev.lower()

str="MaadaM"

if pali(str):
    print("yes")
else:
    print("no")
