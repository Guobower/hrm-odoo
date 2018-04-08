# -*- coding: utf-8 -*-

from odoo import models,fields,api,exceptions

class Nhanvien(models.Model):
    _name = "hrm.nhanvien"
    _description = "quan ly nhan vien"


    manv = fields.Char("Mã Nhân Viên")
    hoten = fields.Char("Họ Tên")
    gioitinh = fields.Selection(string="Giới tính", selection=[('0', 'Nữ'), ('1', 'Nam'), ])
    noisinh = fields.Text("Nơi Sinh")
    ngay_sinh = fields.Date("Ngày Sinh")
    phongban = fields.Many2one(comodel_name="hrm.phongban", string="Phòng Ban", required=False, )
    quequan = fields.Text("Quêu Quán")
    socmt = fields.Integer("Số CMT")
    anh = fields.Binary("Ảnh")

    @api.constrains("hoten")
    def _hoten_validate(self):
        for nv in self:
            if len(nv.hoten) < 6:
                raise exceptions.ValidationError(u"Tên nhân viên quá ngắn")
