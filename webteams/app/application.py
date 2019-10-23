# coding: utf-8
import cherrypy
from .database import Database_cl
from .view import View_cl

#----------------------------------------------------------
class Application_cl(object):
#----------------------------------------------------------

#-------------------------------------------------------
    def __init__(self):
#-------------------------------------------------------
        self.db_o = Database_cl()
        self.view_o = View_cl()
        self.listForm = "tabelle"

    @cherrypy.expose
#-------------------------------------------------------
    def index(self):
#-------------------------------------------------------
        return self.createList_p()

    @cherrypy.expose
#-------------------------------------------------------
    def changeForm(self, listForm):
#-------------------------------------------------------
        if(self.listForm == "tabelle"):
            self.listForm = "aufzaehlung"
            data_o = self.db_o.read_px()
            return self.view_o.createList_pxx(data_o)
        if(self.listForm == "aufzaehlung"):
            self.listForm = "tabelle"
            data_o = self.db_o.read_px()
            return self.view_o.createList_px(data_o)

    @cherrypy.expose
#-------------------------------------------------------
    def back(self):

        if(self.listForm == "tabelle"):
            data_o = self.db_o.read_px()
            return self.view_o.createList_px(data_o)
        if(self.listForm == "aufzaehlung"):
            data_o = self.db_o.read_px()
            return self.view_o.createList_pxx(data_o)
        

    @cherrypy.expose
#-------------------------------------------------------
    def add(self):
#-------------------------------------------------------
        return self.createForm_p()

    @cherrypy.expose
#-------------------------------------------------------
    def edit(self, id_spl):
#-------------------------------------------------------
        return self.createForm_p(id_spl)

    @cherrypy.expose
#-------------------------------------------------------
    def save(self, id_spa, name1_spa, vorname1_spa, matrnr1_spa, semesteranzahl1_spa, name2_spa, vorname2_spa, matrnr2_spa, semesteranzahl2_spa):
#-------------------------------------------------------
        id_s = id_spa
        data_a = [ name1_spa, vorname1_spa, matrnr1_spa, semesteranzahl1_spa, name2_spa, vorname2_spa, matrnr2_spa, semesteranzahl2_spa ]
        if id_s != "None":
            self.db_o.update_px(id_s, data_a)
        else:
            self.db_o.create_px(data_a)
        return self.createList_p()

    @cherrypy.expose
#-------------------------------------------------------
    def delete(self, id):
#-------------------------------------------------------
        self.db_o.delete_px(id)
        raise cherrypy.HTTPRedirect('/')

    @cherrypy.expose
#-------------------------------------------------------
    def default(self, *arguments, **kwargs):
#-------------------------------------------------------
        msg_s = "unbekannte Anforderung: " + \
        str(arguments) + \
        ' ' + \
        str(kwargs)
        raise cherrypy.HTTPError(404, msg_s)
    default.exposed= True

#-------------------------------------------------------
    def createList_p(self):
#-------------------------------------------------------
        if(self.listForm == "tabelle"):
            data_o = self.db_o.read_px()
            return self.view_o.createList_px(data_o)
        if(self.listForm == "aufzaehlung"):
            data_o = self.db_o.read_px()
            return self.view_o.createList_pxx(data_o)

#-------------------------------------------------------
    def createForm_p(self, id_spl = None):
#-------------------------------------------------------
        if id_spl != None:
            data_o = self.db_o.read_px(id_spl)
        else:
            data_o = self.db_o.getDefault_px()
        return self.view_o.createForm_px(id_spl, data_o)

# EOF