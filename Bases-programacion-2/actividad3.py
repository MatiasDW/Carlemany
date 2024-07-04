def max_panels(a, b, x, y):
    def panels_in_orientation(panel_width, panel_height, roof_width, roof_height):
        # Calculate the number of panels that fit in one orientation
        return (roof_width // panel_width) * (roof_height // panel_height)
    
    max_panels = 0
    
    # Try placing panels in original orientation and calculate remaining space
    for i in range(x // a + 1):
        for j in range(y // b + 1):
            remaining_width = x - i * a
            remaining_height = y - j * b
            panels_in_remaining_space = panels_in_orientation(b, a, remaining_width, y) + panels_in_orientation(b, a, x, remaining_height)
            total_panels = i * j + panels_in_remaining_space
            max_panels = max(max_panels, total_panels)
    
    # Try placing panels in rotated orientation and calculate remaining space
    for i in range(x // b + 1):
        for j in range(y // a + 1):
            remaining_width = x - i * b
            remaining_height = y - j * a
            panels_in_remaining_space = panels_in_orientation(a, b, remaining_width, y) + panels_in_orientation(a, b, x, remaining_height)
            total_panels = i * j + panels_in_remaining_space
            max_panels = max(max_panels, total_panels)

    return max_panels

# Ask the user for the dimensions
a = int(input("Ingrese la dimensión a del panel: "))
b = int(input("Ingrese la dimensión b del panel: "))
x = int(input("Ingrese la dimensión x del techo: "))
y = int(input("Ingrese la dimensión y del techo: "))

# Calculate and display the result
resultado = max_panels(a, b, x, y)
print(f"La cantidad máxima de paneles que caben es: {resultado}")

# Automated test examples (you can remove them if not needed)
print(max_panels(1, 2, 2, 4))  # Output: 4
print(max_panels(1, 2, 3, 5))  # Output: 7
print(max_panels(2, 2, 1, 10)) # Output: 0
print(max_panels(2, 3, 2, 3))  # Output: 3
