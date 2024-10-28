import os
import platform

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_banner():
    clear_screen()
    print("\n" * 2)
    print(" _____ ______   ___  ___  ___   _________  ___          _________  ________  ________  ___          ")
    print("|\\   _ \\  _   \\|\\  \\|\\  \\|\\  \\ |\\___   ___\\\\  \\        |\\___   ___\\\\   __  \\|\\   __  \\|\\  \\         ")
    print("\\ \\  \\\\\\__\\ \\  \\ \\  \\\\\\  \\ \\  \\\\|___ \\  \\_\\ \\  \\       \\|___ \\  \\_\\ \\  \\|\\  \\ \\  \\|\\  \\ \\  \\        ")
    print(" \\ \\  \\\\\\|__| \\  \\ \\  \\\\\\  \\ \\  \\    \\ \\  \\ \\ \\  \\           \\ \\  \\ \\ \\  \\\\\\  \\ \\  \\\\\\  \\ \\  \\       ")
    print("  \\ \\  \\    \\ \\  \\ \\  \\\\\\  \\ \\  \\____\\ \\  \\ \\ \\  \\           \\ \\  \\ \\ \\  \\\\\\  \\ \\  \\\\\\  \\ \\  \\____  ")
    print("   \\ \\__\\    \\ \\__\\ \\_______\\ \\_______\\ \\__\\ \\ \\__\\           \\ \\__\\ \\ \\_______\\ \\_______\\ \\_______\\")
    print("    \\|__|     \\|__|\\|_______|\\|_______|\\|__|  \\|__|            \\|__|  \\|_______|\\|_______|\\|_______|")
    print("\n" * 2)

def open_file(filename):
    # Determine the current OS
    current_os = platform.system()
    
    if current_os == "Darwin":  # macOS
        os.system(f'open {filename}')
    elif current_os == "Windows":  # Windows
        os.system(f'type {filename}')  # Use type for displaying file content in Windows
    elif current_os == "Linux":  # Linux
        os.system(f'cat {filename}')  # Use cat for displaying file content in Linux
    else:
        print(f"Unsupported OS: {current_os}")

def main_menu():
    while True:
        print("#═╦═══════»  [Option Gimkit]  [1]")
        print("╚═╦══════»   [Option Blooket]  [2]")
        print("╚═╦═════»    [Option Kahoot] [3]")
        print("╚═╦═════»    [Exit]           [q]")
        
        choice = input("╚══> ")

        if choice == '1':
            open_file('gimkit.txt')  # Opens or displays the gimkit.txt file
        elif choice == '2':
            open_file('blooket.txt')  # Replace with your file name
        elif choice == '3':
            open_file('kahoot.txt')  # Replace with your file name
        elif choice.lower() == 'q':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please choose 1, 2, 3, or q.")

if __name__ == "__main__":
    display_banner()
    main_menu()
