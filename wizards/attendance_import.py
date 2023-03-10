# -*- coding: utf-8 -*-
###############################################################################
#
#    OpenEduCat Inc.
#    Copyright (C) 2009-TODAY OpenEduCat Inc(<http://www.openeducat.org>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from odoo import models, fields


class OpAllStudentWizard(models.TransientModel):
    _name = "school.all.student"
    _description = "All Student Wizard"

    course_id = fields.Many2one(
        'school.class', 'Course',
        default=lambda self: self.env['school.attendance.sheet'].browse(
            self.env.context['active_id']).register_id.course_id.id or False,
        readonly=True)
    batch_id = fields.Many2one(
        'school.subject', 'Batch',
        default=lambda self: self.env['school.attendance.sheet'].browse(
            self.env.context['active_id']).register_id.batch_id.id or False,
        readonly=True)
    student_ids = fields.Many2many('school.student', string='Add Student(s)')

    def confirm_student(self):
        for record in self:
            for sheet in self.env.context.get('active_ids', []):
                sheet_browse = self.env['school.attendance.sheet'].browse(sheet)
                absent_list = [
                    x.student_id for x in sheet_browse.attendance_line]
                all_student_search = self.env['school.student'].search(
                    [('course_detail_ids.course_id', '=',
                      sheet_browse.register_id.course_id.id),
                     ('course_detail_ids.batch_id', '=',
                      sheet_browse.register_id.batch_id.id)])
                all_student_search = list(
                    set(all_student_search) - set(absent_list))
                for student_data in all_student_search:
                    vals = {'student_id': student_data.id, 'present': True,
                            'attendance_id': sheet}
                    if student_data.id in record.student_ids.ids:
                        vals.update({'present': False})
                    self.env['school.attendance.line'].create(vals)
