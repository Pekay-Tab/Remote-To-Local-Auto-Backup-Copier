
# ------------------------------------------------------------------------------------
# - Created by Pekay                                                                 -
# - Please contact me if u have any requests for added features or any other changes -
# - https://www.pekay.tk/discord Or Via Email pekaysmp@gmail.com                     -
# ------------------------------------------------------------------------------------


#Setup Steps

    # This is all setup using sftp so if your famiar with FileZilla Its The Same Procces
    # hostname = The hostname, ip etc of the remote server were the backup file is being stored
    # username = The username of the remote server were the backup file is being stored
    # password = The password of the remote server were the backup file is being stored
    # download = The remote-path were u want to get the backup file from 
    # to = The local-path were u want the remote backup downloaded to
    # hours = The delay before the script will automatically run again keep in mind this WILL work for any amounts under 1 hour ex. ".5" would be 30 minutes

hostname = "45.134.8.207"
username = "root"
password = "pekaysmp15789$156"
download = "/root/SMP/Backups/1-Pekays SMP/"
to = "/media/pi/Pekays Portable Drive/PEKAYS SMP BACKUPS/"
hours = 8