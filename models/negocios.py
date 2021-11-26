# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class negocios(models.Model):
    _name = 'gestion.operaciones.negocios'


    name = fields.Char('Negocio')
    descripcion = fields.Char('Descripcion')
    rubro = fields.Char('Rubro')



