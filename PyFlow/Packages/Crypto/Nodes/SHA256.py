from PyFlow.Core import NodeBase
from PyFlow.Core.NodeBase import NodePinsSuggestionsHelper
from PyFlow.Core.Common import *
import hashlib

class SHA256(NodeBase):
    def __init__(self, name):
        super(SHA256, self).__init__(name)
        self.inExec = self.createInputPin(pinName="inExec", dataType='ExecPin', foo=node.processNode)
        self.outExec = self.createOutputPin(pinName='outExec', dataType='ExecPin')
        self.inp = self.createInputPin(pinName='n', dataType='StringPin')
        self.result = self.createOutputPin(pinName='result', dataType='StringPin')

    @staticmethod
    def pinTypeHints():
        helper = NodePinsSuggestionsHelper()
        helper.addInputDataType('BoolPin')
        helper.addOutputDataType('BoolPin')
        helper.addInputStruct(StructureType.Single)
        helper.addOutputStruct(StructureType.Single)
        return helper

    @staticmethod
    def category():
        return 'Generated from wizard'

    @staticmethod
    def keywords():
        return []

    @staticmethod
    def description():
        return "Description in rst format."

    @staticmethod
    def do_SHA256(n):
        return hashlib.sha256(n.encode()).hexdigest()

    def compute(self, *args, **kwargs):
        var = self.inp.getData()
        self.result.setData("result", do_SHA256(var))
        self['outExec'].call()
