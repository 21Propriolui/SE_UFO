import flet as ft

class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model
        self.anno = None
        self.forma = None

    def populate_dd(self):
        """ Metodo per popolare i dropdown """
        # TODO
        self._view.dd_year.options.clear()
        self._view.dd_shape.options.clear()
        anni = self._model.get_anno()
        forme = self._model.get_forma()
        for anno in anni:
            self._view.dd_year.options.append(ft.dropdown.Option(str(anno)))
        for forma in forme:
            self._view.dd_shape.options.append(ft.dropdown.Option(str(forma)))
        self._view.update()

    def handle_graph(self, e):
        """ Handler per gestire creazione del grafo """
        # TODO

    def handle_path(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del cammino """
        # TODO
