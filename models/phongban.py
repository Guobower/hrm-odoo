# -*- coding: utf-8 -*-

from odoo import models,fields,api,exceptions

class Phongban(models.Model):
    _name = "hrm.phongban"

    name = fields.Char("Tên Phòng Ban")
    diachi = fields.Char("Địa Chỉ")
    sdt = fields.Char("Số Điện Thoại")
    nhanvien = fields.One2many(comodel_name="hrm.nhanvien", inverse_name="phongban", string="Nhân Viên", required=False, )
    sonv = fields.Integer("Số Nhân Viên",compute="_dem_nv", store=True)


    @api.multi
    @api.depends("nhanvien")
    def _dem_nv(self):
        for phongban in self:
            phongban.sonv = len(phongban.nhanvien)




