class EstadoDocumento(object):
    def __init__(self, status, statusDate, reason, sourceID, sourceBilling):
        self.__status = status
        self.__statusDate = statusDate
        self.__reason = reason
        self.__sourceID = sourceID
        self.__sourceBilling = sourceBilling
        self.__index = -1
    @property
    def status(self):
        return self.__status
    @property
    def statusDate(self):
        return self.__statusDate
    @property
    def reason(self):
        return self.__reason
    @property
    def sourceID(self):
        return self.__sourceID
    @property
    def sourceBilling(self):
        return self.__sourceBilling
