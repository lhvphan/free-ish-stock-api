import cherrypy
import serverinfo
import financebackend

server = serverinfo.ServerInfo()
backend = financebackend.FinanceBackend()

class MyWebService(object):

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def status(self):
        output = server.getsysteminfo()
        return output

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def getstock(self):
        data = cherrypy.request.json
        output = backend.getone(data["value"])
        return output

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def getstocks(self):
        data = cherrypy.request.json
        output = backend.getmany(data)
        return output

if __name__ == '__main__':
    config = {'server.socket_host': '0.0.0.0'}
    cherrypy.config.update(config)
    cherrypy.quickstart(MyWebService())
