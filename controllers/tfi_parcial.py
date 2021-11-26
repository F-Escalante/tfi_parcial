from odoo import http
from odoo.http import request


class tfi_parcial(http.Controller):
    @http.route('/operaciones/<int:tipo>',auth='public',website=True)
    def control(self,tipo):

        r = request.uid
        print("id usuario ", r)

        dataset =  [
              ['titulo1',10],
              ['titulo2', 20],
              ['titulo3', 30]
              ]

        jdato = {

            "dato":dataset

        }

        if tipo==1:
            return request.render("gestion_operaciones.id_vista_tabla",jdato)
        elif tipo==2:
            return request.render("gestion_operaciones.id_vista_grafico",jdato)
        else:
            return str(dataset)
