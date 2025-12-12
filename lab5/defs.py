import re
import subprocess
def cmd_getproperties_stdout(process_id):
    command = ['wmic', 'process', 'where', f"ProcessId={process_id}", 'get',
                'Name,ExecutablePath,CommandLine,ParentProcessId', '/format:list']
    
    result = subprocess.run(command, capture_output=True, encoding='cp866')
    c = result.stdout.strip()
    c = c.splitlines()
    for i in range(len(c)//2):
        c.remove('')
    
    result = []
    
    for i in c:
        localdict = {}
        regex = re.search('(?P<name>.*)=(?P<value>.*)', i)
        localdict[regex.group('name')] = regex.group('value')

        result.append(localdict)
    
    return result

def cmd_getprocesslist_stdout(command): #command for cmd
    result = subprocess.run(command, capture_output=True, encoding='cp866')
    return result.stdout

def make_splitline_from_stdout(cmd_stdout):
    result = cmd_stdout.splitlines()
    return result

def structurize_list(processlist_raw):
    result = []
    pattern_nospace = r'\S{0,}'

    for i in processlist_raw:
            f = re.findall(pattern_nospace, str(i))
            f = [x for x in f if x]
            result.append(f)

    return result

def remove_duplicates(structurized_list):
    pattern_noduplicates = r'(0.0.0.0.0)'
    result = []

    for i in range(0, len(structurized_list)):
        if len(re.findall(pattern_noduplicates, structurized_list[i][2])) != 0:
            result.append(structurized_list[i])

    return result

def get_processlist(command:list = ['cmd','/c','netstat -ano | findstr /I LISTENING']):
    processlist_stdout = cmd_getprocesslist_stdout(command)

    processlist_raw = make_splitline_from_stdout(processlist_stdout)

    structurized_list = structurize_list(processlist_raw)

    result = remove_duplicates(structurized_list)

    return result

def form_filtered_dict(whitelist:list, command = ['cmd','/c','netstat -ano | findstr /I LISTENING']):
    final_dict = form_final_dict(command)
    filtered_dict = {}
    for i in final_dict:
        if not(i in whitelist):
            filtered_dict[i] = final_dict[i]
    return filtered_dict

def form_final_dict(command:list = ['cmd','/c','netstat -ano | findstr /I LISTENING']):
    processlist = get_processlist(command)
    dictionary = {}
    for i in processlist:
        dictionary[i[4]] = {'Type':i[0], 'ip1':i[1], 'ip2':i[2], 'status':i[3]}
    for i in dictionary:
        for k in cmd_getproperties_stdout(i):
            dictionary[i].update(k)
    return dictionary