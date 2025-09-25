from pyscript import document, display


def show_info(e):
    name = document("name").getElementById.value
    country = document("cntry").getElementById.value
    contact = document("cntac").getElementById.value
    guitars = document("gitrs").getElementById.value
    info = f"Name: {name}\nCountry: {country}\nContact: {contact}"
    output = document("output")
    output_div = document.getElementById("BRUH")
    output_div.innerText = info
    display(info, target="BRUH")