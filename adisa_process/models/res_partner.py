# -*- coding: utf-8 -*-
import requests
import base64
from odoo import fields, models, api
from odoo.exceptions import ValidationError

WEBMECANIK_COMPANY_FIELDS = {
    'name': {
        'type': 'string',
        'value': 'companyname'
    },
    'street': {
        'type': 'string',
        'value': 'companyaddress1'
    },
    'street2': {
        'type': 'string',
        'value': 'companyaddress2'
    },
    'phone': {
        'type': 'string',
        'value': 'companyphone'
    },
    'city': {
        'type': 'string',
        'value': 'companycity'
    },
    'zip': {
        'type': 'string',
        'value': 'companyzipcode'
    },
    'country_id': {
        'type': 'relation',
        'value': 'companycountry'
    },
    'website': {
        'type': 'string',
        'value': 'companywebsite'
    },
    'industry_id': {
        'type': 'relation',
        'value': 'secteur'
    },
    # 'NO': '',
    'society_type': {
        'type': 'string',
        'value': 'typesoc'
    },
    'activity': {
        'type': 'relation',
        'value': 'activite'
    },
    'society_desc': {
        'type': 'string',
        'value': 'companydescription'
    },
    # 'nbr_employee': '',
    'fax': {
        'type': 'string',
        'value': 'companyfax'
    },
    'twitter': {
        'type': 'string',
        'value': 'twitter'
    },
    'facebook': {
        'type': 'string',
        'value': 'facebook'
    },
    'linkedin': {
        'type': 'string',
        'value': 'linkedin'
    },
    'skype': {
        'type': 'string',
        'value': 'skype'
    },
    'instagram': {
        'type': 'string',
        'value': 'instagram'
    },
    'foursquare': {
        'type': 'string',
        'value': 'foursquare'
    },

}
WEBMECANIK_CONTACT_FIELDS = {
    'sociéty_name': {
        'type': 'relation',
        'value': 'parent_id'
    },
    'points': {
        'type': 'string',
        'value': 'points'
    },
    'title': {
        'type': 'string',
        'value': 'title'
    },
    'function': {
        'type': 'string',
        'value': 'position'
    },
    'personal_city': {
        'type': 'string',
        'value': 'city'
    },
    'email': {
        'type': 'string',
        'value': 'email'
    },
    'phone': {
        'type': 'string',
        'value': 'phone'
    },
    'mobile': {
        'type': 'string',
        'value': 'mobile'
    },
    'fax': {
        'type': 'string',
        'value': 'fax'
    },
    'personal_addr': {
        'type': 'string',
        'value': 'address1'
    },
    'personal_addr2': {
        'type': 'string',
        'value': 'address2'
    },
    # 'personal_state': {
    #     'type': 'string',
    #     'value': 'state'
    # },
    'personal_code_postal': {
        'type': 'string',
        'value': 'zipcode'
    },
    'personal_country': {
        'type': 'relation',
        'value': 'country'
    },
    'function_2': {
        'type': 'relation',
        'value': 'function'
    },
    'source': {
        'type': 'string',
        'value': 'source1'
    },
    'mobile2': {
        'type': 'string',
        'value': 'mobile2'
    },
    'commune': {
        'type': 'string',
        'value': 'commune'
    },
    'website': {
        'type': 'string',
        'value': 'companynamecompanyname'
    },
    'twitter': {
        'type': 'string',
        'value': 'twitter'
    },
    'facebook': {
        'type': 'string',
        'value': 'facebook'
    },
    'linkedin': {
        'type': 'string',
        'value': 'linkedin'
    },
    'skype': {
        'type': 'string',
        'value': 'skype'
    },
    'instagram': {
        'type': 'string',
        'value': 'instagram'
    },
    'foursquare': {
        'type': 'string',
        'value': 'foursquare'
    },

}


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.onchange('linkedin_logo')
    def onchange_image(self, context=None):
        link = self.linkedin_logo
        # photo = base64.encodestring(http.urlopen(link).read())
        # self.image_1920 = photo
        # val = {
        #     'image_1920': photo,
        # }
        # return {'value': val}

    society_nature = fields.Selection([('prospect', 'Prospect'),
                                       ('customer', 'Client'),
                                       ('prescript', 'Prescripteur'),
                                       ('suppliers', 'Fournisseur')], 'Nature société', default='prospect')

    contact_nature = fields.Selection([('prospect', 'Prospect'),
                                       ('freelance', 'Freelance'),
                                       ('customer', 'Client'),
                                       ('suppliers', 'Fournisseur'),
                                       ('prescript', 'Prescripteur'),
                                       ('employee', 'Employé')], 'Nature contact', default='prospect')
    society_type = fields.Selection([('adm', 'ADM'),
                                     ('ge', 'Grande Entreprise'),
                                     ('institute', 'Institut'),
                                     ('ong', 'ONG'),
                                     ('tpe', 'TPE'),
                                     ('pme', 'PME')], 'Type société')
    society_category = fields.Many2one('res.partner.society.category', 'Categorie société')
    activity = fields.Many2one('res.partner.activity', 'Activité', domain="[('industry_id', '=', industry_id)]")
    function_2 = fields.Many2one('res.partner.function', 'Fonction')
    company_type = fields.Selection(string='Company Type',
                                    selection=[('person', 'Individual'), ('company', 'Company')],
                                    compute='_compute_company_type', inverse='_write_company_type', store=True)
    # parent_id = fields.Many2one('res.partner', string='Related Company',
    #                             domain="[('company_type', '=', 'company')", index=True)
    linkedin = fields.Char(string="LinkedIn")
    linkedin_logo = fields.Char('image url', help='Automatically sanitized HTML contents')
    # personal informations
    fax = fields.Char(string="Fax")
    points = fields.Char(string="Points")
    twitter = fields.Char(string="Twitter")
    facebook = fields.Char(string="Facebook")
    # skype = fields.Char(string="Skype")
    instagram = fields.Char(string="Instagram")
    personal_addr = fields.Char(string="Adresse personelle 1")
    personal_addr2 = fields.Char(string="Adresse personelle 2")
    personal_postal = fields.Char(string="Adresse postale personelle")
    postal = fields.Char(string="Adresse postale")
    commune = fields.Char(string="Commune")
    personal_city = fields.Char(string="Ville 2")
    personal_state = fields.Many2one('res.country.state', string="État 2")
    personal_code_postal = fields.Char(string="Code postal 2")
    personal_country = fields.Many2one('res.country', string="Pays 2")
    mobile2 = fields.Char(string="Mobile 2")
    # phone2 = fields.Char(string="Pers. Tel")
    personal_email = fields.Char('Pers. Email')
    source = fields.Char(string="Source")
    first_name = fields.Char(string="Prénom")
    last_name = fields.Char(string="Nom")
    # society informations
    society_desc = fields.Text(string="Description")
    nbr_employee = fields.Selection([('small', '1-10'),
                                     ('medium', '11-50'),
                                     ('large', '51-200'),
                                     ('extra-large', '201-500')], string="Nbr employés")
    # test_fields = fields.Char(string="Test")

    _sql_constraints = [
        ('email_unique', 'unique(email)', 'Choose another value for Email - it has to be unique!')
    ]

    def send_request(self, host, params):
        link = host + params[:0]
        print(host, params)
        print(link)
        r = requests.get(link)
        if r.status_code == 200:
            print("La synchronisation du contact %s OK" % self.name)
        else:
            print("La synchronisation du contact %s NOK" % self.name)

    def _get_link(self):
        ICPsudo = self.env['ir.config_parameter'].sudo()
        webmecanik_link = ICPsudo.get_param('adisa_process.webmecanik_link')
        return webmecanik_link

    def convert_to_params(self, data):
        params = '?'
        for key, item in data.items():
            params += '%s=%s&' % (key, item)
        print(params)
        return params

    def get_data(self, data, fields, object):
        result = {}
        for key in data.keys():
            if key in fields.keys():
                _key = fields[key]['value']
                val = getattr(object, key)
                if fields[key]['type'] == 'string':
                    if val:
                        result[_key] = val
                else:
                    if val:
                        result[_key] = val.name

        return result

    @api.onchange('parent_id')
    def _get_vendor(self):
        if self.parent_id and self.parent_id.user_id:
            self.user_id = self.parent_id.user_id

    @api.model
    def create(self, vals):
        partner = super(ResPartner, self).create(vals)

        # if partner.company_type == 'person':
        #     data = self.get_data(vals, WEBMECANIK_CONTACT_FIELDS, partner)
        #
        # else:
        #     data = self.get_data(vals, WEBMECANIK_COMPANY_FIELDS, partner)
        #
        # if data:
        #     self.send_request(host=self._get_link(), params=self.convert_to_params(data))

        return partner

    def write(self, vals):
        partner = super(ResPartner, self).write(vals)

        # if self.company_type == 'person':
        #     data = self.get_data(vals, WEBMECANIK_CONTACT_FIELDS, self)
        #
        # else:
        #     data = self.get_data(vals, WEBMECANIK_COMPANY_FIELDS, self)
        #
        # print(data)
        # if data:
        #     self.send_request(host=self._get_link(), params=self.convert_to_params(data))

        return partner


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
