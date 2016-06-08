#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gi.repository import Gtk
import MySQLdb
# Contador global para los id
cont = 1

def run_query (query = ''):
    # Conexión base de datos
    conexion = MySQLdb.connect(host='localhost', user='musica',passwd='music', db='BDMusical')
    # Crear cursor
    micursor = conexion.cursor()
    # Consulta
    micursor.execute(query)
    # Traer los resultados de un select
    registro = micursor.fetchall()
    # Se hace efectiva la escritura de datos
    conexion.commit()
    # Cierre cursor
    micursor.close()
    # Cierre de conexión
    conexion.close()
    return registro

def Insertar_Tabla():
    global cont
    nombreCD = str(entry1.get_text())
    grupomusical = str(entry2.get_text())
    generomusical = str(entry3.get_text())
    numpintas = int(entry4.get_text())
    annopublicacion = int(entry5.get_text())
    query = 'INSERT INTO Discos (id,NombreCD,GrupoMusical,GeneroMusical,NumPistas,AnnoPublicacion) VALUES (%d, \"%s\", \"%s\", \"%s\", %d, %d);' % (cont, nombreCD, grupomusical, generomusical, numpintas, annopublicacion)
    run_query(query)
    cont = cont + 1

def Ver_Tabla():
    query = "SELECT id, NombreCD, GrupoMusical, GeneroMusical, NumPistas, AnnoPublicacion FROM Discos"
    Imprimir_Tabla = run_query(query)
    label6.set_text(str(Imprimir_Tabla))

def Borrar_Tabla():
    nombreCD = str(entry6.get_text())
    query = "DELETE FROM Discos WHERE NombreCD = '%s'" % nombreCD
    run_query(query)

def Limpiar_Tabla():
    global cont
    cont = 1
    query = "DELETE FROM Discos"
    run_query(query)

def incluir(button):
    Insertar_Tabla()

def visualizar(button):
    Ver_Tabla()

def borrar(button):
    Borrar_Tabla()

def limpiar(button):
    Limpiar_Tabla()

builder = Gtk.Builder()
builder.add_from_file("02_ismaelburgosroldan_final.glade")

handlers = {
    "terminar_aplicacion": Gtk.main_quit,
    "evento_incluir": incluir,
    "evento_visualizar": visualizar,
    "evento_borrar": borrar,
    "evento_limpiar": limpiar
}

builder.connect_signals(handlers)
entry1 = builder.get_object("entry1")
entry2 = builder.get_object("entry2")
entry3 = builder.get_object("entry3")
entry4 = builder.get_object("entry4")
entry5 = builder.get_object("entry5")
entry6 = builder.get_object("entry6")
label6 = builder.get_object("label6")
window = builder.get_object("window1")
window.show_all()

Gtk.main()
