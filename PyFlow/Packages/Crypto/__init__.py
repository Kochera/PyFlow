PACKAGE_NAME = 'Crypto'

from collections import OrderedDict
from PyFlow.UI.UIInterfaces import IPackage

# Pins


# Function based nodes
from PyFlow.Packages.Crypto.FunctionLibraries.Primitives import Primitives

# Class based nodes
from PyFlow.Packages.Crypto.Nodes.SHA256 import SHA256

# Tools


# Exporters
from PyFlow.Packages.Crypto.Exporters.PrimitiveExporter import PrimitiveExporter

# Factories
from PyFlow.Packages.Crypto.Factories.UIPinFactory import createUIPin
from PyFlow.Packages.Crypto.Factories.UINodeFactory import createUINode
from PyFlow.Packages.Crypto.Factories.PinInputWidgetFactory import getInputWidget
# Prefs widgets
from PyFlow.Packages.Crypto.PrefsWidgets.General import GeneralPreferences
from PyFlow.Packages.Crypto.PrefsWidgets.InputPrefs import InputPreferences
from PyFlow.Packages.Crypto.PrefsWidgets.ThemePrefs import ThemePreferences

_FOO_LIBS = {}
_NODES = {}
_PINS = {}
_TOOLS = OrderedDict()
_PREFS_WIDGETS = OrderedDict()
_EXPORTERS = OrderedDict()

_FOO_LIBS[Primitives.__name__] = Primitives(PACKAGE_NAME)

_NODES = {
}


_PINS = {

}

_TOOLS = OrderedDict()


_EXPORTERS[PrimitiveExporter.__name__] = PrimitiveExporter

_PREFS_WIDGETS = OrderedDict()
_PREFS_WIDGETS["General"] = GeneralPreferences
_PREFS_WIDGETS["Input"] = InputPreferences
_PREFS_WIDGETS["Theme"] = ThemePreferences


class Crypto(IPackage):
	def __init__(self):
		super(Crypto, self).__init__()

	@staticmethod
	def GetExporters():
		return _EXPORTERS

	@staticmethod
	def GetFunctionLibraries():
		return _FOO_LIBS

	@staticmethod
	def GetNodeClasses():
		return _NODES

	@staticmethod
	def GetPinClasses():
		return _PINS

	@staticmethod
	def GetToolClasses():
		return _TOOLS

	@staticmethod
	def UIPinsFactory():
		return createUIPin

	@staticmethod
	def UINodesFactory():
		return createUINode

	@staticmethod
	def PinsInputWidgetFactory():
		return getInputWidget

	@staticmethod
	def PrefsWidgets():
		return _PREFS_WIDGETS

