# -*- coding: utf-8 -*-

from odoo import models,fields,api,exceptions

class Lichdieuchuyen(models.Model):
    _name = "hrm.lichdieuchuyen"
    _rec_name = "nhanvien"

    loai = fields.Selection(string="Loại điều chuyển", selection=[('0','Điều chuyển phòng ban') , ('1','Điều chuyển chức vụ')])
    nhanvien = fields.Many2one(comodel_name="hrm.nhanvien", string="Nhân Viên", required=False )
    chucvu_moi = fields.Many2one(comodel_name="hrm.chucvu",string="Chức vụ mới")
    chucvu_cu = fields.Many2one(comodel_name="hrm.chucvu", string="Chức vụ cũ", readonly=True,compute="_get_cv_nv")
    phongban_cu = fields.Many2one(comodel_name="hrm.phongban",string="Phòng ban cũ")
    phongban_moi = fields.Many2one(comodel_name="hrm.phongban",string="Phòng ban mới")
    date = fields.Date("Ngày bắt đầu")
    date_over = fields.Date("Ngày kết thúc")

    lydo = fields.Text("Lý Do",default="Không")


    @api.onchange("nhanvien")
    def _get_cv_nv(self):
        for lich in self:
            lich.chucvu_cu = lich.nhanvien.chucvu
            lich.phongban_cu = lich.nhanvien.phongban




