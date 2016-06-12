################################################################################
# (c) 2013, COmputer SEcurity (COSEC) - Universidad Carlos III de Madrid
# Author: Guillermo Suarez de Tangil - guillermo.suarez.tangil@uc3m.es
################################################################################

import sys, json, getopt
from collections import OrderedDict
from config_environment import config_environment
from config_os import config_os
from json2telnet import set_context
from collections import OrderedDict
from emulator import stop_emulator
import config


# -----------------------
# Constants
# -----------------------


# -----------------------
# Functions
# -----------------------


# -----------------------
# Params
# -----------------------


input_file = ''
duration = 0
argv = sys.argv
try:
    opts, args = getopt.getopt(argv[1:],"hf:e:p:i",["file=","emulator=","port=","ip="])
except getopt.GetoptError:
    print 'main.py - h -f <file> [-e <emulator>] [-i <ip>] [-p <port>]'
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print 'main.py -h -f <file> [-e <emulator>] [-p <port>]'
        sys.exit()
    elif opt in ("-f", "--file"):
        input_file = arg
    elif opt in ("-e", "--emulator"):
        config.set('emulator', arg)
    elif opt in ("-p", "--port"):
        config.set('port', arg)
    elif opt in ("-i", "--ip"):
        config.set('ip', arg)

# -----------------------
# Main
# -----------------------

try:
    with open(input_file) as file:
        scenarios = json.load(file, object_pairs_hook=OrderedDict)
    for scenario in scenarios:
        print '-----------------'+scenario+'----------------'
        events = scenarios[scenario]
        for context in events:
            print '---------------------- time ' + str(context['t']) +'------------------';
            if context['t'] == -1:
                config_environment(context)
            if context['t'] == 0:
                config_os(context)
            if context['t'] > 0:
                set_context(context)
        stop_emulator()
    print '-------------FIN-------------------'
except EOFError:
    print "Error: cannot open json file"