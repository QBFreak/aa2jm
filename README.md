# Antique Atlas to JourneyMap waypoint converter
Have you been playing SevTech: Ages, marked tons of stuff in your Antique Atlas, and then unlocked JourneyMap and realized that you're still tied to the Atlas for all the markers you made? I had that problem and hacked up a quick and dirty tool to convert the Antique Atlas waypoints to JourneyMap.

## Prerequisites
This makes use of the `nbt` package from PyPi
```
$ pip install nbt
```

## Installation
Download `aa2jm.py` and `TEMPLATE.json` and place both in an empty folder. Trust me. It'll make your life a lot easier if you do. JourneyMap uses a separate file for each marker. You're going to have a _lot_ of files when you're done.

## Configuration
Edit `aa2jm.py` and change the path in the `waypoints = ` line near the top. It should point to something like `world/data/aaMarkers_0.dat`

**Important:** If you run a separate server, your waypoints are stored on the server. You need to use `aaMarkers_0.dat` from the server in that case.

While you're editing `aa2jm.py`, you may wish to change `defaulty = 255` to some other value. The Antique Atlas only records `X` and `Z` coordinates. When converting to JourneyMap a `Y` value must be provided. I defaulted to `255` so that you wouldn't have to worry about suffocating in a wall should you teleport. The downside is that you will absolutely need something to negate fall damage :) You can change this value to any valid `Y` value.

Optionally, you may wish to edit `TEMPLATE.json` and change the `r`, `g`, and `b` values to tweak the color of your imported waypoints. The included template is a maroon color. Note that the RGB values are in decimal, not hex.

## Usage
You should not be connected to the game when you run this. The main menu is fine. JourneyMap will load the new waypoints when you connect.

```
$ python aa2jm.py
```

A listing of your waypoints will appear in the terminal as they are processed. Once the script has finished running, copy all the `aa_import_*.json` files to JourneyMap (but **NOT** `TEMPLATE.json`). JourneyMap keeps its waypoints in one of two places:

Single player: `minecraft/journeymap/data/sp/world/waypoints`

Server: `minecraft/journeymap/data/mp/world/waypoints`

You'll have to tweak the path a little depending on what exactly your map/server is named and where your Minecraft folder is located.

Once the `json` files are copied into the waypoints folder, you can connect to your game and open up your JourneyMap waypoints with `CTRL+B`. Everything from Antique Atlas should be there.

## Versions

This has been tested with SevTech: Ages 3.1.1, which includes Antique Atlas 4.5.0 and JourneyMap 5.5.4
