__author__ = 'Elf'

from handler.create_pyment import CreateHandler
from handler.show_pyment import ShowAllHandler
from handler.edit_pyment import EditHandler

url_pattern = [
    ('/create', CreateHandler),
    ('/show_all', ShowAllHandler),
    ('/edit', EditHandler),

]
