def main():
    filename = "example.txt"

    # 1. Writing data to a file (creates or overwrites)
    with open(filename, "w") as file:
        file.write("Hello, this is the first line.\n")
        file.write("This file demonstrates basic file handling.\n")
    print("Data written to file.")

    # 2. Reading the contents of the file
    with open(filename, "r") as file:
        content = file.read()
    print("\nContents of the file after writing:")
    print(content)

    # 3. Appending additional content to the file
    with open(filename, "a") as file:
        file.write("Appending a new line at the end.\n")
    print("\nData appended to file.")

    # 4. Reading again to see appended content
    with open(filename, "r") as file:
        updated_content = file.read()
    print("\nContents of the file after appending:")
    print(updated_content)

    # Note: Using 'with open(...)' ensures the file is properly closed automatically.

if __name__ == "__main__":
    main()
