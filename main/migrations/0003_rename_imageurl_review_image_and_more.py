# Generated by Django 4.1.7 on 2023-03-06 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_comment_datecreated_alter_follow_datecreated_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='imageURL',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='imageURL',
            new_name='image',
        ),
    ]
