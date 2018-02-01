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
netParams.popParams['PMd'] = {'cellModel': 'VecStim', 'spkTimes': spkTimes,
        'pulses': pulses, 'numCells': 96, 'ynormRange':[-1, -1]}
# TODO ASC is nsloc
netParams.popParams['ASC'] = {'cellModel': 'VecStim', 'cellType': 'RTN',
        'numCells': 64, 'ynormRange':[-1, -1]}
netParams.popParams['EDSC'] = {'cellModel': 'Izh2007a', 'cellType': 'PYR',
        'numCells': 64, 'ynormRange':[-1, -1]}
netParams.popParams['IDSC'] = {'cellModel': 'Izh2007a', 'cellType': 'PYR',
        'numCells': 64,'ynormRange':[-1, -1]}
## L2/3 Cells
netParams.popParams['ER2'] = {'cellModel': 'Izh2007a', 'cellType': 'PYR',
        'numCells': 150, 'ynormRange':[0.1, 0.31]}
netParams.popParams['IF2'] = {'cellModel': 'Izh2007a', 'cellType': 'PYR',
        'numCells': 25,  'ynormRange':[0.1, 0.31]}
netParams.popParams['IL2'] = {'cellModel': 'Izh2007a', 'cellType': 'PYR',
        'numCells': 25, 'ynormRange':[0.1, 0.31]}
## L5A Cells
netParams.popParams['ER5'] = {'cellModel': 'Izh2007a', 'cellType': 'PYR',
        'numCells': 168, 'ynormRange':[0.31, 0.52]}
netParams.popParams['IL5'] = {'cellModel': 'Izh2007a', 'cellType': 'PYR',
        'numCells': 40, 'ynormRange':[0.31, 0.77]}
netParams.popParams['IF5'] = {'cellModel': 'Izh2007a', 'cellType': 'PYR',
        'numCells': 40, 'ynormRange':[0.31, 0.77]}
## L5B Cells
netParams.popParams['EB5'] = {'cellModel': 'Izh2007a', 'cellType': 'PYR',
        'numCells': 72, 'ynormRange':[0.52, 0.77]}
## L6 Cells
netParams.popParams['ER6'] = {'cellModel': 'Izh2007a', 'cellType': 'PYR',
        'numCells': 192, 'ynormRange':[0.77, 1.00]}
netParams.popParams['IF6'] = {'cellModel': 'Izh2007a', 'cellType': 'PYR',
        'numCells': 32, 'ynormRange':[0.77, 1.00]}
netParams.popParams['IL6'] = {'cellModel': 'Izh2007a', 'cellType': 'PYR',
        'numCells': 32, 'ynormRange':[0.77, 1.00]}
# TODO This one just to avoid error
netParams.popParams['EM'] = {'cellModel': 'Izhi', 'cellType': 'RS',
        'numCells': 80} # add dict with params for this pop 

#netParams.popParams['artif3'] = {'cellModel': 'VecStim', 'numCells': 50, 'spkTimes': spkTimes, 'pulses': pulses}



# Izhi cell params (used in cell properties)

###############################################################################
# CELL PARAMETERS
###############################################################################

## Izhi2007a (independent voltage)
cellRule = netParams.importCellParams(label='RS_Izhi', conds={'cellType': 'PYR', 'cellModel':'Izh2007a'},
	fileName='izhi2007Wrapper.py', cellName='IzhiCell',  cellArgs={'type':'RS', 'host':'dummy'})
netParams.renameCellParamsSec('RS_Izhi', 'sec', 'soma')  # rename imported section 'sec' to 'soma'
cellRule['secs']['soma']['pointps']['Izhi2007a_0']['vref'] = 'V' # specify that uses its own voltage V
cellRule['secs']['soma']['pointps']['Izhi2007a_0']['synList'] = ['AMPA', 'NMDA', 'GABAA', 'GABAB']  # specify its own synapses


## LTS Izhi cell params

cellRule = netParams.importCellParams(label='LTS_Izhi', conds={'cellType': 'PYR', 'cellModel':'Izh2007a'},
	fileName='izhi2007Wrapper.py', cellName='IzhiCell',  cellArgs={'type':'LTS', 'host':'dummy'})
