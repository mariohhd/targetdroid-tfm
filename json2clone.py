################################################################################
# (c) 2013, COmputer SEcurity (COSEC) - Universidad Carlos III de Madrid
# Author: Guillermo Suarez de Tangil - guillermo.suarez.tangil@uc3m.es
################################################################################

import sys, json, getopt
from collections import OrderedDict
from modules.set_environment import set_environment
from modules.init_context import init_context
from modules.set_context import inject_events
from libraries.emulator import stop_emulator
import config

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
        print '----------------- ' + scenario['name'] + ' -----------------'
        events = scenario['time']
        for context in events:
            print '----------------- Time: ' + str(context['id']) + ' -----------------';
            if context['id'] == -1:
                set_environment(context)
            if context['id'] == 0:
                init_context(context)
            if context['id'] > 0:
                inject_events(context)
        stop_emulator()
    print '-------------- END --------------------'
except EOFError:
    print "Error: cannot open json file"
except:
    print "Unexpected error:", sys.exc_info()[0]
    stop_emulator()
    raise