import os


class Cleaner:
    def __init__(self):
        self.home = os.getenv('HOME')
        self.from_directory = f'{self.home}/Downloads'
        self.book_list = ['.pdf', '.fb2', '.txt']
        self.torrent_list = ['.torrent']
        self.movie_list = ['.mkv', '.m4v', '.avi']
        self.book_dir = f'{self.home}/books'
        self.torrent_dir = f'{self.home}/torrents'
        self.movie_dir = f'{self.home}/Movies'

    def get_list(self, attr=None):
        if attr:
            files_list = os.listdir(self.from_directory)
            result = []
            for file in files_list:
                for extension in getattr(self, f'{attr}_list'):
                    if extension in file and os.path.isfile(f'{self.from_directory}/{file}'):
                        result.append(file)
                        break
            return result
        print('Не указан тип возвразаемых файлов')

    def move_books(self):
        for file in self.get_list('book'):
            try:
                print(f'Trying to move file {file} to {self.book_dir}/', end='...')
                os.renames(f'{self.from_directory}/{file}', f'{self.book_dir}/{file}')
                print(' Done')
            except:
                print('Error')

    def move_movies(self):
        for file in self.get_list('movie'):
            try:
                print(f'Trying to move file {file} to {self.movie_dir}/', end='...')
                os.renames(f'{self.from_directory}/{file}', f'{self.movie_dir}/{file}')
                print(' Done')
            except:
                print('Error')

    def move_torrents(self):
        for file in self.get_list('torrent'):
            try:
                print(f'Trying to move file {file} to {self.torrent_dir}/', end='...')
                os.renames(f'{self.from_directory}/{file}', f'{self.torrent_dir}/{file}')
                print(' Done')
            except:
                print('Error')


cleaner = Cleaner()
cleaner.move_books()
cleaner.move_movies()
cleaner.move_torrents()
