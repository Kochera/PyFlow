from PyFlow.Packages.Crypto.Nodes.SHA256 import SHA256


from PyFlow.Packages.Crypto.UI.UISHA256Node import UISHA256Node
from PyFlow.UI.Canvas.UINodeBase import UINodeBase


def createUINode(raw_instance):
    if isinstance(raw_instance, SHA256):
        return UISHA256Node(raw_instance)
    return UINodeBase(raw_instance)