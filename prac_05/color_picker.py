
color_names = {"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7", "aquamarine": "#7fffd4", "azure": "#f0ffff", "beige": "#f5f5dc",
               "bisque": "#ffe4c4", "black": "#000000", "blue": "#0000ff", "brown": "#a52a2a", "burlywood": "#deb887", "coral": "#ff7f50"}

color = input("Enter colour name here: ")
while color != "":
    if color in color_names:
        print(color, "is", color_names[color])
    else:
        print("Invalid color name")
    color = input("Enter colour name here: ")
