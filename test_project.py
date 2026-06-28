import pytest
from unittest.mock import MagicMock, mock_open, patch, call
from project import save, save_list, open_registry, write_in_txt


def test_save():
        #cleaning the test list
        save_list.clear()

        #mocking the tk.entrys
        mock_name = MagicMock()
        mock_name.get.return_value = "notebook"

        mock_type = MagicMock()
        mock_type.get.return_value = "pcs"
        
        mock_qtt = MagicMock()
        mock_qtt.get.return_value = "1"
        
        mock_price = MagicMock()
        mock_price.get.return_value = "23.23"

        # mocking a existent file. using project.open and project.os, because the test is writing in 'products.txt'
        with patch('project.open', mock_open(read_data='')), patch('project.os.path.exists', return_value= True):
            # calling the function save
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


def test_write_int_txt_success():
    # mocked list
    mock_save_list = [
        (1, "notebook", "pcs", 10, 1255.50), 
        (2, "cigars", "pack", 5, 7.50)
    ]

    # open file and substituing the global variable
    with patch('builtins.open', mock_open()) as mocked_file, patch('project.save_list', mock_save_list), patch('os.path.exists', return_value=True):
        result = write_in_txt('test_productc.txt')
        assert result == "Save successfully"


def test_write_int_txt_error():
    with patch("builtins.open", side_efect= FileNotFoundError):
        result = write_in_txt('not_existing_file.txt')
        assert result == "File not found"