# pylint: disable=missing-module-docstring,pointless-statement
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    ###########################
    # Delete all the commented lines after editing the module
    ###########################
    "name": "Custom Journal Entry Report",
    "summary": """
        Custom Journal Entry Report allows you to print the journal entries from account.move that are not invoices.""",
    "author": "Humanytek",
    "maintainers": ["mbrehumanytek"],
    "website": "https://humanitek.com/",
    "license": "AGPL-3",
    "category": "Technical Settings",
    "version": "17.0.1.0.0",
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
    ###########################
    # Delete all the commented lines after editing the module
    ###########################
    ### XML Data files
    # "data": [
    #     "security/ir.model.access.csv",
    #     "views/views.xml",
    #     "views/templates.xml",
    # ],
    ### XML Demo files
    # only loaded in demo mode
    # "demo": [
    #     "demo/demo.xml",
    # ],
    ### Assets
    # In 15.0, Odoo adds a new way to add js/css assets files to a module.
    # https://www.holdenrehg.com/blog/2021-10-08_odoo-manifest-asset-bundles
    # "assets": {
    #     "web.assets_backend": [
    #         "/my_module/path/to/file"
    #     ],
    #     "web.assets_qweb": [
    #         "/my_module/path/to/file", # QWeb templates. Example: 'pos_sale/static/src/xml/**/*',
    #     ],
    # }
    ###########################
    # Delete all the commented lines after editing the module
    ###########################
}
