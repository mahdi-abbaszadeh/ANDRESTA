import xml.etree.ElementTree as ET

####################################
# global variables
row_no = 0
col_no = 0
link_bandwidth = 0
processor_load = 0
max_th = 0
desired_th = 0
num_of_graph_cycles = 0
cycles_times = 0
inStream = []
actor_load = []
number_of_actors = 0
links = [] #list of flows

####################################
####################################
####################################
def gen():

    applicationXML = ET.parse('../UserFiles/application.xml')
    applicationRoot = applicationXML.getroot()
    
    hardwareXML = ET.parse('../UserFiles/hw_conf.xml')
    hardwareRoot = hardwareXML.getroot()
    
    pfsXML = ET.parse('../UserFiles/prof_sch.xml')
    pfsRoot = pfsXML.getroot()
    
    ####################################
    # read hardware xml root
    for element in hardwareRoot:
        if element.tag == 'NoC':
            for subelement in element:
                if subelement.tag == 'RowNo':
                    row_no = subelement.text
                if subelement.tag == 'ColNo':
                    col_no = subelement.text
                    
    ####################################
    # read profiling & shceduling xml root
    for element in pfsRoot:
        if element.tag == 'link_bw':
            link_bandwidth = element.text
        if element.tag == 'processor_load':
            processor_load = element.text
        if element.tag == 'max_th':
            max_th = element.text
        if element.tag == 'desired_th':
            desired_th = element.text
        if element.tag == 'num_of_graph_cycles':
            num_of_graph_cycles = element.text
        if element.tag == 'cycles_times':
            cycles_times = element.text
        if element.tag == 'inStream':
            for subelement in element:
                inStream.append(subelement.text)
        if element.tag == 'actor_load':
            for subelement in element:
                actor_load.append(subelement.text)
    
    
    ####################################
    # read application xml root
    i = 0
    for element in applicationRoot:
        if element.tag == 'process':
            i = i + 1
        if element.tag == 'signal':
            src = int(element.get('source').split("_")[1])
            dst = int(element.get('target').split("_")[1])
            tmp = [src, dst]
            links.append(tmp)
    number_of_actors = i
    for i in range(0, len(links)): # we should add 1 to all proc numbers, because we do not have 0 in minizinc
        links[i][0] += 1
        links[i][1] += 1
            
    
    
    # print(number_of_actors)
    # print("links = ")
    # print(links)
    # print(link_bandwidth+" "+processor_load+" "+max_th+" "+desired_th+" "+num_of_graph_cycles+" "+cycles_times)
    # print("inStream = ")
    # print(inStream)
    # print("actor_load = ")
    # print(actor_load)
