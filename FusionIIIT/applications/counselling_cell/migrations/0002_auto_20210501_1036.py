# Generated by Django 3.1.5 on 2021-05-01 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('globals', '0003_auto_20191024_1242'),
        ('counselling_cell', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='counsellingfaq',
            old_name='counseliing_category',
            new_name='counselling_category',
        ),
        migrations.RenameField(
            model_name='studentmeetingrequest',
            old_name='requested_faculty_invitie',
            new_name='requested_faculty_invitee',
        ),
        migrations.RenameField(
            model_name='studentmeetingrequest',
            old_name='requested_student_invitie',
            new_name='requested_student_invitee',
        ),
        migrations.AlterField(
            model_name='counsellingissuecategory',
            name='category_id',
            field=models.CharField(max_length=40, unique=True),
        ),
        migrations.AlterField(
            model_name='counsellingmeeting',
            name='meeting_host',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='globals.extrainfo'),
        ),
    ]