from mecha.quality import validate_spindle_speed

def test_positive_speed() -> None:
    assert validate_spindle_speed(1500) is True

def test_zero_speed() -> None:
    # Vérifier que 0 est accepté
    assert validate_spindle_speed(0) is True


def test_negative_speed() -> None:
    # Vérifier que -500 est rejeté
    assert validate_spindle_speed(-500) is False


def test_missing_speed() -> None:
    # Vérifier que None est rejeté
    assert validate_spindle_speed(None) is False