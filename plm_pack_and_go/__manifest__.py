##############################################################################
#
#    OmniaSolutions, Open Source Management Solution
#    Copyright (C) 2010-2021 OmniaSolutions (<http://www.omniasolutions.eu>).
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
    "name": "Plm Pack and Go",
    "version": "14.0.1",
    "author": "OmniaSolutions",
    "website": "https://github.com/OmniaGit/odooplm",
    "category": "Product Lifecycle Management",
    "sequence": 15,
    "summary": "Download BOM structure files from a component",
    "license": "AGPL-3",
    "images": [],
    "depends": ["plm"],
    "data": [  # security
        "security/plm_security.xml",
        'views/plm_component.xml',
        "views/ir_parameters.xml",
    ],
    "demo": [],
    "test": [],
    "installable": True,
    "application": False,
    "auto_install": False,
}
