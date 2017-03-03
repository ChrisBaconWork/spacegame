#! /usr/bin/env python3
import os

for fn in os.listdir("."):
    if fn == "spacegame.so":
        os.remove("spacegame.so")
    if fn == "spacegame.cpython-35m-x86_64-linux-gnu.so":
        os.rename("spacegame.cpython-35m-x86_64-linux-gnu.so", "spacegame.so")
