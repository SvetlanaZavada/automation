from smartphon import Smartphon


catalog = [
    Smartphon("Apple", "iPhone 15 Pro Max", "+79095665274"),
    Smartphon("Samsung", "Galaxy S24 Ultra", "+79095668274"),
    Smartphon("Xiaomi", "Mi 14 Pro", "+79095665224"),
    Smartphon("Google", "Pixel 8 Pro", "+79092665274"),
    Smartphon("OnePlus", "12", "+79095665278")
]

for phon in catalog:
    print(f"<{phon.brand}>, <{phon.model}>, <{phon.number}>")
