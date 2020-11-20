# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'School Student'
    _rec_name = 'student_identity'

    name = fields.Char("Student Name", required=True)
    student_identity = fields.Char(readonly=True)
    phone = fields.Char(size=10)
    address = fields.Text()
    image_1920 = fields.Image(required=True)
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
        values['student_identity'] = self.env['ir.sequence'].sudo().next_by_code('school.student') or _('New')
        print(values)
        return super(SchoolStudent, self).create(values)
