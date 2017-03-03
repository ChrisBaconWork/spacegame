# Spacegame

This is the canonical spacegame where you shoot things. There are now "capital ships", which have better armour.

## How to run

1. Clone and cd into the repo
2. Run `pip3 install -r requirements.txt` (you may need root privileges; if so, `sudo pip3 install -r requirements.txt`)
3. Run `./run.py`

(Previously, the executable was spacegame.py. But now that has been rewritten into Cython (the .pyx file), which is compiled into a shared object (the spacegame.so), which is used by run.py).

## Controls

A or D to move sidewards. Space to fire.

You can change the framerate, resolution, and music by amending `settings.json`.

## Design Choices

The game is written in a combination of Python and Cython. At the moment it sits at about 99% Python, but I plan on rewriting more and more of it into Cython.

## Assets

The enemy ships were created in Blender. I created the music using an online synthesizer.
