import pytest
from unittest.mock import MagicMock
from project import save, save_list, open_registry


def test_save():
        #mocking the tk.entrys
        mock_name = MagicMock()
        mock_name.get.return_value = "notebook"

        mock_type = MagicMock()
        mock_type.get.return_value = "pcs"
        
        mock_qtt = MagicMock()
        mock_qtt.get.return_value = "1"
        
        mock_price = MagicMock()
        mock_price.get.return_value = "23.23"

        # calling the fundtion save
        save(
            name_entry=mock_name, 
            type_un_entry=mock_type, 
            qtt_entry=mock_qtt, 
            price_entry=mock_price
            )

        #checking the list and validating
        assert len(save_list) == 1
        id_code, name, type_un, qtt, price = save_list[0]
        assert id_code == "0001"
        assert name == "notebook"
        assert type_un == "pcs"
        assert qtt == "1"
        assert price == "23.23"

