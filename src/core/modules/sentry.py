import sentry_sdk

from src import settings
from src.core.modules import log
from src.core.modules.utils import get_operating_system


def setup() -> None:
    # get local environment
    operating_system = get_operating_system()
    version = settings.VERSION
    environment = settings.ENV

    # init the Sentry SDK
    sentry_sdk.init(
        dsn=settings.SENTRY_DSN, environment=environment, attach_stacktrace=True
    )

    # add context to Sentry reports
    sentry_sdk.set_context(
        "app",
        {"version": version, "operating_system": operating_system, "env": environment},
    )

    log.info("Error reporting setup!")
