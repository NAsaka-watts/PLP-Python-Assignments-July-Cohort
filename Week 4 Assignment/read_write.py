# File Read & Write Challenge with Error Handling

def modify_content(text):
    """
    Simple modification: Convert text to uppercase and add a line.
    """
    return text.upper() + "\n--- Modified Successfully ---\n"

def main():
    filename = input("Enter the filename to read: ")

    try:
        # Try opening the input file
        with open(filename, "r") as f:
            content = f.read()
        
        print("\n✅ File read successfully!\n")
        
        # Modify content
        new_content = modify_content(content)

        # Write to new file
        new_filename = "output.txt"
        with open(new_filename, "w") as f:
            f.write(new_content)

        print(f"✅ Modified content written to '{new_filename}'")

    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"❌ Error: Permission denied when accessing '{filename}'.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    main()
