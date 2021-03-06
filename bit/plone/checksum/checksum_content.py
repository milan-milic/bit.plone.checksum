from zope.interface import implements

from bit.content.checksum.interfaces import IChecksumContent


class BlobChecksumContent(object):
    implements(IChecksumContent)

    def __init__(self, context):
        self.context = context

    @property
    def content(self):
        return self.context.getFile().data
