from tkinter import Tk, ttk, constants


class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_menu_view()
    
    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _handle_start_game(self):
        self._show_game_view()

    def _handle_exit_game(self):
        self._show_menu_view()

    def _show_menu_view(self):
        self._hide_current_view()

        self._current_view = MenuView(self._root, self._handle_start_game)

        self._current_view.pack()

    def _show_game_view(self):
        self._hide_current_view()

        self._current_view = GameView(self._root, self._handle_exit_game)

        self._current_view.pack()

class MenuView:
    def __init__(self, root, handle_start_game):
        self._root = root
        self._handle_start_game = handle_start_game
        self._frame = None

        self._initialize()
    
    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        button = ttk.Button(
            master=self._frame,
            text="Start",
            command=self._handle_start_game
        )

        button.grid(row=1, column=0)

class GameView:
    def __init__(self, root, handle_exit_game):
        self._root = root
        self._handle_exit_game = handle_exit_game
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.BOTH, expand=True)
        self._button.pack(padx=10, pady=10)
        self._info.pack(side=constants.RIGHT, fill=constants.Y)
        self._grid.pack(fill=constants.BOTH, expand=True)


    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._info = ttk.Frame(master=self._frame, width=200)
        self._button = ttk.Button(
            master=self._info,
            text="Exit",
            command=self._handle_exit_game
        )

        # 20x20 Gomoku grid
        self._grid = ttk.Frame(master=self._frame)
        for i in range(20):
            self._grid.grid_rowconfigure(i, weight=1)
            for j in range(20):
                self._grid.grid_columnconfigure(j, weight=1)

                #todo: this needs to display the correct mark inside the square
                square = ttk.Label(
                    master=self._grid, 
                    text="", 
                    relief="raised", 
                    anchor="center"
                )
                
                square.grid(row=i, column=j, sticky="nsew")

