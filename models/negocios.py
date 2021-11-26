# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class negocios(models.Model):
    _name = 'gestion.operaciones.negocios'

    _parent_store = True
    _parent_name = "parent_id"  # optional if field is 'parent_id'

    name = fields.Char('Negocio')
    descripcion = fields.Char('Descripcion')
    rubro = fields.Char('Rubro')
    parent_id = fields.Many2one(
        'gestion.operaciones.negocios',
        string='Parent Category',
        ondelete='restrict',
        index=True
    )
    child_ids = fields.One2many(
        'gestion.operaciones.negocios', 'parent_id',
        string='Child Categories')
    parent_path = fields.Char(index=True)

    @api.constrains('parent_id')
    def _check_hierarchy(self):
        if not self._check_recursion():
            raise models.ValidationError('Error! You cannot create recursive negocio.')