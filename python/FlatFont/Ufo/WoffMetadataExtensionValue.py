# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Ufo

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class WoffMetadataExtensionValue(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = WoffMetadataExtensionValue()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsWoffMetadataExtensionValue(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # WoffMetadataExtensionValue
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # WoffMetadataExtensionValue
    def Text(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # WoffMetadataExtensionValue
    def Language(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # WoffMetadataExtensionValue
    def Dir(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # WoffMetadataExtensionValue
    def Class_(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def Start(builder): builder.StartObject(4)
def WoffMetadataExtensionValueStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddText(builder, text): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(text), 0)
def WoffMetadataExtensionValueAddText(builder, text):
    """This method is deprecated. Please switch to AddText."""
    return AddText(builder, text)
def AddLanguage(builder, language): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(language), 0)
def WoffMetadataExtensionValueAddLanguage(builder, language):
    """This method is deprecated. Please switch to AddLanguage."""
    return AddLanguage(builder, language)
def AddDir(builder, dir): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(dir), 0)
def WoffMetadataExtensionValueAddDir(builder, dir):
    """This method is deprecated. Please switch to AddDir."""
    return AddDir(builder, dir)
def AddClass_(builder, class_): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(class_), 0)
def WoffMetadataExtensionValueAddClass_(builder, class_):
    """This method is deprecated. Please switch to AddClass_."""
    return AddClass_(builder, class_)
def End(builder): return builder.EndObject()
def WoffMetadataExtensionValueEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)