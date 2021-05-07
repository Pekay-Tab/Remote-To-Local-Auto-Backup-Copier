import sys
import config_file
import pysftp as ftplib
import time
import math

cnopts = ftplib.CnOpts()
cnopts.hostkeys = None
latest = None

hostname = config_file.hostname
username = config_file.username
password = config_file.password
download = config_file.download
to = config_file.to
hours = config_file.hours


def progressbar(x, y):
    """ Transfer Progress Thing
    """
    bar_len = 60
    filled_len = math.ceil(bar_len * x / float(y))
    percents = math.ceil(100.0 * x / float(y))
    bar = '=' * filled_len + '-' * (bar_len - filled_len)
    filesize = f'{math.ceil(y / 1024):,} KB' if y > 1024 else f'{y} byte'
    sys.stdout.write(f'[{bar}] {percents}%\r')
    sys.stdout.flush()


while True:
    print("===========================================================")
    print("Backup Initiated! [" + time.strftime("%r::%d/%m/%y") + "]")
    with ftplib.Connection(host=hostname, username=username, password=password, cnopts=cnopts) as sftp:
        with sftp.cd(download):
            latest = sftp.listdir()[0]
        print("Approx. Transfer Size -> "+str(math.ceil(sftp.lstat(remotepath=download + latest).st_size / (1024 * 1024)))+"MB")
        timern = time.strftime("%m_%d_%r_SmpBackup.zip")
        sftp.get(remotepath=download + latest, localpath=to + timern, callback=lambda x, y: progressbar(x, y))
        sftp.remove(remotefile=download + latest)
    print("Backup Completed! [" + time.strftime("%r::%d/%m/%y") + "]")
    print("===========================================================")
    time.sleep(hours * 3600)
