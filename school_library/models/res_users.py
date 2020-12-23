from odoo import api, models, fields, _, SUPERUSER_ID
from odoo.exceptions import AccessError


class User(models.Model):
    _inherit = 'res.users'

    # note: a user can only be linked to one employee per company (see sql constraint in ´hr.employee´)
    employee_ids = fields.One2many('hr.employee', 'user_id', string='Related employee')
    employee_id = fields.Many2one('hr.employee', string="Company employee",
                                  compute='_compute_company_employee', search='_search_company_employee', store=False)

    job_title = fields.Char(related='employee_id.job_title', readonly=False, related_sudo=False)
    work_phone = fields.Char(related='employee_id.work_phone', readonly=False, related_sudo=False)
    mobile_phone = fields.Char(related='employee_id.mobile_phone', readonly=False, related_sudo=False)
    employee_phone = fields.Char(related='employee_id.phone', readonly=False, related_sudo=False)
    work_email = fields.Char(related='employee_id.work_email', readonly=False, related_sudo=False)
    category_ids = fields.Many2many(related='employee_id.category_ids', string="Employee Tags", readonly=False,
                                    related_sudo=False)
    school_department_id = fields.Many2one(related='employee_id.department_id', readonly=False, related_sudo=False)
    address_id = fields.Many2one(related='employee_id.address_id', readonly=False, related_sudo=False)
    work_location = fields.Char(related='employee_id.work_location', readonly=False, related_sudo=False)
    employee_parent_id = fields.Many2one(related='employee_id.parent_id', readonly=False, related_sudo=False)
    coach_id = fields.Many2one(related='employee_id.coach_id', readonly=False, related_sudo=False)
    address_home_id = fields.Many2one(related='employee_id.address_home_id', readonly=False, related_sudo=False)
