# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Subject(models.Model):
    _name = 'school.element'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "element record"

    sequence = fields.Integer(string="Sequence")
    name = fields.Char(string="Nom d'élément")
    teacher_ids = fields.Many2one('school.teacher', string="Professeur", )
