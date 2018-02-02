"""
netparams.py

netParams is a dict containing a set of network parameters using a standardized structure

simConfig is a dict containing a set of simulation configurations using a standardized structure

Contributors: salvadordura@gmail.com
"""

from netpyne import specs

netParams = specs.NetParams()   # object of class NetParams to store the network parameters
simConfig = specs.SimConfig()   # object of class SimConfig to store the simulation configuration

###############################################################################
# POPULATION PARAMETERS
###############################################################################

#netParams.scaleConnWeight = 0.001 # Connection weight scale factor
# General network parameters
netParams.scale = 1 # Scale factor for number of cells
# TODO could not find information about distances on the plane
netParams.sizeX = 50 # x-dimension (horizontal length) size in um
netParams.sizeZ = 50 # z-dimension (horizontal depth) size in um
netParams.sizeY = 1350 # y-dimension (vertical height or cortical depth) size in um
netParams.propVelocity = 100.0 # propagation velocity (um/ms)
netParams.probLengthConstExc = 200.0 # length constant for conn probability (um)
netParams.probLengthConstInh = 300.0 # length constant for conn probability (um)

spkTimes = range(0,1000,20), range(0,1000,20)  # TODO report bug

# create list of pulses (each item is a dict with pulse params)
pulses = [{'start': 10, 'end': 100, 'rate': 200, 'noise': 0.5},
         {'start': 400, 'end': 500, 'rate': 1, 'noise': 0.0}]


# Population parameters
# TODO what to do with this?
netParams.popParams['PMd'] = {'cellModel': 'VecStim', 'spkTimes': spkTimes,
        'pulses': pulses, 'numCells': 96}
# TODO ASC is nsloc
netParams.popParams['ASC'] = {'cellModel': 'VecStim', 'spkTimes': spkTimes,
        'numCells': 64}

netParams.popParams['EDSC'] = {'cellModel': 'Izh2007b', 'cellType': 'PYR',
        'numCells': 64}
netParams.popParams['IDSC'] = {'cellModel': 'Izh2007b', 'cellType': 'PYR',
        'numCells': 64}
## L2/3 Cells
netParams.popParams['ER2'] = {'cellModel': 'Izh2007b', 'cellType': 'PYR',
        'numCells': 150}
netParams.popParams['IF2'] = {'cellModel': 'Izh2007b', 'cellType': 'PYR',
        'numCells': 25}
netParams.popParams['IL2'] = {'cellModel': 'Izh2007b', 'cellType': 'PYR',
        'numCells': 25}
## L5A Cells
netParams.popParams['ER5'] = {'cellModel': 'Izh2007b', 'cellType': 'PYR',
        'numCells': 168}
netParams.popParams['IL5'] = {'cellModel': 'Izh2007b', 'cellType': 'PYR',
        'numCells': 40}
netParams.popParams['IF5'] = {'cellModel': 'Izh2007b', 'cellType': 'PYR',
        'numCells': 40}
## L5B Cells
netParams.popParams['EB5'] = {'cellModel': 'Izh2007b', 'cellType': 'PYR',
        'numCells': 72}
## L6 Cells
netParams.popParams['ER6'] = {'cellModel': 'Izh2007b', 'cellType': 'PYR',
        'numCells': 192}
netParams.popParams['IF6'] = {'cellModel': 'Izh2007b', 'cellType': 'PYR',
        'numCells': 32}
netParams.popParams['IL6'] = {'cellModel': 'Izh2007b', 'cellType': 'PYR',
        'numCells': 32}

###############################################################################
# CELL PARAMETERS
###############################################################################

############ Izhi2007b (uses a section voltage)
## RS Izhi cell params
netParams.importCellParams(label='RS_Izhi', conds={'cellType': 'PYR', 'cellModel':'Izhi2007b'},
                fileName='izhi2007Wrapper.py', cellName='IzhiCell',  cellArgs={'type':'RS'})
## LTS Izhi cell params
netParams.importCellParams(label='LTS_Izhi', conds={'cellType': 'PYR', 'cellModel':'Izhi2007b'},
                fileName='izhi2007Wrapper.py', cellName='IzhiCell',  cellArgs={'type':'LTS'})
