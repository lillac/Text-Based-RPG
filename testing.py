import worldspace, items, enemies, player
import glob, os
from os.path import basename

# BELOW - WORKING CODE, GENERATES A LIST OF ROOMS
jrooms = glob.glob('res/rooms/*.json')
rooms = []
for jfile in jrooms:
    room = worldspace.tile(jfile)
    rooms.append(room)

kt = rooms[0]
kt.enter()
