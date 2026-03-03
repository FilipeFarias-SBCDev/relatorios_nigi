# ----- IMPORTS -----
import base64
import os
import shutil
import logging
from datetime import datetime

from flask import (
    Flask,
    redirect,
    render_template,
    request,
    send_from_directory,
    url_for,
)

from config import temp_pdf_folder, converted_file_folder
from utils import upload_file, clear_folder

# ----- VARIABLES -----
app = Flask(__name__, static_folder="static")


# ----- ROUTES -----
@app.route("/")
def main():
    return render_template("nigi_kanban.html")
    # return redirect(url_for("show_links"))


# Rota Kanban (opcional, para ter url explicita)
@app.route("/nigi_kanban")
def nigi_kanban():
    return render_template("nigi_kanban.html")


@app.route("/nigi_cronograma")
def nigi_cronograma():
    return render_template("nigi_cronograma.html")


# Rota Cobertura
@app.route("/nigi_cobertura_contratual")
def nigi_cobertura_contratual():
    # Note que o nome da função é 'cobertura'
    return render_template("nigi_cobertura_contratual.html")


# Rota Métricas
@app.route("/nigi_metricas_sharepoint")
def nigi_metricas_sharepoint():
    return render_template("nigi_metricas_sharepoint.html")


# Rota Inconsistências
@app.route("/nigi_inconsistencias_de_faturamento")
def nigi_inconsistencias_de_faturamento():
    return render_template("nigi_inconsistencias_de_faturamento.html")


# Rota Solicitações
@app.route("/nigi_solicitacoes_de_demandas")
def nigi_solicitacoes_de_demandas():
    return render_template("nigi_solicitacoes_de_demandas.html")


# Rota Solicitações
@app.route("/nigi_atualizacao_do_cnes")
def nigi_atualizacao_do_cnes():
    return render_template("nigi_atualizacao_do_cnes.html")


# @app.route("/convert", methods=["POST"])
# def convert_pdf():
#     upload_file(request.files, temp_pdf_folder)
#     extract_text_from_pdf()
#     remove_incorrect_line_breaks()

#     file_path = os.listdir(converted_file_folder)[0]

#     redirect(url_for("main"))

#     return send_from_directory(
#         directory=converted_file_folder, path=file_path, as_attachment=True
#     )


if __name__ == "__main__":
    logging.info("Limpando pastas")
    clear_folder(temp_pdf_folder)
    clear_folder(converted_file_folder)

    logging.info("Executando")
    app.run(host="0.0.0.0", port=11000, debug=True)
