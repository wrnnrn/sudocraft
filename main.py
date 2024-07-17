import time
import subprocess

print("""
  █████████                 █████            █████████                         ██████   █████   
 ███░░░░░███               ░░███            ███░░░░░███                       ███░░███ ░░███    
░███    ░░░  █████ ████  ███████   ██████  ███     ░░░  ████████   ██████    ░███ ░░░  ███████  
░░█████████ ░░███ ░███  ███░░███  ███░░███░███         ░░███░░███ ░░░░░███  ███████   ░░░███░   
 ░░░░░░░░███ ░███ ░███ ░███ ░███ ░███ ░███░███          ░███ ░░░   ███████ ░░░███░      ░███    
 ███    ░███ ░███ ░███ ░███ ░███ ░███ ░███░░███     ███ ░███      ███░░███   ░███       ░███ ███
░░█████████  ░░████████░░████████░░██████  ░░█████████  █████    ░░████████  █████      ░░█████ 
 ░░░░░░░░░    ░░░░░░░░  ░░░░░░░░  ░░░░░░    ░░░░░░░░░  ░░░░░      ░░░░░░░░  ░░░░░        ░░░░░  
""")

def delay():
    time.sleep(0.1)

print("[1] - List the things that are going to do this script")
delay()
print("[2] - Make the installation")
delay()
print("[3] - Exit")

answer = input("What do you want to do?: ")
print("")

if answer == '1':
    delay()
    print("Applications")
    delay()
    print(" · Sublime Text --> Code editor")
    delay()
    print(" · Nvim --> Terminal code editor")
    delay()
    print(" · PIP --> Python package manager")
    delay()
    print(" · Yay --> Helper of AUR (Archlinux user repo)")
    delay()
    print("")
    delay()
    print("Modifications in scripts")
    delay()
    print(" · Nitrogen --> Change the background (the initial is so white)")
    delay()
    print(" · Icons --> Put the papirus package icons")
    print("")

if answer == '2':
    # Check internet connection
    result = subprocess.run(["ping", "-c", "1", "google.com"], capture_output=True, text=True)
    if result.returncode != 0:
        print("You don't have internet connection, please check your connection and retry")
        exit()

    security_answer = input("The installation is ready, are you sure? (y/n): ").lower()
    if security_answer == 'y':
        # Sublime text
        def install_sublime():
            subprocess.run(["curl", "-O", "https://download.sublimetext.com/sublimehq-pub.gpg"], check=True)
            subprocess.run(["sudo", "pacman-key", "--add", "sublimehq-pub.gpg"], check=True)
            subprocess.run(["sudo", "pacman-key", "--lsign-key", "8A8F901A"], check=True)
            subprocess.run(["rm", "sublimehq-pub.gpg"], check=True)
            with open("/etc/pacman.conf", "a") as pacman_conf:
                pacman_conf.write("\n[sublime-text]\nServer = https://download.sublimetext.com/arch/stable/x86_64\n")
            subprocess.run(["sudo", "pacman", "-Syu"], check=True)
            subprocess.run(["sudo", "pacman", "-S", "sublime-text"])

        # Call the function
        install_sublime()

        # Nvim
        subprocess.run(["sudo", "pacman", "-S", "neovim"], check=True)

        # PIP
        subprocess.run(["sudo", "pacman", "-S", "python-pip"], check=True)

        # Nitrogen
        subprocess.run(["rm", "-r", "$HOME/.config/nitrogen/bg-saved.cfg"], check=True)  # Reemplaza `your_username`
        subprocess.run(["cp", "bg-saved.cfg", "$HOME/.config/nitrogen"], check=True)

    else:
        exit()

if answer == '3':
    exit()
