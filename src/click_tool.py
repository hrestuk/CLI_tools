import click

@click.group()
def cli():
    pass


@cli.command()
@click.option("--name", required=True, help="Ім'я користувача")
def say(name):
    if name.lower().startswith("p"):
        click.echo("Ім'я не підходить")
    else:
        click.echo(name)


if __name__ == "__main__":
    cli()