# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import AccessError, UserError, ValidationError


class StudentAttendance(models.Model):
    _name = 'student.attendance'
    _description = 'School Attendance'
    _rec_name = 'student_id'

    student_id = fields.Many2one('school.student', string='Student')
    attendance = fields.Selection([('present', 'Present'),
                                   ('absent', 'Absent'),
                                   ('leave', 'Leave'),
                                   ('half_day', 'Half Day'),
                                   ('special_permission', 'Special Permission')])
