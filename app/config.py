from pathlib import Path
import os
import string


APP_FOLDER_NAME = "DriveDrop"


def get_destination_path() -> Path:
    drive_root = find_google_drive_folder()

    if drive_root is None:
        raise FileNotFoundError(
            "No se encontró la carpeta local de Google Drive. "
            "Instala Google Drive Desktop o configura la ruta manualmente."
        )

    destination = drive_root / APP_FOLDER_NAME
    destination.mkdir(parents=True, exist_ok=True)

    return destination


def find_google_drive_folder() -> Path | None:
    candidates = get_common_google_drive_paths()
    candidates.extend(get_drive_letter_google_drive_paths())

    for candidate in candidates:
        if candidate.exists() and candidate.is_dir():
            return candidate

    return None


def get_common_google_drive_paths() -> list[Path]:
    user_profile = Path(os.environ.get("USERPROFILE", ""))

    return [
        user_profile / "Google Drive",
        user_profile / "My Drive",
        user_profile / "Mi unidad",
        user_profile / "GoogleDrive",
    ]


def get_drive_letter_google_drive_paths() -> list[Path]:
    candidates = []

    for letter in string.ascii_uppercase:
        root = Path(f"{letter}:/")

        candidates.extend(
            [
                root / "My Drive",
                root / "Mi unidad",
                root / "Google Drive",
            ]
        )

    return candidates