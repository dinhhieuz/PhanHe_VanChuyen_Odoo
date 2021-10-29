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
    ], string='Tình trạng phiếu', default='wait',)
    # sử dụng vòng lập foreach để lấy danh sách vào trong Selection (làm sau)
    ngaytao_phieu = fields.Date(string='Ngày tạo phiếu ', default=datetime.today(), readonly="1")
    # --- Đợi bình yên để kế thừa
    id_xe_phieu = fields.Char('Xe giao hàng')
    id_shipper_phieu = fields.Many2one('shipper.nhom1', string="Người giao hàng", delegate=True, default='')
    id_nhanvien_taophieu = fields.Many2one('hr.employee', string="Nhân viên tạo phiếu", delegate=True, default='')

    # describing customer
    # tự động sinh mã khi tạo (làm sau)

    @api.constrains('tinhtrang_phieu','id_shipper_phieu')
    def onchange_status_shipper(self):
        if self.tinhtrang_phieu == 'doing':
            get_id_shipper = str(self.id_shipper_phieu).strip('shipper.nhom1(,)')
            self.env.cr.execute("""Update shipper_nhom1 set trangthai='danggiaohang' where id = """+get_id_shipper)


    # id_khachhang = fields.One2many(comodel_name='res.users', inverse_name='rel_id')