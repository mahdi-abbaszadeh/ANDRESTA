# TCL File Generated by Component Editor 17.1
# Sat Aug 17 16:20:28 IRDT 2019
# DO NOT MODIFY


# 
# NoC "NoC" v1.0
#  2019.08.17.16:20:28
# 
# 

# -----------------------------------------------------------------
# Script Arguments/Defaults
# -----------------------------------------------------------------
#
if {![info exists quartus_version]} {
	set quartus_version 14.0
}


# 
# request TCL package from ACDS 16.1
# 
package require -exact qsys $quartus_version


# 
# module NoC
# 
set_module_property DESCRIPTION ""
set_module_property NAME NoC
set_module_property VERSION 1.0
set_module_property INTERNAL false
set_module_property OPAQUE_ADDRESS_MAP true
set_module_property GROUP "My Own IP Cores"
set_module_property AUTHOR ""
set_module_property DISPLAY_NAME NoC
set_module_property INSTANTIATE_IN_SYSTEM_MODULE true
set_module_property EDITABLE true
set_module_property REPORT_TO_TALKBACK false
set_module_property ALLOW_GREYBOX_GENERATION false
set_module_property REPORT_HIERARCHY false


# 
# file sets
# 
add_fileset QUARTUS_SYNTH QUARTUS_SYNTH "" ""
set_fileset_property QUARTUS_SYNTH TOP_LEVEL wrapper
set_fileset_property QUARTUS_SYNTH ENABLE_RELATIVE_INCLUDE_PATHS false
set_fileset_property QUARTUS_SYNTH ENABLE_FILE_OVERWRITE_MODE false
add_fileset_file wrapper.v VERILOG PATH "hw_sources/wrapper.v" TOP_LEVEL_FILE
add_fileset_file Computation.vhd VHDL PATH "hw_sources/Computation.vhd"
add_fileset_file ConnectionPack.vhd VHDL PATH "hw_sources/ConnectionPack.vhd"
add_fileset_file FilePack.vhd VHDL PATH "hw_sources/FilePack.vhd"
add_fileset_file NOC.vhd VHDL PATH "hw_sources/NOC.vhd"
add_fileset_file Node.vhd VHDL PATH "hw_sources/Node.vhd"
add_fileset_file RouterA.vhd VHDL PATH "hw_sources/RouterA.vhd"

add_fileset SIM_VERILOG SIM_VERILOG "" ""
set_fileset_property SIM_VERILOG TOP_LEVEL wrapper
set_fileset_property SIM_VERILOG ENABLE_RELATIVE_INCLUDE_PATHS false
set_fileset_property SIM_VERILOG ENABLE_FILE_OVERWRITE_MODE false
add_fileset_file wrapper.v VERILOG PATH "hw_sources/wrapper.v"
add_fileset_file Computation.vhd VHDL PATH "hw_sources/Computation.vhd"
add_fileset_file ConnectionPack.vhd VHDL PATH "hw_sources/ConnectionPack.vhd"
add_fileset_file FilePack.vhd VHDL PATH "hw_sources/FilePack.vhd"
add_fileset_file NOC.vhd VHDL PATH "hw_sources/NOC.vhd"
add_fileset_file Node.vhd VHDL PATH "hw_sources/Node.vhd"
add_fileset_file RouterA.vhd VHDL PATH "hw_sources/RouterA.vhd"


# 
# parameters
#
add_parameter RowNo INTEGER @NoC.RowNo
set_parameter_property RowNo DEFAULT_VALUE 2
set_parameter_property RowNo DISPLAY_NAME RowNo
set_parameter_property RowNo TYPE INTEGER
set_parameter_property RowNo UNITS None
set_parameter_property RowNo ALLOWED_RANGES -2147483648:2147483647
set_parameter_property RowNo HDL_PARAMETER true

add_parameter ColNo INTEGER @NoC.ColNo
set_parameter_property ColNo DEFAULT_VALUE 2
set_parameter_property ColNo DISPLAY_NAME ColNo
set_parameter_property ColNo TYPE INTEGER
set_parameter_property ColNo UNITS None
set_parameter_property ColNo ALLOWED_RANGES -2147483648:2147483647
set_parameter_property ColNo HDL_PARAMETER true 

