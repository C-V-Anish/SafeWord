from utils.dbconfig import dbconfig
from rich import print as printc
from rich.console import Console
import sys
console=Console()

def config():
    #Create a Database
    db=dbconfig()
    cursor=db.cursor()

    try:
        cursor.execute("CREATE DATABASE sw")
    except Exception as e:
        printc("[red][!]An error ocurred while trying to create db.")
        console.print_exception(show_locals=True)
        sys.exit(0)
    printc("[green][+][/green] Database 'pm' created successfully ")

    #Create tables
    query='CREATE TABLES sw.secrets (masterpassword_hash TEXT NOT NULL, device_secret TEXT NOT NULL)'
    exec=cursor.execute(query)
    printc("[green][+][/green] Table 'secrets' created successfully ")

    query='CREATE TABLES sw.secrets (site_name TEXT NOT NULL, url TEXT, email TEXT, username TEXT, password TEXT NOT NULL)'
    exec=cursor.execute(query)
    printc("[green][+][/green] Table 'entries ' created successfully ")