## FS Izhi cell params
netParams.importCellParams(label='FS_Izhi', conds={'cellType': 'PYR', 'cellModel':'Izhi2007b'},
                fileName='izhi2007Wrapper.py', cellName='IzhiCell',  cellArgs={'type':'FS'})
# Synaptic mechanism parameters
netParams.synMechParams['AMPA'] = {'mod': 'Exp2Syn', 'tau1': 0.05, 'tau2': 5.3, 'e': 0} # AMPA
netParams.synMechParams['NMDA'] = {'mod': 'Exp2Syn', 'tau1': 0.15, 'tau2': 1.50, 'e': 0} # NMDA
netParams.synMechParams['GABAA'] = {'mod': 'Exp2Syn', 'tau1': 0.07, 'tau2': 9.1, 'e': -80} # GABAA
# TODO the same as gabaa?
netParams.synMechParams['GABAB'] = {'mod': 'Exp2Syn', 'tau1': 0.07, 'tau2': 9.1, 'e': -80} # GABAA

cellRule = netParams.importCellParams(label='PMd_loc', conds={'cellModel':'VecStim'},
 	fileName='nsloc.py', cellName='nslocCell')
netParams.renameCellParamsSec('PMd', 'sec', 'soma')  # rename imported section 'sec' to 'soma'

###########################################
# STIMULATION PARAMETERS
###########################################
# background inputs
netParams.stimSourceParams['backgroundS'] = {'type': 'NetStim', 'rate': 100, 'noise': 1}
netParams.stimSourceParams['backgroundDSC'] = {'type': 'NetStim', 'interval': 0.1**-1*1e3, 'rate': 'variable', 'noise': 0.3}
netParams.stimSourceParams['backgroundEB5'] = {'type': 'NetStim', 'interval': 100**-1*1e3, 'rate': 'variable', 'noise': 1}
netParams.stimSourceParams['stimER2'] = {'type': 'NetStim', 'rate': 'variable', 'noise': 0} # stim inputs for EM (explor movs)

STDPparams = {'hebbwt': 0.00001, 'antiwt':-0.00001, 'wmax': 8, 'RLon': 1 , 'RLhebbwt': 0.001, 'RLantiwt': -0.000, \
    'tauhebb': 10, 'RLwindhebb': 50, 'useRLexp': 0, 'softthresh': 0, 'verbose':0}

netParams.stimTargetParams['bgS->ER2,ER5,ER6'] = {'source': 'backgroundS',
    'conds': {'pop': ['ER2', 'ER5','ER6']}, # background -> Exc
    'weight': 2,
    'delay': 2,
    'synMech': 'NMDA',
    'sec': 'soma'}

netParams.stimTargetParams['bgS->IF2,IL2,IF5,IL5,IF6,IL6'] = {'source': 'backgroundS',
    'conds': {'pop': ['IF2', 'IL2','IF5','IL5','IF6', 'IL6']}, # background -> Exc
    'weight': 2,
    'delay': 2,
    'synMech': 'NMDA',
    'sec': 'soma'}


netParams.stimTargetParams['bgDSC->EDSC,IDSC'] = {'source': 'backgroundDSC',
    'conds': {'pop': ['EDSC', 'IDSC']},  # Pstim_sh -> P_sh
    'weight': 4,
    'delay': 2,
    'synMech': 'NMDA',
    'sec': 'soma'}



netParams.stimTargetParams['bgEB5->EB5'] = {'source': 'backgroundEB5',
    'conds': {'pop': 'EB5'},  # Pstim_sh -> P_sh
    'weight': 4,
    'delay': 2,
    'synMech': 'NMDA',
    'sec': 'soma'}

netParams.stimTargetParams['stimER2->ER2'] = {'source': 'stimER2',
    'conds': {'pop': 'ER2'}, # EMstim-> EM
    'weight': 0.4,
    'delay': 'uniform(1,5)',
    'synMech': 'NMDA'}

###########################################
# CONNECTION PARAMETERS
###########################################
netParams.connParams['ER2->ER2'] = {
 'preConds': {'pop': 'ER2'}, 'postConds': {'pop': 'ER2'}, 
 'delay': '2+dist_3D/propVelocity',
 'weight': 0.66,
 'probability': '25*0.2*exp(-dist_3D/probLengthConstExc)',   # probability of connection
 'synMech': 'AMPA',
 'sec': 'soma'}

