# Generated by Django 4.0.10 on 2023-09-22 22:02

# Django
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models

# AA SRP
import aasrp.models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("eveuniverse", "0010_alter_eveindustryactivityduration_eve_type_and_more"),
        ("eveonline", "0017_alliance_and_corp_names_are_not_unique"),
        ("aasrp", "0011_default_settings"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="fleettype",
            options={
                "default_permissions": (),
                "verbose_name": "Fleet type",
                "verbose_name_plural": "Fleet types",
            },
        ),
        migrations.AlterModelOptions(
            name="insurance",
            options={
                "default_permissions": (),
                "verbose_name": "Ship insurance",
                "verbose_name_plural": "Ship insurances",
            },
        ),
        migrations.AlterModelOptions(
            name="setting",
            options={
                "default_permissions": (),
                "verbose_name": "Setting",
                "verbose_name_plural": "Settings",
            },
        ),
        migrations.AlterModelOptions(
            name="srplink",
            options={
                "default_permissions": (),
                "verbose_name": "SRP link",
                "verbose_name_plural": "SRP links",
            },
        ),
        migrations.AlterModelOptions(
            name="usersetting",
            options={
                "default_permissions": (),
                "verbose_name": "User settings",
                "verbose_name_plural": "User settings",
            },
        ),
        migrations.AlterField(
            model_name="insurance",
            name="insurance_cost",
            field=models.FloatField(verbose_name="Insurance cost"),
        ),
        migrations.AlterField(
            model_name="insurance",
            name="insurance_level",
            field=models.CharField(
                default="", max_length=254, verbose_name="Insurance level"
            ),
        ),
        migrations.AlterField(
            model_name="insurance",
            name="insurance_payout",
            field=models.FloatField(verbose_name="Insurance payout"),
        ),
        migrations.AlterField(
            model_name="insurance",
            name="srp_request",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="insurance",
                to="aasrp.srprequest",
                verbose_name="SRP request",
            ),
        ),
        migrations.AlterField(
            model_name="requestcomment",
            name="comment_time",
            field=models.DateTimeField(
                blank=True,
                default=django.utils.timezone.now,
                null=True,
                verbose_name="Comment time",
            ),
        ),
        migrations.AlterField(
            model_name="requestcomment",
            name="comment_type",
            field=models.CharField(
                choices=[
                    ("Comment", "Comment"),
                    ("Request Added", "SRP request added"),
                    ("Request Information", "Additional information"),
                    ("Reject Reason", "Reject reason"),
                    ("Status Changed", "Status changed"),
                    ("Reviser Comment", "Reviser comment"),
                ],
                default="Comment",
                max_length=19,
                verbose_name="Comment type",
            ),
        ),
        migrations.AlterField(
            model_name="requestcomment",
            name="new_status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Pending", "Pending"),
                    ("Approved", "Approved"),
                    ("Rejected", "Rejected"),
                ],
                default="",
                max_length=8,
                verbose_name="New SRP request status",
            ),
        ),
        migrations.AlterField(
            model_name="requestcomment",
            name="srp_request",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="srp_request_comments",
                to="aasrp.srprequest",
                verbose_name="SRP request",
            ),
        ),
        migrations.AlterField(
            model_name="setting",
            name="srp_team_discord_channel_id",
            field=models.PositiveBigIntegerField(
                blank=True,
                default=None,
                null=True,
                verbose_name="SRP team Discord channel ID",
            ),
        ),
        migrations.AlterField(
            model_name="srplink",
            name="aar_link",
            field=models.CharField(
                blank=True, default="", max_length=254, verbose_name="AAR link"
            ),
        ),
        migrations.AlterField(
            model_name="srplink",
            name="fleet_commander",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="eveonline.evecharacter",
                verbose_name="Fleet commander",
            ),
        ),
        migrations.AlterField(
            model_name="srplink",
            name="fleet_time",
            field=models.DateTimeField(verbose_name="Fleet time"),
        ),
        migrations.AlterField(
            model_name="srplink",
            name="fleet_type",
            field=models.ForeignKey(
                blank=True,
                default=None,
                help_text="The SRP link fleet type, if it's set",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="aasrp.fleettype",
                verbose_name="Fleet type",
            ),
        ),
        migrations.AlterField(
            model_name="srplink",
            name="srp_code",
            field=models.CharField(default="", max_length=16, verbose_name="SRP code"),
        ),
        migrations.AlterField(
            model_name="srplink",
            name="srp_name",
            field=models.CharField(default="", max_length=254, verbose_name="SRP name"),
        ),
        migrations.AlterField(
            model_name="srplink",
            name="srp_status",
            field=models.CharField(
                choices=[
                    ("Active", "Active"),
                    ("Closed", "Closed"),
                    ("Completed", "Completed"),
                ],
                default="Active",
                max_length=9,
                verbose_name="SRP status",
            ),
        ),
        migrations.AlterField(
            model_name="srprequest",
            name="additional_info",
            field=models.TextField(
                blank=True, default="", verbose_name="Additional information"
            ),
        ),
        migrations.AlterField(
            model_name="srprequest",
            name="creator",
            field=models.ForeignKey(
                blank=True,
                default=None,
                help_text="Who created the SRP request?",
                null=True,
                on_delete=models.SET(aasrp.models.get_sentinel_user),
                related_name="+",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Creator",
            ),
        ),
        migrations.AlterField(
            model_name="srprequest",
            name="killboard_link",
            field=models.CharField(
                default="", max_length=254, verbose_name="Killboard link"
            ),
        ),
        migrations.AlterField(
            model_name="srprequest",
            name="loss_amount",
            field=models.BigIntegerField(default=0, verbose_name="Loss amount"),
        ),
        migrations.AlterField(
            model_name="srprequest",
            name="payout_amount",
            field=models.BigIntegerField(default=0, verbose_name="Payout amount"),
        ),
        migrations.AlterField(
            model_name="srprequest",
            name="post_time",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="Request time"
            ),
        ),
        migrations.AlterField(
            model_name="srprequest",
            name="reject_info",
            field=models.TextField(
                blank=True, default="", verbose_name="Reject reason"
            ),
        ),
        migrations.AlterField(
            model_name="srprequest",
            name="request_code",
            field=models.CharField(
                default="", max_length=254, verbose_name="Request code"
            ),
        ),
        migrations.AlterField(
            model_name="srprequest",
            name="request_status",
            field=models.CharField(
                choices=[
                    ("Pending", "Pending"),
                    ("Approved", "Approved"),
                    ("Rejected", "Rejected"),
                ],
                default="Pending",
                max_length=8,
                verbose_name="Request status",
            ),
        ),
        migrations.AlterField(
            model_name="srprequest",
            name="ship",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="srp_requests",
                to="eveuniverse.evetype",
                verbose_name="Ship type",
            ),
        ),
        migrations.AlterField(
            model_name="srprequest",
            name="ship_name",
            field=models.CharField(
                default="", max_length=254, verbose_name="Ship type"
            ),
        ),
        migrations.AlterField(
            model_name="srprequest",
            name="srp_link",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="srp_requests",
                to="aasrp.srplink",
                verbose_name="SRP link",
            ),
        ),
        migrations.AlterField(
            model_name="usersetting",
            name="disable_notifications",
            field=models.BooleanField(
                default=False, verbose_name="Disable notifications"
            ),
        ),
    ]
