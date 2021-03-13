import sentry_sdk

from src import settings
from src.core.modules import log
from src.core.modules.utils import get_operating_system


def setup() -> None:
    # get local environment
    operating_system = get_operating_system()
    version = settings.VERSION
    environment = settings.ENV
    dsn = settings.SENTRY_DSN

    # init the Sentry SDK
    sentry_sdk.init(
        dsn=dsn,
        environment=environment,
        attach_stacktrace=True,
        sample_rate=1.0,
    )

    # add context to Sentry reports
    sentry_sdk.set_context(
        "app",
        {"version": version, "operating_system": operating_system, "env": environment},
    )

    log.info("Error reporting setup!")
