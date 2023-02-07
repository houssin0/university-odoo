
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class ReservationRoom(models.Model):
    _name = "school.reservation"
    _description = "Réservation school"

    name = fields.Char(string='Nom', required=True)
    faculty_id = fields.Many2one('school.teacher', string="Professeur")
    start_datetime = fields.Datetime(string='Début', default=lambda self: fields.Datetime.now())
    end_datetime = fields.Datetime(string='Fin')
    classroom_ids = fields.Many2many('school.salles', string='Réservation')
    classroom_id = fields.Many2one('school.salles', string='Réservation', domain="[('id', 'in', classroom_ids)]")

    @api.constrains('start_datetime', 'end_datetime')
    def _check_date_time(self):
        # session_start = datetime.datetime.combine(
        #     fields.Date.from_string(self.session_id.start_date),
        #     datetime.time.min)
        # session_end = datetime.datetime.combine(
        #     fields.Date.from_string(self.session_id.end_date),
        #     datetime.time.max)
        # start_time = fields.Datetime.from_string(self.start_time)
        # end_time = fields.Datetime.from_string(self.end_time)
        start_time = fields.Datetime.from_string(self.start_datetime)
        end_time = fields.Datetime.from_string(self.end_datetime)
        if start_time > end_time:
            raise ValidationError(_('End Time cannot be set before Start Time.'))

    @api.onchange('start_datetime', 'end_datetime')
    def _onchange_classroom_ids(self):
        for record in self:
            if record.start_datetime and record.end_datetime:
                domain = [
                    '|', '|', '|',
                    '&', ('start_datetime', '<', record.start_datetime), ('end_datetime', '>', record.start_datetime),
                    '&', ('start_datetime', '<', record.end_datetime), ('end_datetime', '>', record.end_datetime),
                    '&', ('start_datetime', '<', record.start_datetime), ('end_datetime', '>', record.end_datetime),
                    '&', ('start_datetime', '<', record.end_datetime), ('end_datetime', '>', record.start_datetime),
                ]
                reservation_ids = self.search(domain)
                classroom_ids = self.env['school.salles'].search([]).ids
                if not reservation_ids:
                    self.classroom_ids = classroom_ids
                else:
                    reserve_room_list = []
                    for reservation in reservation_ids:
                        reserve_room_list.append(reservation.classroom_id.id)
                    self.classroom_ids = list(set(classroom_ids) - set(reserve_room_list))
