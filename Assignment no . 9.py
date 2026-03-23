import shapes

def main():
    print("Choose a shape to calculate area:")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        radius = float(input("Enter radius of the circle: "))
        print(f"Area of Circle: {shapes.area_circle(radius):.2f}")

    elif choice == "2":
        length = float(input("Enter length of the rectangle: "))
        width = float(input("Enter width of the rectangle: "))
        print(f"Area of Rectangle: {shapes.area_rectangle(length, width):.2f}")

    elif choice == "3":
        base = float(input("Enter base of the triangle: "))
        height = float(input("Enter height of the triangle: "))
        print(f"Area of Triangle: {shapes.area_triangle(base, height):.2f}")

    else:
        print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
