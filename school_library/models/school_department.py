# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class SchoolDepartment(models.Model):
    _name = 'school.department'
    _description = 'School Department'

    name = fields.Char("Department Name", required=True)
    hod = fields.Char()
    course_id = fields.Integer()
    description = fields.Text()
    student_id = fields.One2many('school.student', 'department_id')

    # student_id = fields.Many2one('school.student', string='Students')

    @api.model
    def create(self, values):
        print(values)
        return super(SchoolDepartment, self).create(values)
