from nine import str
from Qt import QtCore
from Qt import QtGui
from Qt import QtWidgets

from PyFlow.Packages.PyFlowBase.Tools import RESOURCES_DIR
from PyFlow.UI.Tool.Tool import DockTool
from PyFlow.UI.Widgets.SecurityRatingFramework import SecurityRatingWidget


class SecurityRatingTool(DockTool):
    """docstring for Properties tool."""
    def __init__(self):
        super(SecurityRatingTool, self).__init__()
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.setWidget(self.scrollArea)
        self.securityWidget = SecurityRatingWidget()
        self.scrollArea.setWidget(self.securityWidget)

        self.securityWidget.searchBoxLayout.removeWidget(self.securityWidget.lockCheckBox)
        self.addButton(self.securityWidget.lockCheckBox)
        self.securityWidget.searchBoxLayout.removeWidget(self.securityWidget.tearOffCopy)
        self.addButton(self.securityWidget.tearOffCopy)
        # self.addButton(self.securityWidget.settingsButton)

        self.setWindowTitle(self.uniqueName())
        self.fillDelegate = None
        self.securityWidget.spawnDuplicate.connect(self.onTearOffCopy)

    def onTearOffCopy(self, *args, **kwargs):
        instance = self.pyFlowInstance.invokeDockToolByName("PyFlowBase", self.name())
        if self.fillDelegate is not None:
            instance.assignSecurityRatingWidget(self.fillDelegate)
        instance.setFloating(True)
        instance.resize(self.size())

    def clear(self):
        self.securityWidget.clear()

    def assignSecurityRatingWidget(self, securityFillDelegate):
        self.fillDelegate = securityFillDelegate
        if not self.securityWidget.isLocked():
            securityFillDelegate(self.securityWidget)

    @staticmethod
    def isSingleton():
        return False

    @staticmethod
    def toolTip():
        return "Analyze Security Rating of Protocol"

    @staticmethod
    def name():
        return str("SecurityRating")
