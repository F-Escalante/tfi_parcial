# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class clientes(models.Model):
    _name = 'gestion.operaciones.clientes'


    name = fields.Char('Cliente')
    fecha_nacimiento = fields.Date('Fecha de Nacimiento')
    direccion = fields.Char('Direccion')
    telefono = fields.Char('Telefono')

