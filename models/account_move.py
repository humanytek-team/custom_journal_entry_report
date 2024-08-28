from odoo import models


class AccountMove(models.Model):
    _inherit = "account.move"

    def print_journal_entry_report(self):
        return self.env.ref(
            "custom_journal_entry_report.journal_entry_report_action"
        ).report_action(self)
