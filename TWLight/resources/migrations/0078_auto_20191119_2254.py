# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-19 22:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("resources", "0077_auto_20191030_0919")]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="short_name",
            field=models.CharField(
                help_text="The form of the contact person's name to use in email greetings (as in 'Hi Jake')",
                max_length=15,
            ),
        ),
        migrations.AlterField(
            model_name="partner",
            name="description",
            field=models.TextField(
                blank=True,
                help_text="Optional detailed description in addition to the short description such as collections, instructions, notes, special requirements, alternate access options, unique features, citations notes.",
                verbose_name="long description",
            ),
        ),
        migrations.AlterField(
            model_name="partner",
            name="description_ar",
            field=models.TextField(
                blank=True,
                help_text="Optional detailed description in addition to the short description such as collections, instructions, notes, special requirements, alternate access options, unique features, citations notes.",
                null=True,
                verbose_name="long description",
            ),
        ),
        migrations.AlterField(
            model_name="partner",
            name="description_br",
            field=models.TextField(
                blank=True,
                help_text="Optional detailed description in addition to the short description such as collections, instructions, notes, special requirements, alternate access options, unique features, citations notes.",
                null=True,
                verbose_name="long description",
            ),
        ),
        migrations.AlterField(
            model_name="partner",
            name="description_da",
            field=models.TextField(
                blank=True,
                help_text="Optional detailed description in addition to the short description such as collections, instructions, notes, special requirements, alternate access options, unique features, citations notes.",
                null=True,
                verbose_name="long description",
            ),
        ),
        migrations.AlterField(
            model_name="partner",
            name="description_de",
            field=models.TextField(
                blank=True,
                help_text="Optional detailed description in addition to the short description such as collections, instructions, notes, special requirements, alternate access options, unique features, citations notes.",
                null=True,
                verbose_name="long description",
            ),
        ),
        migrations.AlterField(
            model_name="partner",
            name="description_en",
            field=models.TextField(
                blank=True,
                help_text="Optional detailed description in addition to the short description such as collections, instructions, notes, special requirements, alternate access options, unique features, citations notes.",
                null=True,
                verbose_name="long description",
            ),
        ),
        migrations.AlterField(
            model_name="partner",
            name="description_en_gb",
            field=models.TextField(
                blank=True,
                help_text="Optional detailed description in addition to the short description such as collections, instructions, notes, special requirements, alternate access options, unique features, citations notes.",
                null=True,
                verbose_name="long description",
            ),
        ),
        migrations.AlterField(
            model_name="partner",
            name="description_eo",
            field=models.TextField(
                blank=True,
                help_text="Optional detailed description in addition to the short description such as collections, instructions, notes, special requirements, alternate access options, unique features, citations notes.",
                null=True,
                verbose_name="long description",
            ),
        ),
        migrations.AlterField(
            model_name="partner",
            name="description_es",
            field=models.TextField(
                blank=True,
                help_text="Optional detailed description in addition to the short description such as collections, instructions, notes, special requirements, alternate access options, unique features, citations notes.",
                null=True,
                verbose_name="long description",
            ),
        ),
        migrations.AlterField(
            model_name="partner",
            name="description_fa",
            field=models.TextField(
                blank=True,
                help_text="Optional detailed description in addition to the short description such as collections, instructions, notes, special requirements, alternate access options, unique features, citations notes.",
                null=True,
                verbose_name="long description",
            ),
        ),
        migrations.AlterField(
            model_name="partner",
            name="description_fi",
            field=models.TextField(
                blank=True,
                help_text="Optional detailed description in addition to the short description such as collections, instructions, notes, special requirements, alternate access options, unique features, citations notes.",
                null=True,
                verbose_name="long description",
            ),
        ),
        migrations.AlterField(
            model_name="partner",
            name="description_fr",
            field=models.TextField(
                blank=True,
                help_text="Optional detailed description in addition to the short description such as collections, instructions, notes, special requirements, alternate access options, unique features, citations notes.",
                null=True,
                verbose_name="long description",
            ),
        ),
        migrations.AlterField(
            model_name="partner",
            name="description_hi",
            field=models.TextField(
                blank=True,
                help_text="Optional detailed description in addition to the short description such as collections, instructions, notes, special requirements, alternate access options, unique features, citations notes.",
                null=True,
                verbose_name="long description",
            ),
        ),
        migrations.AlterField(
            model_name="partner",
            name="description_ja",
            field=models.TextField(
                blank=True,
                help_text="Optional detailed description in addition to the short description such as collections, instructions, notes, special requirements, alternate access options, unique features, citations notes.",
                null=True,
                verbose_name="long description",
            ),
        ),
        migrations.AlterField(
            model_name="partner",
            name="description_ko",
            field=models.TextField(
                blank=True,
                help_text="Optional detailed description in addition to the short description such as collections, instructions, notes, special requirements, alternate access options, unique features, citations notes.",
                null=True,
                verbose_name="long description",
            ),
        ),
        migrations.AlterField(
            model_name="partner",
            name="description_mk",
            field=models.TextField(
                blank=True,
                help_text="Optional detailed description in addition to the short description such as collections, instructions, notes, special requirements, alternate access options, unique features, citations notes.",
                null=True,
                verbose_name="long description",
            ),
        ),
        migrations.AlterField(
            model_name="partner",
            name="description_mr",
            field=models.TextField(
                blank=True,
                help_text="Optional detailed description in addition to the short description such as collections, instructions, notes, special requirements, alternate access options, unique features, citations notes.",
                null=True,
                verbose_name="long description",
            ),
        ),
        migrations.AlterField(
            model_name="partner",
            name="description_my",
            field=models.TextField(
                blank=True,
                help_text="Optional detailed description in addition to the short description such as collections, instructions, notes, special requirements, alternate access options, unique features, citations notes.",
                null=True,
                verbose_name="long description",
            ),
        ),
        migrations.AlterField(
            model_name="partner",
            name="description_pt",
            field=models.TextField(
                blank=True,
                help_text="Optional detailed description in addition to the short description such as collections, instructions, notes, special requirements, alternate access options, unique features, citations notes.",
                null=True,
                verbose_name="long description",
            ),
        ),
        migrations.AlterField(
            model_name="partner",
            name="description_pt_br",
            field=models.TextField(
                blank=True,
                help_text="Optional detailed description in addition to the short description such as collections, instructions, notes, special requirements, alternate access options, unique features, citations notes.",
                null=True,
                verbose_name="long description",
            ),
        ),
        migrations.AlterField(
            model_name="partner",
            name="description_ru",
            field=models.TextField(
                blank=True,
                help_text="Optional detailed description in addition to the short description such as collections, instructions, notes, special requirements, alternate access options, unique features, citations notes.",
                null=True,
                verbose_name="long description",
            ),
        ),
        migrations.AlterField(
            model_name="partner",
            name="description_sv",
            field=models.TextField(
                blank=True,
                help_text="Optional detailed description in addition to the short description such as collections, instructions, notes, special requirements, alternate access options, unique features, citations notes.",
                null=True,
                verbose_name="long description",
            ),
        ),
        migrations.AlterField(
            model_name="partner",
            name="description_ta",
            field=models.TextField(
                blank=True,
                help_text="Optional detailed description in addition to the short description such as collections, instructions, notes, special requirements, alternate access options, unique features, citations notes.",
                null=True,
                verbose_name="long description",
            ),
        ),
        migrations.AlterField(
            model_name="partner",
            name="description_tr",
            field=models.TextField(
                blank=True,
                help_text="Optional detailed description in addition to the short description such as collections, instructions, notes, special requirements, alternate access options, unique features, citations notes.",
                null=True,
                verbose_name="long description",
            ),
        ),
        migrations.AlterField(
            model_name="partner",
            name="description_uk",
            field=models.TextField(
                blank=True,
                help_text="Optional detailed description in addition to the short description such as collections, instructions, notes, special requirements, alternate access options, unique features, citations notes.",
                null=True,
                verbose_name="long description",
            ),
        ),
        migrations.AlterField(
            model_name="partner",
            name="description_vi",
            field=models.TextField(
                blank=True,
                help_text="Optional detailed description in addition to the short description such as collections, instructions, notes, special requirements, alternate access options, unique features, citations notes.",
                null=True,
                verbose_name="long description",
            ),
        ),
        migrations.AlterField(
            model_name="partner",
            name="description_zh_hans",
            field=models.TextField(
                blank=True,
                help_text="Optional detailed description in addition to the short description such as collections, instructions, notes, special requirements, alternate access options, unique features, citations notes.",
                null=True,
                verbose_name="long description",
            ),
        ),
        migrations.AlterField(
            model_name="partner",
            name="description_zh_hant",
            field=models.TextField(
                blank=True,
                help_text="Optional detailed description in addition to the short description such as collections, instructions, notes, special requirements, alternate access options, unique features, citations notes.",
                null=True,
                verbose_name="long description",
            ),
        ),
        migrations.AlterField(
            model_name="partner",
            name="mutually_exclusive",
            field=models.NullBooleanField(
                default=None,
                help_text="If True, users can only apply for one Stream at a time from this Partner. If False, users can apply for multiple Streams at a time. This field must be filled in when Partners have multiple Streams, but may be left blank otherwise.",
            ),
        ),
        migrations.AlterField(
            model_name="partnerlogo",
            name="logo",
            field=models.ImageField(
                blank=True,
                help_text="Optional image file that can be used to represent this partner.",
                null=True,
                upload_to="",
            ),
        ),
    ]