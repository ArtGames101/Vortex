try:
    from user import logindata as l
except:
    pass

try:
    NAMETAG = l.USERNAME
except:
    NAMETAG = None

#= -Settings- =#
# Download Games from the store
# Games:
# Snake
# BattleSim
# squirrel

currentgame = ""

