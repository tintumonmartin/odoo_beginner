# -*- coding: utf-8 -*-

from odoo import models, fields, api


class MarkReportPrint(models.AbstractModel):
    _name = 'report.school_library.print_sample_report'

    @api.model
    def _get_report_values(self, docids, data):
        """in this function can access the data returned from the button
        click function"""
        model_id = data['model_id']
        value = []
        query = """SELECT *
                        FROM sale_order as so
                        JOIN sale_order_line AS sl ON so.id = sl.sale_order_id
                        WHERE sl.id = %s"""
        value.append(model_id)
        self._cr.execute(query, value)
        record = self._cr.dictfetchall()
        return {
            'docs': record,
            'date_today': fields.Datetime.now(),
        }
