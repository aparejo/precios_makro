import unittest
from datetime import datetime
from django.utils import timezone
from myapp.models import Producto

class ProcesarDatosTestCase(unittest.TestCase):
    def setUp(self):
        # Create a sample data dictionary
        self.data = {
            "items": [
                {
                    "CODIGO": "123",
                    "DESCRIPCION": "Product 1",
                    # Add other item_data fields here
                },
                {
                    "CODIGO": "456",
                    "DESCRIPCION": "Product 2",
                    # Add other item_data fields here
                },
            ]
        }

    def test_procesar_datos_existing_product(self):
        # Create a sample existing product
        existing_product = Producto.objects.create(
            codigo="123",
            descripcion="Existing Product",
            # Add other fields here
        )

        # Call the procesar_datos function with the sample data
        procesar_datos(self.data)

        # Retrieve the updated product from the database
        updated_product = Producto.objects.get(codigo="123")

        # Assert that the fields have been updated correctly
        self.assertEqual(updated_product.existencia_total, self.data["items"][0]["EXIS_TOTAL"])
        self.assertEqual(updated_product.pvp_base, self.data["items"][0]["PVP_BASE"])
        # Add assertions for other fields here

    def test_procesar_datos_new_product(self):
        # Call the procesar_datos function with the sample data
        procesar_datos(self.data)

        # Retrieve the newly created product from the database
        new_product = Producto.objects.get(codigo="123")

        # Assert that the fields have been created correctly
        self.assertEqual(new_product.descripcion, self.data["items"][0]["DESCRIPCION"])
        # Add assertions for other fields here

if __name__ == "__main__":
    unittest.main()