# Sensory
netParams.connParams['ER2->EB5'] = {
 'preConds': {'pop': 'ER2'}, 'postConds': {'pop': 'EB5'},  # P_sh,P_el -> ES
 'weight': 0.36,
 'probability': '25*1.6*exp(-dist_3D/probLengthConstExc)',
 'delay': '2+dist_3D/propVelocity',
 'synMech': 'AMPA',
 'sec': 'soma',
 'plast': {'mech': 'STDP', 'params': STDPparams}}

netParams.connParams['ER2->ER5'] = {
 'preConds': {'pop': 'ER2'}, 'postConds': {'pop': 'ER5'},  # ES -> ES
 'weight': 0.93,
 'probability': '25*1.6*exp(-dist_3D/probLengthConstExc)',
 'delay': '2+dist_3D/propVelocity',
 'synMech': 'AMPA',
 'sec': 'soma',
 'plast': {'mech': 'STDP', 'params': STDPparams}}


netParams.connParams['ER2->IL5'] = {
 'preConds': {'pop': 'ER2'}, 'postConds': {'pop': 'IL5'},  # ES -> ES
 'weight': 0.36,
 'probability': '25*0.51*exp(-dist_3D/probLengthConstExc)',
 'delay': '2+dist_3D/propVelocity',
 'synMech': 'AMPA',
 'sec': 'soma'}

netParams.connParams['ER2->ER6'] = {
 'preConds': {'pop': 'ER2'}, 'postConds': {'pop': 'IL5'},  # ES -> ES
 'weight': 0,
 'probability': 0,
 'delay': '2+dist_3D/propVelocity',
 'synMech': 'AMPA',
 'sec': 'soma'}

netParams.connParams['ER2->IL2'] = {
 'preConds': {'pop': 'ER2'}, 'postConds': {'pop': 'IL2'},  # ES -> ES
 'weight': 0.23,
 'probability': '25*0.51*exp(-dist_3D/probLengthConstExc)',
 'delay': '2+dist_3D/propVelocity',
 'synMech': 'AMPA',
 'sec': 'soma'}


netParams.connParams['ER2->IF2'] = {
 'preConds': {'pop': 'ER2'}, 'postConds': {'pop': 'IF2'},  # ES -> ES
 'weight': 0.23,
 'probability': '25*0.43*exp(-dist_3D/probLengthConstExc)',
 'delay': '2+dist_3D/propVelocity',
 'synMech': 'AMPA',
 'sec': 'soma'}

netParams.connParams['EB5->ER2'] = {
 'preConds': {'pop': 'EB5'}, 'postConds': {'pop': 'ER2'},  # ES -> ES
 'weight': 0,
 'probability': 0,
 'delay': '2+dist_3D/propVelocity',
 'synMech': 'AMPA',
 'sec': 'soma'}

netParams.connParams['EB5->EB5'] = {
 'preConds': {'pop': 'EB5'}, 'postConds': {'pop': 'EB5'},  # ES -> ES
 'weight': 0.66,
 'probability': '25*0.16*exp(-dist_3D/probLengthConstExc)',
 'delay': '2+dist_3D/propVelocity',
 'synMech': 'AMPA',
 'sec': 'soma'}


netParams.connParams['EB5->ER5'] = {
 'preConds': {'pop': 'EB5'}, 'postConds': {'pop': 'ER5'},  # ES -> ES
 'weight': 0,
 'probability': 0,
 'delay': '2+dist_3D/propVelocity',
 'synMech': 'AMPA',
 'sec': 'soma'}

netParams.connParams['EB5->ER6'] = {
 'preConds': {'pop': 'EB5'}, 'postConds': {'pop': 'ER6'},  # ES -> ES
 'weight': 0,
 'probability': 0,
 'delay': '2+dist_3D/propVelocity',
 'synMech': 'AMPA',
 'sec': 'soma'}


netParams.connParams['EB5->IL5'] = {
 'preConds': {'pop': 'EB5'}, 'postConds': {'pop': 'IL5'},  # ES -> ES
 'weight': 0,
 'probability': 0,
 'delay': '2+dist_3D/propVelocity',
 'synMech': 'AMPA',
 'sec': 'soma'}

