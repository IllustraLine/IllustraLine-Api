"""Initial migration.

Revision ID: 90c9c7071236
Revises: 
Create Date: 2024-06-28 23:27:09.685609

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "90c9c7071236"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("course")
    op.drop_table("admin_course")
    op.drop_table("my_course")
    op.drop_table("user")
    op.drop_table("reset_password")
    op.drop_table("wallet")
    op.drop_table("account_active")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "account_active",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("user_id", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column("token", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column(
            "created_at",
            sa.DOUBLE_PRECISION(precision=53),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DOUBLE_PRECISION(precision=53),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column(
            "expired_at",
            sa.DOUBLE_PRECISION(precision=53),
            autoincrement=False,
            nullable=False,
        ),
        sa.CheckConstraint(
            "created_at > 0::double precision", name="positive_created_at"
        ),
        sa.CheckConstraint(
            "expired_at > 0::double precision", name="positive_expired_at"
        ),
        sa.CheckConstraint("length(token::text) > 0", name="non_empty_token"),
        sa.CheckConstraint(
            "updated_at > 0::double precision", name="positive_updated_at"
        ),
        sa.CheckConstraint("user_id > 0", name="positive_user_id"),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
            name="account_active_user_id_fkey",
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name="account_active_pkey"),
        sa.UniqueConstraint("token", name="account_active_token_key"),
        sa.UniqueConstraint("user_id", name="account_active_user_id_key"),
    )
    op.create_table(
        "wallet",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("user_id", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column("amount", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column("is_active", sa.BOOLEAN(), autoincrement=False, nullable=False),
        sa.Column(
            "created_at",
            sa.DOUBLE_PRECISION(precision=53),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DOUBLE_PRECISION(precision=53),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column(
            "banned_at",
            sa.DOUBLE_PRECISION(precision=53),
            autoincrement=False,
            nullable=True,
        ),
        sa.Column(
            "unbanned_at",
            sa.DOUBLE_PRECISION(precision=53),
            autoincrement=False,
            nullable=True,
        ),
        sa.CheckConstraint(
            "banned_at > 0::double precision OR banned_at IS NULL",
            name="positive_banned_at_or_null",
        ),
        sa.CheckConstraint(
            "created_at > 0::double precision", name="positive_created_at"
        ),
        sa.CheckConstraint(
            "unbanned_at > 0::double precision OR unbanned_at IS NULL",
            name="positive_un_banned_at_or_null",
        ),
        sa.CheckConstraint(
            "updated_at > 0::double precision", name="positive_updated_at"
        ),
        sa.CheckConstraint("user_id > 0", name="positive_user_id"),
        sa.ForeignKeyConstraint(
            ["user_id"], ["user.id"], name="wallet_user_id_fkey", ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("id", name="wallet_pkey"),
        sa.UniqueConstraint("user_id", name="wallet_user_id_key"),
    )
    op.create_table(
        "reset_password",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("user_id", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column("token", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column(
            "created_at",
            sa.DOUBLE_PRECISION(precision=53),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DOUBLE_PRECISION(precision=53),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column(
            "expired_at",
            sa.DOUBLE_PRECISION(precision=53),
            autoincrement=False,
            nullable=False,
        ),
        sa.CheckConstraint(
            "created_at > 0::double precision", name="positive_created_at"
        ),
        sa.CheckConstraint(
            "expired_at > 0::double precision", name="positive_expired_at"
        ),
        sa.CheckConstraint("length(token::text) > 0", name="non_empty_token"),
        sa.CheckConstraint(
            "updated_at > 0::double precision", name="positive_updated_at"
        ),
        sa.CheckConstraint("user_id > 0", name="positive_user_id"),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
            name="reset_password_user_id_fkey",
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name="reset_password_pkey"),
        sa.UniqueConstraint("token", name="reset_password_token_key"),
        sa.UniqueConstraint("user_id", name="reset_password_user_id_key"),
    )
    op.create_table(
        "user",
        sa.Column(
            "id",
            sa.INTEGER(),
            server_default=sa.text("nextval('user_id_seq'::regclass)"),
            autoincrement=True,
            nullable=False,
        ),
        sa.Column("email", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column("username", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column("password", sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column("is_active", sa.BOOLEAN(), autoincrement=False, nullable=False),
        sa.Column("is_admin", sa.BOOLEAN(), autoincrement=False, nullable=False),
        sa.Column(
            "created_at",
            sa.DOUBLE_PRECISION(precision=53),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DOUBLE_PRECISION(precision=53),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column(
            "banned_at",
            sa.DOUBLE_PRECISION(precision=53),
            autoincrement=False,
            nullable=True,
        ),
        sa.Column(
            "unbanned_at",
            sa.DOUBLE_PRECISION(precision=53),
            autoincrement=False,
            nullable=True,
        ),
        sa.Column("profile_name", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column(
            "profile_image", postgresql.BYTEA(), autoincrement=False, nullable=False
        ),
        sa.CheckConstraint(
            "banned_at > 0::double precision OR banned_at IS NULL",
            name="positive_banned_at_or_null",
        ),
        sa.CheckConstraint(
            "created_at > 0::double precision", name="positive_created_at"
        ),
        sa.CheckConstraint("length(email::text) > 0", name="non_empty_email"),
        sa.CheckConstraint("length(password::text) > 0", name="non_empty_password"),
        sa.CheckConstraint("length(username::text) > 0", name="non_empty_username"),
        sa.CheckConstraint(
            "unbanned_at > 0::double precision OR unbanned_at IS NULL",
            name="positive_un_banned_at_or_null",
        ),
        sa.CheckConstraint(
            "updated_at > 0::double precision", name="positive_updated_at"
        ),
        sa.PrimaryKeyConstraint("id", name="user_pkey"),
        sa.UniqueConstraint("email", name="user_email_key"),
        sa.UniqueConstraint("profile_name", name="user_profile_name_key"),
        sa.UniqueConstraint("username", name="user_username_key"),
        postgresql_ignore_search_path=False,
    )
    op.create_table(
        "my_course",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("user_id", sa.INTEGER(), autoincrement=False, nullable=True),
        sa.Column("course_id", sa.INTEGER(), autoincrement=False, nullable=True),
        sa.Column(
            "created_at",
            sa.DOUBLE_PRECISION(precision=53),
            autoincrement=False,
            nullable=False,
        ),
        sa.CheckConstraint("course_id > 0", name="positive_course_id"),
        sa.CheckConstraint(
            "created_at > 0::double precision", name="positive_created_at"
        ),
        sa.CheckConstraint("user_id > 0", name="positive_user_id"),
        sa.ForeignKeyConstraint(
            ["course_id"],
            ["course.id"],
            name="my_course_course_id_fkey",
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["user_id"], ["user.id"], name="my_course_user_id_fkey", ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("id", name="my_course_pkey"),
        sa.UniqueConstraint("course_id", name="my_course_course_id_key"),
    )
    op.create_table(
        "admin_course",
        sa.Column(
            "id",
            sa.INTEGER(),
            server_default=sa.text("nextval('admin_course_id_seq'::regclass)"),
            autoincrement=True,
            nullable=False,
        ),
        sa.Column("user_id", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column("username", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column(
            "created_at",
            sa.DOUBLE_PRECISION(precision=53),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DOUBLE_PRECISION(precision=53),
            autoincrement=False,
            nullable=False,
        ),
        sa.CheckConstraint(
            "created_at > 0::double precision", name="positive_created_at"
        ),
        sa.CheckConstraint("length(username::text) > 0", name="non_empty_username"),
        sa.CheckConstraint(
            "updated_at > 0::double precision", name="positive_updated_at"
        ),
        sa.CheckConstraint("user_id > 0", name="positive_user_id"),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
            name="admin_course_user_id_fkey",
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name="admin_course_pkey"),
        sa.UniqueConstraint("user_id", name="admin_course_user_id_key"),
        sa.UniqueConstraint("username", name="admin_course_username_key"),
        postgresql_ignore_search_path=False,
    )
    op.create_table(
        "course",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("admin_id", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column("admin_username", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column("title", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column("description", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column("artist", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column("category", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column(
            "tags",
            postgresql.JSONB(astext_type=sa.Text()),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column(
            "created_at",
            sa.DOUBLE_PRECISION(precision=53),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DOUBLE_PRECISION(precision=53),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column(
            "price",
            sa.DOUBLE_PRECISION(precision=53),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column("image_name", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column(
            "course_image", postgresql.BYTEA(), autoincrement=False, nullable=False
        ),
        sa.Column("is_active", sa.BOOLEAN(), autoincrement=False, nullable=False),
        sa.CheckConstraint("admin_id > 0", name="positive_admin_id"),
        sa.CheckConstraint(
            "created_at > 0::double precision", name="positive_created_at"
        ),
        sa.CheckConstraint(
            "jsonb_array_length(tags) >= 1 AND jsonb_array_length(tags) <= 5",
            name="tags_length_between_1_and_5",
        ),
        sa.CheckConstraint(
            "length(admin_username::text) > 0", name="non_empty_admin_username"
        ),
        sa.CheckConstraint("length(artist::text) > 0", name="non_empty_artist"),
        sa.CheckConstraint("length(category::text) > 0", name="non_empty_category"),
        sa.CheckConstraint(
            "length(description::text) > 0", name="non_empty_description"
        ),
        sa.CheckConstraint("length(title::text) > 0", name="non_empty_title"),
        sa.CheckConstraint("price >= 0::double precision", name="positive_price"),
        sa.CheckConstraint(
            "updated_at > 0::double precision", name="positive_updated_at"
        ),
        sa.ForeignKeyConstraint(
            ["admin_id"],
            ["admin_course.id"],
            name="course_admin_id_fkey",
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["admin_username"],
            ["admin_course.username"],
            name="course_admin_username_fkey",
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name="course_pkey"),
        sa.UniqueConstraint("image_name", name="course_image_name_key"),
    )
    # ### end Alembic commands ###
