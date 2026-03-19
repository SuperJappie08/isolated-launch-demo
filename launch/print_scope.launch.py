from pprint import pformat
from typing import TYPE_CHECKING

from launch import LaunchDescription
from launch.actions import OpaqueFunction
from launch.logging import get_logger

if TYPE_CHECKING:
    from launch import LaunchContext

# A global logger
LOGGER = get_logger("launch.context_introspection")

LAST_LAUNCH_FILE_KEY = "last_launch_file"


def report_context(context: "LaunchContext", *args, **kwargs):
    LOGGER.warning(
        "launch locals:\n    "
        + pformat(context.get_locals_as_dict(), indent=4, width=76)
    )

    LOGGER.warning(
        "launch configurations:\n    "
        + pformat(context.launch_configurations, indent=4, width=76)
    )
    LOGGER.info("\n\n" + "=" * 80 + "\n")


def generate_launch_description():
    return LaunchDescription([
        OpaqueFunction(function=report_context),
    ])
