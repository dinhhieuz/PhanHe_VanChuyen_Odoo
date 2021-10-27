# -*- coding: utf-8 -*-
from odoo import _, api, fields, models
class nhom1(models.Model):
    _name = "shipper.nhom1"
    _description = "Module vận chuyển nhóm 1"

    name = fields.Char(string='Mã SP', required=True, copy=False, readonly=True,
                       default=lambda seft: _('New'))
    ten = fields.Char(string='Tên nhân viên',required = True)
    avatar = fields.Binary("Avatar")
    ngaysinh = fields.Date("Ngày sinh")
    diachi = fields.Text("Địa chỉ nhà")
    sdt = fields.Char("Số điện thoại")
    cmnd = fields.Char("CCMND")
    mota = fields.Text('Mô tả công việc')
    covid = fields.Boolean('Đã tiêm Covid', default=False)
    gioitinh = fields.Selection([('nam', 'Nam'), ('nu', 'Nữ')], string='Giới tính', default='nam')
    trangthai = fields.Selection([('danggiaohang', 'Đang giao hàng'), ('chogiaohang', 'Chờ đơn hàng')], string='Trạng thái', default='')
    nameprivate = fields.Char('Tên công việc')
    image = fields.Binary("Hình ảnh đơn hàng")

    def custom_remove(self):
            for module in self:
                module.unlink()
            pass

    @api.model
    def create(self, vals):
        if vals.get('name', ('New')) == ('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('shipper.nhom1') or _('New')
        res = super(nhom1, self).create(vals)
        return res