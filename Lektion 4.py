# Code der überprüft ob eine Zahl positiv, negativ oder null ist.

# Zahl einlesen
zahl = int(input("Zahl eingeben:"))

# Wenn 0
if zahl == 0:
    print("Die Zahl ist 0")

# Wenn gerade
elif zahl % 2 == 0:
    print("Die Zahl ist gerade")

# sonst (Wenn ungerade)
else:
    print("Die Zahl ist ungerade")