import click
from colorama import Fore
from subprocess import Popen


@click.command("bulb")
@click.argument("brightness", type=float)
@click.argument("target", envvar="BULB_TARGET")
def cli(brightness, target):
    """
    A safe CLI for changing the display brightness (via xrandr).
    """
    if brightness < 0.1 or brightness > 1.0:
        _print_err("Brightness can only between 0.1 and 1.0!")
        exit(1)

    brightness = round(brightness, 1)

    args = ["xrandr", "--output", target, "--brightness", str(brightness)]

    with Popen(args) as xrandr:
        exit_code = xrandr.returncode

        if exit_code != 1:
            reason = xrandr.stderr.read()
            _print_err(f"Could not change brightness. Exit code {exit_code} - {reason}")


def main():
    cli()


def _print_err(text):
    print(Fore.RED + text)
    print(Fore.RESET)