netParams.connParams['EB5->IF5'] = {
 'preConds': {'pop': 'EB5'}, 'postConds': {'pop': 'IF5'},  # ES -> ES
 'weight': 0.23,
 'probability': '25*0.43*exp(-dist_3D/probLengthConstExc)',
 'delay': '2+dist_3D/propVelocity',
 'synMech': 'AMPA',
 'sec': 'soma'}

netParams.connParams['ER5->ER2'] = {
 'preConds': {'pop': 'ER5'}, 'postConds': {'pop': 'ER2'},  # ES -> ES
 'weight': 0.66,
 'probability': '25*0.2*exp(-dist_3D/probLengthConstExc)',
 'delay': '2+dist_3D/propVelocity',
 'synMech': 'AMPA',
 'sec': 'soma',
 'plast': {'mech': 'STDP', 'params': STDPparams}}

netParams.connParams['ER5->EB5'] = {
 'preConds': {'pop': 'ER5'}, 'postConds': {'pop': 'EB5'},  # ES -> ES
 'weight': 0.66,
 'probability': '25*0.84*exp(-dist_3D/probLengthConstExc)',
 'delay': '2+dist_3D/propVelocity',
 'synMech': 'AMPA',
 'sec': 'soma',
 'plast': {'mech': 'STDP', 'params': STDPparams}}


netParams.connParams['ER5->ER5'] = {
 'preConds': {'pop': 'ER5'}, 'postConds': {'pop': 'ER5'},  # ES -> ES
 'weight': 0.66,
 'probability': '25*0.44*exp(-dist_3D/probLengthConstExc)',
 'delay': '2+dist_3D/propVelocity',
 'synMech': 'AMPA',
 'sec': 'soma'}

netParams.connParams['ER5->ER6'] = {
 'preConds': {'pop': 'ER5'}, 'postConds': {'pop': 'ER6'},  # ES -> ES
 'weight': 0.66,
 'probability': '25*0.2*exp(-dist_3D/probLengthConstExc)',
 'delay': '2+dist_3D/propVelocity',
 'synMech': 'AMPA',
 'sec': 'soma'}

netParams.connParams['ER5->IL5'] = {
 'preConds': {'pop': 'ER5'}, 'postConds': {'pop': 'IL5'},  # ES -> ES
 'weight': 0,
 'probability': 0,
 'delay': '2+dist_3D/propVelocity',
 'synMech': 'AMPA',
 'sec': 'soma'}

netParams.connParams['ER5->IF5'] = {
 'preConds': {'pop': 'ER5'}, 'postConds': {'pop': 'IF5'},  # ES -> ES
 'weight': 0.46,
 'probability': '25*0.43*exp(-dist_3D/probLengthConstExc)',
 'delay': '2+dist_3D/propVelocity',
 'synMech': 'AMPA',
 'sec': 'soma'}

netParams.connParams['ER6->ER2'] = {
 'preConds': {'pop': 'ER6'}, 'postConds': {'pop': 'ER2'},  # ES -> ES
 'weight': 0,
 'probability': 0,
 'delay': '2+dist_3D/propVelocity',
 'synMech': 'AMPA',
 'sec': 'soma'}


netParams.connParams['ER6->EB5'] = {
 'preConds': {'pop': 'ER6'}, 'postConds': {'pop': 'EB5'},  # ES -> ES
 'weight': 0.66,
 'probability': '25*0.2*exp(-dist_3D/probLengthConstExc)',
 'delay': '2+dist_3D/propVelocity',
 'synMech': 'AMPA',
 'sec': 'soma'}

netParams.connParams['ER6->ER5'] = {
 'preConds': {'pop': 'ER6'}, 'postConds': {'pop': 'ER5'},  # ES -> ES
 'weight': 0.66,
 'probability': '25*0.2*exp(-dist_3D/probLengthConstExc)',
 'delay': '2+dist_3D/propVelocity',
 'synMech': 'AMPA',
 'sec': 'soma'}

