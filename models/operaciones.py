# -*- coding: utf-8 -*-
from odoo import models, fields, _
from odoo.exceptions import UserError
from odoo.tests.common import Form


import logging

_logger = logging.getLogger(__name__)


class operaciones(models.Model):
    _name = 'gestion.operaciones'
    _description = 'Operaciones'

    name = fields.Char('Operaciones', required=True)

    active = fields.Boolean(default=True)
    tipo_operacion = fields.Selection(
        [('recarga', 'Recarga'),
         ('compra', 'Consumo'),
         ('devolucion', 'Devoluciones'),
         ('cancelacion', 'Cancelacion'),
         ('otros', 'Otros')],
        'Tipo de Operación', default="compra")
    importe = fields.Float('Importe')
    cliente_id = fields.Many2one('gestion.operaciones.clientes')
    negocio_id = fields.Many2one('gestion.operaciones.negocios')

    def make_available(self):
        self.ensure_one()
        self.tipo_operacion = 'recarga'

    def make_borrowed(self):
        self.ensure_one()
        self.tipo_operacion = 'compra'

    def make_borrowed(self):
        self.ensure_one()
        self.tipo_operacion = 'devolucion'

    def make_borrowed(self):
        self.ensure_one()
        self.tipo_operacion = 'cancelacion'

    def make_borrowed(self):
        self.ensure_one()
        self.tipo_operacion = 'otros'
