import subprocess
import xml.etree.ElementTree as ET

def run_minizinc():
    # IDE_PATH = 'export PATH=/Applications/MiniZincIDE.app/Contents/Resources:$PATH'
    COMPILE_CMD = 'minizinc --solver Gecode -o result.txt mapping.mzn datafile.dzn'
    
    CMD = COMPILE_CMD
    
    subprocess.call(CMD, shell = True)
    
def run():
    
    output_read_tmp = []
    output_read = []
    with open('result.txt', 'r') as f:
         output_read_tmp = f.read().split("\n")
    for i in range(0, len(output_read_tmp) - 3):
        output_read.append(int(output_read_tmp[i]))
    
    ##########################
    # generating mapping XML file
    s1 = ['<mappings>\n']
    for i in range(0, len(output_read)):
        stmp = ['<process_mapping name="proc_' + str(i) + '" target="node_' + str(output_read[i] - 1) + '" cpuName="nios"/>\n']
        s1 += stmp
    s1 += ['</mappings>\n']
    
    file = open('../UserFiles/mapping.xml', 'w')
    Lines = s1;
    file.writelines(Lines)
    
    ##########################
    # modifying application XML file
    applicationTree = ET.parse('../UserFiles/application.xml')
    applicationRoot = applicationTree.getroot()
    
    i = 0
    for scfile in applicationRoot.iter('source_file'):
        scfile.set('name', 'node_' + str(output_read[i] - 1))
        i += 1
    
    applicationTree.write('../UserFiles/application.xml')
    
#run_minizinc()
#run()
