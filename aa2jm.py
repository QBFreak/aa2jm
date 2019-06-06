#!/usr/bin/env python

## aa2jm.py - Antique Atlas to JourneyMap waypoint converter for modded Minecract
#   v1.0 - QBFreak

from nbt import nbt

# Path to the Antique Atlas NBT file (something like world/data/aaMarkers_0.dat)
waypoints = "/path/to/Minecraft/SevTech_Ages-3.1.1/world/data/aaMarkers_0.dat"
# AA doesn't save the Y value, so pick something to stick in JM. If you've got
#  Slime Boots or anything else that negates fall damage, the top of the world
#  is probably the safest. In case you teleport there. You wont suffocate.
defaulty = 255

nbtfile = nbt.NBTFile(waypoints, 'rb')

converted = {}

template = ""

def write_marker(dimension, marker):
    ## Write a marker to it's own JourneyMap JSON file
    global template, defaulty
    json = template
    # Fill out the template
    json = json.replace('##ID##', str(marker["id"].value))
    json = json.replace('##NAME##', str(marker["label"].value))
    json = json.replace('##X##', str(marker["x"].value))
    json = json.replace('##Y##', str(defaulty))
    json = json.replace('##Z##', str(marker["y"].value))
    json = json.replace('##DIM##', str(dimension["dimID"].value))
    # Replace some of the AA unlocalized strings
    json = json.replace('gui.antiqueatlas.marker.netherPortal', "Portal")
    json = json.replace('gui.antiqueatlas.marker.tomb', "DEATH")
    # Write the new marker to a json file
    outfile = open("aa_import_{0}.json".format(marker["id"].value), 'w')
    outfile.write(json)
    outfile.close()

## Load the template JSON
with open('TEMPLATE.json', 'r') as templatefile:
    template = templatefile.read()

## Load the waypoints from the Antique Atlas NBT file
for dimension in nbtfile["data"]["dimMap"]:
    print("Dimension {0} has {1} markers:".format(dimension["dimID"], len(dimension["markers"])))
    for marker in dimension["markers"]:
        print("{1}\t{1}\t{2}\t{3}".format(marker["x"], marker["y"], marker["id"], marker["label"]))
        if marker["id"].value in converted:
            print("## WARNING: Duplicate marker ID {0}, skipping.".format(marker["id"]))
        else:
            write_marker(dimension, marker)
            converted[marker["id"].value] = marker["id"].value
