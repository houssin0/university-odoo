# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Classes(models.Model):
    _name = 'school.class'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "class record"
    _rec_name = 'name'

    name = fields.Char(string="Nom de Semestre", required=False)
    subject_ids = fields.Many2many('school.subject', string="Modules", required=True, )
    # student_ids = fields.Many2many(comodel_name="school.student", string="Students", required=False, )

    # @api.multi
    # def create_class_report(self):
    #     print("create_class_report")