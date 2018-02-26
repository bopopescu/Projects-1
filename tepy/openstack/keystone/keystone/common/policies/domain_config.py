# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from oslo_policy import policy

from keystone.common.policies import base


domain_config_policies = [
    policy.DocumentedRuleDefault(
        name=base.IDENTITY % 'create_domain_config',
        check_str=base.RULE_ADMIN_REQUIRED,
        description='Create domain configuration.',
        operations=[
            {
                'path': '/v3/domains/{domain_id}/config',
                'method': 'PUT'
            }
        ]
    ),
    policy.DocumentedRuleDefault(
        name=base.IDENTITY % 'get_domain_config',
        check_str=base.RULE_ADMIN_REQUIRED,
        description=('Get the entire domain configuration for a domain, an '
                     'option group within a domain, or a specific '
                     'configuration option within a group for a domain.'),
        operations=[
            {
                'path': '/v3/domains/{domain_id}/config',
                'method': 'GET'
            },
            {
                'path': '/v3/domains/{domain_id}/config',
                'method': 'HEAD'
            },
            {
                'path': '/v3/domains/{domain_id}/config/{group}',
                'method': 'GET'
            },
            {
                'path': '/v3/domains/{domain_id}/config/{group}',
                'method': 'HEAD'
            },
            {
                'path': '/v3/domains/{domain_id}/config/{group}/{option}',
                'method': 'GET'
            },
            {
                'path': '/v3/domains/{domain_id}/config/{group}/{option}',
                'method': 'HEAD'
            }
        ]
    ),
    policy.DocumentedRuleDefault(
        name=base.IDENTITY % 'get_security_compliance_domain_config',
        check_str='',
        description=('Get security compliance domain configuration for '
                     'either a domain or a specific option in a domain.'),
        operations=[
            {
                'path': '/v3/domains/{domain_id}/config/security_compliance',
                'method': 'GET'
            },
            {
                'path': '/v3/domains/{domain_id}/config/security_compliance',
                'method': 'HEAD'
            },
            {
                'path': ('v3/domains/{domain_id}/config/'
                         'security_compliance/{option}'),
                'method': 'GET'
            },
            {
                'path': ('v3/domains/{domain_id}/config/'
                         'security_compliance/{option}'),
                'method': 'HEAD'
            }
        ]
    ),
    policy.DocumentedRuleDefault(
        name=base.IDENTITY % 'update_domain_config',
        check_str=base.RULE_ADMIN_REQUIRED,
        description=('Update domain configuration for either a domain, '
                     'specific group or a specific option in a group.'),
        operations=[
            {
                'path': '/v3/domains/{domain_id}/config',
                'method': 'PATCH'
            },
            {
                'path': '/v3/domains/{domain_id}/config/{group}',
                'method': 'PATCH'
            },
            {
                'path': '/v3/domains/{domain_id}/config/{group}/{option}',
                'method': 'PATCH'
            }
        ]
    ),
    policy.DocumentedRuleDefault(
        name=base.IDENTITY % 'delete_domain_config',
        check_str=base.RULE_ADMIN_REQUIRED,
        description=('Delete domain configuration for either a domain, '
                     'specific group or a specific option in a group.'),
        operations=[
            {
                'path': '/v3/domains/{domain_id}/config',
                'method': 'DELETE'
            },
            {
                'path': '/v3/domains/{domain_id}/config/{group}',
                'method': 'DELETE'
            },
            {
                'path': '/v3/domains/{domain_id}/config/{group}/{option}',
                'method': 'DELETE'
            }
        ]
    ),
    policy.DocumentedRuleDefault(
        name=base.IDENTITY % 'get_domain_config_default',
        check_str=base.RULE_ADMIN_REQUIRED,
        description=('Get domain configuration default for either a domain, '
                     'specific group or a specific option in a group.'),
        operations=[
            {
                'path': '/v3/domains/config/default',
                'method': 'GET'
            },
            {
                'path': '/v3/domains/config/default',
                'method': 'HEAD'
            },
            {
                'path': '/v3/domains/config/{group}/default',
                'method': 'GET'
            },
            {
                'path': '/v3/domains/config/{group}/default',
                'method': 'HEAD'
            },
            {
                'path': '/v3/domains/config/{group}/{option}/default',
                'method': 'GET'
            },
            {
                'path': '/v3/domains/config/{group}/{option}/default',
                'method': 'HEAD'
            }
        ]
    )
]


def list_rules():
    return domain_config_policies
