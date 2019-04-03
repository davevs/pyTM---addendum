from pytm.pytm import Dataflow, Element, Server, Actor, Datastore, Process, SetOfProcesses, Lambda

''' Add threats here '''
Threats = {}
Threats.update(eval(open('default.dict', 'r').read()))
Threats.update(eval(open('gdpr.dict', 'r').read()))