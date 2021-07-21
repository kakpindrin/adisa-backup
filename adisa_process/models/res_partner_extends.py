from odoo import fields, models, api
from odoo.exceptions import ValidationError


class ResPartnerFunction(models.Model):
    _name = 'res.partner.function'

    name = fields.Char('Name', required=True)

    _sql_constraints = [
        ('name_unique', 'unique(name)', 'Choose another value - it has to be unique!')
    ]


class ResPartnerType(models.Model):
    _name = 'res.partner.type'

    name = fields.Char('Name', required=True)

    _sql_constraints = [
        ('name_unique', 'unique(name)', 'Choose another value - it has to be unique!')
    ]


class ResPartnerCategory(models.Model):
    _name = 'res.partner.society.category'

    name = fields.Char('Name', required=True)

    _sql_constraints = [
        ('name_unique', 'unique(name)', 'Choose another value - it has to be unique!')
    ]


class ResPartnerActivity(models.Model):
    _name = 'res.partner.activity'

    name = fields.Char('Name', required=True)
    industry_id = fields.Many2one('res.partner.industry', 'Secteur', ondelete='cascade', required=True)

    _sql_constraints = [
        ('name_unique', 'unique(name)', 'Choose another value - it has to be unique!')
    ]


class ResCompany(models.Model):
    _inherit = 'res.company'

    rccm = fields.Char(string="RCCM")
    bank_name = fields.Char(string="Banque")
    bank_rib = fields.Char(string="RIB")
    society_nature = fields.Char(string="Nature")
    capital = fields.Char(string="Capital")
    name_sale = fields.Char(string="Nom commercial")
