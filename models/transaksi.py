from odoo import api, fields, models

class Transaksi(models.Model):
    _name = 'toko.transaksi'
    _description = 'New Description'

    Kode_Barang = fields.Integer(string='kode barang')
    Tanggal = fields.Datetime(string='tanggal',default=fields.Datetime.now,)
    Nik = fields.Integer(string='nik')
    
    
    barang_ids = fields.One2many(
        comodel_name='toko.barang', 
        inverse_name='transaksi_id', 
        string='Barangnya')