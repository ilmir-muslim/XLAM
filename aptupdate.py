import subprocess
import os


process = subprocess.run(['sudo', 'apt', 'update'])
process = subprocess.run(['sudo', 'apt', 'upgrade'])
process = subprocess.run(['sudo', 'apt', 'autoremove'])
