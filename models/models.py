# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class Document(models.Model):
    _name = 'mrp_documents_share.document'
    _description = 'Mrp documents share Document'

    # fields
    name = fields.Char()
    value = fields.Integer()