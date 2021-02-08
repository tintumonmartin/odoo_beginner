# -*- coding: utf-8 -*-

from odoo import models, fields, api


class RailwayManagement(models.Model):
    _name = 'railway.management'
    _description = 'railway details'

    train_name = fields.Char(string='train name')
    train_source = fields.Char(string='train source')

    destination = fields.Char(string='destination')
    arrival_time = fields.Char(string='arrival_time')
    departure_time = fields.Char(string='departure_time')
    train_no = fields.Char(string='train_no')
    train_seat = fields.Char(string='train seat')
    a_seat1 = fields.Char(string='Seat 1')
    a_seat2 = fields.Char(string='a_seat2')
    a_seat3 = fields.Char(string='a_seat3')
    b_seat1 = fields.Char(string='b_seat1')
    b_seat2 = fields.Char(string='b_seat2')
    b_seat3 = fields.Char(string='b_seat3')
    w_seat1 = fields.Char(string='w_seat1')
    w_seat2 = fields.Char(string='w_seat2')
    w_seat3 = fields.Char(string='w_seat1')
# name = fields.Char()
# value = fields.Integer()
# value2 = fields.Float(compute="_value_pc", store=True)
# description = fields.Text()

# @api.depends('value')
# def _value_pc(self):
#     for record in self:
#         record.value2 = float(record.value) / 100
