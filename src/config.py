from utils.dbconfig import dbconfig
from rich import print as printc
from rich.console import Console
import sys
import getpass
import hashlib
import random
import string

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
    printc("[green][+][/green] Database 'sw' created successfully ")

    #Create tables
    query='CREATE TABLES sw.secrets (masterpassword_hash TEXT NOT NULL, device_secret TEXT NOT NULL)'
    exec=cursor.execute(query)
    printc("[green][+][/green] Table 'secrets' created successfully ")

    query='CREATE TABLES sw.entries (site_name TEXT NOT NULL, url TEXT, email TEXT, username TEXT, password TEXT NOT NULL)'
    exec=cursor.execute(query)
    printc("[green][+][/green] Table 'entries ' created successfully ")

    mp=""
    while 1:
        mp=getpass("Enter a MASTER PASSWORD : ")
        if mp==getpass("Re-Type : ") and mp != "":
            break
        printc("[yellow][-] Please try again.[/yellow]")

    hash_mp=hashlib.sha256(mp.encode()).hexdigest()
    printc("[green][+][/green] Generated hash of MASTER PASSWORD")

    ds=''.join(random.choices(string.ascii_uppercase+string.digits,k=10))
    printc("[green][+][/green] Generated Device Secret.")

    query="INSERT INTO sw.secrets(masterkey_hash,device_secret) values (%s,%s)"
    val=(hash_mp,ds)
    cursor.execute(query,val)
    db.commit()

config()

