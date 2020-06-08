hosts_path = "/etc/hosts"
redirect = "127.0.0.1"
website = input("Enter the website to be blocked.\n")
file = open(hosts_path, "r+")
for char in file:
    char = char
file.write(redirect + " " + website +"\n")
