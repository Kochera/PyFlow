from PyFlow.UI.Canvas.UIPinBase import UIPinBase
from PyFlow.Packages.Crypto.Pins.AnyPin import AnyPin
from PyFlow.Packages.Crypto.Pins.ExecPin import ExecPin

from PyFlow.Packages.Crypto.UI.UIAnyPin import UIAnyPin
from PyFlow.Packages.Crypto.UI.UIExecPin import UIExecPin


def createUIPin(owningNode, raw_instance):
    if isinstance(raw_instance, AnyPin):
        return UIAnyPin(owningNode, raw_instance)
    elif isinstance(raw_instance, ExecPin):
        return UIExecPin(owningNode, raw_instance)
    else:
        return UIPinBase(owningNode, raw_instance)
