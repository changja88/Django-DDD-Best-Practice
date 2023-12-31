# Generated by Django 4.2.5 on 2023-09-13 11:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("address", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="MemberAddressAggregate",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "created",
                    django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name="created"),
                ),
                (
                    "modified",
                    django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name="modified"),
                ),
                (
                    "living_address_level1",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="member_living_address_lv1",
                        to="address.addresslevel1entity",
                    ),
                ),
                (
                    "living_address_level2",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="member_living_address_lv2",
                        to="address.addresslevel2aggregate",
                    ),
                ),
                (
                    "member",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="member_address",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "playing_address_level1",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="member_playing_address_lv1",
                        to="address.addresslevel1entity",
                    ),
                ),
                (
                    "playing_address_level2",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="member_playing_address_lv2",
                        to="address.addresslevel2aggregate",
                    ),
                ),
            ],
            options={
                "verbose_name": "[member_address] 멤버의 주소(거주지/활동지)",
                "verbose_name_plural": "[member_address] 멤버의 주소(거주지/활동지)",
                "db_table": "member_address",
            },
        ),
    ]
