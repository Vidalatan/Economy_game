import os

def upload_player(player):
    with open('player_db.txt', 'a') as db:
        string = player.name + "|" + player.password + "|"
        now = ",".join(player.resources)
        string += (now+"|")
        now = ",".join(player.products)
        string += now
        db.write(string+"\n")

def download_player(player,password):
    with open('player_db.txt') as db:
        for x in db:
            if player in x:
                if player+"|"+password in x:
                    info = x.split("|")
                    return info
                else:
                    return "Password failed to match"
            else:
                return "Username failed to match"

def verify_player(player):
    with open('player_db.txt') as db:
        for x in db:
            if player in x:
                return True
            else:
                return False
