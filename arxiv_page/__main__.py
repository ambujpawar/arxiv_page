from radicli import Radicli


cli = Radicli()

@cli.command('download')
def download():
    from .download import download_data
    print("Downloading data...")
    download_data()

if __name__ == '__main__':
    download()