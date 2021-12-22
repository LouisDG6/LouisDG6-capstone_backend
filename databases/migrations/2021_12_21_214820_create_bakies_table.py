"""CreateBakiesTable Migration."""

from masoniteorm.migrations import Migration


class CreateBakiesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("bakies") as table:
            table.increments("id")
            table.string("name")
            table.string("details")

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("bakies")
