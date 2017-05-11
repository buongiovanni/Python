# -*- coding: utf-8 -*-
# Copyright 2017 Jose Maria Bernet
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)


from odoo import models, fields, api, exceptions    # ← IMPORTS


class OpenAcademyCourse(models.Model):              # ← DEFINICION DE LA CLASE PYTHON
    _name = 'openacademy.course'                    # ← NOMBRE TECNICO DEL MODELO
    _description = 'Curso'                          # ← NOMBRE LEGIBLE DEL MODELO

                                                    # ↓ DEFINICION DE LOS CAMPOS DEL MODELO/ COLUMNAS DB
    name = fields.Char(string='Nombre')
    session_ids = fields.One2many(comodel_name='openacademy.session', inverse_name='course_id', string='Sesiones')
    description = fields.Text(string='Descripcion del curso')
    min_attendance = fields.Integer(string='Asistentes minimos')
    state = fields.Selection(selection=[('por_empezar','Por empezar'),('activo','Activo'), ('finalizado','Finalizado')],
                             string='Estado', default='por_empezar')


    @api.multi
    def open_new_session_dialog(self):
        for course in self:
            return {
                'name': 'Nueva sesion',
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'openacademy.new.session.wizard',
                'type': 'ir.actions.act_window',
                'target': 'new'
            }

    @api.multi
    def finish_course(self):
        for course in self:
            course.state = 'finalizado'

    @api.multi
    def activate_course(self):
        for course in self:
            if not course.session_ids:
                raise exceptions.Warning('Debe de crear al menos una sesión para empezar el curso.')

            for session in course.session_ids:
                if len(session.attendees_ids) < course.min_attendance:
                    raise exceptions.Warning('Una de las sesiones no llega al minimo requerido.')


            course.state = 'activo'