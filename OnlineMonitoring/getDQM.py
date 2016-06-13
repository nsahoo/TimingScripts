#!/usr/env/python

import os
from ROOT import *

runs = [274998,274956,274958,274959,274968,274969,274971,274443,274442,274441,274440,274422,274421,274420,274388,274387,274345,274344,274338,274335,274319,274316,274315,274314,274286,274284,274282]
#runs = [274443,274442,274441,274440,274422,274421,274420,274388,274387,274345,274344,274338,274335,274319,274316,274315,274314,274286,274284,274282]

#for run in runs:
#    f = open("json_%i.txt" %run,"w")
#    f.write("{\"%i\":[[]]}\n")
#    f.close

for run in runs:
    #cd to event directory
    os.chdir('/afs/cern.ch/user/c/clint/Work/TimingValidation/DQMOnline/CMSSW_8_0_10_patch2/src/event_rootFiles')
    command ="python ../dqm-acces.py -s https://cmsweb.cern.ch/dqm/online/data/json -f \"/HLT/TimerService/*/event\" -e \"run == %i and match(\'/Global/Online/ALL\', dataset)\" -r -w" % run
    os.system(command)
    #cd to timing by ls
    os.chdir('/afs/cern.ch/user/c/clint/Work/TimingValidation/DQMOnline/CMSSW_8_0_10_patch2/src/timeByLs_rootFiles')
    command ="python ../dqm-acces.py -s https://cmsweb.cern.ch/dqm/online/data/json -f \"/HLT/TimerService/*/event_byls\" -e \"run == %i and match(\'/Global/Online/ALL\', dataset)\" -r -w" % run
    os.system(command)
    #cd to lumi directory
    os.chdir('/afs/cern.ch/user/c/clint/Work/TimingValidation/DQMOnline/CMSSW_8_0_10_patch2/src/lumi_rootFiles')
    command ="python ../dqm-acces.py -s https://cmsweb.cern.ch/dqm/online/data/json -f \"/Scal/LumiScalers/Instant_Lumi\" -e \"run == %i and match(\'/Global/Online/ALL\', dataset)\" -r -w" % run
    os.system(command)

