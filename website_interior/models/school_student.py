# -*- coding: utf-8 -*-

from odoo import models, fields


class SchoolStudent(models.Model):
    _inherit = 'school.student'

    user_type = fields.Selection([('student', 'Student'),
                                  ('phd', 'PHD'),
                                  ('teacher', 'Teacher'),
                                  ('admin', 'Admin')], default='student')
    mobile = fields.Char()
    landline = fields.Char()
    student_type = fields.Selection([('alumni', 'Alumni'),
                                     ('current', 'Current')], default='current')
    # Fields Incremental Definition
    fine_paid = fields.Float(string='Paid fine',help='Fine paid by student')
