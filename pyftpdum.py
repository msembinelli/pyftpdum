import os
import shutil
import sys
import click
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


def download(db, host, host_path, destination):
    """
    Recursively download all folders in the FTP directory,
    if their folder names do not already exist in the database.
    This prevents downloading the same file twice, even if it has
    been deleted on the destination drive.
    """
    with TinyDB(db.filepath, storage=db.storage, default_table=db.table_name) as pyftpdum_db:
        pass


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
