##############################################################################
#
#    OmniaSolutions, Open Source Management Solution
#    Copyright (C) 2010-2019 OmniaSolutions (<https://www.omniasolutions.website>).
#    $Id$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    "name": "Product Lifecycle Management",
    "version": "14.0.1.0.0",
    "author": "OmniaSolutions",
    "website": "https://github.com/OmniaGit/odooplm",
    "category": "Manufacturing/Product Lifecycle Management",
    "sequence": 15,
    "license": "LGPL-3",
    "summary": "PLM Integration with main CAD editors",
    "images": ["static/img/odoo_plm.png"],
    "depends": ["base", "board", "product", "mrp"],
    "data": [
        # security
        "security/base_plm_security.xml",
        # views
        "views/product_product_first.xml",
        "views/ir_attachment_view.xml",
        "views/ir_attachment_relations.xml",
        "views/plm_dbthread.xml",
        "views/import_stylesheet.xml",
        "views/mrp_extension.xml",
        "views/plm_backupdoc_view.xml",
        "views/plm_checkout_view.xml",
        "views/plm_config_settings.xml",
        "views/plm_description_view.xml",
        "views/plm_finishing_view.xml",
        "views/plm_treatment_view.xml",
        "views/plm_material_view.xml",
        "views/product_product.xml",
        "views/product_template.xml",
        "views/ir_config_parameter.xml",
        "views/ir_cron.xml",
        "views/plm_cad_open.xml",
        "views/plm_cad_open_bck.xml",
        "views/mail_activity_type.xml",
        "views/sequence.xml",
        "views/menu.xml",
        # Reports Template
        "report/bom_structure_report_template.xml",
        "report/document_report_templates.xml",
        "report/product_report_templates.xml",
        # Report
        "report/bom_structure.xml",
        "report/component_report.xml",
        "report/document_report.xml",
    ],
    "qweb": ["views/templates.xml"],
    "demo": [],
    "test": [],
    "installable": True,
    "application": True,
    "auto_install": False,
}