netParams.connParams['ER6->ER6'] = {
 'preConds': {'pop': 'ER6'}, 'postConds': {'pop': 'ER6'},  # ES -> ES
 'weight': 0.66,
 'probability': '25*0.2*exp(-dist_3D/probLengthConstExc)',
 'delay': '2+dist_3D/propVelocity',
 'synMech': 'AMPA',
 'sec': 'soma'}

netParams.connParams['ER6->IL6'] = {
 'preConds': {'pop': 'ER6'}, 'postConds': {'pop': 'IL6'},  # ES -> ES
 'weight': 0.23,
 'probability': '25*0.51*exp(-dist_3D/probLengthConstExc)',
 'delay': '2+dist_3D/propVelocity',
 'synMech': 'AMPA',
 'sec': 'soma'}

netParams.connParams['ER6->IF6'] = {
 'preConds': {'pop': 'ER6'}, 'postConds': {'pop': 'IF6'},  # ES -> ES
 'weight': 0.23,
 'probability': '25*0.43*exp(-dist_3D/probLengthConstExc)',
 'delay': '2+dist_3D/propVelocity',
 'synMech': 'AMPA',
 'sec': 'soma'}

netParams.connParams['IL2->ER2'] = {
 'preConds': {'pop': 'IL2'}, 'postConds': {'pop': 'ER2'},  # ES -> ES
 'weight': 0.83,
 'probability': '25*0.35*exp(-dist_3D/probLengthConstInh)',
 'delay': '2+dist_3D/propVelocity',
 'synMech': 'GABAB',
 'sec': 'soma'}


netParams.connParams['IL2->IL2'] = {
 'preConds': {'pop': 'IL2'}, 'postConds': {'pop': 'IL2'},  # ES -> ES
 'weight': 1.5,
 'probability': '25*0.09*exp(-dist_3D/probLengthConstInh)',
 'delay': '2+dist_3D/propVelocity',
 'synMech': 'GABAB',
 'sec': 'soma'}


netParams.connParams['IL2->IF2'] = {
 'preConds': {'pop': 'IL2'}, 'postConds': {'pop': 'IF2'},  # ES -> ES
 'weight': 1.5,
 'probability': '25*0.53*exp(-dist_3D/probLengthConstInh)',
 'delay': '2+dist_3D/propVelocity',
 'synMech': 'GABAB',
 'sec': 'soma'}

netParams.connParams['IF2->ER2'] = {
 'preConds': {'pop': 'IF2'}, 'postConds': {'pop': 'ER2'}, 
 'delay': '2+dist_3D/propVelocity',
 'weight': 1.5,
 'probability': '25*.44*exp(-dist_3D/probLengthConstInh)',
 'synMech': 'GABAA',
 'sec': 'soma'}

netParams.connParams['IF2->IL2'] = {
 'preConds': {'pop': 'IF2'}, 'postConds': {'pop': 'IL2'}, 
 'delay': '2+dist_3D/propVelocity',
 'weight': 1.5,
 'probability': '25*.34*exp(-dist_3D/probLengthConstInh)',
 'synMech': 'GABAA',
 'sec': 'soma'}

netParams.connParams['IF2->IF2'] = {
 'preConds': {'pop': 'IF2'}, 'postConds': {'pop': 'IF2'}, 
 'delay': '2+dist_3D/propVelocity',
 'weight': 1.5,
 'probability': '25*.62*exp(-dist_3D/probLengthConstInh)',
 'synMech': 'GABAA',
 'sec': 'soma'}

netParams.connParams['IL5->EB5'] = {
 'preConds': {'pop': 'IL5'}, 'postConds': {'pop': 'EB5'}, 
 'delay': '2+dist_3D/propVelocity',
 'weight': .83,
 'probability': '25*.35*exp(-dist_3D/probLengthConstInh)',
 'synMech': 'GABAB',
 'sec': 'soma'}

netParams.connParams['IL5->ER5'] = {
 'preConds': {'pop': 'IL5'}, 'postConds': {'pop': 'ER5'}, 
 'delay': '2+dist_3D/propVelocity',
 'weight': .83,
 'probability': '25*.35*exp(-dist_3D/probLengthConstInh)',
 'synMech': 'GABAB',
 'sec': 'soma'}

