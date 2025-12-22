# Creando una instancia de la clase AFIP
# Una instancia de una clase es un objeto concreto
# creado a partir de la clase. Por ejemplo, dada la clase
# que define los atributos de una factura, una instancia
# de clase sería una factura específica con sus valores.
from afip import Afip

afip = Afip({
    "CUIT": 20409378472,
    "access_token": "2YVVB5clASQSC4hgluzVr3wXLtMdyTZsUo5wKPzqYQgen0mU5lVLwirxAfk8FZmb"
})

# CUIT de prueba (AFIP)
tax_id = 30500010912 

try:
    # Usamos la clase que indica la documentación
    taxpayer_details = afip.RegisterInscriptionProof.getTaxpayerDetails(tax_id)

    if taxpayer_details:
        print(f"--- Datos encontrados para el CUIT {tax_id} ---")
        # El SDK suele devolver los datos dentro de un objeto 'datosGenerales' 
        # o directamente en la raíz del JSON dependiendo del servicio
        print(taxpayer_details) 
    else:
        print("No se recibió respuesta del servidor.")

except Exception as e:
    print(f"Error al intentar obtener los datos: {e}")