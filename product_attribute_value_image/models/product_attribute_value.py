# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in root directory
##############################################################################
from openerp import models, fields


class ProductAttributeValue(models.Model):
    _inherit = 'product.attribute.value'

    image = fields.Binary(
        string='Image')
