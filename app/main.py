import sys
from pathlib import Path

from app.config import get_destination_path
from app.copier import copy_item
from app.notifications import notify


def main(argv: list[str] | None = None) -> int:
    argv = argv if argv is not None else sys.argv[1:]

    if not argv:
        print("Uso: python -m app.main <archivo-o-carpeta> [mas-rutas...]")
        return 1

    destination_root = get_destination_path()

    copied = []
    failed = []

    for raw_path in argv:
        source = Path(raw_path)

        if not source.exists():
            failed.append((raw_path, "La ruta no existe"))
            continue

        try:
            copied_path = copy_item(source, destination_root)
            copied.append(copied_path)
        except Exception as error:
            failed.append((raw_path, str(error)))

    if copied:
        print(f"Copiados {len(copied)} elemento(s) a {destination_root}")

        for path in copied:
            print(f"OK: {path}")

    if failed:
        print(f"Fallaron {len(failed)} elemento(s)")

        for path, error in failed:
            print(f"ERROR: {path} -> {error}")

    if failed and copied:
        notify(
            "DriveDrop",
            f"Copiados {len(copied)} elemento(s), fallaron {len(failed)}.",
        )
        return 2

    if failed:
        notify(
            "DriveDrop",
            f"No se pudieron copiar {len(failed)} elemento(s).",
        )
        return 1

    notify(
        "DriveDrop",
        f"Copiados {len(copied)} elemento(s) a Google Drive.",
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())