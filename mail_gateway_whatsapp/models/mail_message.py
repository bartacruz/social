from odoo import _,models, fields

class MailMessage(models.Model):
    _inherit = 'mail.message'

    whatsapp_template_id = fields.Many2one('mail.whatsapp.template', string=_("WhatsApp Template"), ondelete='set null')