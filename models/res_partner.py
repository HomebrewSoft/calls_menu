# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class Partner(models.Model):
    _inherit = 'res.partner'

    note_count = fields.Integer(
        compute='_compute_note_count',
        string=_('Note'),
    )

    def _compute_note_count(self):
        for record in self:
            record.note_count = self.env['mail.message'].search_count([('partner_id', '=', record.id), ('message_type', '=', 'comment')])
