# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class SchoolDepartment(models.Model):
    _name = 'school.department'
    _description = 'School Department'

    name = fields.Char("Department Name", required=True)
    hod = fields.Char()
    course_ids = fields.One2many('school.course', 'department_id')
    description = fields.Text()
    student_id = fields.One2many('school.student', 'department_id')

    @api.model
    def create(self, values):
        print(values)
        return super(SchoolDepartment, self).create(values)
