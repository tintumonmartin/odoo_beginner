# -*- coding: utf-8 -*-

import datetime
from datetime import date, timedelta

from dateutil import parser
from odoo.exceptions import ValidationError

from odoo import models, fields, api, _


class RailwayUsers(models.Model):
    _name = 'railway.users'
    _description = 'Railway Users'

    user_id = fields.Char("User Id", required=True)
    password = fields.Char("Password", invisible=True)
    first_name = fields.Char("First Name", required=True)
    last_name = fields.Char("Last Name")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('trans_gender', 'Trans_Gender')], required=True)
    dob = fields.Date()
    hide = fields.Boolean()
    email = fields.Char(required=True)
    image_1920 = fields.Image()
    image_512 = fields.Image("Image 512", related="image_1920", max_width=512, max_height=512)
    aadhar_no = fields.Char(size=12)
    # , required=True
    mobile_no = fields.Char(size=10)
    country_id = fields.Many2one('res.country', string='Country', help='Select Country')
    state_id = fields.Many2one('res.country.state', string='State', help='Enter State')
    city = fields.Char('City', help='Enter City')
    pincode = fields.Char("pincode")
    security_ques = fields.Char("Security_question")

    @api.model
    def create(self, values):
        print(values)
        print(values.get('phone'))
        values['user_id'] = self.env['ir.sequence'].sudo().next_by_code('railway.reservation') or _('New')
        res = super(RailwayUsers, self).create(values)
        print(res)
        print(res.phone)
        if res.phone and len(res.phone) != 10:
            raise ValidationError(_('Contact number must have 10 digit! not %s digit and change this value %s' % (
                len(res.phone), res.phone)))
        return res

    @api.model
    def create(self, values):
        print(values)
        print(values.get('aadhar_no'))
        values['user_id'] = self.env['ir.sequence'].sudo().next_by_code('railway.reservation') or _('New')
        res = super(RailwayUsers, self).create(values)
        print(res)
        print(res.aadhar_no)
        if res.aadhar_no and len(res.aadhar_no) != 12:
            raise ValidationError(_('Aadhar number must have 12 digit! not %s digit and change this value %s' % (
                len(res.aadhar_no), res.aadhar_no)))
        return res

    @api.onchange('country_id')
    def _onchange_country_id(self):
        if self.country_id:
            return {'domain': {'state_id': [('countelsery_id', '=', self.country_id.id)]}}
        :
            return {'domain': {'state_id': []}}

    @api.depends('country')
    def _compute_hide(self):
        if self.country:
            self.hide = False
        else:
            self.hide = True

    #     @api.depends('value')
    #     def _value_pc(self):
    #         for record in self:
    #             record.value2 = float(record.value) / 100

    def calculate_age(born):
        today = date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    age = fields.Char(string="Calculated Age", compute="age_calc", store=True)

    @api.depends('dob')
    def age_calc(self):
        if self.dob is not False:
            diff = (datetime.datetime.today().date() - datetime.datetime.strptime(str(self.dob), '%Y-%m-%d').date())
            self.age = diff // timedelta(days=365)
