from odoo import api, fields, models,_
from odoo.exceptions import ValidationError

#creating database table (patient)
class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread']
    _description="patient record"



    #fields of database
    name=fields.Char(string='Name',required=True,tracking=True)  #tracking to view fields in chatter section
    age=fields.Integer(string="age",tracking=True)
    is_child=fields.Boolean(string="IS Child ?",tracking=True)
    notes= fields.Text(string="Notes",tracking=True)
    gender=fields.Selection([('male','Male'),('female','Female'),('others','Others')],string="Gender",tracking=True)
    captalizename=fields.Char(string ='Captalize Name',compute='_compute_captalizename',store=True)
    ref=fields.Char(string='reference',default=lambda self:_('new'))
    #to view the captalize attribute before saving
    @api.depends('name')
    def _compute_captalizename(self):
        for rec in self:
           if rec.name:
              rec.captalizename=rec.name.upper()
           else:
               rec.captalizename=''

    #to define constrains on attributes
    @api.constrains('age','is_child')
    def check_child_age(self):
        for rec in self :
            if rec.is_child and rec.age==0:
                raise ValidationError(_("age must be entered"))


    #function to make the is_child option to set to false depend on the value of age attribute
    #how to define onchange api function
    @api.onchange('age')
    def onchange_age(self):
        if self.age<=10:
            self.is_child=True
        else:
            self.is_child=False
    #used like post in document middle ware to make changes to the database instance after saving
    #inherit create method
    @api.model_create_multi
    def create(self,val_list): #val_list containing all fields of the current database instace
        for val in val_list:
            val['ref']=self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient,self).create(val_list)