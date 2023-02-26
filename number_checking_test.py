import sender_stand_request


# проверка, что запрос успешен
def test_status_code_is_200():
    number_checking = sender_stand_request.response_track_number
    assert number_checking.status_code == 200