netParams.connParams['IL5->IL5'] = {
 'preConds': {'pop': 'IL5'}, 'postConds': {'pop': 'IL5'}, 
 'delay': '2+dist_3D/propVelocity',
 'weight': 1.5,
 'probability': '25*.09*exp(-dist_3D/probLengthConstInh)',
 'synMech': 'GABAB',
 'sec': 'soma'}

netParams.connParams['IL5->IF5'] = {
 'preConds': {'pop': 'IL5'}, 'postConds': {'pop': 'IF5'}, 
 'delay': '2+dist_3D/propVelocity',
 'weight': 1.5,
 'probability': '25*.53*exp(-dist_3D/probLengthConstInh)',
 'synMech': 'GABAB',
 'sec': 'soma'}

netParams.connParams['IF5->EB5'] = {
 'preConds': {'pop': 'IF5'}, 'postConds': {'pop': 'EB5'}, 
 'delay': '2+dist_3D/propVelocity',
 'weight': 1.5,
 'probability': '25*.44*exp(-dist_3D/probLengthConstInh)',
 'synMech': 'GABAA',
 'sec': 'soma'}

netParams.connParams['IF5->ER5'] = {
 'preConds': {'pop': 'IF5'}, 'postConds': {'pop': 'ER5'}, 
 'delay': '2+dist_3D/propVelocity',
 'weight': 1.5,
 'probability': '25*.44*exp(-dist_3D/probLengthConstInh)',
 'synMech': 'GABAA',
 'sec': 'soma'}

netParams.connParams['IF5->IL5'] = {
 'preConds': {'pop': 'IF5'}, 'postConds': {'pop': 'IL5'}, 
 'delay': '2+dist_3D/propVelocity',
 'weight': 1.5,
 'probability': '25*.34*exp(-dist_3D/probLengthConstInh)',
 'synMech': 'GABAA',
 'sec': 'soma'}

netParams.connParams['IF5->IF5'] = {
 'preConds': {'pop': 'IF5'}, 'postConds': {'pop': 'IF5'}, 
 'delay': '2+dist_3D/propVelocity',
 'weight': 1.5,
 'probability': '25*.62*exp(-dist_3D/probLengthConstInh)',
 'synMech': 'GABAA',
 'sec': 'soma'}

netParams.connParams['IL6->ER6'] = {
 'preConds': {'pop': 'IL6'}, 'postConds': {'pop': 'ER6'}, 
 'delay': '2+dist_3D/propVelocity',
 'weight': .83,
 'probability': '25*.35*exp(-dist_3D/probLengthConstInh)',
 'synMech': 'GABAB',
 'sec': 'soma'}

netParams.connParams['IL6->IL6'] = {
 'preConds': {'pop': 'IL6'}, 'postConds': {'pop': 'IL6'}, 
 'delay': '2+dist_3D/propVelocity',
 'weight': 1.5,
 'probability': '25*.09*exp(-dist_3D/probLengthConstInh)',
 'synMech': 'GABAB',
 'sec': 'soma'}

netParams.connParams['IL6->IF6'] = {
 'preConds': {'pop': 'IL6'}, 'postConds': {'pop': 'IF6'}, 
 'delay': '2+dist_3D/propVelocity',
 'weight': 1.5,
 'probability': '25*.53*exp(-dist_3D/probLengthConstInh)',
 'synMech': 'GABAB',
 'sec': 'soma'}

netParams.connParams['IF6->ER6'] = {
 'preConds': {'pop': 'IF6'}, 'postConds': {'pop': 'ER6'}, 
 'delay': '2+dist_3D/propVelocity',
 'weight': 1.5,
 'probability': '25*.44*exp(-dist_3D/probLengthConstInh)',
 'synMech': 'GABAA',
 'sec': 'soma'}

netParams.connParams['IF6->IF6'] = {
 'preConds': {'pop': 'IF6'}, 'postConds': {'pop': 'IF6'}, 
 'delay': '2+dist_3D/propVelocity',
 'weight': 1.5,
 'probability': '25*.62*exp(-dist_3D/probLengthConstInh)',
 'synMech': 'GABAA',
 'sec': 'soma'}

