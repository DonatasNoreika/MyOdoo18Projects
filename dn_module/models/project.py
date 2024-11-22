from odoo import fields, models, _


class DNProject(models.Model):
    _name = 'dn_module.project'
    _description = "DN projektai"

    name = fields.Char(string="Pavadinimas", required=True)
    start_date = fields.Date(string="Data")
    teamleader_id = fields.Many2one(comodel_name='res.partner', string=_("Vadovas"), ondelete="set null")
    employee_ids = fields.Many2many(comodel_name='hr.employee', string=_("Darbuotojai"))
#
    jobs_ids = fields.One2many(comodel_name='dn_module.job', inverse_name='project_id')
#
#
class Job(models.Model):
    _name = "dn_module.job"
    _description = "jobs"

    name = fields.Char(string="Pavadinimas", required=True)
    project_id = fields.Many2one(comodel_name='dn_module.project', string=_("Projektas"), ondelete='set null')
