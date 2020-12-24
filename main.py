import time

import actions
import db_transactions as db
from classes import Player,Product

main_actions = {"discover":actions.discover, "create":actions.create}
db_actions = {"create":db.upload_player,"download":db.download_player, "verify":db.verify_player}

print("Welcome to Delta Bot Resources!")
time.sleep(1)
print("Also known as DBR.")
time.sleep(1)
now = None
while True:
    now = input("Do you have an account?")
    if y in now:
        #do the log in routine
        break
    elif n in now:
        #do the create profile routine
        break
    else:
        print(Please enter a valid response...)

# logging_in = True
# while logging_in:
#     print("Welcome to Delta Bot Resources!")
#     time.sleep(1)
#     print("Also known as DBR.")
#     time.sleep(1)
#     if "y" in input("Do you have an account?"):
#         logu = input("Please enter your username:\n")
#         logp = input("Please enter your password:\n")
#         try:
#             now = db_actions["find"](logu,logp)
#             print(now[0])
#             player = Player(now[0],now[1])
#             player.resources = now[2]
#             player.products = now[3]

#         except:
#             print("Log in unsuccessful.")
#     else:
#         while True:
#             logu = input("Creating profile. Please enter a username:\n")
#             if db_actions["verify"](logu):
#                 print("This username already exists.")
#             logp = input("Please enter a password:\n")
#             log = Player(logu,logp)
#             db_actions["create"](log)
#             break

using = True
while using:
    print("Logging Out")
    using = False
