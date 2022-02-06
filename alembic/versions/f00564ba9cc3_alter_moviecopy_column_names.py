"""Alter MovieCopy column names

Revision ID: f00564ba9cc3
Revises: 03bf01236a89
Create Date: 2022-02-06 10:57:18.129215

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "f00564ba9cc3"
down_revision = "03bf01236a89"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("movie_copies", sa.Column("movie_id", sa.Integer(), nullable=True))
    op.add_column("movie_copies", sa.Column("owner_id", sa.Integer(), nullable=True))
    op.drop_constraint("movie_copies_owner_fkey", "movie_copies", type_="foreignkey")
    op.drop_constraint("movie_copies_movie_fkey", "movie_copies", type_="foreignkey")
    op.create_foreign_key(None, "movie_copies", "movies", ["movie_id"], ["id"])
    op.create_foreign_key(None, "movie_copies", "users", ["owner_id"], ["id"])
    op.drop_column("movie_copies", "owner")
    op.drop_column("movie_copies", "movie")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "movie_copies",
        sa.Column("movie", sa.INTEGER(), autoincrement=False, nullable=True),
    )
    op.add_column(
        "movie_copies",
        sa.Column("owner", sa.INTEGER(), autoincrement=False, nullable=True),
    )
    op.drop_constraint(None, "movie_copies", type_="foreignkey")
    op.drop_constraint(None, "movie_copies", type_="foreignkey")
    op.create_foreign_key(
        "movie_copies_movie_fkey", "movie_copies", "movies", ["movie"], ["id"]
    )
    op.create_foreign_key(
        "movie_copies_owner_fkey", "movie_copies", "users", ["owner"], ["id"]
    )
    op.drop_column("movie_copies", "owner_id")
    op.drop_column("movie_copies", "movie_id")
    # ### end Alembic commands ###
