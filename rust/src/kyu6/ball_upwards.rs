#![allow(dead_code)]
const G_M_PER_S_SQUARED: f64 = 9.81;

// Calculate in SI units first.
fn max_ball_seconds(v0_km_per_h: i32) -> f64 {
    let v0_m_per_s = (v0_km_per_h as f64) * 1000.0 / 3600.0;

    v0_m_per_s / G_M_PER_S_SQUARED
}

fn max_ball(v0: i32) -> i32 {
    let time_deci_seconds = 10.0 * max_ball_seconds(v0);
    time_deci_seconds.round() as i32
}

#[cfg(test)]
mod tests {
    fn testequal(v0: i32, exp: i32) -> () {
        assert_eq!(exp, super::max_ball(v0))
    }

    #[test]
    fn basic_tests() {
        testequal(37, 10);
        testequal(45, 13);
    }
}