netParams.connParams['ASC->ER2'] = {
 'preConds': {'pop': 'ASC'}, 'postConds': {'pop': 'ER2'}, 
 'delay': '2+dist_3D/propVelocity',
 'weight': 1.0,
 'probability': '25*.6*exp(-dist_3D/probLengthConstExc)',
 'synMech': 'AMPA',
 'sec': 'soma',
 'plast': {'mech': 'STDP', 'params': STDPparams}}

netParams.connParams['EB5->EDSC'] = {
 'preConds': {'pop': 'EB5'}, 'postConds': {'pop': 'EDSC'}, 
 'delay': '2+dist_3D/propVelocity',
 'weight': 2.0,
 'probability': '25*1.0*exp(-dist_3D/probLengthConstExc)',
 'synMech': 'AMPA',
 'sec': 'soma',
 'plast': {'mech': 'STDP', 'params': STDPparams}}

netParams.connParams['EB5->IDSC'] = {
 'preConds': {'pop': 'EB5'}, 'postConds': {'pop': 'IDSC'}, 
 'delay': '2+dist_3D/propVelocity',
 'weight': 0.5,
 'probability': 0,
 'synMech': 'AMPA',
 'sec': 'soma',
 'plast': {'mech': 'STDP', 'params': STDPparams}}

netParams.connParams['IDSC->EDSC'] = {
 'preConds': {'pop': 'IDSC'}, 'postConds': {'pop': 'EDSC'}, 
 'delay': '2+dist_3D/propVelocity',
 'weight': 0.5,
 'probability': 0,
 'synMech': 'AMPA',
 'sec': 'soma'}

netParams.connParams['PMd->ER5'] = {
 'preConds': {'pop': 'PMd'}, 'postConds': {'pop': 'ER5'}, 
 'delay': '2+dist_3D/propVelocity',
 'weight': 2.0,
 'probability': '25*2.0*exp(-dist_3D/probLengthConstExc)',
 'synMech': 'AMPA',
 'sec': 'soma',
 'plast': {'mech': 'STDP', 'params': STDPparams}}

###############################################################################
# SIMULATION PARAMETERS
###############################################################################

# Simulation parameters
# TODO following line doesnt appear to make a difference
#simConfig.duration = 3*1e3 # Duration of the simulation, in ms
simConfig.dt = 0.1 # Internal integration timestep to use
simConfig.seeds = {'conn': 1, 'stim': 1, 'loc': 1} # Seeds for randomizers (connectivity, input stimulation and cell locations)
simConfig.createNEURONObj = True  # create HOC objects when instantiating network
simConfig.createPyStruct = True  # create Python structure (simulator-independent) when instantiating network
simConfig.timing = True  # show timing  and save to file
simConfig.verbose = False # show detailed messages 

# Recording 
simConfig.recordCells = ['all']  # list of cells to record from 
simConfig.recordTraces = {}
# 'V':{'sec':'soma','loc':0.5,'var':'v'}, 
#     'u':{'sec':'soma', 'pointp':'Izhi', 'var':'u'}, 
#     'I':{'sec':'soma', 'pointp':'Izhi', 'var':'i'}, 
#     'NMDA_g': {'sec':'soma', 'loc':0.5, 'synMech':'NMDA', 'var':'g'},
#     'NMDA_i': {'sec':'soma', 'loc':0.5, 'synMech':'NMDA', 'var':'i'},
#     'GABA_g': {'sec':'soma', 'loc':0.5, 'synMech':'GABA', 'var':'g'},
#     'GABA_i': {'sec':'soma', 'loc':0.5, 'synMech':'GABA', 'var':'i'}}
simConfig.recordStim = True  # record spikes of cell stims
simConfig.recordStep = 1.0 # Step size in ms to save data (eg. V traces, LFP, etc)

# Saving
simConfig.filename = 'simdata'  # Set file output name
simConfig.saveFileStep = 1000 # step size in ms to save data to disk
simConfig.savePickle = False # Whether or not to write spikes etc. to a .mat file
simConfig.saveJson = False # Whether or not to write spikes etc. to a .mat file
simConfig.saveMat = True # Whether or not to write spikes etc. to a .mat file
simConfig.saveTxt = False # save spikes and conn to txt file
simConfig.saveDpk = False # save to a .dpk pickled file


# Analysis and plotting
simConfig.analysis['plotRaster'] = True # Whether or not to plot a raster

