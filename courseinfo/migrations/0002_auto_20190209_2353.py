# Generated by Django 2.1.5 on 2019-02-09 23:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseinfo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['course_number', 'course_name']},
        ),
        migrations.AlterModelOptions(
            name='instructor',
            options={'ordering': ['last_name', 'first_name']},
        ),
        migrations.AlterModelOptions(
            name='registration',
            options={'ordering': ['section', 'student']},
        ),
        migrations.AlterModelOptions(
            name='section',
            options={'ordering': ['course__course_numebr', 'section_name', 'semester__semester_name']},
        ),
        migrations.AlterModelOptions(
            name='semester',
            options={'ordering': ['semester_name']},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['last_name', 'first_name', 'nickname']},
        ),
        migrations.AlterUniqueTogether(
            name='course',
            unique_together={('course_number', 'course_name')},
        ),
        migrations.AlterUniqueTogether(
            name='instructor',
            unique_together={('last_name', 'first_name')},
        ),
        migrations.AlterUniqueTogether(
            name='registration',
            unique_together={('section', 'student')},
        ),
        # migrations.AlterUniqueTogether(
        #     name='student',
        #     unique_together={('last_name', 'first_name', 'nickname')},
        # ),
    ]
