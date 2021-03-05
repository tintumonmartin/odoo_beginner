# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library book'

    name = fields.Char("Book Name", required=True)
    book_identity = fields.Char()
    author = fields.Char()
    color = fields.Integer('Color Index')
    total_count = fields.Integer()
    availability = fields.Integer()
    teacher_ids = fields.Many2many('school.teacher')
    student_ids = fields.Many2many('school.student', 'library_book_student_rel', 'book_id', 'student_id',
                                   string="Student", copy=False)
    remarks = fields.Text()

    @api.model
    def create(self, values):
        print(values)
        return super(LibraryBook, self).create(values)
