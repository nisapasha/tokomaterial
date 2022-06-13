from odoo import api, fields, models


class Penjualan(models.Model):
    _name = 'toko.penjualan'
    _description = 'Penjualan'

    name = fields.Char(string='Kode Order')
    tanggal = fields.Datetime(string='Tanggal Penjualan',default=fields.Datetime.now)
    