add_parameter PackWidth INTEGER @NoC.PackWidth
set_parameter_property PackWidth DEFAULT_VALUE 8
set_parameter_property PackWidth DISPLAY_NAME PackWidth
set_parameter_property PackWidth TYPE INTEGER
set_parameter_property PackWidth UNITS None
set_parameter_property PackWidth ALLOWED_RANGES -2147483648:2147483647
set_parameter_property PackWidth HDL_PARAMETER true

add_parameter DataWidth INTEGER @NoC.DataWidth
set_parameter_property DataWidth DEFAULT_VALUE 8
set_parameter_property DataWidth DISPLAY_NAME DataWidth
set_parameter_property DataWidth TYPE INTEGER
set_parameter_property DataWidth UNITS None
set_parameter_property DataWidth ALLOWED_RANGES -2147483648:2147483647
set_parameter_property DataWidth HDL_PARAMETER true

add_parameter AddrWidth INTEGER @NoC.AddrWidth
set_parameter_property AddrWidth DEFAULT_VALUE 2
set_parameter_property AddrWidth DISPLAY_NAME AddrWidth
set_parameter_property AddrWidth TYPE INTEGER
set_parameter_property AddrWidth UNITS None
set_parameter_property AddrWidth ALLOWED_RANGES -2147483648:2147483647
set_parameter_property AddrWidth HDL_PARAMETER true

add_parameter RoChAddr INTEGER @NoC.RoChAddr
set_parameter_property RoChAddr DEFAULT_VALUE 1
set_parameter_property RoChAddr DISPLAY_NAME RoChAddr
set_parameter_property RoChAddr TYPE INTEGER
set_parameter_property RoChAddr UNITS None
set_parameter_property RoChAddr ALLOWED_RANGES -2147483648:2147483647
set_parameter_property RoChAddr HDL_PARAMETER true

add_parameter PhyChAddr INTEGER @NoC.PhyChAddr
set_parameter_property PhyChAddr DEFAULT_VALUE 2
set_parameter_property PhyChAddr DISPLAY_NAME PhyChAddr
set_parameter_property PhyChAddr TYPE INTEGER
set_parameter_property PhyChAddr UNITS None
set_parameter_property PhyChAddr ALLOWED_RANGES -2147483648:2147483647
set_parameter_property PhyChAddr HDL_PARAMETER true

add_parameter ViChAddr INTEGER @NoC.ViChAddr
set_parameter_property ViChAddr DEFAULT_VALUE 1
set_parameter_property ViChAddr DISPLAY_NAME ViChAddr
set_parameter_property ViChAddr TYPE INTEGER
set_parameter_property ViChAddr UNITS None
set_parameter_property ViChAddr ALLOWED_RANGES -2147483648:2147483647
set_parameter_property ViChAddr HDL_PARAMETER true

add_parameter PhyRoChAddr INTEGER @NoC.PhyRoChAddr
set_parameter_property PhyRoChAddr DEFAULT_VALUE 3
set_parameter_property PhyRoChAddr DISPLAY_NAME PhyRoChAddr
set_parameter_property PhyRoChAddr TYPE INTEGER
set_parameter_property PhyRoChAddr UNITS None
set_parameter_property PhyRoChAddr ALLOWED_RANGES -2147483648:2147483647
set_parameter_property PhyRoChAddr HDL_PARAMETER true

add_parameter RoCh INTEGER @NoC.RoCh
set_parameter_property RoCh DEFAULT_VALUE 1
set_parameter_property RoCh DISPLAY_NAME RoCh
set_parameter_property RoCh TYPE INTEGER
set_parameter_property RoCh UNITS None
set_parameter_property RoCh ALLOWED_RANGES -2147483648:2147483647
set_parameter_property RoCh HDL_PARAMETER true

add_parameter PhyCh INTEGER @NoC.PhyCh
set_parameter_property PhyCh DEFAULT_VALUE 4
set_parameter_property PhyCh DISPLAY_NAME PhyCh
set_parameter_property PhyCh TYPE INTEGER
set_parameter_property PhyCh UNITS None
set_parameter_property PhyCh ALLOWED_RANGES -2147483648:2147483647
set_parameter_property PhyCh HDL_PARAMETER true

