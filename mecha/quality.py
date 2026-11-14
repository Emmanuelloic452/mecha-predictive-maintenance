def validate_spindle_speed(speed_rpm: float | None) -> bool:
    """
    Vérifie si une vitesse de broche CNC est valide.

    Args:
        speed_rpm: Vitesse mesurée en tours par minute.

    Returns:
        True si la mesure respecte notre convention,
        False sinon.
    """

    # TODO: Implémenter la validation
    if speed_rpm is None:
        return False
    elif speed_rpm >= 0:
        return True
    else:
        return False     