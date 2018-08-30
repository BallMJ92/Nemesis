import win32evtlog

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

        return total, logDump
        
    def main(self):

        logt = "System"
        evlog = self.event_logs(self.host, logt)
        print(len(evlog[1]))
        print(evlog[0])       
        
        for key, value in n.items():
            print("EventID: %s: %s\n" % (str(key), value))

if __name__ == "__main__":
    dump = SystemDumper()
    dump.main()
