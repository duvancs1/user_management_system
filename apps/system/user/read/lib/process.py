from django.db.models           import QuerySet

from ...common                  import common_processes as common_process_lib

from django_gravatar.helpers    import has_gravatar


def get_gravatar_images(users: QuerySet) -> QuerySet:

    for user in users:

        # If we've already hashed the email, no need for us to process it again
        if user.hashed_email_gravatar:
            continue

        email = user.email

        # Check first if the user has a Gravatar profile
        gravatar_exists = has_gravatar(user.email)

        if gravatar_exists:

            hashed_email = common_process_lib.sanitize_and_hash_email(email)

            user.hashed_email_gravatar = hashed_email

    return users


