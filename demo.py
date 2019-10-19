class Packet:
    def __init__(self, id, src_if, dst_if, interfaces, routes, stage):
        self.id = id
        self.src_if = src_if
        self.dst_if = dst_if
        self.interfaces = interfaces
        self.routes = routes
        # stages: start, Success, Error: different kinds
        self.stage = stage
    def getID(self):
        return self.id
    def getSrcIf(self):
        return self.src_if
    def getDstIf(self):
        return self.dst_if
    def transfer(self):
        if self.stage == "start":
            ifs = []
            for ifn in self.interfaces:
                if ifn[0] == self.src_if:
                    host = ifn[1]
                    ifs.append(ifn[0])
            if host is None:
                self.stage = "Error: Host is not found."
                return self.stage  
            else:
                for ifn in self.interfaces:
                    if ifn[1] == host:
                        ifs.append(ifn[0])
            for r in self.routes:
                if r[2] in ifs and r[1] == self.dst_if:
                    self.stage = "Success"
                else:
                    self.stage = "Error: Route is not found."
        return self.stage 
    def __str__(self):
        return "Packet {} has stage {}.".format(self.id, self.stage)

class Host:
    def __init__(self, host):
        self.host = host

class Interface(Host):
    def __init__(self, host, interface):
        Host.__init__(self, host)
        self.interface = interface
    def __str__(self):
        return "Interface {} on host {}.".format(self.interface, self.host)
    def getInterface(self):
        return (self.interface, self.host)
    def getIfName(self):
        return self.interface

class Route:
    def __init__(self, number, dst_if, frwd_if):
        self.number = number
        self.dst_if = dst_if
        self.frwd_if = frwd_if
    def getRoute(self):
        return (self.number, self.dst_if, self.frwd_if)

# manage host data
interfaces = []
if1 = Interface("A", "if1")
if2 = Interface("A", "if2")
if3 = Interface("B", "if3")
interfaces.append(if1.getInterface())
interfaces.append(if2.getInterface())
interfaces.append(if3.getInterface())
# test
print(interfaces)
# manage routing table
routing_table = []
r1 = Route(1, if3.getIfName(), if2.getIfName())
routing_table.append(r1.getRoute())
# test
print(routing_table)
# Transfer packet
pack1 = Packet(1, "if1", "if3", interfaces, routing_table, "start")
pack1.transfer()
print(pack1)