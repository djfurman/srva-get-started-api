from orator.migrations import Migration


class CreateMessagesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('messages') as table:
            table.increments('id')
            table.text('uuid')
            table.text('name')
            table.text('email_address')
            table.text('phone_number')
            table.text('message')
            table.timestamps()


    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('messages')
