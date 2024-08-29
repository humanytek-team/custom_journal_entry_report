# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Custom Journal Entry Report",
    "summary": """
        Custom Journal Entry Report allows you to print the journal entries from account.move that are not invoices.""",
    "author": "Humanytek",
    "maintainers": ["mbrehumanytek"],
    "website": "https://humanytek.com/",
    "license": "AGPL-3",
    "category": "Technical Settings",
    "version": "17.0.1.2.0",
    "development_status": "Production/Stable",
    "application": False,
    "installable": True,
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends": ["account"],
    "data": [
        "views/account_move_views.xml",
        "reports/journal_entry_report.xml",
        "reports/journal_entry_template.xml",
    ],
}
