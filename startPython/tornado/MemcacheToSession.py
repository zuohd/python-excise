import memcache
import hashlib
import uuid
import json


conn = memcache.Client(['192.168.1.143:11211'])


class Session:
    CookieID = 'uc'
    ExpiresTime = 60 * 20

    def __init__(self, handler):
        self.handler = handler
        SessionID = self.handler.get_secure_cookie(Session.CookieID, None)
        if SessionID and conn.get(SessionID):
            self.SessionID = SessionID
        else:
            self.SessionID = self.SessionKey()
            conn.set(self.SessionID, json.dumps({}), Session.ExpiresTime)
        conn.set(self.SessionID, conn.get(self.SessionID))
        self.handler.set_secure_cookie('uc', self.SessionID)

    def SessionKey(self):
        UUID = str(uuid.uuid1()).replace('-', '')
        MD5 = hashlib.md5()
        MD5.update(bytes(UUID, encoding='utf-8'))
        SessionKey = MD5.hexdigest()
        return SessionKey

    def __setitem__(self, key, value):
        SessionDict = json.loads(conn.get(self.SessionID))
        SessionDict[key] = value
        conn.set(self.SessionID, json.dumps(SessionDict), Session.ExpiresTime)

    def __getitem__(self, item):
        SessionDict = json.loads(conn.get(self.SessionID))
        ResultData = SessionDict.get(item, None)
        return ResultData

    def __delitem__(self, key):
        SessionDict = json.loads(conn.get(self.SessionID))
        del SessionDict[key]
        conn.set(self.SessionID, json.dumps(SessionDict), Session.ExpiresTime)

    def GetAll(self):
        SessionData = conn.get(self.SessionID)
        return SessionData
