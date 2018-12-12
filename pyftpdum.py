import os
import errno
import shutil
import sys
import click
import ftplib
import time
import multiprocessing

from yaml_storage import YamlStorage
from tinydb import TinyDB, Query


class PyftpdumConfig:
    """
    Contains the path, storage type, and default table name for
    the internal database.
    """

    def __init__(self, filepath, table, storage):
        self.filepath = filepath
        self.storage = storage
        self.table = table


def init(ctx, db_path='.pyftpdum/', db_table='downloads', db_filename='pyftpdum-db.yml', db_storage=YamlStorage):
    """
    Initialize the pyftpdum database. Called on every command
    issued with pyftpdum. If the file does not already exist,
    create it. Save the database information in the DBWrapper
    class, to be passed to the other commands.
    """
    if not os.path.exists(db_path):
        os.mkdir(db_path)
    db_filepath = os.path.join(db_path, db_filename)

    # Create files if they don't already exist
    with TinyDB(db_filepath, storage=db_storage, default_table=db_table):
        pass

    config = PyftpdumConfig(
        db_filepath, db_table, db_storage)
    ctx.obj = config  # Set the click context object

    return config


def index(db, destination):
    """
    Recursively index all folders in the final destination directory.
    Indexing assumes that these files have already been fully downloaded and unpacked
    """
    with TinyDB(db.filepath, storage=db.storage, default_table=db.table) as pyftpdum_db:
        pass


# def download(db, host, host_path, destination):
def download():
    """
    Recursively download all folders in the FTP directory,
    if their folder names do not already exist in the database.
    This prevents downloading the same file twice, even if it has
    been deleted on the destination drive.
    """
    # with TinyDB(db.filepath, storage=db.storage, default_table=db.table_name) as pyftpdum_db:
    #    pass
    #!/usr/bin/python

    server = "test"
    user = "test"
    password = "password"
    source = "/testsrc/"
    destination = "testdst/"
    interval = 0.05

    ftp = ftplib.FTP(server)
    ftp.login(user, password)
    print("downloading files...")
    downloadFiles(ftp, interval, source, destination)


def downloadFiles(ftp, interval, path, destination):
    try:
        ftp.cwd(path)
        mkdir_p(destination)
        os.chdir(destination)
        mkdir_p(destination[0:len(destination)-1] + path)
        print("Created: " + destination[0:len(destination)-1] + path)
    except OSError:
        pass
    except ftplib.error_perm:
        print("Error: could not change to " + path)
        sys.exit("Ending Application")

    log = []
    ftp.retrlines('LIST', callback=log.append)
    files = (' '.join(line.split()[8:]) for line in log)
    filelist = list(files)

    for file in filelist:
        time.sleep(interval)
        try:
            ftp.cwd(path + file + "/")
            downloadFiles(ftp, interval, path + file + "/", destination)
        except ftplib.error_perm:
            os.chdir(destination[0:len(destination)-1] + path)

            try:
                with open(os.path.join(destination + path, file), "wb") as dl:
                    ftp.retrbinary("RETR " + file, dl.write)
                print("Downloaded: " + file)
            except:
                print("Error: File could not be downloaded " +
                      file)
    return


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


def unpack(db, destination):
    """
    Recursively unpack all multi-rars in the destination directory.
    After the unpack is complete, delete the archive files.
    """
    with TinyDB(db.filepath, storage=db.storage, default_table=db.table_name) as pyftpdum_db:
        pass


def move(db, src, destination):
    """
    Recursively move all folders from the src to destination directory.
    """
    with TinyDB(db.filepath, storage=db.storage, default_table=db.table_name) as pyftpdum_db:
        pass
