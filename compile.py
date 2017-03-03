#! /usr/bin/env python3
import subprocess

subprocess.run(["python3", "setup.py", "build_ext", "--inplace"])
subprocess.run(["./rename.py"])
