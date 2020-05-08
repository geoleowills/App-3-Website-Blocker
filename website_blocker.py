import time
from datetime import datetime as dt

hosts_path = "/private/etc/hosts"
# Redirect to local
redirect = "127.0.0.1"
# List of websites to block
website_list = ["www.facebook.com", "facebook.com",
                "www.instagram.com", "instagram.com"]

while True:
    # Checks the time
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        # Print whether it is working or fun hours
        print("Working hours")
        # Opens and reads the hosts file if within the specified working hours
        with open(hosts_path, "r+") as file:
            content = file.read()
            # If the website is already listed there, does nothing
            for website in website_list:
                if website in content:
                    pass
                # If website is not listed there and needs to be added, adds the local IP and website address
                else:
                    file.write("\n" + redirect + " " + website)

    else:
        # Prints whether it is working or fun hours
        print("Fun hours")
        # Opens and reads the hosts file if outside of the specified working hours
        with open(hosts_path, "r+") as file:
            # Opens file as list of each line
            content = file.readlines()
            # Sets the cursor back to the beginning of file
            file.seek(0)
            # Loops through each line
            for line in content:
                # Checks if line is a line with one of the specified websites on
                if not any(website in line for website in website_list):
                    # If line has website on, does nothing. If line does not have website on,
                    # copies that line to where to cursor is. This rewrites the whole file,
                    # above the old one, apart from lines with the websites on.
                    file.write(line)
                    # Deletes everything below the cursor, so only the new rewritten file is left.
            file.truncate()
    time.sleep(5)
