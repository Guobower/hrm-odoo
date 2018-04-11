# -*- coding: utf-8 -*-

from odoo import models,fields,api,exceptions

class Chucvu(models.Model):
    _name = "hrm.chucvu"

    macv = fields.Char("Mã Chức Vụ", default="001")
    name = fields.Char("Tên chức Vụ")
    ghichu = fields.Text("Ghi Chú", default="Không")
    nhanvien = fields.One2many(comodel_name="hrm.nhanvien", inverse_name="chucvu", string="Nhân Viên")
    sonv = fields.Integer("Số nhân viên",compute="_dem_nv",store=True)

    @api.depends("nhanvien")
    def _dem_nv(self):
        for chucvu in self:
            chucvu.sonv = len(chucvu.nhanvien)



