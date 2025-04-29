import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_analizza(self, e):
        self._view.txt_result.controls.clear()
        x = self._view.txt_distanza.value
        if x is None or x == "":
            self._view.create_alert("Inserire la distanza")
            return

        numNodi, numArchi, grafo = self._model.buildGraph(x)
        self._view.txt_result.controls.append(ft.Text(f"Il grafo per la distanza minima {x} è stato correttamente creato!"))
        self._view.txt_result.controls.append(ft.Text(f"Il numero di nodi è: {numNodi}"))
        self._view.txt_result.controls.append(ft.Text(f"Il numero di archi è: {numArchi}"))

        for aeroP in grafo:
            for areoA in grafo[aeroP]:
                self._view.txt_result.controls.append(ft.Text(f"La distanza media tra {aeroP} e {areoA} è: {grafo[aeroP][areoA]["weight"]} miglia"))

        self._view.update_page()
        return
