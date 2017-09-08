# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Cells(models.Model):
    id = models.AutoField()
    description = models.CharField(max_length=300)
    plants = models.ForeignKey('Plants', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Cells'
        unique_together = (('id', 'plants'),)


class Checkpointdefects(models.Model):
    id = models.IntegerField()
    checkpoints_id_check_points = models.ForeignKey('Checkpoints', models.DO_NOTHING, db_column='Checkpoints_id_check_points')  # Field name made lowercase.
    defects = models.ForeignKey('Defects', models.DO_NOTHING, db_column='Defects_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CheckpointDefects'
        unique_together = (('id', 'checkpoints_id_check_points', 'defects'),)


class Checkpoints(models.Model):
    id_check_points = models.IntegerField()
    description = models.CharField(max_length=45)
    checkpoint_defect_id = models.IntegerField(db_column='Checkpoint_defect_id')  # Field name made lowercase.
    inspectiontypes = models.ForeignKey('Inspectiontypes', models.DO_NOTHING, db_column='InspectionTypes_id')  # Field name made lowercase.
    stages = models.ForeignKey('Stages', models.DO_NOTHING, db_column='Stages_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Checkpoints'
        unique_together = (('id_check_points', 'inspectiontypes', 'stages'),)


class Defectcategories(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DefectCategories'


class Defectclosure(models.Model):
    id = models.IntegerField()
    image_1 = models.TextField()
    image_2 = models.TextField()
    image_3 = models.TextField()
    created_time = models.TimeField()
    updated_time = models.TimeField()
    activity_id = models.IntegerField()
    repair_id = models.IntegerField()
    users = models.ForeignKey('Users', models.DO_NOTHING)
    inspection_defects = models.ForeignKey('Inspectiondefects', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'DefectClosure'
        unique_together = (('id', 'users', 'inspection_defects'),)


class Defects(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=300)
    defect_category_id = models.IntegerField()
    source_gate_id = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Defects'


class Inspectiondefects(models.Model):
    id = models.IntegerField(db_column='Id')  # Field name made lowercase.
    vin = models.CharField(max_length=45)
    check_point_id = models.IntegerField(blank=True, null=True)
    part_defect_id = models.CharField(max_length=45)
    observations = models.CharField(max_length=45)
    image_1 = models.TextField()
    image_2 = models.TextField()
    image_3 = models.TextField()
    created_time = models.TimeField()
    updated_time = models.TimeField()
    users = models.ForeignKey('Users', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'InspectionDefects'
        unique_together = (('id', 'users'),)


class Inspectiontypes(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'InspectionTypes'


class Modelparts(models.Model):
    id_model_parts = models.IntegerField()
    image = models.TextField(blank=True, null=True)
    parts = models.ForeignKey('Parts', models.DO_NOTHING)
    models = models.ForeignKey('Models', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ModelParts'
        unique_together = (('id_model_parts', 'parts', 'models'),)


class Modelstationstages(models.Model):
    id = models.IntegerField(primary_key=True)
    model_id = models.IntegerField()
    station_id = models.IntegerField()
    stage_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ModelStationStages'


class Models(models.Model):
    id = models.IntegerField(primary_key=True)
    sales_code = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    base_sales_code = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Models'


class Partdefect(models.Model):
    id_part_defect = models.IntegerField()
    parts = models.ForeignKey('Parts', models.DO_NOTHING)
    defects = models.ForeignKey(Defects, models.DO_NOTHING)
    stages = models.ForeignKey('Stages', models.DO_NOTHING, db_column='Stages_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PartDefect'
        unique_together = (('id_part_defect', 'parts', 'defects', 'stages'),)


class Parts(models.Model):
    id_parts = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=45)
    image = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Parts'


class Plants(models.Model):
    plant_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'Plants'


class Repairs(models.Model):
    id = models.IntegerField()
    description = models.CharField(max_length=300, blank=True, null=True)
    defects = models.ForeignKey(Defects, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Repairs'
        unique_together = (('id', 'defects'),)


class Reportdelivery(models.Model):
    id = models.IntegerField()
    user_id = models.IntegerField()
    role_id = models.IntegerField()
    report_schedule = models.ForeignKey('Reportschedule', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ReportDelivery'
        unique_together = (('id', 'report_schedule'),)


class Reportschedule(models.Model):
    id = models.IntegerField()
    hour = models.CharField(max_length=45)
    day = models.CharField(max_length=45)
    month = models.CharField(max_length=45)
    shift = models.CharField(max_length=45)
    week = models.CharField(max_length=45)
    reports = models.ForeignKey('Reports', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ReportSchedule'
        unique_together = (('id', 'reports'),)


class Reports(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'Reports'


class Roles(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'Roles'


class Shifts(models.Model):
    id = models.IntegerField()
    start_time = models.TimeField()
    end_time = models.TimeField(blank=True, null=True)
    plants = models.ForeignKey(Plants, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Shifts'
        unique_together = (('id', 'plants'),)


class Sourcegate(models.Model):
    idsourcegate = models.IntegerField(db_column='idSourceGate', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SourceGate'


class Stages(models.Model):
    id = models.IntegerField()
    description = models.CharField(max_length=300)
    station = models.ForeignKey('Stations', models.DO_NOTHING)
    image = models.TextField(db_column='Image')  # Field name made lowercase.
    modelstationstages = models.ForeignKey(Modelstationstages, models.DO_NOTHING, db_column='ModelStationStages_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Stages'
        unique_together = (('id', 'station', 'modelstationstages'),)


class Stations(models.Model):
    id = models.IntegerField()
    description = models.CharField(max_length=300)
    cells = models.ForeignKey(Cells, models.DO_NOTHING, db_column='Cells_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Stations'
        unique_together = (('id', 'cells'),)


class Thresholdhistory(models.Model):
    id = models.IntegerField()
    timestamp = models.DateTimeField(blank=True, null=True)
    thresholds = models.ForeignKey('Thresholds', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ThresholdHistory'
        unique_together = (('id', 'thresholds'),)


class Thresholdnotifications(models.Model):
    id = models.IntegerField()
    role_id = models.IntegerField()
    user_id = models.IntegerField()
    thresholds = models.ForeignKey('Thresholds', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ThresholdNotifications'
        unique_together = (('id', 'thresholds'),)


class Thresholds(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    no_of_occurances = models.CharField(max_length=100)
    duration = models.CharField(max_length=45)
    reset_upon_notification = models.CharField(max_length=45)
    inspection_point_defects_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Thresholds'


class Users(models.Model):
    id = models.IntegerField()
    user_code = models.CharField(max_length=300)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100, blank=True, null=True)
    mobile_number = models.IntegerField()
    email_id = models.CharField(max_length=200)
    roles = models.ForeignKey(Roles, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Users'
        unique_together = (('id', 'roles'),)
