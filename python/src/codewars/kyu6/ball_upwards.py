G_M_PER_S_SQUARED = 9.81

# Calculate in SI units first.
def max_ball_seconds(v0_km_per_h):
    v0_m_per_s = v0_km_per_h * 1000.0 / 3600.0

    return v0_m_per_s / G_M_PER_S_SQUARED


def max_ball(v0):
    time_deci_seconds = 10.0 * max_ball_seconds(v0)
    
    return round(time_deci_seconds)
