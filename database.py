import tkinter as tk
# definir archivo de AgenciaVehiculosApp

def main():
    root = tk.Tk()
    app = AgenciaVehiculosApp(root)
    
    root.protocol("WM_DELETE_WINDOW", app.al_cerrar)
    
    root.mainloop()

if __name__ == "__main__":
    main()