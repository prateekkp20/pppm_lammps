import os
from lammps_logfile import File
from pathlib2 import Path 
import numpy as np
import pandas as pd

def replace_line_in_file(file_path, start_words, new_line):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    modified_lines = []
    for line in lines:
        if line.startswith(start_words):
            modified_lines.append(new_line + '\n')
        else:
            modified_lines.append(line)

    with open(file_path, 'w') as file:
        file.writelines(modified_lines)

last = 28
Lx = np.zeros(last-1)
Ly = np.zeros(last-1)
Lz = np.zeros(last-1)
E_coul = np.zeros(last-1)
E_long = np.zeros(last-1)
PotEng = np.zeros(last-1)

input = "changesize/output"
outputfile = "terminal_lammps.txt"  
lammps_file = "in.input"

os.system(f"echo {input} Files Simulation Lammps Output > {outputfile}")
os.system(f"echo  >> {outputfile}")

for i in range(1,last):
    replace_line_in_file(lammps_file,"read_data "+input,"read_data "+input+str(i)+".data")

    run_lammps = 'lmp -in in.input'
    os.system(f"{run_lammps} >> {outputfile}")
    os.system(f"echo  >> {outputfile}")

    log = File("log.lammps")
    # print(log.get_keywords())
    E_coul[i-1] = log.get("E_coul")
    E_long[i-1] = log.get("E_long")
    PotEng[i-1] = log.get("PotEng")

os.system(f"rm {outputfile}")

data ={
    "Ecoul": E_coul,
    "Elong": E_long,
    "Total": PotEng
}

df= pd.DataFrame(data)
# df.to_csv("energy45.csv")