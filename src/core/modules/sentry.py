import sentry_sdk

from src import settings, __version__
from src.core.modules import log


def setup() -> None:
    # get local environment
    version = __version__.__version__
    operating_system = settings.OPERATING_SYSTEM
    environment = settings.ENV

    # init the Sentry SDK
    sentry_sdk.init(
        dsn=settings.SENTRY_DSN,
        environment=environment,
        attach_stacktrace=True
    )

    # add context to Sentry reports
    sentry_sdk.set_context(
        "app",
        {
            "version": version,
            "operating_system": operating_system,
            "env": environment
        }
    )

    log.info("Error reporting setup!")
