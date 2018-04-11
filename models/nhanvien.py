# -*- coding: utf-8 -*-

from odoo import models,fields,api,exceptions
import re

class Nhanvien(models.Model):
    _name = "hrm.nhanvien"
    _description = "quan ly nhan vien"
    _rec_name = "hoten"

    manv = fields.Char("Mã Nhân Viên")
    hoten = fields.Char("Họ Tên",help="Nhập đầy đủ họ tên nhân viên")
    gioitinh = fields.Selection(string="Giới tính", selection=[('0', 'Nữ'), ('1', 'Nam'), ])
    noisinh = fields.Text("Nơi Sinh")
    ngaysinh = fields.Date("Ngày Sinh")
    sdt = fields.Char("Số Điện Thoại")
    quequan = fields.Text("Quê Quán")
    diachi = fields.Text("Địa Chỉ")
    socmt = fields.Char("Số CMT")
    anh = fields.Binary("Ảnh")
    dantoc = fields.Char("Dân Tộc")
    email = fields.Char("Email")
    tongiao = fields.Selection(string="Tôn Giáo", selection=[('0', 'Có'), ('1', 'Không'), ])
    phongban = fields.Many2one(comodel_name="hrm.phongban", string="Phòng Ban", required=False, )
    chucvu = fields.Many2one(comodel_name="hrm.chucvu", string="Chức Vụ")
    bangcap = fields.Selection(string="Bằng cấp", selection=[
                ('0', 'Cao học'), ('1', 'Đại học'),
                ('2','Cao đẳng'),('3','Trung cấp'),('4','Khác') ], required=False, )

    lichdieuchuyen = fields.One2many(comodel_name="hrm.lichdieuchuyen",inverse_name="nhanvien",string="Lịch Điều Chuyển",readonly=True)


    _sql_constraints = [
        ('unique_manv','unique(manv)',u'Mã nhân viên đã tồn tại!!!'),
    ]
    

    @api.constrains("hoten")
    def _hoten_validate(self):
        for nv in self:
            if len(nv.hoten) < 6:
                raise exceptions.ValidationError(u"Tên nhân viên quá ngắn")

    @api.constrains("sdt")
    def _sdt_validate(self):
        for nv in self:
            if re.match(nv.sdt,"/^0(1\d{9}|9\d{8})$/") == False:
                raise  exceptions.ValidationError(u'Sai định dạng số điện thoại')







