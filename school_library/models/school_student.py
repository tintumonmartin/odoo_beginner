# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import AccessError, UserError, ValidationError


class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'School Student'
    _rec_name = 'student_identity'

    name = fields.Char("Student Name", required=True)
    active = fields.Boolean('Active', default=True)
    student_identity = fields.Char(readonly=True)
    phone = fields.Char(size=10)
    address = fields.Text()
    image_1920 = fields.Image()
    image_512 = fields.Image("Image 512", related="image_1920", max_width=512, max_height=512)
    department_id = fields.Many2one('school.department')
    department_hod = fields.Char(related='department_id.hod')
    date_time_of_joining = fields.Datetime()
    deposit = fields.Float(default=10000)
    fine = fields.Float(default=0.0)
    fine_paid = fields.Float()
    fine_pending = fields.Float()
    remarks = fields.Text()
    mark = fields.Integer()
    result = fields.Selection([('pass', 'Pass'), ('fail', 'Fail')], compute="_compute_result")
    book_ids = fields.Many2many('library.book', 'library_book_student_rel', 'student_id', 'book_id',
                                string="Books", copy=False)

    @api.depends('mark')
    def _compute_result(self):
        for record in self:
            print(record)
            if record.mark >= 30:
                record.result = 'pass'
            else:
                record.result = 'fail'

    @api.model
    def create(self, values):
        print(values)
        print(values.get('phone'))
        values['student_identity'] = self.env['ir.sequence'].sudo().next_by_code('school.student') or _('New')
        res = super(SchoolStudent, self).create(values)
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
        res = super(SchoolStudent, self).write(values)
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
        return super(SchoolStudent, self).copy(default=default)

    def unlink(self):
        raise ValidationError(_('Not able to delete'))
        return super(SchoolStudent, self).unlink()
