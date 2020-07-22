# Copyright 2017 Cisco Systems, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

from django.core.management.base import BaseCommand
from django.utils import translation
import requests

ZANATA_LOCALES = requests.get("https://translate.openstack.org/rest/project"
                              "/horizon/version/main/locales").json()
LANGUAGE_CODES = [x['localeId'] for x in ZANATA_LOCALES]
DOMAINS = ['django', 'djangojs']
MODULES = ['horizon', 'openstack_dashboard']
PROJECT = 'horizon'
POFILE = "{module}/locale/{locale}/LC_MESSAGES/{domain}.po"
POFILE_URL = ("https://translate.openstack.org/rest/file/translation/{project}"
              "/main/{language}/po?docId={module}%2Flocale%2F{domain}")


class Command(BaseCommand):
    help = ("Pull a translation catalog from Zanata "
            "(https://translate.openstack.org) for all languages or a "
            "specified language")

    def add_arguments(self, parser):
        parser.add_argument('-l', '--language', choices=LANGUAGE_CODES,
                            metavar='LANG',
                            default=LANGUAGE_CODES, nargs='+',
                            help=("The language code(s) to pull language "
                                  "catalogs for. The default is all "
                                  "languages. Available languages are: %s"
                                  % ', '.join(sorted(LANGUAGE_CODES))))
        parser.add_argument('-p', '--project', type=str, default=PROJECT,
                            help=("The name of the project to extract "
                                  "strings from e.g. 'horizon'. The default "
                                  "is 'horizon'"))
        parser.add_argument('-m', '--module', type=str, nargs='+',
                            default=MODULES,
                            help=("The target python module(s) to extract "
                                  "strings from e.g. 'openstack_dashboard'. "
                                  "The default modules are 'horizon' and "
                                  "'openstack_dashboard'"))

    def handle(self, *args, **options):
        for module in options['module']:
            for domain in DOMAINS:
                for language in options['language']:
                    locale = translation.to_locale(language)

                    pofile = POFILE.format(module=module,
                                           locale=locale,
                                           domain=domain)

                    pofile_dir = os.path.dirname(pofile)
                    if not os.path.exists(pofile_dir):
                        os.makedirs(pofile_dir)

                    new_po = requests.get((POFILE_URL).format(
                        language=language,
                        project=options['project'],
                        module=module,
                        domain=domain))

                    # Ensure to use UTF-8 encoding
                    new_po.encoding = 'utf-8'

                    with open(pofile, 'w+') as f:
                        f.write(new_po.text.encode('utf-8'))