netParams.renameCellParamsSec('LTS_Izhi', 'sec', 'soma')  # rename imported section 'sec' to 'soma'
cellRule['secs']['soma']['pointps']['Izhi2007a_0']['vref'] = 'V' # specify that uses its own voltage V
cellRule['secs']['soma']['pointps']['Izhi2007a_0']['synList'] = ['AMPA', 'NMDA', 'GABAA', 'GABAB']  # specify its own synapses



## FS Izhi cell params
cellRule = netParams.importCellParams(label='FS_Izhi', conds={'cellType': 'PYR', 'cellModel':'Izh2007a'},
	fileName='izhi2007Wrapper.py', cellName='IzhiCell',  cellArgs={'type':'FS', 'host':'dummy'})
netParams.renameCellParamsSec('FS_Izhi', 'sec', 'soma')  # rename imported section 'sec' to 'soma'
cellRule['secs']['soma']['pointps']['Izhi2007a_0']['vref'] = 'V' # specify that uses its own voltage V
cellRule['secs']['soma']['pointps']['Izhi2007a_0']['synList'] = ['AMPA', 'NMDA', 'GABAA', 'GABAB']  # specify its own synapses


cellRule = netParams.importCellParams(label='PMd_loc', conds={'cellModel':'VecStim'},
 	fileName='nsloc.py', cellName='nslocCell')
netParams.renameCellParamsSec('PMd', 'sec', 'soma')  # rename imported section 'sec' to 'soma'




# Synaptic mechanism parameters


###########################################
# STIMULATION PARAMETERS
###########################################
# background inputs
netParams.stimSourceParams['backgroundS'] = {'type': 'NetStim', 'rate': 100, 'noise': 1}
netParams.stimSourceParams['backgroundDSC'] = {'type': 'NetStim', 'interval': 0.1**-1*1e3, 'rate': 'variable', 'noise': 0.3}
netParams.stimSourceParams['backgroundEB5'] = {'type': 'NetStim', 'interval': 100**-1*1e3, 'rate': 'variable', 'noise': 1}

# Connectivity parameters
# STDPparams = {'hebbwt': 0.00001, 'antiwt':-0.000013, 'wmax': 50, 'RLon': 1 , 'RLhebbwt': 0.001, 'RLantiwt': -0.001, \
#     'tauhebb': 10, 'RLwindhebb': 50, 'useRLexp': 1, 'softthresh': 0, 'verbose':0}

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

###########################################
# CONNECTION PARAMETERS
###########################################
# Background and stims
#Plasticity Connections


#[[s.ASC,s.ER2], [s.EB5,s.EDSC], [s.EB5,s.IDSC], [s.PMd,s.ER5], # spinal cord + pmd
#        [s.ER2,s.ER5], [s.ER5,s.EB5], [s.ER2,s.EB5], [s.ER5,s.ER2]] # + L2-L5

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
 'sec': 'soma',}

netParams.connParams['ER2->ER6'] = {
 'preConds': {'pop': 'ER2'}, 'postConds': {'pop': 'IL5'},  # ES -> ES
 'weight': 0,
 'probability': 0,
 'delay': '2+dist_3D/propVelocity',
 'synMech': 'AMPA',
 'sec': 'soma',}






netParams.connParams['ES->EM'] = {
 'preConds': {'pop': 'ES'}, 'postConds': {'pop': 'EM'},  # ES -> EM (plastic)
 'weight': 5,
 'probability': 0.33750,
 'delay': 5,
 'synMech': 'AMPA',
 'sec': 'soma',
 'plast': {'mech': 'STDP', 'params': STDPparams}}


netParams.connParams['IS->ES'] = {
 'preConds': {'pop': 'IS'}, 'postConds': {'pop': 'ES'},  # IS -> ES
 'weight': 5,
 'probability': 0.495,
 'delay': 5,
 'sec': 'soma',
 'synMech': 'GABA'}


netParams.connParams['IS->IS'] = {
 'preConds': {'pop': 'IS'}, 'postConds': {'pop': 'IS'},  # IS -> IS
 'weight': 5,
 'probability': 0.69750,
 'delay': 5,
 'sec': 'soma',
 'synMech': 'GABA'}

