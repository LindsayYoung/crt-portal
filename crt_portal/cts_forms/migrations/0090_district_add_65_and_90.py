# Generated by Django 2.2.15 on 2020-09-03 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cts_forms', '0089_crm-referral-to-fbi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='district',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('6', '6'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('11E', '11E'), ('12', '12'), ('12C', '12C'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('17M', '17M'), ('18', '18'), ('19', '19'), ('19M', '19M'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('26S', '26S'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '30'), ('31', '31'), ('32', '32'), ('32M', '32M'), ('33', '33'), ('34', '34'), ('35', '35'), ('36', '36'), ('37', '37'), ('38', '38'), ('39', '39'), ('40', '40'), ('41', '41'), ('42', '42'), ('43', '43'), ('44', '44'), ('45', '45'), ('46', '46'), ('47', '47'), ('48', '48'), ('49', '49'), ('50', '50'), ('51', '51'), ('52', '52'), ('53', '53'), ('54', '54'), ('54M', '54M'), ('55', '55'), ('55 ', '55 '), ('56', '56'), ('57', '57'), ('58', '58'), ('59', '59'), ('59N', '59N'), ('60', '60'), ('61', '61'), ('62', '62'), ('63', '63'), ('64', '64'), ('65', '65'), ('66', '66'), ('67', '67'), ('69', '69'), ('70', '70'), ('71', '71'), ('72', '72'), ('73', '73'), ('74', '74'), ('75', '75'), ('76', '76'), ('77', '77'), ('78', '78'), ('79', '79'), ('80', '80'), ('81', '81'), ('82', '82'), ('83', '83'), ('84', '84'), ('85', '85'), ('86', '86'), ('87', '87'), ('90', '90')], max_length=7, null=True),
        ),
    ]