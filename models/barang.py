from odoo import api, fields, models

class Barang(models.Model):
    _name = 'toko.barang'
    _description = 'New Description'

    Kode_Barang = fields.Integer(string='kode barang')
    Nama_Barang = fields.Char(string='nama barang')
    Jumlah_Beli = fields.Integer(string='jumlah beli')
    Harga_Beli = fields.Integer(string='harga beli')
    Harga_Jual = fields.Integer(string='harga jual')

    
    transaksi_id = fields.Many2one(
        comodel_name='toko.transaksi', 
        string='')
    
    