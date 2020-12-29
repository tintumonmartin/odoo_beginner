from odoo import models, fields


class User(models.Model):
    _inherit = 'res.users'

    teacher_id = fields.One2many('school.teacher', 'user_id', string="Teacher")
    teacher_department_id = fields.Many2one(related='teacher_id.department_id')

    student_id = fields.One2many('school.student', 'user_id', string="Student")
    student_department_id = fields.Many2one(related='student_id.department_id')
