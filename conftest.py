import eventlet
eventlet.monkey_patch()


def pytest_configure(config):
    import logging
    logging.basicConfig(level=logging.DEBUG)
