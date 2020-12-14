# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import AccessError, UserError, ValidationError


class SchoolTeacher(models.Model):
    _name = 'school.teacher'
    _description = 'School Teacher'
    _rec_name = 'teacher_identity'

    name = fields.Char("Teacher Name", required=True)
    active = fields.Boolean('Active', default=True)
    user_id = fields.Many2one('res.users', string='Login id')
    teacher_identity = fields.Char(readonly=True)
    phone = fields.Char(size=10)
    address = fields.Text()
    signature = fields.Binary()
    image_1920 = fields.Image()
    image_512 = fields.Image("Image 512", related="image_1920", max_width=512, max_height=512)
    department_id = fields.Many2one('school.department')
    department_hod = fields.Char(related='department_id.hod')
    date_time_of_joining = fields.Datetime()

    @api.model
    def create(self, values):
        print(values)
        print(values.get('phone'))
        values['teacher_identity'] = self.env['ir.sequence'].sudo().next_by_code('school.student') or _('New')
        res = super(SchoolTeacher, self).create(values)
        print(res)
        print(res.phone)
        if res.phone and len(res.phone) != 10:
            raise ValidationError(_('Contact number must have 10 digit! not %s digit and change this value %s' % (
                len(res.phone), res.phone)))
        return res

    def write(self, values):
        print("Write")
        print(values)
        print(values.get('phone'))
        # if not values.get('mark'):
        #     raise ValidationError(_('Please enter mark'))
        res = super(SchoolTeacher, self).write(values)
        print(self)
        print(self.mark)
        if not self.mark or self.mark == 0:
            raise ValidationError(_('Please enter mark 2'))
        print(self.phone)
        if self.phone and len(self.phone) != 10:
            raise ValidationError(_('Contact number must have 10 digit! not %s digit and change this value %s' % (
                len(self.phone), self.phone)))
        return res

    def copy(self, default=None):
        print(self)
        print(self.name)
        if self.name:
            self.name = self.name + '(Copy)'
        print(self.mark)
        return super(SchoolTeacher, self).copy(default=default)

    def unlink(self):
        raise ValidationError(_('Not able to delete'))
        return super(SchoolTeacher, self).unlink()
