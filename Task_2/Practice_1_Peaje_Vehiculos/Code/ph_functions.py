def calc_disc_amount(amount_vehic:float, disc:float) -> float:
    """
    function: calc_disc_amount()
    description: Calcula el monto de descuento por utilizar la hora pico.
    params: amount_vehic, disc
    """
    disc_amount = amount_vehic - ((disc/100)*amount_vehic)

    return disc_amount


def calc_volunt_amount(amount_vehic:float, increase:float) -> float:
    """
    function: calc_volunt_amount()
    description: Calcula el aumento por utilizar el carril de voluntario.
    params: amount_vehic, increase
    """
    volunt_amount = amount_vehic + ((increase/100)*amount_vehic)

    return volunt_amount


def calc_total(total:float, amount_vehic:float) -> float:
    """
    function: calc_total()
    description: Suma los ingresos totales del peaje.
    params: total, amount_vehic
    """
    total = total + amount_vehic
    
    return total

def calc_avg(total_earn, cant_vehics):
    """
    function: calc_avg()
    description: Calcula el promedio total del ingreso diario del peaje
    params: total_earn, cant_vehics
    """

    avg = total_earn / cant_vehics

    return avg




