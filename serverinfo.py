import json
import platform
import socket
import re
import uuid
import psutil

class ServerInfo:
    def getsysteminfo(self):
        """
        function getsysteminfo: get server information
        :param self: self object
        :return returnval: json object
        """

        # get various system information
        info={}
        info['platform']=platform.system()
        info['platform-release']=platform.release()
        info['platform-version']=platform.version()
        info['architecture']=platform.machine()
        info['hostname']=socket.gethostname()
        info['ip-address']=socket.gethostbyname(socket.gethostname())
        info['mac-address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
        info['processor']=platform.processor()
        info['ram']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
        
        # convert object to json object
        returnval = json.dumps(info)
        print("system information (json): %s" % returnval)
        return returnval