add_parameter ViCh INTEGER @NoC.ViCh
set_parameter_property ViCh DEFAULT_VALUE 1
set_parameter_property ViCh DISPLAY_NAME ViCh
set_parameter_property ViCh TYPE INTEGER
set_parameter_property ViCh UNITS None
set_parameter_property ViCh ALLOWED_RANGES -2147483648:2147483647
set_parameter_property ViCh HDL_PARAMETER true

add_parameter PhyRoCh INTEGER @NoC.PhyRoCh
set_parameter_property PhyRoCh DEFAULT_VALUE 5
set_parameter_property PhyRoCh DISPLAY_NAME PhyRoCh
set_parameter_property PhyRoCh TYPE INTEGER
set_parameter_property PhyRoCh UNITS None
set_parameter_property PhyRoCh ALLOWED_RANGES -2147483648:2147483647
set_parameter_property PhyRoCh HDL_PARAMETER true


# 
# display items
# 


# 
# connection point reset
# 
add_interface reset reset end
set_interface_property reset associatedClock clock
set_interface_property reset synchronousEdges DEASSERT
set_interface_property reset ENABLED true
set_interface_property reset EXPORT_OF ""
set_interface_property reset PORT_NAME_MAP ""
set_interface_property reset CMSIS_SVD_VARIABLES ""
set_interface_property reset SVD_ADDRESS_GROUP ""

add_interface_port reset reset reset Input 1

#for @tile in @tiles:

# 
# connection point sink_@{tile.number}
# 
add_interface sink_@{tile.number} avalon_streaming end
set_interface_property sink_@{tile.number} associatedClock clock
set_interface_property sink_@{tile.number} associatedReset reset
set_interface_property sink_@{tile.number} dataBitsPerSymbol 8
set_interface_property sink_@{tile.number} errorDescriptor ""
set_interface_property sink_@{tile.number} firstSymbolInHighOrderBits true
set_interface_property sink_@{tile.number} maxChannel 0
set_interface_property sink_@{tile.number} readyLatency 0
set_interface_property sink_@{tile.number} ENABLED true
set_interface_property sink_@{tile.number} EXPORT_OF ""
set_interface_property sink_@{tile.number} PORT_NAME_MAP ""
set_interface_property sink_@{tile.number} CMSIS_SVD_VARIABLES ""
set_interface_property sink_@{tile.number} SVD_ADDRESS_GROUP ""

add_interface_port sink_@{tile.number} PE@{tile.number}_OutpData data Input DataWidth
add_interface_port sink_@{tile.number} PE@{tile.number}_OutpEn valid Input 1
add_interface_port sink_@{tile.number} PE@{tile.number}_OutpReady ready Output 1
add_interface_port sink_@{tile.number} PE@{tile.number}_OutpSel channel Input ViChAddr

#end

#for @tile in @tiles:

# 
# connection point source_@tile.number
# 
add_interface source_@{tile.number} avalon_streaming start
set_interface_property source_@{tile.number} associatedClock clock
set_interface_property source_@{tile.number} associatedReset reset
set_interface_property source_@{tile.number} dataBitsPerSymbol 8
set_interface_property source_@{tile.number} errorDescriptor ""
set_interface_property source_@{tile.number} firstSymbolInHighOrderBits true
set_interface_property source_@{tile.number} maxChannel 0
set_interface_property source_@{tile.number} readyLatency 0
set_interface_property source_@{tile.number} ENABLED true
set_interface_property source_@{tile.number} EXPORT_OF ""
set_interface_property source_@{tile.number} PORT_NAME_MAP ""
set_interface_property source_@{tile.number} CMSIS_SVD_VARIABLES ""
set_interface_property source_@{tile.number} SVD_ADDRESS_GROUP ""

add_interface_port source_@{tile.number} PE@{tile.number}_InpData data Output DataWidth
add_interface_port source_@{tile.number} PE@{tile.number}_InpEn valid Output 1
add_interface_port source_@{tile.number} PE@{tile.number}_InpReady ready Input 1
add_interface_port source_@{tile.number} PE@{tile.number}_InpSel channel Output ViChAddr

#end

# 
# connection point clock
# 
add_interface clock clock end
set_interface_property clock clockRate 0
set_interface_property clock ENABLED true
set_interface_property clock EXPORT_OF ""
set_interface_property clock PORT_NAME_MAP ""
set_interface_property clock CMSIS_SVD_VARIABLES ""
set_interface_property clock SVD_ADDRESS_GROUP ""

add_interface_port clock clock clk Input 1

