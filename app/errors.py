from flask import render_template
from typing import Callable


def make_handler(status: int, message: str) -> Callable[[Exception], str]:
    return lambda error: render_template(
        "errors/error.html", status=status, message=message
    )
