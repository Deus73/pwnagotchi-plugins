from pwnagotchi.plugins import BasePlugin

class TrafficSniffer(BasePlugin):
    __author__ = 'Deus Dust'
    __version__ = '1.0.0'
    __license__ = 'MIT'

    def __init__(self):
        super(TrafficSniffer, self).__init__()

    def on_loaded(self):
        self.log.info("Traffic Sniffer Plugin loaded")

    def on_packet(self, agent, packet):
        # Analyze or log the packet as needed
        pass

    def on_unload(self):
        self.log.info("Traffic Sniffer Plugin unloaded")

# Instantiate the plugin
plugin = TrafficSniffer()
