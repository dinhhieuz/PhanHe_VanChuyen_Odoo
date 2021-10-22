from odoo import api, fields, models
class stock(models.Model):
    _inherit = "stock.picking"
    _description = "Module giao hàng nhóm 1 kế thừa từ odoo"
    # ahieu=fields.Text(string='Anh Hiếu')

