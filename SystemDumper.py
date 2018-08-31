import win32evtlog, win32api, os

class SystemDumper:

    def __init__(self):
        self.host = "localhost"
        
    def event_logs(self, host, logtype):
        bind = win32evtlog.OpenEventLog(host, logtype)
        flag = win32evtlog.EVENTLOG_BACKWARDS_READ|win32evtlog.EVENTLOG_SEQUENTIAL_READ
        total = win32evtlog.GetNumberOfEventLogRecords(bind)
        logDump = {}
        for t in range(0, total):
            events = win32evtlog.ReadEventLog(bind, flag, 0)
            dataExtract = []
            if events:
                for event in events:
                    data = event.StringInserts
                    if data:
                        for d in data:
                            dataExtract.append(d)
            logDump[event.EventID] = ["EventCategory: %s" % str(event.EventCategory), "TimeGenerated: %s" % str(event.TimeGenerated),
                                                      "SourceName: %s" % str(event.SourceName), "EventType: %s" % str(event.EventType),
                                                      "StringInserts: %s" % str(event.StringInserts), "data: %s" % dataExtract]

        return logDump

    def mbr_read(self):
        """Reading Master Boot Record on Host PC"""
        diskBootRec = os.open(r"\\.\PhysicalDrive0", os.O_RDONLY | os.O_BINARY)
        data = os.read(diskBootRec, 512)
        os.close(diskBootRec)

        return data

    def local_drives(self):
        """Returns drive letters in use on machine"""
        drives = win32api.GetLogicalDriveStrings()
        drives = drives.split('\000')[:-1]

        return drives
    
    def main(self):
        """logt = "System"
        evlog = self.event_logs(self.host, logt)
        print(len(evlog))

        for key, value in evlog.items():
            print("EventID: %s: %s\n" % (str(key), value))"""

        print(self.local_drives())

if __name__ == "__main__":
    dump = SystemDumper()
    dump.main()
