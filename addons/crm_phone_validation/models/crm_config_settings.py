# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class CrmConfigSettings(models.TransientModel):
    _inherit = 'crm.config.settings'

    crm_phone_valid_method = fields.Boolean(related="company_id.phone_international_format", required=True)
