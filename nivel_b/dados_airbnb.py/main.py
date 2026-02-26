from web_scraping import WebScraping

url = "https://www.airbnb.com.br/s/Fortaleza--CE/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJL1zB9iFPxwcRqid5ywZnbf0&location_bb=wGxLV8IZmu%2FAeNfiwhqL2g%3D%3D&acp_id=5f60fc28-f302-4247-a18e-669d39e78c76&date_picker_type=calendar&flexible_date_search_filter_type=3&adults=1&search_type=unknown"
web_scraping = WebScraping(url)

web_scraping.seleciona_todos_quartos()
