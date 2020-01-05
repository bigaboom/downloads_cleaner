import os


class Cleaner:
    def __init__(self):
        self.home = os.getenv('HOME')
        self.from_directory = os.path.join(self.home, 'Downloads')
        self.book_list = ['.pdf', '.fb2', '.txt']
        self.torrent_list = ['.torrent']
        self.movie_list = ['.mkv', '.m4v', '.avi']
        self.book_dir = os.path.join(self.home, 'books')
        self.torrent_dir = os.path.join(self.home, 'torrents')
        self.movie_dir = os.path.join(self.home, 'Movies')

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
        print('Type of returned files is not specified')

    def move_files(self, attr=None):
        for file in self.get_list(attr):
            try:
                print(f'Trying to move file {file} to {getattr(self,f"{attr}_dir")}/', end='... ')
                os.renames(f'{self.from_directory}/{file}', f'{getattr(self,f"{attr}_dir")}/{file}')
                print('Done')
            except:
                print('Error')


cleaner = Cleaner()
cleaner.move_files('book')
cleaner.move_files('movie')
cleaner.move_files('torrent')
