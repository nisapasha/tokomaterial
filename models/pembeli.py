from odoo import api, fields, models

class Pembeli(models.Model):
    _name = 'toko.pembeli'
    _description = 'New Description'

    name = fields.Char(string='nama')
    alamat = fields.Char(string='alamat')
    
    