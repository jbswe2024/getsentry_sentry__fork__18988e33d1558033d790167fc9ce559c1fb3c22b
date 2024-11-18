# Generated by Django 5.1.1 on 2024-11-13 15:32

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models

import sentry.db.models.fields.bounded
import sentry.db.models.fields.foreignkey
import sentry.db.models.fields.hybrid_cloud_foreign_key
from sentry.new_migrations.migrations import CheckedMigration


class Migration(CheckedMigration):
    # This flag is used to mark that a migration shouldn't be automatically run in production.
    # This should only be used for operations where it's safe to run the migration after your
    # code has deployed. So this should not be used for most operations that alter the schema
    # of a table.
    # Here are some things that make sense to mark as post deployment:
    # - Large data migrations. Typically we want these to be run manually so that they can be
    #   monitored and not block the deploy for a long period of time while they run.
    # - Adding indexes to large tables. Since this can take a long time, we'd generally prefer to
    #   run this outside deployments so that we don't block them. Note that while adding an index
    #   is a schema change, it's completely safe to run the operation after the code has deployed.
    # Once deployed, run these manually via: https://develop.sentry.dev/database-migrations/#migration-deployment

    is_post_deployment = False

    dependencies = [
        ("flags", "0001_add_flag_audit_log"),
        ("sentry", "0787_make_dashboard_perms_col_nullable"),
    ]

    operations = [
        migrations.CreateModel(
            name="FlagWebHookSigningSecretModel",
            fields=[
                (
                    "id",
                    sentry.db.models.fields.bounded.BoundedBigAutoField(
                        primary_key=True, serialize=False
                    ),
                ),
                (
                    "created_by",
                    sentry.db.models.fields.hybrid_cloud_foreign_key.HybridCloudForeignKey(
                        "sentry.User", db_index=True, null=True, on_delete="SET_NULL"
                    ),
                ),
                ("date_added", models.DateTimeField(default=django.utils.timezone.now)),
                ("provider", models.CharField(db_index=True)),
                ("secret", models.CharField()),
                (
                    "organization",
                    sentry.db.models.fields.foreignkey.FlexibleForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="sentry.organization"
                    ),
                ),
            ],
            options={
                "db_table": "flags_webhooksigningsecret",
                "unique_together": {("organization", "provider", "secret")},
            },
        ),
    ]