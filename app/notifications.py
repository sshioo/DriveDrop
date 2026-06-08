def notify(title: str, message: str) -> None:
    try:
        from winotify import Notification
    except ImportError:
        print(f"{title}: {message}")
        return

    toast = Notification(
        app_id="DriveDrop",
        title=title,
        msg=message,
    )

    toast.show()