from odoo import api, fields, models

class Karyawan(models.Model):
    _name = 'toko.karyawan'
    _description = 'New Description'

    Nik = fields.Integer(string='nik')
    Name = fields.Char(string='name')
    Bagian = fields.Char(string='bagian')
    
    
    