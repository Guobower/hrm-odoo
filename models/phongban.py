# -*- coding: utf-8 -*-

from odoo import models,fields,api,exceptions

class Phongban(models.Model):
    _name = "hrm.phongban"

    name = fields.Char("Tên Phòng Ban")
    diachi = fields.Char("Địa Chỉ")
    sdt = fields.Integer("Số Điện Thoại")
