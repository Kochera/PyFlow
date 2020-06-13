from datetime import datetime
from PyFlow.UI.UIInterfaces import IDataExporter
from PyFlow.Core.version import Version


class PrimitiveExporter(IDataExporter):
    """docstring for DemoExporter."""

    def __init__(self):
        super(PrimitiveExporter, self).__init__()

    @staticmethod
    def createImporterMenu():
        return True

    @staticmethod
    def creationDateString():
        return datetime.now().strftime("%I:%M%p on %B %d, %Y")

    @staticmethod
    def version():
        return Version(1, 0, 0)

    @staticmethod
    def toolTip():
        return "Primitive Export/Import."

    @staticmethod
    def displayName():
        return "Primitive exporter"

    @staticmethod
    def doImport(pyFlowInstance):
        print("PrimitiveExporter import!")

    @staticmethod
    def doExport(pyFlowInstance):
        print("PrimitiveExporter export!")
