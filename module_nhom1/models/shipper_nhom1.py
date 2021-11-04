# -*- coding: utf-8 -*-
from odoo import _, api, fields, models
class nhom1(models.Model):
    _name = "shipper.nhom1"
    _description = "Module vận chuyển nhóm 1"

    name = fields.Char(string='Mã SP', required=True, copy=False, readonly=True,
                       default=lambda seft: _('New'))
    ten = fields.Char(string='Họ và tên', required = True)
    avatar = fields.Binary("Avatar")
    ngaysinh = fields.Date("Ngày sinh")
    diachi = fields.Text("Địa chỉ thường trú")
    gioitinh = fields.Selection([('nam', 'Nam'), ('nu', 'Nữ')], string='Giới tính', default='nam')
    emailsp = fields.Char(string='Email')
    sdt = fields.Char("Số điện thoại")
    cmnd = fields.Char("Số CMND/CCCD")
    covid = fields.Boolean('Đã tiêm Covid', default=False)
    datecovid = fields.Date('Thời gian tiêm')
    idbanglai = fields.Char(string='Mã số bằng lái', required=True)
    hang = fields.Selection([('B2','B2'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F')], string='Hạng', default='B2')
    ngayhethan = fields.Date('Có giá trị đến ')
    suckhoe = fields.Boolean('Đã khám sức khỏe', default=False)
    imagesuckhoe = fields.Binary('Giấy khám sức khỏe')
    imagebanglai = fields.Binary('Bằng lái xe')
    trangthai = fields.Selection([('danggiaohang', 'Đang giao hàng'), ('chogiaohang', 'Chờ giao hàng')], string='Trạng thái', default='')
    mota = fields.Text('Mô tả công việc')

    _sql_constraints = [
        ('cmnd', 'unique (cmnd)', 'CMND đã tồn tại, vui lòng nhập khác!!!')
    ]

    # def custom_remove(self):
    #         for module in self:
    #             module.unlink()
    #         pass

    @api.model
    def create(self, vals):
        if vals.get('name', ('New')) == ('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('shipper.nhom1') or _('New')
        res = super(nhom1, self).create(vals)
        return res
