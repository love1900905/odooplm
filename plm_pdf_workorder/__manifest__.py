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
    "name": "PLM Report PDF Workorder",
    "version": "14.0.1.0.0",
    "author": "OmniaSolutions",
    "website": "https://github.com/OmniaGit/odooplm",
    "category": "Product Lifecycle Management",
    "sequence": 15,
    "summary": "",
    "images": [],
    "license": "LGPL-3",
    "depends": [
        "plm",
        "mrp_workorder",
    ],
    "data": [
        "views/mrp_routing_workcenter.xml",
        "views/mrp_workorder.xml",
    ],
    "demo": [],
    "test": [],
    "installable": True,  # FIXME: mrp_workorder has been moved to enterprise
    "application": False,
    "auto_install": False,
}
