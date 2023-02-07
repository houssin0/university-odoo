# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Student(models.Model):
    _name = 'school.student'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "student record"





    class_id = fields.Many2one(comodel_name="school.class", string="Filière", required=True, )
    line_ids = fields.Many2one(comodel_name="school.subject",  string="Subject Lines", )
    first_name = fields.Char('Prénom', size=128, translate=True, required=True)
    last_name = fields.Char('Nom de famille', size=128, required=True)
    phone_number = fields.Char(string="Numéro de telephone", size=11, )

    birth_date = fields.Date('Date de naissance', required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], 'Gender', required=True)
    nationality = fields.Many2one('res.country', 'Nationality')
    image = fields.Binary('Image', )
    email = fields.Char('Email', size=30)
    student_id = fields.Char(string='CNE', size=10, required=True)
    cni_id = fields.Char(string="CNI", size=7, required=True)
    # @api.multi
    # def create_student_report(self):
    #     data = {'model': 'payroll_salary.wizard', 'form': self.read()[0]}
    #     students = self.env['school.student'].search([])
    #     for rec in self:
    #         if rec.teacher_ids:
    #             for student in students:
    #                 if student.teacher_ids.id in rec.teacher_ids:
    #                     print(student.name)

    # return self.env.ref('school.student_report_print').report_action(self, data)