####################################
####################################
####################################

    s1 = ['row = ' + str(row_no) + ';\n',
            'col = ' + str(col_no) + ';\n',
            'no_links = 2*2*(row-1)*col;\n',
            'no_actors = ' + str(number_of_actors) + ';\n',
            'no_flows = ' + str(len(links)) + ';\n',
            'link_bandwidth = ' + str(link_bandwidth) + ';\n',
            'source_destination_actor = [| \n']
    
    s2 = []
    for i in range(0, len(links)):
        stmp = []
        if i == len(links) - 1:
            stmp = [str(links[i][0]) + ', ' + str(links[i][1]) + ' |']
        else:
            stmp = [str(links[i][0]) + ', ' + str(links[i][1]) + ' |\n']
        s2 += stmp
    s2 += ['];\nactor_processor = [\n']
    
    # we assume that all actors have output flow
    s3 = []
    for j in range(0, number_of_actors):
        stmp = []
        for i in range(0, len(links)):
            if links[i][0] == (j+1):
                stmp = ['flow_processor[' + str(i+1) +'],\n']
        s3 += stmp
    s3 += ['];\ninStream = [ \n']
    
    s4 = []
    for i in range(0, len(inStream)):
        s4 += [str(inStream[i]) + ', ']
    s4 += ['];\nb = [|\n']
    
    # creating b array for .dzn
    s5 = []
    zeros = []
    for i in range(0, int(col_no)*int(row_no)):
        zeros.append(0)
    for i in range(0, len(links)):
        stmp = []
        ztmp = ''
        for j in range(0, len(zeros)):
            ztmp += '0, '
        if i == len(links) - 1:
            stmp = [ztmp + 'inStream['+ str(i+1) +'], -inStream[' + str(i+1) +'] |']
        else:
            stmp = [ztmp + 'inStream['+ str(i+1) +'], -inStream[' + str(i+1) +'] |\n']
        s5 += stmp
    s5 += ['];\nflows = array2d(1..no_flows, 1..m,\n']
    
    s6 = []
    for i in range(0, len(links)):
        stmp = []
        if i == (len(links) - 1):
            stmp = ['[inFlow[' + str(i+1) + ',i] | i in 1..k] ++ [commFlow[' + str(i+1) + ',i] | i in 1..no_links] ++ [outFlow[' + str(i+1) + ',i] | i in 1..k] \n']
        else:
            stmp = ['[inFlow[' + str(i+1) + ',i] | i in 1..k] ++ [commFlow[' + str(i+1) + ',i] | i in 1..no_links] ++ [outFlow[' + str(i+1) + ',i] | i in 1..k] ++\n']
        s6 += stmp
    s6 += [');\nbalance = array2d(1..no_flows, 1..n, [b[i,j] | i in 1..no_flows, j in 1..n]);\nunit_cost = [\n']
    
    s7 = []
    ztmp1 = ''
    ztmp2 = ''
    ones = []
    for i in range(0, (2*2*(int(row_no)-1)*int(col_no))):
        ones.append(1)
    for i in range(0, len(zeros)):
        ztmp1 += '0, '
    for i in range(0, len(ones)):
        ztmp2 += '1, '
    s7 += [ztmp1 + ztmp2 + ztmp1 + '];\nprocessor_load = ' + str(processor_load) + ';\nactor_load = [']
    
    s8 = []
    for i in range(0, len(actor_load)):
        s8 += [str(actor_load[i]) + ', ']
    s8 += ['];\n\n']
    
    s9 = ['load = array2d(1..2, 1..no_flows,\n' +
            '[if (not exists (k in 1..i-1) (source_destination_actor[k,j+1] = source_destination_actor[i,j+1] \/\n'+
            'source_destination_actor[k,((j+1) mod 2) + 1] = source_destination_actor[i,j+1]))\n'+
            'then actor_load[source_destination_actor[i,j+1]] else 0 endif | j in 0..1, i in 1..no_flows]);\n\n']
        
    ####################################
    # P A Y    A T T E N T I O N
    ####################################
    # it just work for 2D mesh network for 2x2 nodes
    s10 = [
        'arc =[| 5, 1 | 5, 2 | 5, 3 | 5, 4 |\n'+
        '1, 2 | 1, 3 |\n'+
        '2, 1 | 2, 4 |\n'+
        '3, 1 | 3, 4 |\n'+
        '4, 2 | 4, 3 |\n'+
        '1, 6 | 2, 6 | 3, 6 | 4, 6 |];\n\n'
    ]
    
    s11 = [
        'in_connections = [if ((i mod 2) mod 2) = 0 then (k+1)+(i div (2*k)) else ((i div 2) mod k + 1) endif | i in 0..2*no_flows*k-1];\n'+
        'out_connections = [if ((i mod 2) mod 2) = 0 then ((i div 2) mod k + 1) else (k+no_flows+1)+(i div (2*k)) endif | i in 0..2*no_flows*k-1];\n'+
        'all_connections = array2d(1..2*no_flows*k+no_links, 1..2, in_connections ++ [arc[i,j] | i in k+1..no_links+k, j in 1..2] ++ out_connections);\n'+
        'total_flow = [flows[i,j] | i in 1..no_flows, j in 1..k] ++\n'+
        'comm_full ++\n'+
        '[flows[i,j] | i in 1..no_flows, j in k+no_links+1..2*k+no_links];\n'+
        'total_unit_cost = [0 | i in 1..no_flows, j in 1..k] ++ [ 1 | i in 1..no_links] ++ [0 | i in 1..no_flows, j in 1..k];\n'+
        'total_balance = [0 | i in 1..k] ++ [balance[i,j] | i in 1..no_flows, j in k+1..k+1] ++ [balance[i,j] | i in 1..no_flows, j in k+2..k+2];\n\n'
    ]
    
    s12 = [
        'max_th = ' + str(max_th) + ';\n'+
        'desired_th = ' + str(desired_th) + ';\n'+
        'num_of_graph_cycles = ' + str(num_of_graph_cycles) + ';\n'+
        'cycles_times = [' + str(cycles_times) + '];\n\n'
    ]
    
    file = open('datafile.dzn', 'w')
    Lines = s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8 + s9 + s10 + s11 + s12;
    file.writelines(Lines)
    
    # print("zeros = ")
    # print(zeros)

####################################
####################################
####################################
