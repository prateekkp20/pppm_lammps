import os
from lammps_logfile import File
from pathlib2 import Path 
import numpy as np
import pandas as pd

last = 10
E_coul = np.zeros(last-1)
E_long = np.zeros(last-1)
PotEng = np.zeros(last-1)

input = "exp1box45/out"
outputfile = "terminal_lammps.txt"  
os.system(f"echo {input} Files Simulation Lammps Output > {outputfile}")
os.system(f"echo  >> {outputfile}")

for i in range(1,last):
    search_txt = "read_data "+input+str(i-1)+".data"
    replace_txt = "read_data "+input+str(i)+".data"
    file = Path(r"in.input") 
    data = file.read_text() 
    data = data.replace(search_txt, replace_txt) 
    file.write_text(data) 

    run_lammps = 'lmp -in in.input'
    os.system(f"{run_lammps} >> {outputfile}")
    os.system(f"echo  >> {outputfile}")

    log = File("log.lammps")
    # print(log.get_keywords())
    E_coul[i-1] = log.get("E_coul")
    E_long[i-1] = log.get("E_long")
    PotEng[i-1] = log.get("PotEng")

    if i==last-1:
        file = Path(r"in.input")
        data = file.read_text() 
        end = "read_data "+input+str(0)+".data"
        data = data.replace(replace_txt, end)
        file.write_text(data)

os.system(f"rm {outputfile}")

data ={
    "Ecoul": E_coul,
    "Elong": E_long,
    "Total": PotEng
}

df= pd.DataFrame(data)
df.to_csv("energy45.csv")