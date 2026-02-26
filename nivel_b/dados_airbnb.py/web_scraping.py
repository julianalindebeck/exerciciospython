from bs4 import BeautifulSoup
import requests

class WebScraping:
    def __init__(self, url):
        self.url = url
        self.soup = self.get_html()

    def get_html(self):
        req = requests.get(self.url)
        soup = BeautifulSoup(req.content, "html.parser")
        return soup
    
    def get_quartos(self):
        return self.soup.find_all("div", class_ = "g1qv1ctd atm_u80d3j_pqaxnk atm_c8_o7aogt atm_g3_8jkm7i atm_gw_iv6dct c95t3t6 atm_9s_11p5wf0 atm_cx_1mo6erc atm_dz_7esijk atm_e0_1lo05zz dir dir-ltr")

    def get_titulo(self, quarto):
        return quarto.find("div", class_ = "t1jojoys atm_g3_1kw7nm4 atm_ks_15vqwwr atm_sq_1l2sidv atm_9s_cj1kg8 atm_6w_1e54zos atm_fy_1vgr820 atm_7l_hfv0h6 atm_cs_1mexzig atm_w4_1eetg7c atm_ks_zryt35__1rgatj2 dir dir-ltr").text
    
    def get_subtitulo(self, quarto):
        return quarto.find("span", class_ = "t6mzqp7 atm_g3_1kw7nm4 atm_ks_15vqwwr atm_sq_1l2sidv atm_9s_cj1kg8 atm_6w_1e54zos atm_fy_kb7nvz atm_7l_xeyu1p atm_am_qk3dho atm_ks_zryt35__1rgatj2 dir dir-ltr").text

    def seleciona_todos_quartos(self):
        for quarto in self.get_quartos():
            titulo = self.get_titulo(quarto)
            subtitulo = self.get_subtitulo(quarto)
            print(titulo)
            print(f'{subtitulo}\n')