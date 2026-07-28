import tkinter as tk
from tkinter import ttk, messagebox
from mysql.connector import Error
from database import DatabaseManager

class AgenciaVehiculosApp:
    def __init__(self, root):
        self.root = root