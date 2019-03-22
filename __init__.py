import platform
import logging


__alias__ = 'linux mpris2'
__version__ = '0.0.1'
__desc__ = '实现 linux 的 mpris2 dbus 接口'


def enable(app):
    logger = logging.getLogger(__name__)
    if platform.system() != 'Linux':
        logger.warning('not a linux system, wont load mpris2 plugin')
        return
    import dbus.mainloop.pyqt5
    from .service import MprisServer
    dbus.mainloop.pyqt5.DBusQtMainLoop(set_as_default=True)
    MprisServer(app)
    logger.info('load mpris2 plugin')


def disable(app):
    logger = logging.getLogger(__name__)
    logger.info('disable mpris2 plugin')
