# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-11 07:14
from __future__ import unicode_literals

import c3nav.mapdata.fields
import c3nav.mapdata.models.locations
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('mapdata', '0001_initial'), ('mapdata', '0002_door_obstacle'), ('mapdata', '0003_auto_20161016_1133'), ('mapdata', '0004_auto_20161128_1536'), ('mapdata', '0005_auto_20161128_1735'), ('mapdata', '0006_auto_20161128_1809'), ('mapdata', '0007_auto_20161128_1903'), ('mapdata', '0008_hole'), ('mapdata', '0009_levelconnector'), ('mapdata', '0010_auto_20161203_2139'), ('mapdata', '0011_auto_20161204_1041'), ('mapdata', '0012_auto_20161204_1544'), ('mapdata', '0013_auto_20161208_0937'), ('mapdata', '0014_lineobstacle'), ('mapdata', '0015_auto_20161208_2020'), ('mapdata', '0016_auto_20161208_2023'), ('mapdata', '0017_auto_20161208_2039'), ('mapdata', '0018_auto_20161212_1205'), ('mapdata', '0019_auto_20161216_0923'), ('mapdata', '0020_auto_20161216_0934'), ('mapdata', '0021_auto_20161217_2333'), ('mapdata', '0022_escalator'), ('mapdata', '0023_escalatorslope'), ('mapdata', '0024_oneway'), ('mapdata', '0025_auto_20161219_1440'), ('mapdata', '0026_auto_20161219_1501'), ('mapdata', '0027_auto_20161219_1748'), ('mapdata', '0028_auto_20161219_1757'), ('mapdata', '0029_auto_20161221_1120'), ('mapdata', '0030_remove_locationgroup_routing_inclusion'), ('mapdata', '0031_locationgroup_compiled_room'), ('mapdata', '0032_auto_20161223_2225'), ('mapdata', '0033_auto_20161224_1803'), ('mapdata', '0034_auto_20161224_2104'), ('mapdata', '0035_auto_20161226_1154'), ('mapdata', '0036_arealocation_bssids'), ('mapdata', '0037_auto_20170428_0902'), ('mapdata', '0038_source_image'), ('mapdata', '0039_auto_20170501_1523'), ('mapdata', '0040_auto_20170504_0953'), ('mapdata', '0041_room_outside_area'), ('mapdata', '0042_auto_20170504_1007'), ('mapdata', '0043_auto_20170504_1010'), ('mapdata', '0044_auto_20170504_1023'), ('mapdata', '0045_merge_areas'), ('mapdata', '0046_assign_area'), ('mapdata', '0047_auto_20170505_1002'), ('mapdata', '0048_elevator_area'), ('mapdata', '0049_auto_20170505_1125'), ('mapdata', '0050_categorize_intermediate_areas'), ('mapdata', '0051_move_intermediate_areas'), ('mapdata', '0052_remove_level_intermediate'), ('mapdata', '0053_auto_20170505_1212'), ('mapdata', '0054_remove_obstacle_crop_to_level'), ('mapdata', '0055_auto_20170505_1334'), ('mapdata', '0056_auto_20170506_1531'), ('mapdata', '0057_auto_20170506_1534'), ('mapdata', '0058_auto_20170506_1549'), ('mapdata', '0059_auto_20170507_0937'), ('mapdata', '0060_auto_20170507_0952'), ('mapdata', '0061_auto_20170507_0953'), ('mapdata', '0062_auto_20170508_1400'), ('mapdata', '0063_auto_20170508_1404'), ('mapdata', '0064_auto_20170509_1140'), ('mapdata', '0065_auto_20170509_1140'), ('mapdata', '0066_auto_20170509_1148'), ('mapdata', '0067_auto_20170510_1311'), ('mapdata', '0068_area_stuffed'), ('mapdata', '0069_auto_20170510_1329'), ('mapdata', '0070_point'), ('mapdata', '0071_auto_20170510_1413'), ('mapdata', '0072_auto_20170510_1540'), ('mapdata', '0073_remove_locationgroup_slug'), ('mapdata', '0074_auto_20170510_1556'), ('mapdata', '0075_auto_20170510_1557'), ('mapdata', '0076_auto_20170510_1629'), ('mapdata', '0077_auto_20170510_1637'), ('mapdata', '0078_auto_20170510_1639'), ('mapdata', '0079_auto_20170510_1641'), ('mapdata', '0080_auto_20170510_1642'), ('mapdata', '0081_arealocation_groups'), ('mapdata', '0082_auto_20170510_1644'), ('mapdata', '0083_auto_20170510_1645'), ('mapdata', '0084_auto_20170510_1701'), ('mapdata', '0085_assign_location_level_room'), ('mapdata', '0086_auto_20170510_1820'), ('mapdata', '0087_assign_location_roomsegment_poi'), ('mapdata', '0088_locationgroup_compiled_area'), ('mapdata', '0089_assign_location_area'), ('mapdata', '0090_auto_20170510_1931'), ('mapdata', '0002_fix_space_foreign_keys')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geometry', c3nav.mapdata.fields.GeometryField(geomtype='polygon')),
            ],
            options={
                'verbose_name': 'Building',
                'verbose_name_plural': 'Buildings',
                'default_related_name': 'buildings',
            },
        ),
        migrations.CreateModel(
            name='Door',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('', 'normal'), ('upper', 'upper'), ('lower', 'lower')], default='', max_length=16, verbose_name='level')),
                ('geometry', c3nav.mapdata.fields.GeometryField(geomtype='polygon')),
            ],
            options={
                'verbose_name': 'Door',
                'verbose_name_plural': 'Doors',
                'default_related_name': 'doors',
            },
        ),
        migrations.CreateModel(
            name='Hole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geometry', c3nav.mapdata.fields.GeometryField(geomtype='polygon')),
            ],
            options={
                'verbose_name': 'Hole',
                'verbose_name_plural': 'Holes',
                'default_related_name': 'holes',
            },
        ),
        migrations.CreateModel(
            name='LineObstacle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geometry', c3nav.mapdata.fields.GeometryField(geomtype='linestring')),
                ('width', models.DecimalField(decimal_places=2, default=0.15, max_digits=4, verbose_name='obstacle width')),
            ],
            options={
                'verbose_name': 'Line Obstacle',
                'verbose_name_plural': 'Line Obstacles',
                'default_related_name': 'lineobstacles',
            },
        ),
        migrations.CreateModel(
            name='LocationSlug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(null=True, unique=True, verbose_name='name')),
            ],
            options={
                'verbose_name': 'Slug for Location',
                'verbose_name_plural': 'Slugs für Locations',
                'default_related_name': 'locationslugs',
            },
        ),
        migrations.CreateModel(
            name='Obstacle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geometry', c3nav.mapdata.fields.GeometryField(geomtype='polygon')),
            ],
            options={
                'verbose_name': 'Obstacle',
                'verbose_name_plural': 'Obstacles',
                'default_related_name': 'obstacles',
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField(unique=True, verbose_name='Name')),
                ('bottom', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='bottom coordinate')),
                ('left', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='left coordinate')),
                ('top', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='top coordinate')),
                ('right', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='right coordinate')),
                ('image', models.BinaryField(verbose_name='image data')),
            ],
            options={
                'verbose_name': 'Source',
                'verbose_name_plural': 'Sources',
                'default_related_name': 'sources',
            },
        ),
        migrations.CreateModel(
            name='Stair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geometry', c3nav.mapdata.fields.GeometryField(geomtype='linestring')),
            ],
            options={
                'verbose_name': 'Stair',
                'verbose_name_plural': 'Stairs',
                'default_related_name': 'stairs',
            },
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('locationslug_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='areas', serialize=False, to='mapdata.LocationSlug')),
                ('titles', c3nav.mapdata.fields.JSONField(default={})),
                ('can_search', models.BooleanField(default=True, verbose_name='can be searched')),
                ('can_describe', models.BooleanField(default=True, verbose_name='can be used to describe a position')),
                ('color', models.CharField(blank=True, help_text='if set, has to be a valid color for svg images', max_length=16, null=True, verbose_name='background color')),
                ('public', models.BooleanField(default=True, verbose_name='public')),
                ('geometry', c3nav.mapdata.fields.GeometryField(geomtype='polygon')),
                ('stuffed', models.BooleanField(default=False, verbose_name='stuffed area')),
            ],
            options={
                'verbose_name': 'Area',
                'verbose_name_plural': 'Areas',
                'default_related_name': 'areas',
            },
            bases=('mapdata.locationslug', models.Model),
        ),
        migrations.CreateModel(
            name='LocationGroup',
            fields=[
                ('locationslug_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='locationgroups', serialize=False, to='mapdata.LocationSlug')),
                ('titles', c3nav.mapdata.fields.JSONField(default={})),
                ('can_search', models.BooleanField(default=True, verbose_name='can be searched')),
                ('can_describe', models.BooleanField(default=True, verbose_name='can be used to describe a position')),
                ('color', models.CharField(blank=True, help_text='if set, has to be a valid color for svg images', max_length=16, null=True, verbose_name='background color')),
                ('public', models.BooleanField(default=True, verbose_name='public')),
                ('compiled_room', models.BooleanField(default=False, verbose_name='is a compiled room')),
                ('compiled_area', models.BooleanField(default=False, verbose_name='is a compiled area')),
            ],
            options={
                'verbose_name': 'Location Group',
                'verbose_name_plural': 'Location Groups',
                'default_related_name': 'locationgroups',
            },
            bases=('mapdata.locationslug', models.Model),
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('locationslug_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='points', serialize=False, to='mapdata.LocationSlug')),
                ('titles', c3nav.mapdata.fields.JSONField(default={})),
                ('can_search', models.BooleanField(default=True, verbose_name='can be searched')),
                ('can_describe', models.BooleanField(default=True, verbose_name='can be used to describe a position')),
                ('color', models.CharField(blank=True, help_text='if set, has to be a valid color for svg images', max_length=16, null=True, verbose_name='background color')),
                ('public', models.BooleanField(default=True, verbose_name='public')),
                ('geometry', c3nav.mapdata.fields.GeometryField(geomtype='point')),
                ('groups', models.ManyToManyField(blank=True, related_name='points', to='mapdata.LocationGroup', verbose_name='Location Groups')),
            ],
            options={
                'verbose_name': 'Point',
                'verbose_name_plural': 'Points',
                'default_related_name': 'points',
            },
            bases=('mapdata.locationslug', models.Model),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('locationslug_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='sections', serialize=False, to='mapdata.LocationSlug')),
                ('titles', c3nav.mapdata.fields.JSONField(default={})),
                ('can_search', models.BooleanField(default=True, verbose_name='can be searched')),
                ('can_describe', models.BooleanField(default=True, verbose_name='can be used to describe a position')),
                ('color', models.CharField(blank=True, help_text='if set, has to be a valid color for svg images', max_length=16, null=True, verbose_name='background color')),
                ('public', models.BooleanField(default=True, verbose_name='public')),
                ('name', models.SlugField(unique=True, verbose_name='section name')),
                ('altitude', models.DecimalField(decimal_places=2, max_digits=6, unique=True, verbose_name='section altitude')),
                ('groups', models.ManyToManyField(blank=True, related_name='sections', to='mapdata.LocationGroup', verbose_name='Location Groups')),
            ],
            options={
                'verbose_name': 'Section',
                'verbose_name_plural': 'Sections',
                'ordering': ['altitude'],
                'default_related_name': 'sections',
            },
            bases=('mapdata.locationslug', models.Model),
        ),
        migrations.CreateModel(
            name='Space',
            fields=[
                ('locationslug_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='spaces', serialize=False, to='mapdata.LocationSlug')),
                ('titles', c3nav.mapdata.fields.JSONField(default={})),
                ('can_search', models.BooleanField(default=True, verbose_name='can be searched')),
                ('can_describe', models.BooleanField(default=True, verbose_name='can be used to describe a position')),
                ('color', models.CharField(blank=True, help_text='if set, has to be a valid color for svg images', max_length=16, null=True, verbose_name='background color')),
                ('level', models.CharField(choices=[('', 'normal'), ('upper', 'upper'), ('lower', 'lower')], default='', max_length=16, verbose_name='level')),
                ('geometry', c3nav.mapdata.fields.GeometryField(geomtype='polygon')),
                ('public', models.BooleanField(default=True, verbose_name='public')),
                ('category', models.CharField(choices=[('', 'normal'), ('stairs', 'stairs'), ('escalator', 'escalator'), ('elevator', 'elevator')], default='', max_length=16, verbose_name='category')),
                ('groups', models.ManyToManyField(blank=True, related_name='spaces', to='mapdata.LocationGroup', verbose_name='Location Groups')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spaces', to='mapdata.Section', verbose_name='section')),
            ],
            options={
                'verbose_name': 'Space',
                'verbose_name_plural': 'Spaces',
                'default_related_name': 'spaces',
            },
            bases=('mapdata.locationslug', models.Model),
        ),
        migrations.AddField(
            model_name='stair',
            name='space',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stairs', to='mapdata.Space', verbose_name='space'),
        ),
        migrations.AddField(
            model_name='point',
            name='space',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='points', to='mapdata.Space', verbose_name='space'),
        ),
        migrations.AddField(
            model_name='obstacle',
            name='space',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='obstacles', to='mapdata.Space', verbose_name='space'),
        ),
        migrations.AddField(
            model_name='lineobstacle',
            name='space',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lineobstacles', to='mapdata.Space', verbose_name='space'),
        ),
        migrations.AddField(
            model_name='hole',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='holes', to='mapdata.Section', verbose_name='section'),
        ),
        migrations.AddField(
            model_name='door',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doors', to='mapdata.Section', verbose_name='section'),
        ),
        migrations.AddField(
            model_name='building',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buildings', to='mapdata.Section', verbose_name='section'),
        ),
        migrations.AddField(
            model_name='area',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='areas', to='mapdata.LocationGroup', verbose_name='Location Groups'),
        ),
        migrations.AddField(
            model_name='area',
            name='space',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='areas', to='mapdata.Space', verbose_name='space'),
        ),
    ]
