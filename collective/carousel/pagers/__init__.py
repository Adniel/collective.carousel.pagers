from zope.i18nmessageid import MessageFactory

LocalMessageFactory=MessageFactory('collective.carousel.pagers')

def initialize(context):
    """Initializer called when used as a Zope 2 product."""
