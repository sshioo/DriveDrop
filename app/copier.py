from pathlib import Path
import shutil


def copy_item(source: Path, destination_root: Path) -> Path:
    source = source.resolve()
    destination_root.mkdir(parents=True, exist_ok=True)

    destination = destination_root / source.name

    if source.is_dir():
        return copy_directory(source, destination)

    if source.is_file():
        return copy_file(source, destination)

    raise FileNotFoundError(f"Ruta no soportada: {source}")


def copy_file(source: Path, destination: Path) -> Path:
    destination = unique_destination(destination)
    shutil.copy2(source, destination)
    return destination


def copy_directory(source: Path, destination: Path) -> Path:
    destination = unique_destination(destination)
    shutil.copytree(source, destination)
    return destination


def unique_destination(destination: Path) -> Path:
    if not destination.exists():
        return destination

    stem = destination.stem
    suffix = destination.suffix
    parent = destination.parent

    index = 1

    while True:
        candidate = parent / f"{stem} ({index}){suffix}"

        if not candidate.exists():
            return candidate

        index += 1