netParams.connParams['IS->ISL'] = {
 'preConds': {'pop': 'IS'}, 'postConds': {'pop': 'ISL'},  # IS -> ISL
 'weight': 5,
 'probability': 0.38250,
 'delay': 5,
 'sec': 'soma',
 'synMech': 'GABA'}

netParams.connParams['ISL->ES'] = {
 'preConds': {'pop': 'ISL'}, 'postConds': {'pop': 'IS'},  # ISL -> ES
 'weight': 5,
 'probability': 0.39375,
 'delay': 5,
 'sec': 'soma',
 'synMech': 'GABA'}

netParams.connParams['ISL->IS'] = {
 'preConds': {'pop': 'ISL'}, 'postConds': {'pop': 'IS'},  # ISL -> IS
 'weight': 5,
 'probability': 0.59625,
 'delay': 5,
 'sec': 'soma',
 'synMech': 'GABA'}

netParams.connParams['ISL->ISL'] = {
 'preConds': {'pop': 'ISL'}, 'postConds': {'pop': 'ISL'},  # ISL -> ISL
 'weight': 5,
 'probability': 0.10125,
 'sec': 'soma',
 'delay': 5,
 'synMech': 'GABA'}


netParams.connParams['EM->ES'] = {
 'preConds': {'pop': 'EM'}, 'postConds': {'pop': 'ES'},  # EM -> ES
 'weight': 5,
 'probability': 0.01125,
 'delay': 5,
 'sec': 'soma',
 'synMech': 'AMPA'}

#,
#    'plast': {'mech': 'STDP', 'params': STDPparams}})


# Motor

netParams.connParams['EM->EM'] = {
 'preConds': {'pop': 'EM'}, 'postConds': {'pop': 'EM'},  # EM -> EM
 'weight': 5,
 'probability': 0.05625,
 'delay': 5,
 'sec': 'soma',
 'synMech': 'AMPA'}

netParams.connParams['EM->IM'] = {
 'preConds': {'pop': 'EM'}, 'postConds': {'pop': 'IM'},  # EM -> IM
 'weight': 5,
 'probability': 0.48375,
 'delay': 5,
 'sec': 'soma',
 'synMech': 'AMPA'}

netParams.connParams['EM->IML'] = {
 'preConds': {'pop': 'EM'}, 'postConds': {'pop': 'IML'},  # EM -> IML
 'weight': 5,
 'probability': 0.57375,
 'delay': 5,
 'sec': 'soma',
 'synMech': 'AMPA'}

netParams.connParams['IM->EM'] = {
 'preConds': {'pop': 'IM'}, 'postConds': {'pop': 'EM'},  # IM -> EM
 'weight': 5,
 'probability': 0.495,
 'delay': 5,
 'sec': 'soma',
 'synMech': 'GABA'}

netParams.connParams['IM->IM'] = {
 'preConds': {'pop': 'IM'}, 'postConds': {'pop': 'IM'},  # IM -> IM
 'weight': 5,
 'probability': 0.69750,
 'delay': 5,
 'sec': 'soma',
 'synMech': 'GABA'}

netParams.connParams['IM->IML'] = {
 'preConds': {'pop': 'IM'}, 'postConds': {'pop': 'IML'},  # IM -> IML
 'weight': 5,
 'probability': 0.38250,
 'delay': 5,
 'sec': 'soma',
 'synMech': 'GABA'}

netParams.connParams['IML->EM'] = {
 'preConds': {'pop': 'IML'}, 'postConds': {'pop': 'EM'},  # IML -> EM
 'weight': 5,
 'probability': 0.39375,
 'delay': 5,
 'sec': 'soma',
 'synMech': 'GABA'}

netParams.connParams['IML->IM'] = {
 'preConds': {'pop': 'IML'}, 'postConds': {'pop': 'IM'},  # IML -> IM
 'weight': 5,
 'probability': 0.59625,
 'delay': 5,
 'sec': 'soma',
 'synMech': 'GABA'}

netParams.connParams['IML->IML'] = {
 'preConds': {'pop': 'IML'}, 'postConds': {'pop': 'IML'},  # IML -> IML
 'weight': 5,
 'probability': 0.10125,
 'delay': 5,
 'sec': 'soma',
 'synMech': 'GABA'}


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


