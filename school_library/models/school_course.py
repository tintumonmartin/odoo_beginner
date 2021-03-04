# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class SchoolCourse(models.Model):
    _name = 'school.course'
    _description = 'School Course'
    _order = "name asc"
    _rec_name = "name"

    name = fields.Char("Course Name", required=True)
    hod = fields.Char(related='department_id.hod')
    department_id = fields.Many2one('school.department')
    description = fields.Text()
    student_ids = fields.One2many('school.student', 'course_id')

    @api.model
    def create(self, values):
        print(values)
        return super(SchoolCourse, self).create(values)
