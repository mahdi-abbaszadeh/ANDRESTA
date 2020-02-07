import os

import cp_mdl_gnr
import download_engine
import node_engine
import packet_transaction_c_engine
import packet_transaction_h_engine
import sw_script_engine
import makfile_engine
import HardwareEngine
import subprocess


# This is top script which calls other scripts and results in *.sh files

os.chdir('../')
dirName = 'sw_scripts'
if not os.path.exists(dirName):
    os.mkdir(dirName)
    print("Directory "+dirName+" Created ")
else:
    print("Directory "+dirName+" already exists")


dirName = 'packet_transaction_lib'
if not os.path.exists(dirName):
    os.mkdir(dirName)
    print("Directory "+dirName+" Created ")
else:
    print("Directory "+dirName+" already exists")

os.chdir('templateEngine')
cp_mdl_gnr.gen()
HardwareEngine.gen()
packet_transaction_h_engine.gen()
packet_transaction_c_engine.gen()
node_engine.gen()
download_engine.gen()
sw_script_engine.gen()
makfile_engine.gen()

os.chdir('../')
CommandShellAddress = r'"D:\intelFPGA\17.1\nios2eds\Nios II Command Shell.bat"'
CMD = CommandShellAddress+ ' quartus_sh -t hw_scripts/synth.tcl'
subprocess.call(CMD, shell = True)

os.chdir('sw_scripts')
CMD = CommandShellAddress+ ' sh create_node_0.sh'
subprocess.call(CMD, shell = True)
CMD = CommandShellAddress+ ' sh create_node_1.sh'
subprocess.call(CMD, shell = True)
CMD = CommandShellAddress+ ' sh create_node_2.sh'
subprocess.call(CMD, shell = True)
CMD = CommandShellAddress+ ' sh create_node_3.sh'
subprocess.call(CMD, shell = True)

os.chdir('../')
CMD = CommandShellAddress+ ' sh download.sh'
subprocess.call(CMD, shell = True)



