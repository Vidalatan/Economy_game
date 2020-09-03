import time

import actions
import db_transactions as db
from classes import Player,Product

main_actions = {"discover":actions.discover, "create":actions.create}
db_actions = {"create":db.upload_player,"find":db.download_player}

logging_in = True
while logging_in:
    print("Welcome to Delta Bot Resources!")
    time.sleep(1)
    print("Also known as DBR.")
    time.sleep(1)
    if "y" in input("Do you have an account?"):
        logu = input("Please enter your username:\n")
        logp = input("Please enter your password:\n")
        try:
            now = db_actions["find"](logu,logp)
            player = Player(now[0],now[1])
            player.resources = now[2]
            player.products = now[3]
            logging_in = False

        except:
            print("Log in unsuccessful.")
    else:
        logu = input("Creating profile. Please enter a username:\n")
        logp = input("Please enter a password:\n")
        log = Player(logu,logp)
        db_actions["create"](log)

using = True
while using:
    print("Logging Out")
    using = False
