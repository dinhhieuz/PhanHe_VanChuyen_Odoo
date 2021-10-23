from odoo import api, fields, models
from datetime import datetime
class stock(models.Model):
    _inherit = "stock.picking"
    _description = "Module giao hàng nhóm 1 kế thừa từ odoo"

    tinhtrang_phieu = fields.Selection([
        ('wait', 'Chờ chuyển'),
        ('doing', 'Đang chuyển'),
        ('done', 'Đã chuyển'),
        ('delay', 'Trì hoãn chuyển')
    ], string='Tình trạng phiếu', default='wait')
    # sử dụng vòng lập foreach để lấy danh sách vào trong Selection (làm sau)
    nguoitao_phieu = fields.Char('Người tạo phiếu', required=True)
    ngaytao_phieu = fields.Date(string='Ngày tạo phiếu ', default=datetime.today(),readonly = "1")

    # IDnguoitao_phieu = fields.One2many(comodel_name='res.users', inverse_name='rel_id')

    # describing customer
    # tự động sinh mã khi tạo (làm sau)

    # id_khachhang = fields.One2many(comodel_name='res.users', inverse_name='rel_id')
