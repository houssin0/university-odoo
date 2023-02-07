 # -*- coding: utf-8 -*-

from odoo import models, fields, api


class School(models.Model):
    _name = 'school.teacher'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "teacher record"

    name = fields.Char('Le nom Complét', size=128, required=True)
    phone_number = fields.Char(string="Numéro de telephone", size=11, )
    birth_date = fields.Date('Date de naissance', required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], 'Gender', required=True)
    nationality = fields.Many2one('res.country', 'Nationality')
    image = fields.Binary('Image', )
    email=fields.Char('Email',size=30)
    subject_id = fields.Many2many('school.element', string="Module", required=False, )
    cni_id = fields.Char(string="CNI", size=7, required=True)
    #
    # def _get_teacher_subjects(self):
    #     for rec in self:
    #         subjects = rec.env['school.subject'].search([('teacher_id', '=', self.id)])
    #         for subject in subjects:
    #             self.subject_id = subject.teacher_ids.name
