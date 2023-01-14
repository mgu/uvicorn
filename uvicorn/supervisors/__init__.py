from typing import TYPE_CHECKING, Type

if TYPE_CHECKING:
    from uvicorn.supervisors.basereload import BaseReload


def get_reload_class() -> "Type[BaseReload]":
    try:
        from uvicorn.supervisors.watchfilesreload import WatchFilesReload

        return WatchFilesReload
    except ImportError:  # pragma: no cover
        try:
            from uvicorn.supervisors.watchgodreload import WatchGodReload

            return WatchGodReload
        except ImportError:
            from uvicorn.supervisors.statreload import StatReload

            return StatReload


__all__ = ["get_reload_class"]
