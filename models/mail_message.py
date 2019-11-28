# -*- coding: utf-8 -*-

from odoo import api, fields, models


class MailMessage(models.Model):
    _inherit = 'mail.message'

    partner_id = fields.Many2one(
        comodel_name='res.partner',
        store=True,
        index=True,
        compute='_get_partner_id'
    )
    partner_parent_id = fields.Many2one(
        comodel_name='res.partner',
        store=True,
        index=True,
        compute='_get_partner_id'
    )

    @api.depends('model', 'res_id')
    def _get_partner_id(self):
        for record in self:
            record.partner_id = False
            if record.model and record.res_id:
                if record.model == 'res.partner':
                    record.partner_id = self.env['res.partner'].browse(record.res_id)
                    record.partner_parent_id = record.partner_id.parent_id
