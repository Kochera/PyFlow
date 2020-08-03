from nine import str
from Qt import QtCore
from Qt import QtGui
from Qt import QtWidgets

from PyFlow.Packages.PyFlowBase.Tools import RESOURCES_DIR
from PyFlow.UI.Tool.Tool import DockTool
from PyFlow.UI.Widgets.PropertiesFramework import PropertiesWidget


class SecurityRatingTool(DockTool):
    """docstring for Properties tool."""
    def __init__(self):
        super(SecurityRatingTool, self).__init__()
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.setWidget(self.scrollArea)
        self.propertiesWidget = PropertiesWidget()
        self.scrollArea.setWidget(self.propertiesWidget)

        self.propertiesWidget.searchBoxLayout.removeWidget(self.propertiesWidget.lockCheckBox)
        self.addButton(self.propertiesWidget.lockCheckBox)
        self.propertiesWidget.searchBoxLayout.removeWidget(self.propertiesWidget.tearOffCopy)
        self.addButton(self.propertiesWidget.tearOffCopy)
        # self.addButton(self.propertiesWidget.settingsButton)

        self.setWindowTitle(self.uniqueName())
        self.fillDelegate = None
        self.propertiesWidget.spawnDuplicate.connect(self.onTearOffCopy)

    def onTearOffCopy(self, *args, **kwargs):
        instance = self.pyFlowInstance.invokeDockToolByName("PyFlowBase", self.name())
        if self.fillDelegate is not None:
            instance.assignPropertiesWidget(self.fillDelegate)
        instance.setFloating(True)
        instance.resize(self.size())

    def clear(self):
        self.propertiesWidget.clear()

    def assignPropertiesWidget(self, propertiesFillDelegate):
        self.fillDelegate = propertiesFillDelegate
        if not self.propertiesWidget.isLocked():
            propertiesFillDelegate(self.propertiesWidget)

    @staticmethod
    def isSingleton():
        return False

    @staticmethod
    def toolTip():
        return "Analyze Security Rating of Protocol"

    @staticmethod
    def name():
        return str("SecurityRating")
