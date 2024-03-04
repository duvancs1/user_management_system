from typing                     import Dict

from django.db.models           import QuerySet


def create_user_hierarchy_dict(users: QuerySet) -> Dict:

    hierarchy_dict = {}

    for user in users:
        manager = user.reporting_line_manager

        if manager:
            if manager not in hierarchy_dict:
                hierarchy_dict[manager] = []

            hierarchy_dict[manager].append(user)

    return hierarchy_dict
